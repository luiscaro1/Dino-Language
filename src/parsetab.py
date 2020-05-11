
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AN ARE ARE_UP BY COLON COMMA DIVIDED FALSE ID IS IS_UP MINUS NEGATIVE NUMBER PERIOD PLUS QUEST TIMES TRUE WHATprogram : program sentence\n               | sentencesentence : expression PERIOD\n                | definition PERIOD\n                | questionexpression : termexpression : expression PLUS term\n                  | expression MINUS term\n        term      : term TIMES factor\n                  | term DIVIDED BY factorterm : factorfactor : numberdefinition : id IS A id\n                  | id IS AN id\n                  | id ARE COLON list\n                  | id IS COLON list\n                  | id IS datatypequestion : WHAT IS entity QUESTquestion : IS_UP entity bool QUEST\n                | IS_UP entity A datatype QUEST\n                | IS_UP entity entity QUESTquestion : ARE_UP list entity QUEST\n                | ARE_UP entity A datatype QUESTentity : id\n              | datatypedatatype : number\n                | boollist : entity COMMA list\n            | entitybool : TRUE\n            | FALSEnumber : NUMBER\n              | NEGATIVE NUMBERid : ID'
    
_lr_action_items = {'WHAT':([0,1,2,5,16,17,20,58,59,60,62,65,66,],[8,8,-2,-5,-1,-3,-4,-18,-21,-19,-22,-20,-23,]),'IS_UP':([0,1,2,5,16,17,20,58,59,60,62,65,66,],[9,9,-2,-5,-1,-3,-4,-18,-21,-19,-22,-20,-23,]),'ARE_UP':([0,1,2,5,16,17,20,58,59,60,62,65,66,],[10,10,-2,-5,-1,-3,-4,-18,-21,-19,-22,-20,-23,]),'ID':([0,1,2,5,9,10,12,14,16,17,20,25,26,27,28,29,30,31,32,33,34,35,40,41,42,44,51,56,58,59,60,62,64,65,66,],[12,12,-2,-5,12,12,-34,-32,-1,-3,-4,12,12,-27,-25,-24,-26,-30,-31,12,-29,-33,12,12,12,12,12,-29,-18,-21,-19,-22,-28,-20,-23,]),'NUMBER':([0,1,2,5,9,10,12,14,15,16,17,18,19,20,21,23,25,26,27,28,29,30,31,32,33,34,35,39,42,44,48,50,51,56,58,59,60,62,64,65,66,],[14,14,-2,-5,14,14,-34,-32,35,-1,-3,14,14,-4,14,14,14,14,-27,-25,-24,-26,-30,-31,14,-29,-33,14,14,14,14,14,14,-29,-18,-21,-19,-22,-28,-20,-23,]),'NEGATIVE':([0,1,2,5,9,10,12,14,16,17,18,19,20,21,23,25,26,27,28,29,30,31,32,33,34,35,39,42,44,48,50,51,56,58,59,60,62,64,65,66,],[15,15,-2,-5,15,15,-34,-32,-1,-3,15,15,-4,15,15,15,15,-27,-25,-24,-26,-30,-31,15,-29,-33,15,15,15,15,15,15,-29,-18,-21,-19,-22,-28,-20,-23,]),'$end':([1,2,5,16,17,20,58,59,60,62,65,66,],[0,-2,-5,-1,-3,-4,-18,-21,-19,-22,-20,-23,]),'PERIOD':([3,4,6,11,12,13,14,27,28,29,30,31,32,35,36,37,38,43,52,53,54,55,56,57,64,],[17,20,-6,-11,-34,-12,-32,-27,-25,-24,-26,-30,-31,-33,-7,-8,-9,-17,-10,-13,-14,-16,-29,-15,-28,]),'PLUS':([3,6,11,13,14,35,36,37,38,52,],[18,-6,-11,-12,-32,-33,-7,-8,-9,-10,]),'MINUS':([3,6,11,13,14,35,36,37,38,52,],[19,-6,-11,-12,-32,-33,-7,-8,-9,-10,]),'TIMES':([6,11,13,14,35,36,37,38,52,],[21,-11,-12,-32,-33,21,21,-9,-10,]),'DIVIDED':([6,11,13,14,35,36,37,38,52,],[22,-11,-12,-32,-33,22,22,-9,-10,]),'IS':([7,8,12,],[23,25,-34,]),'ARE':([7,12,],[24,-34,]),'TRUE':([9,10,12,14,23,25,26,27,28,29,30,31,32,33,34,35,42,44,48,50,51,56,64,],[31,31,-34,-32,31,31,31,-27,-25,-24,-26,-30,-31,31,-29,-33,31,31,31,31,31,-29,-28,]),'FALSE':([9,10,12,14,23,25,26,27,28,29,30,31,32,33,34,35,42,44,48,50,51,56,64,],[32,32,-34,-32,32,32,32,-27,-25,-24,-26,-30,-31,32,-29,-33,32,32,32,32,32,-29,-28,]),'A':([12,14,23,26,27,28,29,30,31,32,34,35,],[-34,-32,40,48,-27,-25,-24,-26,-30,-31,50,-33,]),'COMMA':([12,14,27,28,29,30,31,32,34,35,56,],[-34,-32,-27,-25,-24,-26,-30,-31,51,-33,51,]),'QUEST':([12,14,27,28,29,30,31,32,35,45,46,47,49,61,63,],[-34,-32,-27,-25,-24,-26,-30,-31,-33,58,59,60,62,65,66,]),'BY':([22,],[39,]),'AN':([23,],[41,]),'COLON':([23,24,],[42,44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'sentence':([0,1,],[2,16,]),'expression':([0,1,],[3,3,]),'definition':([0,1,],[4,4,]),'question':([0,1,],[5,5,]),'term':([0,1,18,19,],[6,6,36,37,]),'id':([0,1,9,10,25,26,33,40,41,42,44,51,],[7,7,29,29,29,29,29,53,54,29,29,29,]),'factor':([0,1,18,19,21,39,],[11,11,11,11,38,52,]),'number':([0,1,9,10,18,19,21,23,25,26,33,39,42,44,48,50,51,],[13,13,30,30,13,13,13,30,30,30,30,13,30,30,30,30,30,]),'entity':([9,10,25,26,33,42,44,51,],[26,34,45,46,49,56,56,56,]),'bool':([9,10,23,25,26,33,42,44,48,50,51,],[27,27,27,27,47,27,27,27,27,27,27,]),'datatype':([9,10,23,25,26,33,42,44,48,50,51,],[28,28,43,28,28,28,28,28,61,63,28,]),'list':([10,42,44,51,],[33,55,57,64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program sentence','program',2,'p_program','dparse.py',10),
  ('program -> sentence','program',1,'p_program','dparse.py',11),
  ('sentence -> expression PERIOD','sentence',2,'p_sentence','dparse.py',28),
  ('sentence -> definition PERIOD','sentence',2,'p_sentence','dparse.py',29),
  ('sentence -> question','sentence',1,'p_sentence','dparse.py',30),
  ('expression -> term','expression',1,'p_expression','dparse.py',38),
  ('expression -> expression PLUS term','expression',3,'p_binary_operators','dparse.py',44),
  ('expression -> expression MINUS term','expression',3,'p_binary_operators','dparse.py',45),
  ('term -> term TIMES factor','term',3,'p_binary_operators','dparse.py',46),
  ('term -> term DIVIDED BY factor','term',4,'p_binary_operators','dparse.py',47),
  ('term -> factor','term',1,'p_term','dparse.py',64),
  ('factor -> number','factor',1,'p_factor','dparse.py',70),
  ('definition -> id IS A id','definition',4,'p_definition','dparse.py',76),
  ('definition -> id IS AN id','definition',4,'p_definition','dparse.py',77),
  ('definition -> id ARE COLON list','definition',4,'p_definition','dparse.py',78),
  ('definition -> id IS COLON list','definition',4,'p_definition','dparse.py',79),
  ('definition -> id IS datatype','definition',3,'p_definition','dparse.py',80),
  ('question -> WHAT IS entity QUEST','question',4,'p_question','dparse.py',89),
  ('question -> IS_UP entity bool QUEST','question',4,'p_question_is','dparse.py',94),
  ('question -> IS_UP entity A datatype QUEST','question',5,'p_question_is','dparse.py',95),
  ('question -> IS_UP entity entity QUEST','question',4,'p_question_is','dparse.py',96),
  ('question -> ARE_UP list entity QUEST','question',4,'p_question_are','dparse.py',104),
  ('question -> ARE_UP entity A datatype QUEST','question',5,'p_question_are','dparse.py',105),
  ('entity -> id','entity',1,'p_entity','dparse.py',114),
  ('entity -> datatype','entity',1,'p_entity','dparse.py',115),
  ('datatype -> number','datatype',1,'p_datatype','dparse.py',121),
  ('datatype -> bool','datatype',1,'p_datatype','dparse.py',122),
  ('list -> entity COMMA list','list',3,'p_list','dparse.py',128),
  ('list -> entity','list',1,'p_list','dparse.py',129),
  ('bool -> TRUE','bool',1,'p_bool','dparse.py',140),
  ('bool -> FALSE','bool',1,'p_bool','dparse.py',141),
  ('number -> NUMBER','number',1,'p_number','dparse.py',150),
  ('number -> NEGATIVE NUMBER','number',2,'p_number','dparse.py',151),
  ('id -> ID','id',1,'p_id','dparse.py',160),
]
