
# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab5 | variant 3

import re


'''
The class Lexer: statement indicates the start of a class definition, which is a 
logical block that groups together related variables and functions. 
The def __init__(self, file): statement is a function definition that 
is a member of the class. It is used to initialize the object when it is 
created, and takes a file name as an argument. The def tokenize(self): statement 
is another function definition that is a member of the class. It is used to split 
the file content into individual tokens.
'''

# Define a class called Lexer
class Lexer:
    # Constructor to initialize the object with a file
    def __init__(self, file):
        # Open the file for reading
        self.f = open(file, 'r')
        # Define a grammar dictionary that maps tokens to their respective categories
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

        # Initialize an empty list to store the tokenized output
        self.token_list = []

        # Read the contents of the file and split it into tokens
        self.unorganized_tokens = self.f.read().split()

    # Define a method to tokenize the input
    def tokenize(self):

        '''
        In the tokenize function, the while loop uses an index variable i to iterate through 
        each token in the self.unorganized_tokens list. The if statements check if the current 
        token needs to be split into smaller tokens based on certain conditions, such as if it contains 
        a dot or semicolon. If it does, the token is split into smaller tokens and inserted into the
        list using the insert() method.
        '''
        # Initialize a counter variable to keep track of the current token being processed
        i = -1

        # Loop through all the tokens in the input
        while i < len(self.unorganized_tokens)-1:
            
            # Increment the counter variable
            i += 1

            
            '''
            The 'if 'statement checks whether the current token contains a dot (.) and is not equal to 
            a single dot character. If the condition is true, it means that the token needs to be 
            split into two or more smaller tokens.
            The 'pos' variable is assigned the index of the first occurrence of the 
            dot character in the token using the 'index()' method.

            Three new tokens are inserted into the list using the insert() method:
                - The first new token is the substring of the original token up to but not including the dot 
                character, which is obtained using Python slicing syntax ('self.unorganized_tokens[i][:pos]'). 
                This new token is inserted at the same index as the original token.
                
                - The second new token is simply the dot character, which is inserted at the index immediately 
                after the first new token.
                
                - The third new token is the substring of the original token starting from the character 
                immediately after the dot and continuing to the end of the string, which is obtained using slicing 
                '(self.unorganized_tokens[i][pos+1:]'). This new token is only inserted if the original 
                token contains characters after the dot character.

            Finally, the 'continue' statement causes the loop to skip over the remaining statements in the loop and continue
            with the next iteration, effectively ignoring the original token that was just split.
            '''

            # Check if the current token has a dot somewhere in the middle
            if '.' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != '.':
                
                # If it does, split it into two tokens and insert them into the list
                pos = self.unorganized_tokens[i].index('.')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, '.')
                
                # If there are characters after the period, insert them as a separate token
                if pos != len(self.unorganized_tokens[i])-1:
                    self.unorganized_tokens.insert(i + 3, self.unorganized_tokens[i][pos+1:])
                continue

            # Check if the current token is an endline semicolon
            if ';' in self.unorganized_tokens[i] and self.unorganized_tokens[i] != ';':
                # If it is, split it into two tokens and insert them into the list
                pos = self.unorganized_tokens[i].index(';')
                self.unorganized_tokens.insert(i + 1, self.unorganized_tokens[i][:pos])
                self.unorganized_tokens.insert(i + 2, ';')
                continue

            # If the current token is a known keyword or operator, add it to the token list with its category
            if self.unorganized_tokens[i] in self.grammar:
                self.token_list.append([self.grammar[self.unorganized_tokens[i]], self.unorganized_tokens[i]])
            # If the current token is a numeric value, add it to the token list with the category 'numeric'
            elif self.unorganized_tokens[i].isnumeric():
                self.token_list.append(['numeric', self.unorganized_tokens[i]])
            # If the current token is unknown, add it to the token list with the category 'unknown'
            else:
                self.token_list.append(['unknown', self.unorganized_tokens[i]])

        # Return the token list
        return self.token_list



    def regex_tokenize(self):  # Function to classify tokens using regular expressions
        for token in self.unorganized_tokens:
            category = self.categorize_token(token)  # Classify the token using the categorize_token function
            self.token_list.append([category, token])  # Add the classified token to the token_list

        return self.token_list  # Return the list of classified tokens

    def categorize_token(self, token):  # Function to classify a single token
        for pattern, category in self.grammar.items():  # Iterate through each pattern in the grammar
            if token.isnumeric():  # If the token is numeric, classify it as such
                return 'numeric'

            if re.match(pattern, token):  # If the token matches a pattern, classify it accordingly
                return category

        return 'unknown'  # If the token doesn't match any patterns, classify it as 'unknown'







