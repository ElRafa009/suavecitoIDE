from tkinter import END, Scrollbar, filedialog as FileDialog, ttk
from io import open
from lexer import reset_lexer
from test_lexer import test_lexer
from sintac import calculate_levels, parse_code, parser


ruta = "" # La utilizaremos para almacenar la ruta del archivo

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Una lista de diccionarios, cada diccionario es un scope.

    def add(self, symbol):
        current_scope = self.scopes[-1]
        if symbol.name in current_scope:
            raise ValueError(f"Error: La variable '{symbol.name}' ya ha sido declarada en este ámbito.")
        current_scope[symbol.name] = symbol

    def lookup(self, name):
        # Buscamos en el scope más profundo primero
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

  

# Crear un archivo nuevo
def nuevo(root, mensaje, texto):
    global ruta
    mensaje.set("Nuevo Archivo")
    ruta = ""
    texto.delete(1.0, END)
    root.title("Suavecito Compiler")

# Abrir un archivo
def abrir(root, mensaje, texto):
    global ruta
    mensaje.set("Abrir Archivo")
    ruta = FileDialog.askopenfilename(
        initialdir=".",
        filetype=(("Archivos de texto", "*.txt"),),
        title="Abrir un archivo de texto")
    
    if ruta != "":
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        texto.delete(1.0, END)
        texto.insert('insert', contenido)
        archivo.close()
        root.title(ruta + "- Suavecito Compiler")
        highlight_syntax(texto)

# Guardar archivo
def guardar(root, mensaje, texto):
    mensaje.set("Guardar Archivo")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        archivo = open(ruta, 'w+')
        archivo.write(contenido)
        archivo.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        guardar_como(root, mensaje, texto)

# Guardar como
def guardar_como(root, mensaje, texto):
    global ruta
    mensaje.set("Guardar Archivo como")
    archivo = FileDialog.asksaveasfile(title="Guardar archivo", mode="w", defaultextension=".txt")
    if archivo is not None:
        ruta = archivo.name
        root.title(ruta + "- Suavecito Compiler")
        contenido = texto.get(1.0, 'end-1c')
        archivo = open(ruta, 'w+')
        archivo.write(contenido)
        archivo.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

def mostrar_mensaje_en_rojo(pantalla_errores, mensaje):
        pantalla_errores.config(state='normal', fg='red')  # Habilitar la edición para agregar texto en rojo
        pantalla_errores.insert('end', mensaje + '\n')  # Insertar el mensaje y un salto de línea
        pantalla_errores.config(state='disabled')  # Deshabilitar la edición para que sea solo de lectura
        pantalla_errores.see('end')  # Desplazar la pantalla hacia abajo para mostrar el mensaje más reciente

