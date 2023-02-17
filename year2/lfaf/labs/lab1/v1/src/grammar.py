import random

class Grammar:
    """
    This is the main class representing the grammar. It has three attributes:

        VN: a set of non-terminal symbols
        VT: a set of terminal symbols
        P: a set of productions
    """
    #__init__(self): this is the constructor for the Grammar class. It initializes the three attributes of the grammar.
    def __init__(self):
        # Define the set of non-terminal symbols
        self.VN = {'S', 'D', 'R'}
        # Define the set of terminal symbols
        self.VT = {'a', 'b', 'c', 'd', 'f'}
        # Define the start symbol
        self.start_symbol = 'S'
        # Define the production rules
        self.productions = {
            'S': ['aS', 'bD', 'fR'],
            'D': ['cD', 'dR', 'd'],
            'R': ['bR', 'f']
        }
    
    def generate_string(self, symbol):
        """
        Recursively generate a random string from the given symbol
        (Generate n valid strings)
        """
        # If the symbol is a terminal symbol, return it as is
        if symbol in self.VT:
            return symbol
        # Otherwise, randomly choose a production rule for the symbol and expand it
        production = random.choice(self.productions[symbol])
        return ''.join([self.generate_string(c) for c in production])
    # generate_valid_strings(self, n): this method generates n valid strings for the grammar. 
    # It does this by repeatedly calling generate_string() starting from the start symbol until a valid string is produced. 
    # It then adds the string to a list of valid strings, and continues until n strings have been generated.
    def generate_valid_strings(self, count):
        """
        Generate a list of valid strings from the grammar
        """
        # Initialize the list of generated strings
        strings = []
        # Repeat until the desired number of strings is generated
        while len(strings) < count:
            # Generate a string from the start symbol
            string = self.generate_string(self.start_symbol)
            # If the generated string contains only terminal symbols, add it to the list
            if set(string).difference(set(self.VT)) == set():
                strings.append(string)
        return strings
