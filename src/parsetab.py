
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AN ARE BY COLON COMMA DIVIDED FALSE ID IS IS_UP LENGTH MINUS NEGATIVE NUMBER OF PERIOD PLUS QUEST THE THE_UP TIMES TRUE WHATprogram : program sentence\n               | sentencesentence : expression PERIOD\n                | definition PERIOD\n                | modification PERIOD\n                | question QUESTexpression : termexpression : expression PLUS term\n                  | expression MINUS term\n        term      : term TIMES factor\n                  | term DIVIDED BY factorterm : factorfactor : numberdefinition : id IS A id\n                  | id IS AN id\n                  | id ARE COLON list\n                  | id IS COLON list\n                  | id IS datatype\n                  | id IS expressionmodification : THE_UP id OF id IS entity\n                    | THE_UP id OF id IS list\n                    | THE_UP id OF id ARE listquestion : WHAT IS id\n                | WHAT ARE list\n                | WHAT IS THE id OF id\n                | WHAT ARE THE id OF id\n                | WHAT ARE id OF id\n                | WHAT IS id OF idquestion :  WHAT IS THE LENGTH OF COLON list\n                | WHAT IS THE LENGTH OF idquestion : IS_UP id A id\n                | IS_UP id AN id\n                | IS_UP id identity : id\n              | datatypedatatype : number\n                | boollist : entity COMMA list\n            | entitybool : TRUE\n            | FALSEnumber : NUMBER\n              | NEGATIVE NUMBERid : ID'
    
