class FiniteAutomaton:
    def __init__(self, grammar):
        self.states = []
        self.alphabet = grammar.VT
        self.transitions = {}
        self.start_state = 'S'
        self.accept_states = []

        for symbol in grammar.VN + grammar.VT:
            self.states.append(symbol)

        for symbol in grammar.VN:
            for production in grammar.P[symbol]:
                self.transitions[(symbol, production)] = []

        for symbol in grammar.VN:
            for production in grammar.P[symbol]:
                next_state = None
                if set(production).difference(set(grammar.VT)) == set():
                    next_state = 'F'
                    self.accept_states.append(next_state)
                else:
                    next_symbol = list(set(production).difference(set(grammar.VT)))[0]
                    next_state = next_symbol + '_' + str(len(self.transitions[(symbol, production)]))
                    self.transitions[(symbol, production)].append((next_state, next_symbol))
                    self.states.append(next_state)

        for state in self.states:
            """
            Check if the given input string can be obtained via the state transition
            """
            if state != 'F':
                for symbol in self.alphabet:
                    next_state = 'F'
                    if (state, symbol) in self.transitions:
                        next_states = [t[0] for t in self.transitions[(state, symbol)]]
                        if len(next_states) == 1:
                            next_state = next_states[0]

                    self.transitions[(state, symbol)] = next_state

    def check_string(self, string):
        current_state = self.start_state
        for symbol in string:
            if (current_state, symbol) not in self.transitions:
                return False

            current_state = self.transitions[(current_state, symbol)]

        return current_state in self.accept_states
