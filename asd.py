# -*- coding: utf-8 -*-
"""ASD.ipynb
"""


import sys

class Lexico:
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
                "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_")

    reserved_word = ("var", "print", "input", "when", "if", "unless", "while", "return",
                     "until", "else", "do", "for", "next", "break", "and", "or", "num",
                     "bool", "end", "function", "true", "false", "not", "repeat", "loop")

    flag = 0
    pointer = 0
    buffer = []
    state = 1
    line = 1
    endLine = 0
    token = {}

    def __init__(self, buffer):
        self.buffer = buffer

    def getNextToken(self):
        while True:
            if self.token != {}:
                token = self.token
                self.token = {}
                return token
            if self.state == -1:
                print(f">>>Error léxico(línea:{self.line},posición:{self.flag + 1 - self.endLine})")
                sys.exit(0)
                return -1
            if self.pointer == len(self.buffer):
                self.token = {"token": "EOF", "lexeme": "EOF", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                return self.token

            self.c = self.buffer[self.pointer]
            self.state = self.delta()
            self.pointer = self.pointer + 1


    def delta(self):
        if self.state == 1:
            if self.c == ";":
                # print(f"<tk_puntoycoma,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_puntoycoma", "lexeme": ";", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            elif self.c == ",":
                self.token = {"token": "tk_coma", "lexeme": ",", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_coma,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1
            elif self.c == "(":
                # print(f"<tk_par_izq,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_par_izq", "lexeme": "(", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            elif self.c == ")":
                self.token = {"token": "tk_par_der", "lexeme": ")", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_par_der,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1
            elif self.c == "}":
                # print(f"<tk_llave_der,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_llave_der", "lexeme": "}", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            elif self.c == "{":
                self.token = {"token": "tk_llave_izq", "lexeme": "{", "line": self.line,
                              "position": (self.flag + 1) - self.endLine }
                # print(f"<tk_llave_izq, {self.line}, {(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1
            elif self.c == "\n":
                self.line = self.line + 1
                self.flag = self.pointer + 1
                self.endLine = self.pointer + 1
                return 1
            elif self.c == "\t":
                self.flag = self.pointer + 1
                return 1
            elif self.c == " ":
                self.flag = self.pointer + 1
                return 1
            elif self.c == "+":
                return 34
            elif self.c == "-":
                return 30
            elif self.c == "*":
                return 27
            elif self.c == "/":
                return 24
            elif self.c == "%":
                return 21
            elif self.c == "<":
                return 18
            elif self.c == ">":
                return 15
            elif self.c == "=":
                return 12
            elif self.c == "!":
                return 10
            elif self.c == ":":
                return 7
            elif self.c in self.alphabet:
                return 47
            elif self.c in "@":
                return 44
            elif self.c in self.digits:
                return 49
            elif self.c in "#":
                return 42
            else:
                return -1
        elif self.state == 34:
            if self.c == "+":
                # print(f"<tk_incremento,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_incremento", "lexeme": "++", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            elif self.c == "=":
                # print(f"<tk_sum_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_sum_asig", "lexeme": "+=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            else:
                self.token = {"token": "tk_mas", "lexeme": "+", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_mas,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer + 1
                return 1
        elif self.state == 30:
            if self.c == "-":
                # print(f"<tk_decremento,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_decremento", "lexeme": "--", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            elif self.c == "=":
                self.token = {"token": "tk_res_asig", "lexeme": "-=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_res_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1
            else:
                self.token = {"token": "tk_menos", "lexeme": "-", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_menos,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1
        elif self.state == 27:
            if self.c == "=":
                self.token = {"token": "tk_mul_asig", "lexeme": "*=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_mul_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                flag = self.pointer + 1
                return 1
            else:
                self.token = {"token": "tk_mul", "lexeme": "*", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_mul,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer + 1
                return 1
        elif self.state == 24:
            if self.c == "=":
                self.token = {"token": "tk_div_asig", "lexeme": "/=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_div_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                flag = self.pointer + 1
                return 1
            else:
                # print(f"<tk_div,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_div", "lexeme": "/", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1
        elif self.state == 21:
            if self.c == "=":
                # print(f"<tk_mod_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_mod_asig", "lexeme": "%=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            else:
                # print(f"<tk_mod,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_mod", "lexeme": "%", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1
        elif self.state == 18:
            if self.c == "=":
                # print(f"<tk_menor_igual,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_menor_igual", "lexeme": "<=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                flag = self.pointer + 1
                return 1
            else:
                self.token = {"token": "tk_menor", "lexeme": "<", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_menor,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer + 1
                return 1
        elif self.state == 15:
            if self.c == "=":
                self.token = {"token": "tk_mayor_igual", "lexeme": ">=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_mayor_igual,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1
            else:
                # print(f"<tk_mayor,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_mayor", "lexeme": ">", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 12:
            if self.c == "=":
                # print(f"<tk_igualdad,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_igualdad", "lexeme": "==", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            else:
                return -1
        elif self.state == 10:
            if self.c == "=":
                # print(f"<tk_diferente,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_diferente", "lexeme": "!=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1
            else:
                return -1
        elif self.state == 7:
            if self.c == "=":
                self.token = {"token": "tk_asignacion", "lexeme": ":=", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_asignacion,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1
            else:
                self.token = {"token": "tk_dospuntos", "lexeme": ";", "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_dospuntos,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 47:
            if self.c in self.alphabet:
                return 47
            elif self.c in self.digits:
                return 47
            else:
                lexeme = ''.join(self.buffer[self.flag:self.pointer])
                if lexeme in self.reserved_word:
                    # print(f"<{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                    self.token = {"token": lexeme, "lexeme": lexeme, "line": self.line,
                                  "position": (self.flag + 1) - self.endLine}
                else:
                    # print(f"<id,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                    self.token = {"token": "id", "lexeme": lexeme, "line": self.line,
                                  "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 44:
            if self.c in self.alphabet:
                return 45
            else:
                return -1
        elif self.state == 45:
            if self.c in self.alphabet:
                return 45
            elif self.c in self.digits:
                return 45
            else:
                lexeme = ''.join(self.buffer[self.flag:self.pointer])
                # print(f"<fid,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "fid", "lexeme": lexeme, "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 49:
            if self.c in self.digits:
                return 49
            elif self.c in ".":
                return 50
            else:
                lexeme = ''.join(self.buffer[self.flag:self.pointer])
                self.token = {"token": "tk_num", "lexeme": lexeme, "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                # print(f"<tk_num,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 50:
            if self.c in self.digits:
                return 52
            else:
                self.pointer = self.pointer - 1
                lexeme = ''.join(self.buffer[self.flag:self.pointer])
                # print(f"<tk_num,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_num", "lexeme": lexeme, "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 52:
            if self.c in self.digits:
                return 52
            else:
                lexeme = ''.join(self.buffer[self.flag:self.pointer])
                # print(f"<tk_num,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token": "tk_num", "lexeme": lexeme, "line": self.line,
                              "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1
        elif self.state == 42:
            if self.c != "\n":
                return 42
            else:
                self.line = self.line + 1
                self.flag = self.pointer + 1
                self.endLine = self.pointer + 1
                return 1

dict_lexical = {
    'and': 'and', 
    'for': 'for', 
    'tk_par_izq': '(',
    'tk_menor_igual': '<=',
    'tk_num': 'numero',
    'tk_asignacion': ':=',
    'loop': 'loop',
    'tk_mul_asig': '*=',
    'var': 'var',
    'tk_incremento': '++', 
    'tk_mayor_igual': '>=',
    'tk_diferente': '-',
    'function': 'function',
    'tk_mul': '*', 
    'tk_mas': '+',
    'if': 'if',
    'input': 'input',
    'when': 'when',
    'tk_decremento': '--',
    'return': 'return',
    'tk_coma': ',', 
    'tk_mod': '%',
    'else': 'else',
    'tk_menor': '<',
    'tk_menos': '-',
    'tk_par_der': ')',
    'bool': 'bool',
    'tk_llave_der': '}',
    'next': 'next',
    'not': 'not',
    'tk_igualdad': '==', 
    'until': 'until', 
    'or': 'or',
    'num': 'num',
    'repeat': 'repeat',
    'end': 'end', 
    'tk_dospuntos': ':',
    'until': 'until', 
    'tk_div': '/', 
    'id': 'identificador',
    'tk_mayor': '>',
    'tk_sum_asig': '+=',
    'tk_llave_izq': '{',
    'fid': 'identificador de funcion',
    'break': 'break',
    'do': 'do', 
    'while': 'while',
    'tk_mod_asig': '%=',
    'print': 'print', 
    'tk_puntoycoma': ';', 
    'tk_res_asig': '-=', 
    'unless': 'unless',
    'while': 'while', 
    'tk_div_asig': '/=',
    'false': 'false',
    'true': 'true',
    'EOF': 'final de archivo'
  }



grammar_specification = """prog -> aux_1 main_prog .
aux_1 -> fn_decl_list aux_1 .
aux_1 -> .

datatype -> num .
datatype -> bool .

var_decl -> id tk_dospuntos datatype aux_2 .
aux_2 -> tk_coma id tk_dospuntos datatype aux_2 .
aux_2 -> .

fn_decl_list -> function fid tk_dospuntos datatype tk_par_izq aux_3 tk_par_der aux_4 stmt_block . 
aux_3 -> var_decl .
aux_3 -> .
aux_4 -> var var_decl tk_puntoycoma .
aux_4 -> .

stmt_block -> tk_llave_izq aux_6 tk_llave_der .
aux_6 -> stmt aux_7 .
aux_7 -> aux_6 .
aux_7 -> .

stmt_block -> stmt .

stmt -> print lexpr tk_puntoycoma .
stmt -> input id tk_puntoycoma .
stmt -> when tk_par_izq lexpr tk_par_der do stmt_block .
stmt -> if tk_par_izq lexpr tk_par_der do stmt_block else stmt_block .
stmt -> unless tk_par_izq lexpr tk_par_der do stmt_block .
stmt -> while tk_par_izq lexpr tk_par_der do stmt_block .
stmt -> return lexpr tk_puntoycoma .
stmt -> until tk_par_izq lexpr tk_par_der do stmt_block .
stmt -> loop stmt_block .
stmt -> do stmt_block aux_c_1 .

aux_c_1 -> while tk_par_izq lexpr tk_par_der .
aux_c_1 -> until tk_par_izq lexpr tk_par_der .

stmt -> repeat tk_num tk_dospuntos stmt_block .
stmt -> for tk_par_izq lexpr tk_puntoycoma lexpr tk_puntoycoma lexpr tk_par_der do stmt_block .
stmt -> next tk_puntoycoma .
stmt -> break tk_puntoycoma .
stmt -> id aux_c_2 .
aux_c_2 -> tk_asignacion lexpr tk_puntoycoma .
aux_c_2 -> tk_sum_asig lexpr tk_puntoycoma .
aux_c_2 -> tk_res_asig lexpr tk_puntoycoma .
aux_c_2 -> tk_mul_asig lexpr tk_puntoycoma .
aux_c_2 -> tk_div_asig lexpr tk_puntoycoma .
aux_c_2 -> tk_mod_asig lexpr tk_puntoycoma .
aux_c_2 -> tk_incremento tk_puntoycoma .
aux_c_2 -> tk_decremento tk_puntoycoma .

stmt -> tk_decremento id tk_puntoycoma .
stmt -> tk_incremento id tk_puntoycoma .

lexpr -> nexpr aux_8 .
aux_8 -> aux_9 nexpr aux_8 .
aux_8 -> .
aux_9 -> or .
aux_9 -> and .



nexpr -> not tk_par_izq lexpr tk_par_der .
nexpr -> rexpr .

rexpr -> simple_expr aux_10 .
aux_10 -> tk_menor simple_expr .
aux_10 -> tk_igualdad simple_expr .
aux_10 -> tk_menor_igual simple_expr .
aux_10 -> tk_mayor simple_expr .
aux_10 -> tk_mayor_igual simple_expr .
aux_10 -> tk_diferente simple_expr .
aux_10 -> .

simple_expr -> term aux_11 .
aux_11 -> tk_mas term aux_11 .
aux_11 -> tk_menos term aux_11 .
aux_11 -> .

term -> factor aux_12 . 
aux_12 -> tk_mul factor aux_12 .
aux_12 -> tk_div factor aux_12 .
aux_12 -> tk_mod factor aux_12 .
aux_12 -> .

tk_bool -> false .
tk_bool -> true .

factor -> tk_num .
factor -> tk_bool .
factor -> id aux_13 .
aux_13 -> tk_incremento . 
aux_13 -> tk_decremento . 
aux_13 -> .
factor -> aux_14 id .
aux_14 -> tk_incremento . 
aux_14 -> tk_decremento .
factor -> tk_par_izq lexpr tk_par_der .
factor -> fid tk_par_izq aux_15 tk_par_der . 
aux_15 -> lexpr aux_16 .
aux_15 -> .
aux_16 -> tk_coma lexpr aux_16 .
aux_16 -> .

main_prog -> aux_18 aux_17 end .
aux_17 -> stmt aux_17.
aux_17 -> .
aux_18 -> var var_decl tk_puntoycoma .
aux_18 -> .
"""
grammar = {}
terminal = set()
all = set()
no_terminal = set()
epsilon = 'e'
grammar_specification = grammar_specification.replace("\n","").split(".")

def generateGrammar(grammar_specification):
  for i in range(0, len(grammar_specification)-1):
    st = grammar_specification[i]
    st = st.strip().split(" ")
    terminal.add(st[0])
    if len(st)==2:
      st.append(epsilon)
    try:
      grammar[st[0]].append(st[2:]) 
    except: 
      grammar[st[0]] =[st[2:]]
    for i in st:
      all.add(i)

generateGrammar(grammar_specification)
no_terminal = terminal.difference({""})
terminal = all.difference(terminal,{""},{"->"})

#print(terminal)
#print(no_terminal)
#print(grammar)

def computeFirst(production):
  if production == [epsilon]:
    return {epsilon}
  if production[0] in terminal:
    return {production[0]}
  else:
    first_a1 = first(production[0])
    if epsilon in first_a1:
      if len(production) == 1:
        return first_a1
      if len(production) > 1:
        return first_a1.difference({epsilon}).union(computeFirst(production[1:]))
    return first_a1.difference({epsilon})


def first(alpha):
  temp = set()
  for i in grammar[alpha]:
    if i[0] == alpha:
      i.remove(alpha)
    temp = temp.union(computeFirst(i))

  return temp
      
  

def follow(alpha, update):
  follow_set = set()
  if alpha == 'prog':
    follow_set = follow_set.union({'$'})
  for rule in grammar:
    for production in grammar[rule]:
      for i in range(len(production)):
        if production[i] == alpha:
          temp = set()
          if len(follow_set) >= update:
              update = len(follow_set)
          else:
              return follow_set
          if i + 1 < len(production):
            temp = computeFirst(production[i+1:])
            follow_set = follow_set.union(temp).difference({epsilon})
          if not i + 1 < len(production) or epsilon in temp:
            follow_set = follow_set.union(follow(rule, update))


  return follow_set

def prediction(rule, production):
  prediction_set = set()
  first_set = computeFirst(production)
  if epsilon in first_set:
    return prediction_set.union(first_set.difference({epsilon}), follow(rule, 0))
  else:
    #print(first_set)
    return first_set

#print(i, first(i), len(first(i)))
#print(i, follow(i, 0), len(follow(i, 0)))

"""id, function, var, tk_llave_der, print, input, when, do, if, else, unless, while, return, until, loop, repeat, for, next, break, tk_incremento, tk_decremento, end"""

prediction('aux_8', ['e'])

def tokesToLexemes(list):
  lexemes = []
  for i in list:
    lexemes.append(dict_lexical[i])
  for i in range(len(lexemes)):
    lexemes[i] = "'" + lexemes[i] + "'"
  return sorted(lexemes)
  
def fix(lexemeList):
    fixString = ""
    for i in lexemeList:
      fixString = fixString + i 
      if (i != lexemeList[-1]):
        fixString = fixString + ", "
    return fixString

def match(expected_token):
  global token
  print(token['token'])
  if expected_token == token['token']:
    token = lexico.getNextToken()
    #print(token)
  elif expected_token == 'e':
    pass
    #print(token)
  else:
    #print(expected_token)
    syntaxError1([expected_token])

def syntaxError(rule):
  expected = set()
  for production in grammar[rule]:
    if rule == "aux_8" and production == ['e']:
      expected = {'tk_puntoycoma'}
      break
    expected = expected.union(prediction(rule, production))
  if dict_lexical[token['token']] == "final de archivo":
    message = f"<{token['line']}:{token['position'] - 1}> Error sintactico: se encontro final de archivo; se esperaba 'end'."
  else:
    if token['token'] == "id":
      message = f"<{token['line']}:{token['position']}> Error sintactico: se encontro: '{token['lexeme']}'; se esperaba: { fix(tokesToLexemes(expected)) }."
    else:
      message = f"<{token['line']}:{token['position']}> Error sintactico: se encontro: '{dict_lexical[token['token']]}'; se esperaba: { fix(tokesToLexemes(expected)) }."

  print(message)
  sys.exit(0)

def syntaxError1(expected_token):
  if dict_lexical[token['token']] == "final de archivo":
    message = f"<{token['line']}:{token['position'] - 1}> Error sintactico: se encontro final de archivo; se esperaba 'end'."
  else:
    if token['token'] == "id":
      message = f"<{token['line']}:{token['position']}> Error sintactico: se encontro: '{token['lexeme']}'; se esperaba: { fix(tokesToLexemes(expected_token))}."
    else:
      message = f"<{token['line']}:{token['position']}> Error sintactico: se encontro: '{dict_lexical[token['token']]}'; se esperaba: { fix(tokesToLexemes(expected_token))}."

  print(message)
  sys.exit(0)

code = ""
#code = code + "tree = Tree()\n"
#code = code + "tree.create_node('prog', 'prog')\n"
for rule in grammar:
  code = code + "def " + rule + "():\n"
  #code = code + "\t" + f"print('{rule}', token['token'])\n"
  for production in range(len(grammar[rule])):
    condition = "if " if production == 0 else "elif "
    code = code + "\t" + condition + f"token['token'] in prediction('{rule}', grammar['{rule}'][{production}]):\n"
    for term in range(len(grammar[rule][production])):
      if grammar[rule][production][term] in terminal:
        #code = code + "\t\t" + f"tree.create_node('{grammar[rule][production][term]}', '{grammar[rule][production][term] + '-' + rule}', parent='{rule}')\n"
        code = code + "\t\t" + f"match('{grammar[rule][production][term]}')\n"
      else:
        #if grammar[rule][production][term] != rule:
          #code = code + "\t\t" + f"tree.create_node('{grammar[rule][production][term]}', '{grammar[rule][production][term]}', parent='{rule}')\n"
        code = code + "\t\t" + f"{grammar[rule][production][term]}()\n"
  
  code = code + "\t" + f"else:\n"
  code = code + "\t\t" + f"syntaxError('{rule}')\n"

exec(code)

#st = sys.stdin.readlines()
#buffer = "".join(st) + " "
buffer = """var flag:bool;

flag:=true;
flag := not (flag and (not(false) or true)) + ;
end
"""

buffer = buffer.replace("\t", "    ").replace("\r","")
lexico = Lexico(buffer)
token = lexico.getNextToken()
prog()

print('El analisis sintactico ha finalizado correctamente.')
