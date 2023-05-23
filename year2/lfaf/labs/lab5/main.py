
# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab5 | variant 3


# Importing necessary classes from modules

#from Grammar import RegularGrammar
#from finiteautomata import FiniteAutomata
from lexer import Lexer
from parserator import Parser



print('')
print(' ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023')
print(' ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab4  | variant 3')
print('')

'''
# Defining a dictionary representing a context-free grammar
p = {
    'S' : ['dB', 'A'],
    'A' : ['d', 'dS', 'aAdAB'],
    'B' : ['aC', 'aS', 'AC'],
    'C' : [''],
    'E' : ['AS']
}

# Defining the non-terminals and terminals of the grammar
vn = ['S', 'A', 'B', 'C', 'E']
vt = ['a', 'd']
a = vt

# Creating a RegularGrammar object with the specified parameters
new_grammar = RegularGrammar(vn, vt, p, a)

# Converting the grammar into Chomsky Normal Form and storing it in a new object
cnf_form = new_grammar.ConvertCNF()

# Iterating over the dictionary of productions in the CNF form and printing them out
for key in cnf_form.p:
    print(f'{key} : {cnf_form.p[key]}')

'''

NewLexer = Lexer('code.txt')
tokens = NewLexer.regex_tokenize()
print(tokens)

new_parser = Parser(tokens)
new_parser.parse()