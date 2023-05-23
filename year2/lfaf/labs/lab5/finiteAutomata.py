# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab5 | variant 3

# Importing Grammar module as G
import Grammar as G

# Define a class called FiniteAutomata to create and manage Finite Automaton
class FiniteAutomata:
    # Initialization of the FiniteAutomata class
    def __init__(self, q0, F, sigma, delta, Q):
        self.q0 = q0  # Initial state of the automaton
        self.F = F  # Final states of the automaton
        self.sigma = sigma  # Set of all the input symbols, alphabet of the automaton
        self.delta = delta  # Transition function represented as a dictionary
        self.Q = Q  # Set of all states of the automaton

    # Method to verify if a word is accepted by the automaton
    def checkWord(self, word):
        # Check if the first letter of the word is in the initial state
        if word[0] not in self.q0:
            return False

        # Check if the last letter of the word is in the final state
        if word[-1] not in self.F:
            return False

        # Check if each letter in the word is in the alphabet
        for letter in word:
            if letter not in self.sigma:
                return False

        # Initialize the transitions list
        transitions = []
        # Create a list of transitions for the word
        for letter in word:
            transitions.append(['', letter, ''])

        # Mark the beginning and the end of the transitions
        transitions[0][0] = 'S'
        transitions[-1].pop(-1)

        # Traverse through the transitions list and fill the current and next states
        for i in range(len(transitions) - 1):
            for state in self.delta:
                # If the current state and letter match with the transition state
                if transitions[i][0] == state[0] and transitions[i][1] == state[1]:
                    # Set the next state and the current state for the next transition
                    transitions[i][2] = state[2]
                    transitions[i + 1][0] = state[2]
                    break
            # If no next state is found return False
            if transitions[i][-1] == '':
                return False

        # Print the transitions attempted by the automaton
        print(f'transitions tried by the automaton{transitions}')

        return True

    # Method to convert the finite automaton to regular grammar
    def convertGrammar(self):
        p = {}
        # Traverse through all the states
        for key in self.Q:
            finals = []
            # Traverse through all the transitions
            for transition in self.delta:
                str = ''
                # If the current state matches with the transition state
                if transition[0] == key:
                    # Append the input symbol and the next state to the string
                    for i in range(1, len(transition)):
                        str = str + transition[i]
                    # Append the string to the finals list
                    finals.append(str)
            # Map the current state to the finals list
            p[key] = finals

        # Create a RegularGrammar object using the states, final states, productions and alphabet
        reg_gram = G.RegularGrammar(self.Q, self.F, p, self.sigma)

        return reg_gram

    # Method to determine the type of the automaton (Deterministic or Non-deterministic)
    def automatonType(self):

        # Traverse through all the states
        for letter in self.Q:
            inputs = []
            # Traverse through all the transitions
            for transition in self.delta:
                # If the current state matches with the transition state
                if transition[0] == letter:
                    # If the input symbol already exists in the inputs list return 'NFA'
                    if transition[1] in inputs:
                        return 'NFA'
                    # Add the input symbol to the inputs list
                    inputs.append(transition[1])

            # If the set of input symbols is not the same as the alphabet return 'NFA'
            if set(inputs) != set(self.sigma):
                return 'NFA'

        return 'DFA'

    # Method to convert NFA to DFA
    def nfa_to_dfa(self):

        # Step 1: Initial array creation
        array1 = []
        # Traverse through all the states
        for letter in self.Q:
            row = ['' for i in range(len(self.sigma))]
            # Traverse through each input symbol
            for inpt in self.sigma:
                # Traverse through all the transitions
                for transition in self.delta:
                    # If the current state and input symbol match with the transition
                    if transition[0] == letter:
                        if transition[1] == inpt:
                            # If the next state is not a lowercase letter, add it to the row
                            if not transition[-1].islower():
                                row[self.sigma.index(inpt)] += transition[-1]
            # Add the row to the array1
            array1.append(row)

        # Step 2: Second array creation
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

    # Method to visualize the automaton using Graphviz library
    def display(self):
        import graphviz

        # Create a new directed graph
        f = graphviz.Digraph('finite_state_machine', filename='../../Automaton Graphs/fsm.gv')
        # Set the layout direction of the graph from left to right
        f.attr(rankdir='LR', size='8,5')

        # Define the final states as doublecircle nodes
        f.attr('node', shape='doublecircle')
        for state in self.F:
            f.node(state)

        # Define the rest of the states as circle nodes
        f.attr('node', shape='circle')
        # Traverse through all the transitions and add edges to the graph
        for transition in self.delta:
            if len(transition)>2:
                f.edge(transition[0],transition[2],transition[1])

        # Display the graph
        f.view()
