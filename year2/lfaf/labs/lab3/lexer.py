# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab3  | variant 3


# Define a Lexer class
class Lexer:
    def __init__(self, file):
        self.f = open(file, 'r')  # Open the specified file in read mode
        self.grammar = {
            'BEGIN': 'keywords',
            'END': 'keywords',
            'INPUT': 'keywords',
            'OUTPUT': 'keywords',
            'RAM': 'keywords',
            'I': 'variables',
            'Q': 'variables',
            'M': 'variables',
            'AND': 'logic gates',
            'OR': 'logic gates',
            'XOR': 'logic gates',
            'NOT': 'logic gates',
            'CN01': 'contacts',
            'CN02': 'contacts',
            'CN03': 'contacts',
            'CN04': 'contacts',
            ':=': 'operators',
            ';': 'separators',
            '.': 'separators'
        }

        self.token_list = []  # Initialize an empty list for tokens
        self.unorganized_tokens = self.f.read().split()  # Read the file and split its contents into tokens

    def tokenize(self):
        i = -1
        while i < len(self.unorganized_tokens)-1:
            i += 1

            # Check if token has a dot somewhere in the middle
            if '.' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != '.':
                pos = self.unorganized_tokens[i].index('.')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, '.')
                if pos != len(self.unorganized_tokens[i])-1:
                    self.unorganized_tokens.insert(i + 3, self.unorganized_tokens[i][pos+1:])
                continue

            # Check if there is an endline semicolon
            if ';' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != ';':
                pos = self.unorganized_tokens[i].index(';')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, ';')
                continue

            # Classify the token based on the defined grammar
            if self.unorganized_tokens[i] in self.grammar:
                self.token_list.append([self.grammar[self.unorganized_tokens[i]], self.unorganized_tokens[i]])
            elif self.unorganized_tokens[i].isnumeric():
                self.token_list.append(['numeric', self.unorganized_tokens[i]])
            else:
                self.token_list.append(['unknown', self.unorganized_tokens[i]])

        return self.token_list


# Create a Lexer instance and tokenize the code
NewLexer = Lexer('code.txt')
tokens = NewLexer.tokenize()

# Print the tokens
print(tokens)
