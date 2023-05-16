# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab3  | variant 3

# Importing necessary classes from modules
import random
from finiteAutomata import FiniteAutomata


'''
Then, we define a class called RegularGrammar. It has an initializer 
    method __init__ which takes four parameters: Vn (non-terminal symbols), 
Vt (terminal symbols), P (production rules), and a (alphabet).
    Inside the __init__ method, we initialize the class attributes self.Vn, 
    self.Vt, self.P, self.alphabet with the corresponding parameter values. 
    Additionally, we initialize self.word_list as an empty list to store 
    generated words, and self.word as an empty string to represent the current 
    word being generated.
'''
# Defining the RegularGrammar class
class RegularGrammar:
    def __init__(self, Vn, Vt, P, a):
        self.Vn = Vn       # Non-terminal symbols
        self.Vt = Vt       # Terminal symbols
        self.P = P         # Production rules
        self.alphabet = a  # Alphabet
        self.word_list = []  # List to store generated words
        self.word = ''       # Current word being generated




    '''
method called GenerateWord defined within the RegularGrammar class. 
    This method is responsible for generating a word based on the provided 
    production rules.
First, we reset the self.word_list attribute to an empty list and set the 
    initial word to 'S'. We add the initial word to the word list.
Then, using a while loop, we continue generating the word until the last 
    character of the word is not uppercase. Within the loop, we create a 
    temporary list called aux to store information about the current 
    transition.
We append the current non-terminal symbol (last character of the word) 
    to the aux list. Next, we generate the next character of the word b
    ased on the production rules. The choice of the production rule is 
    made randomly using random.choice().
If the new character is uppercase (indicating a non-terminal symbol), 
    we append the previous non-terminal symbol and the current non-terminal 
    symbol to the aux list. Otherwise, if the new character is a terminal 
    symbol, we simply append it to the aux list.
After each iteration, we add the aux list (representing the transition) to 
    the self.word_list.
Once the loop finishes, we remove the initial word from the word list 
    (self.word_list[1:]), print the generated word, print the transitions 
    used to create the word, and finally return the generated word.
    '''
    # Defining the GenerateWord method
    def GenerateWord(self):
        self.word_list = []  # Reset the word list
        self.word = 'S'  # Set the initial word to 'S'
        self.word_list.append(self.word)  # Add the initial word to the word list
        
        # Continue generating words until the last character of the word is not uppercase
        while self.word[-1].isupper():
            aux = []  # Temporary list to store information about the current transition
            aux.append(self.word[-1])  # Add the current non-terminal symbol to the transition list
            
            # Generate the next character of the word based on the production rules
            self.word = self.word[:-1] + random.choice(self.P[self.word[-1]])
            
            if self.word[-1].isupper():
                aux.append(self.word[-2])  # Add the previous non-terminal symbol to the transition list
                aux.append(self.word[-1])  # Add the current non-terminal symbol to the transition list
            else:
                aux.append(self.word[-1])  # Add the current terminal symbol to the transition list
            
            self.word_list.append(aux)  # Add the transition list to the word list
        
        self.word_list = self.word_list[1:]  # Remove the initial word from the word list
        print(f'generated word: {self.word}')  # Print the generated word
        print(f'used transitions for created word: {self.word_list}')  # Print the transitions used to create the word
        return self.word  # Return the generated word


    '''
    method called ConvertFA within the RegularGrammar class. This method 
        is responsible for converting the regular grammar into a finite 
        automaton representation.
    First, we initialize an empty list called initial_states to store the 
        initial states. We iterate over the production rules for the 
        non-terminal symbol 'S' and extract the first element of each 
        state, adding it to the initial_states list.
    Next, we initialize an empty list called transition_functions to 
        store the transition functions. We iterate over the production 
        rules stored in self.P and for each key (non-terminal symbol), 
        we iterate over the states. Inside the loop, we create a temporary 
        list called aux to represent a transition function. We add the key 
        (non-terminal symbol) to aux and concatenate it with the elements 
        of the state (terminal and non-terminal symbols). Finally, we add 
        aux to the transition_functions list.
    After collecting the necessary information, we print the valid 
        transitions using the transition_functions list.
    Finally, we create a FiniteAutomata object named automaton using 
        the collected information: initial_states, self.Vt (terminal 
        symbols), self.alphabet, transition_functions, and self.Vn 
        (non-terminal symbols). We return the automaton object as 
        the result of the method.
    '''
    # Defining the ConvertFA method
    def ConvertFA(self):
        initial_states = []  # List to store initial states
        for state in self.P['S']:
            initial_states.append(state[0])  # Add the first element of each production rule for 'S' to the initial states list

        transition_functions = []  # List to store transition functions
        for key in self.P:
            for state in self.P[key]:
                aux = []  # Temporary list to store a transition function
                aux.append(key)  # Add the key (non-terminal symbol) to the transition function
                aux = aux + list(state)  # Add the elements of the state (terminal and non-terminal symbols) to the transition function
                transition_functions.append(aux)  # Add the transition function to the list of transition functions

        print(f'valid transitions: {transition_functions}')  # Print the valid transitions

        # Create a FiniteAutomata object using the collected information
        automaton = FiniteAutomata(initial_states,
                                self.Vt,
                                self.alphabet,
                                transition_functions,
                                self.Vn)
        return automaton  # Return the created automaton


    
    '''
    method called chumsky_type within the RegularGrammar class. This method is used to determine the Chomsky type of the regular grammar.

Inside the method, there are two nested functions: upper_number and    
    upper_pos. These functions are utility functions to count the number 
    of uppercase letters in a state and find the position of the last 
    uppercase letter in a state, respectively.
The chumsky_type starts with the default value of chum_type set to 3 
    (representing Chomsky type 3).
First, it checks for Chomsky type 1 and empty states by iterating over 
    the production rules. If a non-terminal symbol has a length of 2 or 
    more, it sets chum_type to 1. Additionally, if there is an empty 
    state and chum_type is 1, it returns 0.
If chum_type is still 3, it checks for Chomsky type 2. It iterates over the 
    production rules and states, counting the number of uppercase letters in 
    each state. If a state has more than one uppercase letter, it returns 2. 
    If a state has exactly one uppercase letter, it stores its position in 
    the variable location.
Next, the code checks for Chomsky type 3. It iterates over the production 
    rules and examines each state. It checks if the first state has more 
    than one uppercase letter or if the position of the uppercase letter 
    is neither 0 nor -1, returning 2 in those cases. Then, it iterates 
    over the remaining states and checks for non-initial states that 
    have more than one uppercase letter or where the position of the 
    uppercase letter differs from the previous state. If either condition 
    is met, it returns 2.
If none of the conditions for Chomsky type 1, 2, or 3 are met, the code 
    returns the default value of chum_type, which is 3.


    '''

    # Defining the chumsky_type method
    def chumsky_type(self):
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
                    pos = i
            if pos == len(state) - 1:
                return -1
            return pos

        chum_type = 3  # Default value for the Chomsky type

        # Check for Chomsky type 1 and empty states
        for key in self.P:
            if len(key) >= 2:
                chum_type = 1
            for state in self.P[key]:
                if state == '' and chum_type == 1:
                    return 0  # Return 0 if there is an empty state and Chomsky type is 1

        if chum_type == 1:
            return 1  # Return 1 if Chomsky type is 1

        # Check for Chomsky type 2
        for key in self.P:
            for state in self.P[key]:
                if upper_number(state) > 1:
                    return 2  # Return 2 if there is more than one uppercase letter in a state
                elif upper_number(state) == 1:
                    location = upper_pos(state)  # Get the position of the uppercase letter

        # Check for Chomsky type 3
        for key in self.P:
            if upper_number(self.P[key][0]) > 1:
                return 2  # Return 2 if the first state has more than one uppercase letter
            if upper_pos(self.P[key][0]) not in [0, -1]:
                return 2  # Return 2 if the position of the uppercase letter in the first state is not 0 or -1
            for i in range(1, len(self.P[key])):
                if not self.P[key][i].islower() and self.P[key][i] != '':
                    if upper_number(self.P[key][i]) > 1:
                        return 2  # Return 2 if a non-initial state has more than one uppercase letter
                    if upper_pos(self.P[key][i]) != upper_pos(self.P[key][i - 1]):
                        return 2  # Return 2 if the position of the uppercase letter changes between consecutive states

        return chum_type  # Return the Chomsky type (default is 3 if not determined as type 1 or 2)




