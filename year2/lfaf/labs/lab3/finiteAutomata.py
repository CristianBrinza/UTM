# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab3  | variant 3

# Importing necessary classes from modules
import Grammar as G


class FiniteAutomata:
    def __init__(self, q0, F, sigma, delta, Q):
        self.q0 = q0
        self.F = F
        self.sigma = sigma
        self.delta = delta
        self.Q = Q



    '''
    Method called checkWord within a class. This method is used to check 
        whether a given word is valid according to the automaton's states, 
        alphabet, and transitions.
    First, the code checks if the initial state (word[0]) is a valid initial 
        state (self.q0). If it is not, the method returns False.
    Next, it checks if the final state (word[-1]) is a valid final state 
        (self.F). If it is not, the method returns False.
    Then, the code iterates through each letter in the word and checks 
        if each letter is present in the valid alphabet (self.sigma). 
        If any letter is not in the valid alphabet, the method returns False.
    The code creates a list of transitions called transitions, initially 
        filled with empty values. Each transition is represented as a 
        sublist with three elements: the current state, the input symbol, 
        and the next state.
    The initial state of the first transition is set as 
        'S' (transitions[0][0] = 'S'), and the last element (empty string) is 
        removed from the last transition (transitions[-1].pop(-1)).
    The code then iterates through the transitions to determine the 
        next states based on the current states and input symbols. 
        It compares the current state and input symbol of each 
        transition with the states and symbols in self.delta (transitions 
        of the automaton). If a match is found, it sets the next state for 
        the current transition and the current state for the next transition. 
        If there is no match (incomplete transition), the 
        method returns False.
    Finally, the method prints the transitions tried by the automaton 
        (transitions) and returns True if the word passes all the checks 
        and transitions successfully.
    '''
    # Defining the checkWord method
    def checkWord(self, word):
        if word[0] not in self.q0:
            return False  # Return False if the initial state is not valid for the given word

        if word[-1] not in self.F:
            return False  # Return False if the final state is not valid for the given word

        for letter in word:
            if letter not in self.sigma:
                return False  # Return False if any letter in the word is not in the valid alphabet

        transitions = []
        for letter in word:
            transitions.append(['', letter, ''])  # Create a list of transitions with empty values

        transitions[0][0] = 'S'  # Set the initial state of the first transition as 'S'
        transitions[-1].pop(-1)  # Remove the last element (empty string) from the last transition

        # Iterate through the transitions to determine the next states based on the current states and input symbols
        for i in range(len(transitions) - 1):
            for state in self.delta:
                if transitions[i][0] == state[0] and transitions[i][1] == state[1]:
                    transitions[i][2] = state[2]  # Set the next state for the current transition
                    transitions[i + 1][0] = state[2]  # Set the current state for the next transition
                    break
            if transitions[i][-1] == '':
                return False  # Return False if there is an incomplete transition

        print(f'transitions tried by the automaton: {transitions}')  # Print the transitions tried by the automaton

        return True  # Return True if the word passes all the checks and transitions successfully
        

    # Defining the convertGrammar method
    def convertGrammar(self):
        p = {}  # Dictionary to store the converted production rules

        # Iterate over each key in self.Q (states)
        for key in self.Q:
            finals = []  # List to store the converted final states for each key

            # Iterate over each transition in self.delta
            for transition in self.delta:
                str = ''  # String to concatenate the symbols of the transition

                # Check if the first element of the transition matches the current key
                if transition[0] == key:
                    # Concatenate the symbols from index 1 to the end of the transition
                    for i in range(1, len(transition)):
                        str = str + transition[i]
                    finals.append(str)  # Add the concatenated string to the finals list

            p[key] = finals  # Assign the finals list to the corresponding key in the dictionary

        # Create a new instance of the RegularGrammar class with the converted data
        reg_gram = G.RegularGrammar(self.Q, self.F, p, self.sigma)

        return reg_gram  # Return the converted regular grammar


    # Defining the automatonType method
    def automatonType(self):
        for letter in self.Q:
            inputs = []  # List to store the input symbols for each state

            # Iterate over each transition in self.delta
            for transition in self.delta:
                if transition[0] == letter:
                    if transition[1] in inputs:
                        return 'NFA'  # Return 'NFA' if there is a repeated input symbol for a state
                    inputs.append(transition[1])  # Add the input symbol to the inputs list

            if set(inputs) != set(self.sigma):
                return 'NFA'  # Return 'NFA' if the inputs for a state don't match the valid alphabet

        return 'DFA'  # Return 'DFA' if none of the conditions for 'NFA' are met, indicating it's a deterministic automaton


    # Defining the nfa_to_dfa method
    def nfa_to_dfa(self):
        array1 = []  # First array for conversion

        # Iterate over each letter in self.Q
        for letter in self.Q:
            row = ['' for i in range(len(self.sigma))]  # Initialize a row with empty strings
            for inpt in self.sigma:
                for transition in self.delta:
                    if transition[0] == letter and transition[1] == inpt:
                        if not transition[-1].islower():
                            row[self.sigma.index(inpt)] += transition[-1]
            array1.append(row)  # Add the row to array1

        array2 = []  # Second array for conversion
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

        # Replace empty strings in array2_1 with 'dead_state'
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

    # Defining the display method
    def display(self):
        import graphviz

        f = graphviz.Digraph('finite_state_machine', filename='../Automaton Graphs/fsm.gv')
        f.attr(rankdir='LR', size='8,5')  # Specifying the direction left-to-right

        f.attr('node', shape='doublecircle')  # Specifying final states by double-circling them
        for state in self.F:
            f.node(state)

        f.attr('node', shape='circle')  # Creating the nodes and the edges in-between
        for transition in self.delta:
            if len(transition) > 2:
                f.edge(transition[0], transition[2], transition[1])

        f.view()
