
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOL BREAK COMMA DIVIDE DO ELSE EQ FALSE FI FLOAT GE GT IDENTIFIER IF INT LBRACE LE LPAREN LT MINUS NE NOT NUMBER OR PLUS POWER PROGRAM RBRACE READ RPAREN SEMICOLON THEN TIMES TRUE UNTIL WHILE WRITEprogram : PROGRAM LBRACE list_decl list_sent RBRACElist_decl : list_decl decl\n                 | decl\n                 | emptydecl : tipo list_id SEMICOLONtipo : INT\n            | FLOAT\n            | BOOLlist_id : list_id COMMA IDENTIFIER\n               | IDENTIFIERlist_sent : list_sent sent\n                 | sent\n                 | emptysent : sent_if\n            | sent_while\n            | sent_do\n            | sent_read\n            | sent_write\n            | bloque\n            | sent_assign\n            | BREAKsent_if : IF LPAREN exp_bool RPAREN THEN bloque else_part FIelse_part : ELSE bloque\n                 | emptysent_while : WHILE LPAREN exp_bool RPAREN bloquesent_do : DO bloque UNTIL LPAREN exp_bool RPAREN SEMICOLONsent_read : READ IDENTIFIER SEMICOLONsent_write : WRITE exp_bool_or_value SEMICOLONexp_value : NUMBER\n                 | IDENTIFIERbloque : LBRACE list_sent RBRACEsent_assign : IDENTIFIER ASSIGN expr SEMICOLONsent_assign : IDENTIFIER ASSIGN exp_bool SEMICOLONsent_assign : IDENTIFIER ASSIGN factor SEMICOLONexp_bool : exp_bool OR comb\n                | exp_bool OR expr\n                | combexp_bool_or_value : exp_bool\n                         | exp_valuecomb : comb AND igualdad\n            | comb AND expr\n            | igualdadigualdad : igualdad EQ rel\n                | igualdad NE rel\n                | relrel : expr op_rel exprop_rel : LT\n              | LE\n              | GT\n              | GE\n              | EQ\n              | NEexpr : expr PLUS term\n            | expr MINUS term\n            | termterm : term TIMES unario\n            | term DIVIDE unario\n            | unariounario : PLUS unario\n              | MINUS unario\n              | factorfactor : NUMBER\n              | IDENTIFIER\n              | TRUE\n              | FALSE\n              | LPAREN expr RPAREN\n              | LPAREN exp_bool RPARENempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,33,],[0,-1,]),'LBRACE':([2,3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,26,32,34,57,59,65,69,91,93,94,95,109,110,115,117,118,],[3,-68,11,-3,-4,11,11,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,11,11,-11,-5,-31,-27,-28,11,-32,-33,-34,11,-25,11,-26,-22,]),'BREAK':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,23,-3,-4,23,23,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,23,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'INT':([3,4,5,6,13,57,],[8,8,-3,-4,-2,-5,]),'FLOAT':([3,4,5,6,13,57,],[9,9,-3,-4,-2,-5,]),'BOOL':([3,4,5,6,13,57,],[10,10,-3,-4,-2,-5,]),'IF':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,24,-3,-4,24,24,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,24,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'WHILE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,25,-3,-4,25,25,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,25,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'DO':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,26,-3,-4,26,26,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,26,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'READ':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,27,-3,-4,27,27,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,27,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'WRITE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,29,-3,-4,29,29,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,29,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'IDENTIFIER':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27,29,32,34,35,36,39,49,51,56,57,58,59,65,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,92,93,94,95,110,117,118,],[-68,28,-3,-4,31,-6,-7,-8,28,28,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,38,46,28,-11,62,62,62,62,62,62,-5,89,-31,-27,-28,62,62,62,62,62,-47,-48,-49,-50,-51,-52,62,62,62,62,62,-32,-33,-34,-25,-26,-22,]),'RBRACE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,32,34,57,59,65,69,93,94,95,110,117,118,],[-68,-68,-3,-4,-68,33,-2,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,59,-11,-5,-31,-27,-28,-32,-33,-34,-25,-26,-22,]),'LPAREN':([24,25,29,35,36,39,49,51,56,64,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,92,],[35,36,56,56,56,56,56,56,56,92,56,56,56,56,56,-47,-48,-49,-50,-51,-52,56,56,56,56,56,]),'ASSIGN':([28,],[39,]),'NUMBER':([29,35,36,39,49,51,56,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,92,],[45,61,61,61,61,61,61,61,61,61,61,61,-47,-48,-49,-50,-51,-52,61,61,61,61,61,]),'PLUS':([29,35,36,39,44,45,46,49,50,51,52,53,54,55,56,61,62,66,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,92,97,99,100,101,102,105,106,107,108,],[49,49,49,49,73,-62,-63,49,-55,49,-58,-61,-64,-65,49,-62,-63,73,-61,49,49,49,49,49,-47,-48,-49,-50,-51,-52,49,49,-59,49,49,-60,73,49,73,73,73,-53,-54,-56,-57,-66,-67,]),'MINUS':([29,35,36,39,44,45,46,49,50,51,52,53,54,55,56,61,62,66,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,92,97,99,100,101,102,105,106,107,108,],[51,51,51,51,74,-62,-63,51,-55,51,-58,-61,-64,-65,51,-62,-63,74,-61,51,51,51,51,51,-47,-48,-49,-50,-51,-52,51,51,-59,51,51,-60,74,51,74,74,74,-53,-54,-56,-57,-66,-67,]),'TRUE':([29,35,36,39,49,51,56,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,92,],[54,54,54,54,54,54,54,54,54,54,54,54,-47,-48,-49,-50,-51,-52,54,54,54,54,54,]),'FALSE':([29,35,36,39,49,51,56,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,92,],[55,55,55,55,55,55,55,55,55,55,55,55,-47,-48,-49,-50,-51,-52,55,55,55,55,55,]),'SEMICOLON':([30,31,38,40,41,42,43,45,46,47,48,50,52,53,54,55,61,62,66,67,68,83,86,89,96,97,98,99,100,101,102,103,104,105,106,107,108,113,],[57,-10,65,69,-38,-39,-37,-29,-30,-42,-45,-55,-58,-61,-64,-65,-62,-63,93,94,95,-59,-60,-9,-35,-36,-40,-41,-46,-53,-54,-43,-44,-56,-57,-66,-67,117,]),'COMMA':([30,31,89,],[58,-10,-9,]),'UNTIL':([37,59,],[64,-31,]),'OR':([41,43,47,48,50,52,53,54,55,60,61,62,63,67,83,86,88,96,97,98,99,100,101,102,103,104,105,106,107,108,111,],[70,-37,-42,-45,-55,-58,-61,-64,-65,70,-62,-63,70,70,-59,-60,70,-35,-36,-40,-41,-46,-53,-54,-43,-44,-56,-57,-66,-67,70,]),'RPAREN':([43,47,48,50,52,53,54,55,60,61,62,63,83,86,87,88,96,97,98,99,100,101,102,103,104,105,106,107,108,111,],[-37,-42,-45,-55,-58,-61,-64,-65,90,-62,-63,91,-59,-60,107,108,-35,-36,-40,-41,-46,-53,-54,-43,-44,-56,-57,-66,-67,113,]),'AND':([43,47,48,50,52,53,54,55,61,62,83,86,96,98,99,100,101,102,103,104,105,106,107,108,],[71,-42,-45,-55,-58,-61,-64,-65,-62,-63,-59,-60,71,-40,-41,-46,-53,-54,-43,-44,-56,-57,-66,-67,]),'LT':([44,45,46,50,52,53,54,55,61,62,66,68,83,86,87,97,99,101,102,105,106,107,108,],[75,-62,-63,-55,-58,-61,-64,-65,-62,-63,75,-61,-59,-60,75,75,75,-53,-54,-56,-57,-66,-67,]),'LE':([44,45,46,50,52,53,54,55,61,62,66,68,83,86,87,97,99,101,102,105,106,107,108,],[76,-62,-63,-55,-58,-61,-64,-65,-62,-63,76,-61,-59,-60,76,76,76,-53,-54,-56,-57,-66,-67,]),'GT':([44,45,46,50,52,53,54,55,61,62,66,68,83,86,87,97,99,101,102,105,106,107,108,],[77,-62,-63,-55,-58,-61,-64,-65,-62,-63,77,-61,-59,-60,77,77,77,-53,-54,-56,-57,-66,-67,]),'GE':([44,45,46,50,52,53,54,55,61,62,66,68,83,86,87,97,99,101,102,105,106,107,108,],[78,-62,-63,-55,-58,-61,-64,-65,-62,-63,78,-61,-59,-60,78,78,78,-53,-54,-56,-57,-66,-67,]),'EQ':([44,45,46,47,48,50,52,53,54,55,61,62,66,68,83,86,87,97,98,99,100,101,102,103,104,105,106,107,108,],[79,-62,-63,81,-45,-55,-58,-61,-64,-65,-62,-63,79,-61,-59,-60,79,79,81,79,-46,-53,-54,-43,-44,-56,-57,-66,-67,]),'NE':([44,45,46,47,48,50,52,53,54,55,61,62,66,68,83,86,87,97,98,99,100,101,102,103,104,105,106,107,108,],[80,-62,-63,82,-45,-55,-58,-61,-64,-65,-62,-63,80,-61,-59,-60,80,80,82,80,-46,-53,-54,-43,-44,-56,-57,-66,-67,]),'TIMES':([45,46,50,52,53,54,55,61,62,68,83,86,101,102,105,106,107,108,],[-62,-63,84,-58,-61,-64,-65,-62,-63,-61,-59,-60,84,84,-56,-57,-66,-67,]),'DIVIDE':([45,46,50,52,53,54,55,61,62,68,83,86,101,102,105,106,107,108,],[-62,-63,85,-58,-61,-64,-65,-62,-63,-61,-59,-60,85,85,-56,-57,-66,-67,]),'ELSE':([59,112,],[-31,115,]),'FI':([59,112,114,116,119,],[-31,-68,118,-24,-23,]),'THEN':([90,],[109,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'list_decl':([3,],[4,]),'decl':([3,4,],[5,13,]),'empty':([3,4,11,112,],[6,15,15,116,]),'tipo':([3,4,],[7,7,]),'list_sent':([4,11,],[12,32,]),'sent':([4,11,12,32,],[14,14,34,34,]),'sent_if':([4,11,12,32,],[16,16,16,16,]),'sent_while':([4,11,12,32,],[17,17,17,17,]),'sent_do':([4,11,12,32,],[18,18,18,18,]),'sent_read':([4,11,12,32,],[19,19,19,19,]),'sent_write':([4,11,12,32,],[20,20,20,20,]),'bloque':([4,11,12,26,32,91,109,115,],[21,21,21,37,21,110,112,119,]),'sent_assign':([4,11,12,32,],[22,22,22,22,]),'list_id':([7,],[30,]),'exp_bool_or_value':([29,],[40,]),'exp_bool':([29,35,36,39,56,92,],[41,60,63,67,88,111,]),'exp_value':([29,],[42,]),'comb':([29,35,36,39,56,70,92,],[43,43,43,43,43,96,43,]),'expr':([29,35,36,39,56,70,71,72,81,82,92,],[44,44,44,66,87,97,99,100,44,44,44,]),'igualdad':([29,35,36,39,56,70,71,92,],[47,47,47,47,47,47,98,47,]),'rel':([29,35,36,39,56,70,71,81,82,92,],[48,48,48,48,48,48,48,103,104,48,]),'term':([29,35,36,39,56,70,71,72,73,74,81,82,92,],[50,50,50,50,50,50,50,50,101,102,50,50,50,]),'unario':([29,35,36,39,49,51,56,70,71,72,73,74,81,82,84,85,92,],[52,52,52,52,83,86,52,52,52,52,52,52,52,52,105,106,52,]),'factor':([29,35,36,39,49,51,56,70,71,72,73,74,81,82,84,85,92,],[53,53,53,68,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'op_rel':([44,66,87,97,99,],[72,72,72,72,72,]),'else_part':([112,],[114,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM LBRACE list_decl list_sent RBRACE','program',5,'p_program','sintac.py',33),
  ('list_decl -> list_decl decl','list_decl',2,'p_list_decl','sintac.py',37),
  ('list_decl -> decl','list_decl',1,'p_list_decl','sintac.py',38),
  ('list_decl -> empty','list_decl',1,'p_list_decl','sintac.py',39),
  ('decl -> tipo list_id SEMICOLON','decl',3,'p_decl','sintac.py',46),
  ('tipo -> INT','tipo',1,'p_tipo','sintac.py',50),
  ('tipo -> FLOAT','tipo',1,'p_tipo','sintac.py',51),
  ('tipo -> BOOL','tipo',1,'p_tipo','sintac.py',52),
  ('list_id -> list_id COMMA IDENTIFIER','list_id',3,'p_list_id','sintac.py',56),
  ('list_id -> IDENTIFIER','list_id',1,'p_list_id','sintac.py',57),
  ('list_sent -> list_sent sent','list_sent',2,'p_list_sent','sintac.py',64),
  ('list_sent -> sent','list_sent',1,'p_list_sent','sintac.py',65),
  ('list_sent -> empty','list_sent',1,'p_list_sent','sintac.py',66),
  ('sent -> sent_if','sent',1,'p_sent','sintac.py',73),
  ('sent -> sent_while','sent',1,'p_sent','sintac.py',74),
  ('sent -> sent_do','sent',1,'p_sent','sintac.py',75),
  ('sent -> sent_read','sent',1,'p_sent','sintac.py',76),
  ('sent -> sent_write','sent',1,'p_sent','sintac.py',77),
  ('sent -> bloque','sent',1,'p_sent','sintac.py',78),
  ('sent -> sent_assign','sent',1,'p_sent','sintac.py',79),
  ('sent -> BREAK','sent',1,'p_sent','sintac.py',80),
  ('sent_if -> IF LPAREN exp_bool RPAREN THEN bloque else_part FI','sent_if',8,'p_sent_if','sintac.py',84),
  ('else_part -> ELSE bloque','else_part',2,'p_else_part','sintac.py',88),
  ('else_part -> empty','else_part',1,'p_else_part','sintac.py',89),
  ('sent_while -> WHILE LPAREN exp_bool RPAREN bloque','sent_while',5,'p_sent_while','sintac.py',93),
  ('sent_do -> DO bloque UNTIL LPAREN exp_bool RPAREN SEMICOLON','sent_do',7,'p_sent_do','sintac.py',97),
  ('sent_read -> READ IDENTIFIER SEMICOLON','sent_read',3,'p_sent_read','sintac.py',101),
  ('sent_write -> WRITE exp_bool_or_value SEMICOLON','sent_write',3,'p_sent_write','sintac.py',105),
  ('exp_value -> NUMBER','exp_value',1,'p_exp_value','sintac.py',109),
  ('exp_value -> IDENTIFIER','exp_value',1,'p_exp_value','sintac.py',110),
  ('bloque -> LBRACE list_sent RBRACE','bloque',3,'p_bloque','sintac.py',114),
  ('sent_assign -> IDENTIFIER ASSIGN expr SEMICOLON','sent_assign',4,'p_sent_assign_expr','sintac.py',118),
  ('sent_assign -> IDENTIFIER ASSIGN exp_bool SEMICOLON','sent_assign',4,'p_sent_assign_exp_bool','sintac.py',122),
  ('sent_assign -> IDENTIFIER ASSIGN factor SEMICOLON','sent_assign',4,'p_sent_assign_factor','sintac.py',126),
  ('exp_bool -> exp_bool OR comb','exp_bool',3,'p_exp_bool','sintac.py',130),
  ('exp_bool -> exp_bool OR expr','exp_bool',3,'p_exp_bool','sintac.py',131),
  ('exp_bool -> comb','exp_bool',1,'p_exp_bool','sintac.py',132),
  ('exp_bool_or_value -> exp_bool','exp_bool_or_value',1,'p_exp_bool_or_value','sintac.py',139),
  ('exp_bool_or_value -> exp_value','exp_bool_or_value',1,'p_exp_bool_or_value','sintac.py',140),
  ('comb -> comb AND igualdad','comb',3,'p_comb','sintac.py',145),
  ('comb -> comb AND expr','comb',3,'p_comb','sintac.py',146),
  ('comb -> igualdad','comb',1,'p_comb','sintac.py',147),
  ('igualdad -> igualdad EQ rel','igualdad',3,'p_igualdad','sintac.py',154),
  ('igualdad -> igualdad NE rel','igualdad',3,'p_igualdad','sintac.py',155),
  ('igualdad -> rel','igualdad',1,'p_igualdad','sintac.py',156),
  ('rel -> expr op_rel expr','rel',3,'p_rel','sintac.py',164),
  ('op_rel -> LT','op_rel',1,'p_op_rel','sintac.py',168),
  ('op_rel -> LE','op_rel',1,'p_op_rel','sintac.py',169),
  ('op_rel -> GT','op_rel',1,'p_op_rel','sintac.py',170),
  ('op_rel -> GE','op_rel',1,'p_op_rel','sintac.py',171),
  ('op_rel -> EQ','op_rel',1,'p_op_rel','sintac.py',172),
  ('op_rel -> NE','op_rel',1,'p_op_rel','sintac.py',173),
  ('expr -> expr PLUS term','expr',3,'p_expr','sintac.py',177),
  ('expr -> expr MINUS term','expr',3,'p_expr','sintac.py',178),
  ('expr -> term','expr',1,'p_expr','sintac.py',179),
  ('term -> term TIMES unario','term',3,'p_term','sintac.py',186),
  ('term -> term DIVIDE unario','term',3,'p_term','sintac.py',187),
  ('term -> unario','term',1,'p_term','sintac.py',188),
  ('unario -> PLUS unario','unario',2,'p_unario','sintac.py',195),
  ('unario -> MINUS unario','unario',2,'p_unario','sintac.py',196),
  ('unario -> factor','unario',1,'p_unario','sintac.py',197),
  ('factor -> NUMBER','factor',1,'p_factor','sintac.py',204),
  ('factor -> IDENTIFIER','factor',1,'p_factor','sintac.py',205),
  ('factor -> TRUE','factor',1,'p_factor','sintac.py',206),
  ('factor -> FALSE','factor',1,'p_factor','sintac.py',207),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','sintac.py',208),
  ('factor -> LPAREN exp_bool RPAREN','factor',3,'p_factor','sintac.py',209),
  ('empty -> <empty>','empty',0,'p_empty','sintac.py',216),
]
