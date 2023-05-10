import itertools


'''
the Grammar class type object is created to intake the grammar. 
A new method in the Grammar class that using this given grammar, 
returns a new type of object, from a new class:

    def ConvertCNF(self):
    
        # Create convertor instance
        chomsky_form = CNFConvertor(self.P, self.Vn)

        # Remove Epsilon-transitions
        chomsky_form.RemoveEpsilon()
        
        # Remove unit productions, key by key
        for key in chomsky_form.p:
            chomsky_form.RemoveUnitProd(key)
       
       # Remove unproductive symbols:
        chomsky_form.RemoveUnproductive()
       
         # Remove inaccesible, and cleanup the grammar
        chomsky_form.Cleanup()
       
         # Obtain the final Chomsky form
        chomsky_form.Transform()
        return chomsky_form
'''
class CNFConvertor:
    def __init__(self, p, Vn):
        self.p = p
        self.Vn = Vn
        self.unavailable_tokens = [ord(x) for x in self.Vn]

    '''
    Method RemoveEpsilon which removes epsilon productions from a grammar. 
    The method takes in a grammar object, which is assumed to be a dictionary with non-terminal 
        symbols as keys and lists of production rules as values. The method first identifies all 
        non-terminals that produce epsilon by iterating over the productions and checking if they contain 
        an empty string. It then generates all possible combinations of non-terminals that can produce epsilon 
        by iterating over the set of epsilon-producing non-terminals and creating new combinations by 
        appending each non-terminal to existing combinations. 
    Next, it generates new productions to replace the epsilon-producing non-terminals by iterating over each 
        production and each combination and removing the combination from the production. 
    It then updates the grammar with the new productions  by iterating over each non-terminal and 
        appending the new productions to its list of production rules. 
    If the empty string is in a non-terminal's list of production rules, it removes it. Finally, it 
        removes any non-terminals that only produce epsilon and updates the non-terminal list accordingly. 
    The method returns the updated grammar.
    '''

    # Define a method to remove epsilon productions from a grammar
    def RemoveEpsilon(self):
        # Step 1: Identify all non-terminals that produce ε.
        # Create an empty set to store non-terminal symbols that produce epsilon (empty string)
        eps_producing = set()

        # Iterate over the keys (non-terminal symbols) and values (productions) of self.p dictionary
        for nt, prods in self.p.items():
            # Check if the empty string is in the set of productions for the current non-terminal symbol
            if "" in prods:
                # If so, add the current non-terminal symbol to the set of epsilon-producing symbols
                eps_producing.add(nt)


        # Step 2: Generate all possible combinations of non-terminals that can produce ε.
        # Define an empty list to hold the epsilon combinations
        eps_combinations = [[]]
        '''
        The code defines a list called eps_combinations and initializes it with an empty list. 
        It then loops through each non-terminal symbol in a variable called eps_producing. For each 
          non-terminal symbol, it loops through each existing combination of epsilon-producing non-terminals
          in the eps_combinations list. It then creates a new combination by appending the current 
          non-terminal to the existing combination and adds it to the list of combinations. 
        The resulting list of all combinations is stored in eps_combinations.
        '''
        # Loop through each non-terminal symbol that produces epsilon
        for nt in eps_producing:
            # Loop through each existing combination of epsilon-producing non-terminals
            for i in range(len(eps_combinations)):
                # Append the current non-terminal to the existing combination and add it to the list of combinations
                eps_combinations.append(eps_combinations[i] + [nt])


        # Step 3: Generate new productions to replace non-terminals that produce ε.
        # This code is used to remove empty productions from the grammar productions.

        # A new dictionary `new_productions` is initialized to store the modified productions.
        new_productions = {}

        # The for loop iterates over the grammar productions `self.p`.
        # `nt` represents the non-terminal in the production and `prods` represents its corresponding productions.
        for nt, prods in self.p.items():
            
            # A new empty list is created for each non-terminal.
            new_productions[nt] = []
            
            # The nested for loop iterates over the individual productions of each non-terminal.
            for prod in prods:
                
                # The `eps_combinations` is a list of empty productions.
                # The following code replaces each empty production in the individual production with an empty string.
                # A new production is created and stored in `new_prod`.
                # The loop runs for each empty production in `eps_combinations`.
                for combination in eps_combinations:
                    new_prod = prod
                    for c in combination:
                        new_prod = new_prod.replace(c, "")
                    
                    # The new production is appended to the list of new productions for the current non-terminal
                    # only if it is not already present in the list of new productions.
                    if new_prod != prod and new_prod not in new_productions[nt]:
                        new_productions[nt].append(new_prod)


        # Step 4: Update the grammar with the new productions.
        # The following code loops over a dictionary of new productions, where each key represents a non-terminal symbol
        # and its value is a list of productions that can be generated by that symbol. 

        for nt, prods in new_productions.items():
            # For each production in the list, check if it's not an empty string and not already in the list of productions
            # associated with the non-terminal symbol. If it satisfies both conditions, append the production to the list.
            for prod in prods:
                if prod != "" and prod not in self.p[nt]:
                    self.p[nt].append(prod)
            
            # Check if there is an empty production in the list of productions associated with the non-terminal symbol. 
            # If so, remove it from the list.
            if "" in self.p[nt]:
                self.p[nt].remove("")


        # Step 5: Remove the element if it consisted only of an epsilon transition

        # This code iterates through the keys in the dictionary self.p.
        # For each key, it checks if its corresponding value is an empty list.
        # If the value is an empty list, it iterates through all keys in the dictionary again.
        # For each of those keys, it iterates through the list of states associated with that key.
        # If the current key being checked is found within a state, that state is removed from the list of states associated with that key.
        # The key with an empty list is added to the to_be_popped list.
        to_be_popped = []
        for key in self.p:
            if self.p[key] == []:
                for key1 in self.p:
                    for state in self.p[key1]:
                        if key in state:
                            self.p[key1].remove(state)

                to_be_popped.append(key)

        # Remove it from dictionary and from nonterminals lists
        # The following code removes the keys in the 'to_be_popped' list from the dictionary 'self.p' and also removes them from the list 'self.Vn'. Finally, it returns the modified dictionary 'self.p'.
        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)
            '''
            This code iterates over the keys in the to_be_popped list, which presumably contains 
            the keys that need to be removed from the dictionary self.p. For each key, the pop() 
            method is used to remove the corresponding key-value pair from the dictionary, and the
              remove() method is used to remove the key from the list self.Vn. Finally, the modified 
              dictionary self.p is returned.
            '''
        return self.p


    # Remove any possible cycle that forms
    # Define a method named RemoveCycles which takes in a 'self' parameter
    def RemoveCycles(self):
        # Iterate through each key in the dictionary 'self.p'
        for key in self.p:
            # Iterate through each state in the value list of the current key
            for state in self.p[key]:
                # Check if the length of the state is 1 and if it's an uppercase letter
                if len(state) == 1 and state.isupper():
                    # Iterate through each state in the value list of the current state
                    for state1 in self.p[state]:
                        # Check if the current state is equal to the current key
                        if state1 == key:
                            # Iterate through each state in the value list of the current state
                            for state2 in self.p[state]:
                                # Check if the current state is not equal to the current key
                                if state2 != key:
                                    # Append the current state to the value list of the current key
                                    self.p[key].append(state2)

                            # Set the value list of the current state to an empty list
                            self.p[state] = []
                            # Break out of the loop
                            break


    # Define a method for removing unit productions
    def RemoveUnitProd(self, key):
        # Loop through the productions of the given key
        for state in self.p[key]:
            # Remove any cycles in the production
            self.RemoveCycles()
            # Check if the production is a unit production
            if len(state) == 1 and state.isupper():
                # If so, iterate over the next production
                for state1 in self.p[state]:
                    # If the next production is also a unit production, call the method recursively
                    if len(state1) == 1 and state1.isupper():
                        self.RemoveUnitProd(state)
                    # Add the next production to the current key's production list
                    self.p[key].append(state1)
                # Remove the unit production from the current key's production list
                self.p[key].remove(state)

    # Define a method for removing unproductive productions
    def RemoveUnproductive(self):
        to_be_popped = []

        # Loop through the keys in the production dictionary
        for key in self.p:
            # Count the number of terminals in each production for the current key
            terminals = 0
            for state in self.p[key]:
                if state.islower():
                    terminals += 1
            # If there are no terminals in any production for the current key, add it to the list of keys to be removed
            if terminals == 0:
                to_be_popped.append(key)

        # Loop through the keys to be removed
        for key in to_be_popped:
            # Remove the key and its productions from the production dictionary
            self.p.pop(key)
            # Remove the key from the list of non-terminal symbols
            self.Vn.remove(key)

        # Return the updated production dictionary
        return self.p


   # Define a method named Cleanup that belongs to a class (self)
    def Cleanup(self):
        # Iterate through all keys in dictionary 'p'
        for key in self.p:
            # Iterate through all states in 'p[key]'
            for state in self.p[key]:
                # Iterate through all letters in 'state'
                for letter in state:
                    # Check if 'letter' is an uppercase letter and not in 'Vn'
                    if letter.isupper() and letter not in self.Vn:
                        # Remove 'state' from 'p[key]'
                        self.p[key].remove(state)

        # Iterate through all non-terminals in 'Vn'
        for nont in self.Vn:
            # Initialize a counter variable 'encounters' to zero
            encounters = 0
            # Iterate through all keys in 'p'
            for key in self.p:
                # Check if 'key' is not equal to 'nont'
                if key != nont:
                    # Iterate through all states in 'p[key]'
                    for state in self.p[key]:
                        # Check if 'nont' is in 'state'
                        if nont in state:
                            # Increment 'encounters' by 1
                            encounters += 1

            # If 'encounters' is equal to 0
            if encounters == 0:
                # Check if 'nont' is in 'p'
                if nont in self.p:
                    # Remove 'nont' from 'p'
                    self.p.pop(nont)
                # Remove 'nont' from 'Vn'
                self.Vn.remove(nont)

        # Return the updated 'p'
        return self.p

    # Define a method named Modifiable that belongs to a class (self) and takes a parameter named 'state'
    def Modifiable(self,state):
        # Check if the length of 'state' is 1 and 'state' is lowercase
        if len(state) == 1 and state.islower():
            # Return False
            return False

        # Check if the length of 'state' is 2 and 'state' is uppercase
        if len(state) == 2 and state.isupper():
            # Return False
            return False

        # Otherwise, return True
        return True


    def Transform(self):
        # For looking up any matching transitions already made
        new_dict = {}
        changes = True
        # These list is useful in generating non-terminals for the final form
        available_tokens = [x for x in range(65, 91) if x not in self.unavailable_tokens]
        while changes:
            changes = False

            for key in self.p:
                #print(f'Current key is {key}')
                for state in self.p[key]:
                    if self.Modifiable(state):
                        #print(f'Current key working on is {key}')
                        new_state = ''
                        # Looking over the first half of a raw state
                        if len(state[0:len(state)//2]) == 1 and state[0:len(state)//2].isupper():
                            new_state += state[0:len(state)//2]
                        elif state[0:len(state)//2] in new_dict:
                            new_state += new_dict[state[0:len(state)//2]]
                        else:
                            xnode1 = chr(available_tokens[0])
                            available_tokens.pop(0)

                            new_state += xnode1
                            self.Vn.append(xnode1)
                            self.p[xnode1] = []
                            self.p[xnode1].append(state[0:len(state)//2])
                            new_dict[state[0:len(state)//2]] = xnode1

                        # Looking over the second half of a raw state
                        if len(state[len(state)//2:]) == 1 and state[len(state)//2:].isupper():
                            new_state += state[len(state)//2:]
                        elif state[len(state)//2:] in new_dict:
                            new_state += new_dict[state[len(state)//2:]]
                        else:
                            xnode2 = chr(available_tokens[0])
                            available_tokens.pop(0)

                            new_state += xnode2
                            self.Vn.append(xnode2)
                            self.p[xnode2] = []
                            self.p[xnode2].append(state[len(state)//2:])
                            new_dict[state[len(state)//2:]] = xnode2

                        # add the newly created state and remove the old one
                        self.p[key].remove(state)
                        self.p[key].append(new_state)

                        changes = True
                        break
                if changes:
                    break

                    '''
                    
        Method called Transform that belongs to a class. The code first declares an empty
          dictionary new_dict and a boolean variable changes set to True. It also creates a 
          list available_tokens of all characters between ASCII 65 and 91 (exclusive) that 
          are not in a list self.unavailable_tokens.
        The method then enters a while loop that continues as long as changes is True. Inside
          the loop, it iterates through each key and value in the dictionary self.p. 
          For each state in a key's list of values, the method checks if the state is modifiable 
          by calling another method Modifiable with the state as an argument.
        If the state is modifiable, the method creates an empty string new_state. It then checks
          the first half of the state and either adds it to new_state if it is a single uppercase 
          letter or looks up the corresponding value in new_dict and adds it to new_state. If it is 
          not found in either place, the method creates a new variable xnode1 from the first character 
          in available_tokens, removes that character from available_tokens, adds xnode1 to the list 
          self.Vn, adds a new key-value
                    '''
        
            # removing duplicates
            for key in self.p:
                self.p[key] = list(dict.fromkeys(self.p[key]))

