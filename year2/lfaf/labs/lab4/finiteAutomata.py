# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab4  | variant 3
import Grammar 


'''
FiniteAutomata that represents a finite automaton. An instance of the class is initialized with 
    the following parameters:

q0: a string representing the initial state.
F: a list of strings representing the final states.
sigma: a list of strings representing the alphabet.
delta: a list of lists representing the transition function.
Q: a list of strings representing the states.
The class has several methods:

- checkWord(word): This method takes a string word and returns True if the word is accepted by the 
    automaton and False otherwise. It checks if the first state is the initial state, if the last 
    state is a final state, and if all the letters in the word belong to the alphabet. It then uses 
    the transition function to simulate the automaton and check if it reaches a final state.
- convertGrammar(): This method converts the finite automaton to a regular grammar.
- automatonType(): This method determines if the automaton is a DFA or an NFA.
- nfa_to_dfa(): This method converts an NFA to a DFA.
- display(): This method creates a graphical representation of the finite automaton using the graphviz 
    library.
--------------------------------------------------------------------

The transition function is represented as a list of lists. Each sublist has three elements: the 
    current state, the input letter, and the next state. If the next state is a list of states, it 
    means the automaton can transition to any of those states given the input letter. The empty 
    string represents the dead state, which is a state that cannot transition to any other state.

The checkWord(word) method simulates the automaton by iterating over each letter in the word and 
    checking the corresponding transition in the transition function. If no transition is found for 
    a given letter and current state, the automaton is stuck and cannot reach a final state, so the method returns False. If the method reaches the end of the word and the current state is a final state, the method returns True.

The convertGrammar() method converts the transition function to a regular grammar. Each key in 
    the dictionary represents a non-terminal symbol in the grammar. The value associated with each 
    key is a list of strings that represent the production rules for that non-terminal symbol. The 
    production rules are obtained by iterating over each transition in the transition function and 
    collecting the letters after the input letter for each non-terminal symbol.

The automatonType() method determines the type of the automaton by checking if it is deterministic 
    or not. An automaton is deterministic if each state has exactly one transition for each input 
    letter. If the automaton has multiple transitions for the same input letter and state, it is 
    non-deterministic.

The nfa_to_dfa() method converts an NFA to a DFA by creating a new transition function and set of 
    states. The new transition function is obtained by computing the epsilon closure of each state 
    and combining them into a new state. The epsilon closure of a state is the set of all states 
    that can be reached from that state by taking epsilon transitions (transitions without input 
    letters). The new set of states is the set of all possible combinations of the old states. 
    The new final states are the sets of old states that contain at least one final state.

The display() method creates a graphical representation of the finite automaton using the graphviz 
    library. It creates a directed graph with nodes representing the states and edges representing 
    the transitions. The initial state is represented by an arrow pointing to it, and the final 
    states are represented by double circles. The resulting graph is saved as a file and 
    displayed in the default viewer for the system.
'''



