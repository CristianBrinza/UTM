# import the necessary library
import grammar as G
import graphviz

# Defining the FiniteAutomata class
class FiniteAutomata:

    # Defining the constructor method
    def __init__(self, q0, F, sigma, delta, Q):
        self.q0 = q0
        self.F = F
        self.sigma = sigma
        self.delta = delta
        self.Q = Q

## Defining a method to check if a given word is accepted by the automaton
    def checkWord(self, word):

        # Checking if the first state of the word is in the initial state
        if word[0] not in self.q0:
            return False

# Checking if the last state of the word is in the final state
        if word[-1] not in self.F:
            return False

# Checking if all the letters of the word are in the alphabet
        for letter in word:
            if letter not in self.sigma:
                return False

 # Computing the transitions made by the automaton for the given word
        transitions = []
        for letter in word:
            transitions.append(['', letter, ''])

        transitions[0][0] = 'S'
        transitions[-1].pop(-1)

        for i in range(len(transitions) - 1):
            for state in self.delta:
                if transitions[i][0] == state[0] and transitions[i][1] == state[1]:
                    transitions[i][2] = state[2]
                    transitions[i + 1][0] = state[2]
                    break
            if transitions[i][-1] == '':
                return False

        # Printing the transitions made by the automaton for the given word
        print(f'transitions tried by the automaton{transitions}')
        

        return True
    
# Defining a method to convert the automaton to a regular grammar
    def convertGrammar(self):

        # Initializing a dictionary to store the productions of the grammar
        p = {}
        for key in self.Q:
            finals = []
            for transition in self.delta:
                str = ''
                if transition[0] == key:
                    for i in range(1, len(transition)):
                        str = str + transition[i]
                    finals.append(str)
            p[key] = finals

        # Creating the regular grammar from the dictionary of productions
        reg_gram = G.RegularGrammar(self.Q, self.F, p, self.sigma)

        return reg_gram

    # Defining a method to determine if the automaton is a DFA or a NFA
    def automatonType(self):

        for letter in self.Q:
            inputs = []
            for transition in self.delta:
                if transition[0] == letter:
                    if transition[1] in inputs:
                        return 'NFA'
                    inputs.append(transition[1])

            if set(inputs) != set(self.sigma):
                return 'NFA'

        return 'DFA'

    # Defining a method to convert a NFA to a DFA
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

# define the display method for the finite state machine
    def display(self):

# create a new graph with the specified filename
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
            # check if there is a label for the edge
            if len(transition)>2:
                # add the edge with the specified label
                # add the edge with no label
                f.edge(transition[0],transition[2],transition[1])
         # view the graph in the default viewer
        f.view()


        '''
The code first imports the necessary library, graphviz, which is used to create and display the finite state machine.
The display method takes in the finite state machine self as an argument, which is an object that has F (a set of final states) and delta (a list of transitions between states) as attributes.
Inside the method, a new graph is created using graphviz.Digraph, with a specified filename. The direction of the graph is set to go from left to right using f.attr(rankdir='LR').
Final states are specified by setting the node shape to 'doublecircle' using f.attr('node', shape='doublecircle'), and then each final state is added to the graph using f.node(state) in a loop over the set of final states self.F.
Nodes and edges are added to the graph using f.attr('node', shape='circle') to set the node shape to 'circle', and then looping over the list of transitions self.delta. If there is a label for the edge (i.e., the length of the transition is greater than 2), it is added using f.edge(transition[0], transition[2], transition[1]). Otherwise, the edge is added with no label using f.edge(transition[0], transition[1]).
Finally, the graph is displayed in the default viewer using f.view().
        '''