_lr_action_items = {'THE_UP':([0,1,2,17,18,21,22,23,],[9,9,-2,-1,-3,-4,-5,-6,]),'WHAT':([0,1,2,17,18,21,22,23,],[10,10,-2,-1,-3,-4,-5,-6,]),'IS_UP':([0,1,2,17,18,21,22,23,],[11,11,-2,-1,-3,-4,-5,-6,]),'ID':([0,1,2,9,11,13,17,18,21,22,23,29,30,31,37,38,39,46,47,49,51,57,58,66,70,71,74,75,77,78,79,86,],[13,13,-2,13,13,-44,-1,-3,-4,-5,-6,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'NUMBER':([0,1,2,16,17,18,19,20,21,22,23,24,26,30,36,39,46,71,74,75,86,],[15,15,-2,32,-1,-3,15,15,-4,-5,-6,15,15,15,15,15,15,15,15,15,15,]),'NEGATIVE':([0,1,2,17,18,19,20,21,22,23,24,26,30,36,39,46,71,74,75,86,],[16,16,-2,-1,-3,16,16,-4,-5,-6,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,2,17,18,21,22,23,],[0,-2,-1,-3,-4,-5,-6,]),'PERIOD':([3,4,5,7,12,13,14,15,32,33,34,35,40,41,42,43,44,45,53,54,55,59,60,61,62,63,64,81,82,83,84,],[18,21,22,-7,-12,-44,-13,-42,-43,-8,-9,-10,-18,-19,-13,-37,-40,-41,-39,-35,-36,-11,-14,-15,-34,-17,-16,-38,-20,-21,-22,]),'PLUS':([3,7,12,14,15,32,33,34,35,41,42,59,],[19,-7,-12,-13,-42,-43,-8,-9,-10,19,-13,-11,]),'MINUS':([3,7,12,14,15,32,33,34,35,41,42,59,],[20,-7,-12,-13,-42,-43,-8,-9,-10,20,-13,-11,]),'QUEST':([6,13,15,32,43,44,45,48,50,52,53,54,55,56,62,72,73,76,80,81,85,87,88,89,],[23,-44,-42,-43,-37,-40,-41,-23,-24,-34,-39,-35,-36,-33,-34,-31,-32,-28,-27,-38,-25,-30,-26,-29,]),'TIMES':([7,12,14,15,32,33,34,35,42,59,],[24,-12,-13,-42,-43,24,24,-10,-13,-11,]),'DIVIDED':([7,12,14,15,32,33,34,35,42,59,],[25,-12,-13,-42,-43,25,25,-10,-13,-11,]),'IS':([8,10,13,65,],[26,29,-44,74,]),'ARE':([8,10,13,65,],[27,30,-44,75,]),'OF':([13,28,48,52,67,68,69,],[-44,47,66,70,77,78,79,]),'A':([13,26,31,],[-44,37,57,]),'AN':([13,26,31,],[-44,38,58,]),'COMMA':([13,15,32,43,44,45,52,53,54,55,62,82,],[-44,-42,-43,-37,-40,-41,-34,71,-35,-36,-34,71,]),'BY':([25,],[36,]),'COLON':([26,27,78,],[39,46,86,]),'TRUE':([26,30,39,46,71,74,75,86,],[44,44,44,44,44,44,44,44,]),'FALSE':([26,30,39,46,71,74,75,86,],[45,45,45,45,45,45,45,45,]),'THE':([29,30,],[49,51,]),'LENGTH':([49,],[68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'sentence':([0,1,],[2,17,]),'expression':([0,1,26,],[3,3,41,]),'definition':([0,1,],[4,4,]),'modification':([0,1,],[5,5,]),'question':([0,1,],[6,6,]),'term':([0,1,19,20,26,],[7,7,33,34,7,]),'id':([0,1,9,11,29,30,31,37,38,39,46,47,49,51,57,58,66,70,71,74,75,77,78,79,86,],[8,8,28,31,48,52,56,60,61,62,62,65,67,69,72,73,76,80,62,62,62,85,87,88,62,]),'factor':([0,1,19,20,24,26,36,],[12,12,12,12,35,12,59,]),'number':([0,1,19,20,24,26,30,36,39,46,71,74,75,86,],[14,14,14,14,14,42,55,14,55,55,55,55,55,55,]),'datatype':([26,30,39,46,71,74,75,86,],[40,54,54,54,54,54,54,54,]),'bool':([26,30,39,46,71,74,75,86,],[43,43,43,43,43,43,43,43,]),'list':([30,39,46,71,74,75,86,],[50,63,64,81,83,84,89,]),'entity':([30,39,46,71,74,75,86,],[53,53,53,53,82,53,53,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program sentence','program',2,'p_program','dparse.py',9),
  ('program -> sentence','program',1,'p_program','dparse.py',10),
  ('sentence -> expression PERIOD','sentence',2,'p_sentence','dparse.py',27),
  ('sentence -> definition PERIOD','sentence',2,'p_sentence','dparse.py',28),
  ('sentence -> modification PERIOD','sentence',2,'p_sentence','dparse.py',29),
  ('sentence -> question QUEST','sentence',2,'p_sentence','dparse.py',30),
  ('expression -> term','expression',1,'p_expression','dparse.py',39),
  ('expression -> expression PLUS term','expression',3,'p_binary_operators','dparse.py',45),
  ('expression -> expression MINUS term','expression',3,'p_binary_operators','dparse.py',46),
  ('term -> term TIMES factor','term',3,'p_binary_operators','dparse.py',47),
  ('term -> term DIVIDED BY factor','term',4,'p_binary_operators','dparse.py',48),
  ('term -> factor','term',1,'p_term','dparse.py',65),
  ('factor -> number','factor',1,'p_factor','dparse.py',71),
  ('definition -> id IS A id','definition',4,'p_definition','dparse.py',77),
  ('definition -> id IS AN id','definition',4,'p_definition','dparse.py',78),
  ('definition -> id ARE COLON list','definition',4,'p_definition','dparse.py',79),
  ('definition -> id IS COLON list','definition',4,'p_definition','dparse.py',80),
  ('definition -> id IS datatype','definition',3,'p_definition','dparse.py',81),
  ('definition -> id IS expression','definition',3,'p_definition','dparse.py',82),
  ('modification -> THE_UP id OF id IS entity','modification',6,'p_modification','dparse.py',91),
  ('modification -> THE_UP id OF id IS list','modification',6,'p_modification','dparse.py',92),
  ('modification -> THE_UP id OF id ARE list','modification',6,'p_modification','dparse.py',93),
  ('question -> WHAT IS id','question',3,'p_question','dparse.py',98),
  ('question -> WHAT ARE list','question',3,'p_question','dparse.py',99),
  ('question -> WHAT IS THE id OF id','question',6,'p_question','dparse.py',100),
  ('question -> WHAT ARE THE id OF id','question',6,'p_question','dparse.py',101),
  ('question -> WHAT ARE id OF id','question',5,'p_question','dparse.py',102),
  ('question -> WHAT IS id OF id','question',5,'p_question','dparse.py',103),
  ('question -> WHAT IS THE LENGTH OF COLON list','question',7,'p_question_length','dparse.py',113),
  ('question -> WHAT IS THE LENGTH OF id','question',6,'p_question_length','dparse.py',114),
  ('question -> IS_UP id A id','question',4,'p_question_is','dparse.py',122),
  ('question -> IS_UP id AN id','question',4,'p_question_is','dparse.py',123),
  ('question -> IS_UP id id','question',3,'p_question_is','dparse.py',124),
  ('entity -> id','entity',1,'p_entity','dparse.py',143),
  ('entity -> datatype','entity',1,'p_entity','dparse.py',144),
  ('datatype -> number','datatype',1,'p_datatype','dparse.py',150),
  ('datatype -> bool','datatype',1,'p_datatype','dparse.py',151),
  ('list -> entity COMMA list','list',3,'p_list','dparse.py',157),
  ('list -> entity','list',1,'p_list','dparse.py',158),
  ('bool -> TRUE','bool',1,'p_bool','dparse.py',167),
  ('bool -> FALSE','bool',1,'p_bool','dparse.py',168),
  ('number -> NUMBER','number',1,'p_number','dparse.py',177),
  ('number -> NEGATIVE NUMBER','number',2,'p_number','dparse.py',178),
  ('id -> ID','id',1,'p_id','dparse.py',187),
]
