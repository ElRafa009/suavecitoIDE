from tkinter import END, Scrollbar, filedialog as FileDialog, ttk
from io import open
from lexer import reset_lexer
from semantic import SemanticAnalyzer, SemanticError
from test_lexer import test_lexer
from sintac import calculate_levels, parse_code, parser

ruta = "" # La utilizaremos para almacenar la ruta del archivo

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
        print(f"Mostrando mensaje: {mensaje}")  # Depuración
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
        
        # Limpiar tabla léxica, sintáctica y semántica
        for child in frame_lexico.winfo_children():
            child.destroy()
        for child in frame_sintactico.winfo_children():
            child.destroy()
        for child in frame_semantico.winfo_children():
            child.destroy()

        # Crear tabla de tokens
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

            # Ejecutar el análisis sintáctico
            run_syntax_analysis(mensaje, tokens_to_text(tokens), frame_sintactico, pantalla_errores, tokens, frame_semantico)

    else:
        mensaje.set("No hay archivo abierto para ejecutar análisis léxico.")

def run_syntax_analysis(mensaje, texto, frame_sintactico, pantalla_errores, tokens, frame_semantico):
    mensaje.set("Ejecutando análisis sintáctico...")

    if tokens:
        # Crear el Treeview para el árbol sintáctico
        tree = ttk.Treeview(frame_sintactico, columns=('Nodo', 'Valor'), show='headings')
        tree.heading('Nodo', text='Nodo')
        tree.heading('Valor', text='Valor')
        tree.pack(fill='both', expand=True)

        tree.column('Nodo', width=150, anchor='center')
        tree.column('Valor', width=150, anchor='center')

        # Ejecutar el análisis sintáctico
        result, errors = parse_code(texto)

        if result:
            calculate_levels(result)
            
            # Función para agregar nodos recursivamente
            def add_nodes(tree, node, parent=''):
                # Añadir el nodo actual al Treeview
                tree_id = tree.insert(parent, 'end', text=str(node), values=(node.type,node.leaf if node.leaf else node.type), open=True)
                # Iterar sobre los hijos del nodo y añadirlos recursivamente
                for child in node.children:
                    add_nodes(tree, child, tree_id)

            # Comenzar desde la raíz del árbol
            add_nodes(tree, result)

            mensaje.set("Análisis sintáctico completado.")
            # Ejecutar análisis semántico

            run_semantic_analysis(result, mensaje, frame_semantico, pantalla_errores)
        else:
            # Manejo de errores sintácticos
            pantalla_errores.config(state='normal')
            if errors:
                for error in errors:
                    mostrar_mensaje_en_rojo(pantalla_errores, error)
            mensaje.set("Análisis sintáctico fallido.")
            pantalla_errores.config(state='disabled')
    else:
        mensaje.set("No hay archivo abierto para ejecutar análisis sintáctico.")

# Función para el análisis semántico
def run_semantic_analysis(result, mensaje, frame_semantico, pantalla_errores):
    mensaje.set("Ejecutando análisis semántico...")
    
    # Crear TreeView para árbol semántico
    tree = ttk.Treeview(frame_semantico, columns=('Nodo', 'Anotación'), show='headings')
    tree.heading('Nodo', text='Nodo')
    tree.heading('Anotación', text='Anotación')
    tree.pack(fill='both', expand=True)
    tree.column('Nodo', width=150, anchor='center')
    tree.column('Anotación', width=150, anchor='center')

    # Crear instancia del analizador semántico
    analyzer = SemanticAnalyzer()
    errors = []  # Lista para almacenar errores semánticos

    try:
        # Realizar análisis semántico
        analyzer.analyze(result)

        # Función para agregar nodos con anotaciones
        def add_semantic_nodes(tree, node, parent=''):
            annotation = getattr(node, 'semantic_annotation', "Sin anotación")
            tree_id = tree.insert(parent, 'end', text=str(node), values=(node.leaf if node.leaf else node.type, annotation), open=True)

            # Propagar las anotaciones a los nodos hijos
            for child in node.children:
                add_semantic_nodes(tree, child, tree_id)

        # Comenzar a agregar nodos desde la raíz del árbol sintáctico
        add_semantic_nodes(tree, result)

        mensaje.set("Análisis semántico completado.")
    except SemanticError as e:
        # Manejo de errores semánticos
        errors.append(str(e))
        print(f"Error semántico: {e}")  # Mensaje de depuración
        mostrar_mensaje_en_rojo(pantalla_errores, str(e))
        mensaje.set("Errores en análisis semántico.")

    # Mostrar errores si hay alguno
    if errors:
        pantalla_errores.config(state='normal')
        for error in errors:
            mostrar_mensaje_en_rojo(pantalla_errores, error)
        pantalla_errores.config(state='disabled')


def tokens_to_text(tokens):
    """
    Convierte una lista de tokens en texto plano.
    """
    return ' '.join(str(token.value) for token in tokens)

def highlight_syntax(texto):
    
    keywords = ['int', 'float', 'if', 'else', 'for', 'while', 'do', 'bool']

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
