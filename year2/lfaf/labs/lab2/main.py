# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab2  | variant 3


# Importing necessary classes from modules
from grammar import RegularGrammar
from finiteautomata import FiniteAutomata


print('')
print(' ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023')
print(' ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab2  | variant 3')
print('')




vn = ['S','D','R']
vt = ['a','b','c','d','f']
p = {
    'S':['aS','bD','fR'],
    'D':['cD','dR','d'],
    'R':['bR','f']
}
a= vt

print('---------------------')
new_grammar = RegularGrammar(vn,vt,p,a)
new_automaton = new_grammar.ConvertFA()

print('---------------------')
user_input = input('generate 5 strings (y/n)')
if user_input.lower() == 'y':
    print()
    print('Generating 5 strings')
    print('--------------------------------------------------')
    for i in range(5):
        word = new_grammar.GenerateWord()
        if new_automaton.checkWord(word):
            print('Valid word')
        print('--------------------------------------------------')

user_input = input('test a string (y/n)')
if user_input.lower() == 'y':
    user_word = input('Your string : ')
    # the valid answer
    print()
    if new_automaton.checkWord(user_word):
        print('!!!   user word is valid  !!!')
    else:
        print('!!!  user word not valid  !!!')
    print()
    print('---------------------')
    print()
    print()



for key in new_grammar.P:
    print(f'{key} -> {new_grammar.P[key]}')
print('---------------------')
print('grammar type : ',new_grammar.chumsky_type())

print('---------------------')

'''
Variant 3:
VN={S, D, R}, 
VT={a, b, c, d, f},
P={ 
    S → aS
    S → bD
    S → fR
    D → cD
    D → dR
    R → bR
    R → f
    D → d
}

Q = {q0,q1,q2,q3,q4},
∑ = {a,b},
F = {q4},
δ(q0,a) = q1,
δ(q1,b) = q1,
δ(q1,a) = q2,
δ(q2,b) = q2,
δ(q2,b) = q3,
δ(q3,b) = q4, 
δ(q3,a) = q1.

q0 ~ S
q1 ~ A
q2 ~ B
q3 ~ C
q4 ~ D
'''

# Defining the states of the automaton
# Q = {q0,q1,q2,q3,q4},
Q = ['S','A','B','C','D']

#Defining the initial state
q0 = 'S'

# Defining the final state
# F = {q4}
F = 'D'

# Defining the alphabet
# ∑ = {a,b},
sigma = ['a','b']

# Defining the transition table
delta =[
# δ (q0,  a)= q1,
#     |   |   |
    ['S','a','A'],
    ['A','b','A'],
    ['A','a','B'],
    ['B','b','B'],
    ['B','b','C'],
    ['C','b','D'],
    ['C','a','A']
]


# Creating a new automaton object using the defined values
new_new_automaton = FiniteAutomata(q0,F,sigma,delta,Q)
# Converting the NFA to DFA
new_dfa = new_new_automaton.nfa_to_dfa()

# Printing the attributes of the DFA
print(f'Q = {new_dfa.Q}')
print('---------------------')
print(f'start state: {new_dfa.q0}')
print('---------------------')
print(f'final states: {new_dfa.F}')
print('---------------------')
print(f'sigma: {new_dfa.sigma}')
print('---------------------')

# Printing the transition table in a tabular format
print('delta:')
for row in new_dfa.delta:
   print(row)

# Prompting the user to generate and display the automaton
print('---------------------')
user_input = input('gennerating visual (y/n)')
if user_input.lower() == 'y':
    new_new_automaton.display()

print('---------------------')


user_input = input('debugging (y/n)')
if user_input.lower() == 'y':
    #Printing the transitions of the NFA
    for transition in new_new_automaton.delta:
        print(transition)

    print('---------------------') 
    print(f'automaton type: {new_new_automaton.automatonType()}')
    print('---------------------') 

    # Converting the NFA to a regular grammar and printing it
    generated_grammar = new_new_automaton.convertGrammar()

    for key in generated_grammar.P:
        print(f'{key} -> {generated_grammar.P[key]}')

# Converting the DFA to a regular grammar and printing it
    new_dfa_automaton = new_new_automaton.nfa_to_dfa()
    dfa_grammar = new_dfa_automaton.convertGrammar()
    print('---------------------') 
    print(new_dfa_automaton.delta)
    print('---------------------') 
    print(dfa_grammar.P)