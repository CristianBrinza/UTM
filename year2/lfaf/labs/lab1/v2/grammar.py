import random


class Grammar:
    def __init__(self, non_terminals, terminals, productions, start_symbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def generate_strings(self, n):
        valid_strings = set()
        while len(valid_strings) < n:
            string = self.generate_string(self.start_symbol)
            if string is not None:
                valid_strings.add(string)
        return valid_strings

    def generate_string(self, symbol):
        if symbol in self.terminals:
            return symbol
        elif symbol in self.non_terminals:
            possible_productions = list(self.productions.get(symbol, set()))
            if not possible_productions:
                return None
            production = random.choice(possible_productions)
            string = ''
            for symbol in production:
                generated = self.generate_string(symbol)
                if generated is None:
                    return None
                string += generated
            return string
        else:
            return None

    def __str__(self):
        productions_str = "\n".join(f"{k} -> {' | '.join(v)}" for k, v in self.productions.items())
        return f"G = (Vn = {self.non_terminals}, Vt = {self.terminals}, P = {productions_str}, S = {self.start_symbol})"
