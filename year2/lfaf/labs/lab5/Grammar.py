
# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab5 | variant 3

# Importing required libraries
import random
from finiteAutomata import FiniteAutomata  # A module for creating Finite Automata
from cnf import CNFConvertor  # A module for converting to Chomsky Normal Form (CNF)

# Defining a class for Regular Grammar
class RegularGrammar:
    '''
    The constructor method initializes the object with the given variables Vn, Vt, P, and a, representing 
    the non-terminals, terminals, production rules, and alphabet of the grammar, respectively. The word_list
      and word variables are also initialized to empty lists and an empty string, respectively.
    '''
    # Constructor of the class
    def __init__(self,Vn,Vt,P,a):
        self.Vn = Vn  # Non-terminal symbols
        self.Vt = Vt  # Terminal symbols
        self.P = P  # Production rules
        self.alphabet = a  # Alphabet
        self.word_list = []  # Initializing list for generated words
        self.word = ''  # Initializing the word


    '''
    The GenerateWord method generates a random word from the grammar using a while loop that selects 
    random production rules until a terminal symbol is reached. The method also updates the word_list 
    variable to keep track of the production rules used to generate the word. The method returns the generated word.
    '''
    # Method to generate a word using the grammar
    def GenerateWord(self):
        # Resetting the word and the word list
        self.word_list = []
        self.word='S'
        self.word_list.append(self.word)
        # Continue generating the word until the last character is non-terminal
        while self.word[-1].isupper():
            aux = []
            aux.append(self.word[-1])
            # Replace the last character with a production of it
            self.word = self.word[:-1]+random.choice(self.P[self.word[-1]])
            # Append the generated symbols to aux
            if self.word[-1].isupper():
                aux.append(self.word[-2])
                aux.append(self.word[-1])
            else:
                aux.append(self.word[-1])
            self.word_list.append(aux)
        self.word_list=self.word_list[1:]
        # Print the generated word and its transitions
        print(f'generated word: {self.word}')
        print(f'used transitions for created word: {self.word_list}')
        return self.word

    # Method to convert the grammar to a Finite Automata
    def ConvertFA(self):
        # Identify the initial states by looking at productions of 'S'
        initial_states =[]
        for state in self.P['S']:
            initial_states.append(state[0])
        # Convert the production rules into transition functions
        transition_functions = []
        for key in self.P:
            for state in self.P[key]:
                aux = []
                aux.append(key)
                aux = aux + list(state)
                transition_functions.append(aux)
        # Print the valid transitions
        print(f'valid transitions: {transition_functions}')
        # Create and return a Finite Automata using the identified components
        automaton = FiniteAutomata(initial_states, self.Vt, self.alphabet, transition_functions, self.Vn)
        return automaton

    # Method to determine the Chomsky type of the grammar
    def chumsky_type(self):
        # Helper functions to count the number of non-terminals and to find the position of a non-terminal
        def upper_number(state):
            uppers = 0
            for letter in state:
                if letter.isupper():
                    uppers += 1
            return uppers
        def upper_pos(state):
            pos = 0
            for i in range(0, len(state)):
                if state[i].isupper():
                    pos=i
            if pos == len(state)-1:
                return -1
            return pos
        # Initialize chum_type as type 3
        chum_type = 3
        # Check all productions to update the chum_type accordingly
        # A lot of conditions checking for specific type rules
        # ...
        # Returning the final type
        return chum_type

    # Method to convert the grammar to Chomsky Normal Form (CNF)
    def ConvertCNF(self):
        # Initialize CNFConvertor instance
        chomsky_form = CNFConvertor(self.P, self.Vn)
        # Remove Epsilon-transitions, print the productions, remove unit productions, and so on...
        # ...
        # Obtain and return the final Chomsky normal form
        chomsky_form.Transform()
        return chomsky_form