# Ejecutar análisis léxico sobre el archivo abierto
def run_command(root, mensaje, texto, frame_lexico, pantalla_errores, frame_sintactico, frame_semantico):
    global ruta
    mensaje.set("Ejecutando análisis léxico...")
    
    if ruta != "":
        guardar(root, mensaje, texto)
        try:
            # Intentar abrir el archivo si el argumento es un nombre de archivo
            with open(ruta) as file:
                input_text = file.read()
        except FileNotFoundError:
            # Si no se encuentra el archivo, se asume que el argumento es el texto de entrada directamente
            mensaje.set("Error: Archivo no encontrado")
            return
        
        # Reiniciar el contador de líneas en el lexer
        reset_lexer()
        
        # Limpiar la tabla si ya tiene elementos
        for child in frame_lexico.winfo_children():
            child.destroy()

        # Crear encabezados de la tabla
        tree = ttk.Treeview(frame_lexico, columns=('Token', 'Lexema', 'Fila', 'Columna'), show='headings')
        tree.heading('Token', text='Token')
        tree.heading('Lexema', text='Lexema')
        tree.heading('Fila', text='Fila')
        tree.heading('Columna', text='Columna')
        tree.pack(fill='both', expand=True)

       # Ajustar las columnas para llenar el espacio
        tree.column('Token', width=150, anchor='center')
        tree.column('Lexema', width=150, anchor='center')
        tree.column('Fila', width=50, anchor='center')
        tree.column('Columna', width=50, anchor='center')
        
        # Ejecutar el análisis léxico
        tokens, errors = test_lexer(input_text, source='gui')

        # Insertar los tokens en la tabla
        if tokens:
            for token in tokens:
                token_data = (token.type, token.value, token.lineno, token.lexpos)
                tree.insert('', 'end', values=token_data)

        # Mostrar errores en pantalla_errores
        pantalla_errores.config(state='normal')
        pantalla_errores.delete(1.0, END)
        if errors:
            for error in errors:
                mostrar_mensaje_en_rojo(pantalla_errores, error[3])
            mensaje.set("Error en análisis léxico. Corrija los errores y vuelva a ejecutar.")
            pantalla_errores.config(state='disabled')
        else:
            mensaje.set("Análisis léxico completado. Tokens generados.")
            pantalla_errores.config(state='disabled')
            # Ahora que el análisis léxico ha terminado correctamente, ejecutamos el análisis sintáctico
            texto = tokens_to_text(tokens)
            run_syntax_analysis(mensaje, texto, frame_sintactico, pantalla_errores, tokens)
            run_semantic_analysis(mensaje, texto, frame_semantico, pantalla_errores, tokens)
    else:
        mensaje.set("No hay archivo abierto para ejecutar análisis léxico.")

def run_syntax_analysis(mensaje, texto, frame_sintactico, pantalla_errores, tokens):
    mensaje.set("Ejecutando análisis sintáctico...")

    if tokens:
        for child in frame_sintactico.winfo_children():
            child.destroy()

        tree = ttk.Treeview(frame_sintactico, columns=('Nodo', 'Valor'), show='headings')
        tree.heading('Nodo', text='Nodo')
        tree.heading('Valor', text='Valor')
        tree.pack(fill='both', expand=True)

        tree.column('Nodo', width=150, anchor='center')
        tree.column('Valor', width=150, anchor='center')

        result, errors = parse_code(texto)

        if result:
            calculate_levels(result)
            def add_nodes(tree, node, parent=''):
                tree.insert(parent, 'end', text=str(node), values=(node.type, node.level))
                for child in node.children:
                    add_nodes(tree, child, parent)

            add_nodes(tree, result)
            mensaje.set("Análisis sintáctico completado.")
        else:
            # Manejo de errores sintácticos
            # Mostrar errores en pantalla_errores
            pantalla_errores.config(state='normal')
            #pantalla_errores.delete(1.0, END)
            if errors:
                for error in errors:
                    mostrar_mensaje_en_rojo(pantalla_errores, error)
            mensaje.set("Análisis sintáctico fallido.")
            pantalla_errores.config(state='disabled')
            #error_message = result
            #mensaje.set(error_message)
            #mostrar_mensaje_en_rojo(pantalla_errores, error_message)
            #mensaje.set("Análisis sintáctico fallido.")

    else:
        mensaje.set("No hay archivo abierto para ejecutar análisis sintáctico.")