class FiniteAutomata:
    def __init__(self, q0, F, sigma, delta, Q):
        self.q0 = q0
        self.F = F
        self.sigma = sigma
        self.delta = delta
        self.Q = Q

    # Define a method named "checkWord" that takes two parameters "self" and "word"
    def checkWord(self, word):
        # Check if the first character of "word" is not in the set of initial states "q0", return False if not
        if word[0] not in self.q0:
            return False

        # Check if the last character of "word" is not in the set of final states "F", return False if not
        if word[-1] not in self.F:
            return False

        # Check if all characters in "word" belong to the input alphabet "sigma", return False if not
        for letter in word:
            if letter not in self.sigma:
                return False

        # Create an empty list "transitions" to store the transitions taken by the automaton
        transitions = []
        # For each character in "word", add an empty transition to "transitions" list
        for letter in word:
            transitions.append(['', letter, ''])

        # Set the start state of the automaton to the first transition in "transitions"
        transitions[0][0] = 'S'
        # Remove the destination state of the last transition in "transitions"
        transitions[-1].pop(-1)

        # For each transition in "transitions", determine the next state by checking the delta function of the automaton
        for i in range(len(transitions) - 1):
            for state in self.delta:
                if transitions[i][0] == state[0] and transitions[i][1] == state[1]:
                    transitions[i][2] = state[2]
                    transitions[i + 1][0] = state[2]
                    break
            # If no valid transition is found for a character in "word", return False
            if transitions[i][-1] == '':
                return False

        # Print the transitions taken by the automaton for the input word
        print(f'transitions tried by the automaton{transitions}')

        # Return True if the automaton accepts the input word
        return True





    '''
    This code defines a method called convertGrammar that takes an object 
        instance (self) as a parameter. The method creates an empty dictionary 
        named p, iterates through each key in the dictionary self.Q, and for 
        each key, it iterates through each element in the list self.delta. 
    
    If the first element of the current element in self.delta is equal 
        to the current key, it creates a string by concatenating the rest 
        of the elements in the element of self.delta. It then adds this 
        string to a list called finals. Finally, it adds finals to the 
        dictionary p with the key being the current key. The method then 
        creates a new object of class RegularGrammar with the parameters
        self.Q, self.F, p, and self.sigma, and returns it
    '''
    # Define a method named "convertGrammar" that takes "self" as a parameter.
    def convertGrammar(self):
        # Create an empty dictionary named "p".
        p = {}
        # Iterate through each key in the dictionary "self.Q".
        for key in self.Q:
            # Create an empty list named "finals".
            finals = []
            # Iterate through each element in the list "self.delta".
            for transition in self.delta:
                # Create an empty string named "str".
                str = ''
                # If the first element of the "transition" is equal to "key", then iterate through each element in "transition" except for the first one.
                if transition[0] == key:
                    for i in range(1, len(transition)):
                        str = str + transition[i]
                    # Add "str" to the list "finals".
                    finals.append(str)
            # Add "finals" to the dictionary "p" with the key "key".
            p[key] = finals

        # Create a new RegularGrammar object named "reg_gram" with the parameters "self.Q", "self.F", "p", and "self.sigma".
        reg_gram = Grammar.RegularGrammar(self.Q, self.F, p, self.sigma)

        # Return "reg_gram".
        return reg_gram

    '''
    automatonType that takes in an object of a class (an automaton) 
        as an argument. The function checks whether the automaton is deterministic 
        or non-deterministic by examining its transitions. If any state has multiple 
        transitions on the same input symbol, the automaton is considered to be 
        non-deterministic. If any input symbol has no transition from a state, the
        automaton is also considered to be non-deterministic. If none of these 
        conditions are met, the automaton is considered to be deterministic.

    The function achieves this by iterating through each state in the automaton,
        and for each state, iterating through all transitions from that state. For each 
        transition, the function checks if the input symbol has already been seen for 
        that state. If it has, the automaton is non-deterministic and the function returns
        'NFA'. If it hasn't, the input symbol is added to the list of seen inputs for that 
        state. If, at the end of this process, any state has not seen all input symbols, 
        the automaton is non-deterministic and the function returns 'NFA'. Otherwise, the 
        automaton is deterministic and the function returns 'DFA'.
    '''
    # Define a method called automatonType that takes the self parameter.
    def automatonType(self):
         # Loop through each state in the Q set.
        for letter in self.Q:

             # Initialize an empty list called inputs.
            inputs = []
             # Loop through each transition in the delta set.
            for transition in self.delta:
                 # If the transition starts at the current state.
                if transition[0] == letter:
                    # If the transition symbol is already in the inputs list.
                    if transition[1] in inputs:
                        
                        # Return 'NFA' if there are multiple transitions for the same symbol.
                        return 'NFA'
                    
                    # Add the transition symbol to the inputs list.
                    inputs.append(transition[1])

            # If the set of transition symbols is not the same as the set of input symbols.
            if set(inputs) != set(self.sigma):
                # Return 'NFA' if there are missing transitions.
                return 'NFA'
        # If all states have complete and unique transitions, return 'DFA'.
        return 'DFA'




    '''
The `p` dictionary and the `vn` and `vt` lists seem to define a context-free grammar (CFG) 
    that can generate a language recognized by an NFA.
The `nfa_to_dfa` function starts by creating two arrays (`array1` and `array2`) to represent the 
    transitions of the DFA. The first array (`array1`) is created by looping over each state 
    (`letter`) and input symbol (`inpt`) of the NFA and checking all possible transitions 
    (`transition`) from that state on that input symbol. If a transition is found, its destination 
    state is added to the corresponding cell of the array.
The second array (`array2`) is then created by applying the subset construction algorithm, which 
    constructs a DFA from an NFA by considering each set of states that the NFA can be in after 
    reading a string from the input alphabet. The algorithm starts with the set containing the 
    initial state of the NFA and adds new sets to the DFA until all possible sets of states have 
    been considered. Each set is represented as a row of the `array2` array, and the cells in
    each row contain the set of states that the NFA can be in after reading the corresponding 
    input symbol.
Once `array2` has been created, the function removes any duplicate rows and replaces empty cells 
    with a special "dead state" symbol. The transitions of the DFA are then generated from `array2`,
    and the states of the DFA are extracted from these transitions.
Finally, the function creates a new `FiniteAutomata` object (presumably defined elsewhere 
    in the code) with the initial state, final states, input symbols, transitions, and states 
    of the DFA, and returns it.
    '''
    def nfa_to_dfa(self):

        # creating the first array for conversion
        array1 = []
        for letter in self.Q:
            row = ['' for i in range(len(self.sigma))]
            for inpt in self.sigma:
                for transition in self.delta:
                    if transition[0] == letter:
                        if transition[1] == inpt:
                            if not transition[-1].islower():
                                row[self.sigma.index(inpt)] += transition[-1]
            array1.append(row)

        # creating the second array
        array2 = []
        used = []
        unused = [self.Q[0]]

        while unused:
            aux = [unused[0]]
            for i in range(0, len(self.sigma)):
                strng = ''
                for letter in unused[0]:
                    aux2 = array1[self.Q.index(letter)][i]
                    if aux2 not in strng:
                        strng += aux2
                aux.append(strng)

                if strng not in used:
                    unused.append(strng)
            array2.append(aux)

            used.append(unused[0])
            unused.remove(unused[0])

        array2_1 = []
        [array2_1.append(x) for x in array2 if x not in array2_1]
        for row in array2_1:
            for i in range(0, len(row)):
                if row[i] == '':
                    row[i] = 'dead_state'

        delta2 = []
        for row in array2_1:
            for i in range(0, len(self.sigma)):
                aux = [row[0], self.sigma[i], row[i + 1]]
                delta2.append(aux)

        Q2 = []
        for row in delta2:
            if row[0] not in Q2:
                Q2.append(row[0])

        finals = []
        for state in self.F:
            for other_state in Q2:
                if state in other_state:
                    finals.append(other_state)

        new_automaton = FiniteAutomata(self.q0[0], finals, self.sigma, delta2, Q2)
        return new_automaton








    def display(self):
        import graphviz

        f = graphviz.Digraph('finite_state_machine', filename='../Automaton Graphs/fsm.gv')
        # specifying the direction left-to-right
        f.attr(rankdir='LR', size='8,5')

        # specifying final states by double-circling them
        f.attr('node', shape='doublecircle')
        for state in self.F:
            f.node(state)

        # creating the nodes and the edges in-between
        f.attr('node', shape='circle')
        for transition in self.delta:
            if len(transition)>2:
                f.edge(transition[0],transition[2],transition[1])

        f.view()
