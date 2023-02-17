from typing import Set


class Grammar:
    def __init__(
        self,
        non_terminals: Set[str],
        terminals: Set[str],
        productions: dict,
        start_symbol: str
    ):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def generate_strings(self, n):
        valid_strings = set()
        self.generate_strings_helper(self.start_symbol, '', n, valid_strings)
        return list(valid_strings)[:n]

    def generate_strings_helper(self, symbol, string, n, strings):
        if symbol not in self.non_terminals:
            string += symbol
            strings.add(string)
        elif n > 0:
            for production in self.productions[symbol]:
                for i in range(len(production)):
                    self.generate_strings_helper(
                        production[i],
                        string + production[:i],
                        n - 1,
                        strings
                    )
                    if len(strings) == n:
                        return

    def __str__(self):
        return f'Grammar with non-terminals: {self.non_terminals}, terminals: {self.terminals}, productions: {self.productions}, start symbol: {self.start_symbol}'