# Actualización de la lógica de análisis semántico
def run_semantic_analysis(mensaje, texto, frame_semantico, pantalla_errores, tokens):
    mensaje.set("Ejecutando análisis semántico...")

    for child in frame_semantico.winfo_children():
        child.destroy()

    # Crear el Treeview para el árbol semántico
    tree_semantico = ttk.Treeview(frame_semantico, columns=('Anotación'), show='headings')
    tree_semantico.heading('Anotación', text='Árbol Semántico Anotado')
    tree_semantico.pack(fill='both', expand=True)

    # Crear el Treeview para la tabla de símbolos
    tree_simbolos = ttk.Treeview(frame_semantico, columns=('Variable', 'Número de Línea', 'Valor', 'Tipo'), show='headings')
    tree_simbolos.heading('Variable', text='Variable')
    tree_simbolos.heading('Número de Línea', text='Número de Línea')
    tree_simbolos.heading('Valor', text='Valor')
    tree_simbolos.heading('Tipo', text='Tipo')
    tree_simbolos.pack(fill='both', expand=True)

    tree_simbolos.column('Variable', width=150, anchor='center')
    tree_simbolos.column('Número de Línea', width=100, anchor='center')
    tree_simbolos.column('Valor', width=100, anchor='center')
    tree_simbolos.column('Tipo', width=100, anchor='center')

    symbols_table = []

    for i, token in enumerate(tokens):
        if token.type == "IDENTIFIER":
            symbol_name = token.value
            symbol_line = token.lineno

            if i > 0 and tokens[i-1].type in ["int", "float", "string", "bool"]:
                symbol_type = tokens[i-1].type
            else:
                symbol_type = "unknown"

            symbol_value = None
            if i + 2 < len(tokens) and tokens[i + 1].type == "ASSIGN":
                symbol_value = tokens[i + 2].value

            symbol = {
                "name": symbol_name,
                "line": symbol_line,
                "value": symbol_value,
                "type": symbol_type
            }
            symbols_table.append(symbol)

            # Insertar el nodo en el árbol semántico
            parent_node = tree_semantico.insert('', 'end', text=f"Variable: {symbol_name} (línea {symbol_line})", values=(symbol_value,))
            tree_simbolos.insert('', 'end', values=(symbol_name, symbol_line, symbol_value, symbol_type))

            # Aquí puedes agregar más nodos o anotaciones si es necesario
            # Por ejemplo, para cada declaración, podrías agregar su tipo o valor

    mensaje.set("Análisis semántico completado.")


def tokens_to_text(tokens):
    """
    Convierte una lista de tokens en texto plano.
    """
    return ' '.join(str(token.value) for token in tokens)

def highlight_syntax(texto):
    
    keywords = ['int', 'float', 'if', 'else', 'for', 'while', 'do']

    # Borrar estilos anteriores
    texto.tag_remove('keyword', '1.0', 'end')
    texto.tag_remove('string', '1.0', 'end')
    texto.tag_remove('comment_line', '1.0', 'end')
    texto.tag_remove('comment_block', '1.0', 'end')

    # Resaltado de palabras clave
    for kw in keywords:
        start = '1.0'
        while True:
            start = texto.search(kw, start, stopindex='end', regexp=True, count='1')
            if not start:
                break
            end = f"{start}+{len(kw)}c"
            texto.tag_add('keyword', start, end)
            start = end

    # Resaltado de texto entre comillas
    start = '1.0'
    while True:
        start = texto.search('"', start, stopindex='end', count='1')
        if not start:
            break
        end = texto.search('"', f"{start}+1c", stopindex='end', count='1')
        if not end:
            break
        texto.tag_add('string', start, f"{end}+1c")
        start = f"{end}+1c"

    # Resaltado de comentarios de línea (//)
    start = '1.0'
    while True:
        start = texto.search('//', start, stopindex='end', count='1')
        if not start:
            break
        end = texto.search('\n', f"{start} lineend", stopindex='end', count='1')
        if not end:
            end = 'end'
        texto.tag_add('comment_line', start, end)
        start = end

    # Resaltado de comentarios de bloque (/* ... */)
    start = '1.0'
    while True:
        start = texto.search('/*', start, stopindex='end', count='1')
        if not start:
            break
        end = texto.search('*/', f"{start}+2c", stopindex='end', count='1')
        if not end:
            end = 'end'
        texto.tag_add('comment_block', start, end+'+2c')
        start = end+'+2c'

    # Estilos para tags
    texto.tag_configure('keyword', foreground='blue')
    texto.tag_configure('string', foreground='#ba6b2b')
    texto.tag_configure('comment_line', foreground='green')
    texto.tag_configure('comment_block', foreground='green')
