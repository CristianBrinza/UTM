# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab4  | variant 3
import random

from finiteAutomata import FiniteAutomata

from cnf import CNFConvertor

class RegularGrammar:
    '''
    The constructor method initializes the object with the given variables Vn, Vt, P, and a, representing 
    the non-terminals, terminals, production rules, and alphabet of the grammar, respectively. The word_list
      and word variables are also initialized to empty lists and an empty string, respectively.
    '''
    def __init__(self,Vn,Vt,P,a):
        self.Vn = Vn
        self.Vt = Vt
        self.P = P
        self.alphabet = a
        self.word_list = []
        self.word = ''


    '''
    The GenerateWord method generates a random word from the grammar using a while loop that selects 
    random production rules until a terminal symbol is reached. The method also updates the word_list 
    variable to keep track of the production rules used to generate the word. The method returns the generated word.
    '''
    # Define a method called GenerateWord in a class, which takes no arguments but uses instance variables
    def GenerateWord(self):
        # Create an empty list to store generated words
        self.word_list = []
        # Initialize a string variable with the letter 'S'
        self.word='S'
        # Append the initial word to the word list
        self.word_list.append(self.word)
        # Loop until the last letter of the word is not uppercase
        while self.word[-1].isupper():
            # Create a list to store the last letter of the previous word
            aux = []
            aux.append(self.word[-1])
            # Generate a new letter randomly based on the previous letter using the transition probability
            self.word = self.word[:-1]+random.choice(self.P[self.word[-1]])
            # Check if the newly generated letter is uppercase
            if self.word[-1].isupper():
                # If it is uppercase, append the last two letters to the aux list
                aux.append(self.word[-2])
                aux.append(self.word[-1])
            else:
                # If it is lowercase, append the last letter to the aux list
                aux.append(self.word[-1])
            # Append the aux list to the word list
            self.word_list.append(aux)
        # Remove the initial word from the word list
        self.word_list=self.word_list[1:]
        # Print the generated word and the list of transitions used to create the word
        print(f'generated word: {self.word}')
        print(f'used transitions for created word: {self.word_list}')
        # Return the generated word
        return self.word


    '''
    The ConvertFA method converts the given context-free grammar to a finite automaton (FA). It first 
    extracts the initial states from the production rules of the start symbol ('S'). Then, it constructs 
    a list of transition functions by iterating over all production rules and adding the corresponding transitions 
    to the list. Finally, it creates an instance of the FiniteAutomata class with the extracted information and returns it.
    '''
    # Define a method named "ConvertFA" within a class, taking in "self" as the argument.
    def ConvertFA(self):
        # Define an empty list named "initial_states".
        initial_states =[]
        # Iterate through each state in the "S" key of dictionary "P", and append the first element of the state to "initial_states" list.
        for state in self.P['S']:
            initial_states.append(state[0])

        # Define an empty list named "transition_functions".
        transition_functions = []
        # Iterate through each key in dictionary "P", and for each state in the key, add the key and the state to a temporary list named "aux".
        # The temporary list "aux" is then appended to the "transition_functions" list.
        for key in self.P:
            for state in self.P[key]:
                aux = []
                aux.append(key)
                aux = aux + list(state)
                transition_functions.append(aux)

        # Print the valid transitions in a formatted string using the "transition_functions" list.
        print(f'valid transitions: {transition_functions}')

        # Create a FiniteAutomata object named "automaton" using the arguments "initial_states", "Vt", "alphabet", "transition_functions", and "Vn".
        automaton = FiniteAutomata(initial_states, self.Vt, self.alphabet, transition_functions, self.Vn)
        # Return the created "automaton" object.
        return automaton


    # Define a function named "chumsky_type" that takes in a self argument.
    def chumsky_type(self):

        # Define a function named "upper_number" that takes in a state argument.
        # This function counts the number of uppercase letters in the state string and returns the count.
        def upper_number(state):
            uppers = 0
            for letter in state:
                if letter.isupper():
                    uppers += 1
            return uppers

        # Define a function named "upper_pos" that takes in a state argument.
        # This function finds the position of the last uppercase letter in the state string and returns the position.
        def upper_pos(state):
            pos = 0
            for i in range(0, len(state)):
                if state[i].isupper():
                    pos=i
            if pos == len(state)-1:
                return -1
            return pos

        # Initialize chum_type to 3.
        chum_type = 3

        # Loop through the keys in the self.P dictionary.
        for key in self.P:
            # If the length of the key is greater than or equal to 2, set chum_type to 1.
            if len(key)>=2:
                chum_type = 1
            # Loop through the states associated with the key.
            for state in self.P[key]:
                # If the state is an empty string and chum_type is 1, return 0.
                if state == '' and chum_type == 1:
                    return 0

        # If chum_type is 1, return 1.
        if chum_type==1:
            return 1

        # Loop through the keys in the self.P dictionary.
        for key in self.P:
            # Loop through the states associated with the key.
            for state in self.P[key]:
                # If the state has more than one uppercase letter, return 2.
                if upper_number(state)>1:
                    return 2
                # If the state has exactly one uppercase letter, find the location of the uppercase letter.
                elif upper_number(state)==1:
                    location = upper_pos(state)

        # Loop through the keys in the self.P dictionary.
        for key in self.P:
            # If the first state associated with the key has more than one uppercase letter, return 2.
            if upper_number(self.P[key][0])>1:
                return 2
            # If the position of the uppercase letter in the first state associated with the key is not at the beginning or the end of the string, return 2.
            if upper_pos(self.P[key][0]) not in [0,-1]:
                return 2
            # Loop through the remaining states associated with the key.
            for i in range(1,len(self.P[key])):
                # If the state is not lowercase and not an empty string, and has more than one uppercase letter, return 2.
                if not self.P[key][i].islower() and self.P[key][i] != '':
                    if upper_number(self.P[key][i])>1:
                        return 2
                    # If the position of the uppercase letter in the state is different from the position of the uppercase letter in the previous state, return 2.
                    if upper_pos(self.P[key][i]) != upper_pos(self.P[key][i-1]):
                        return 2
        # Return chum_type.
        return chum_type


    def ConvertCNF(self):
        # Create convertor instance
        chomsky_form = CNFConvertor(self.P, self.Vn)
        # Remove Epsilon-transitions
        chomsky_form.RemoveEpsilon()
        # Remove unit productions, key by key
        for key in chomsky_form.p:
            chomsky_form.RemoveUnitProd(key)
        # Remove unproductive symbols:
        chomsky_form.RemoveUnproductive()
        # Remove inaccesible, and cleanup the grammar
        chomsky_form.Cleanup()
        # Obtain the final Chomsky normal form
        chomsky_form.Transform()


        return chomsky_form







