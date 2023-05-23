
# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab5 | variant 3
import itertools



'''
implementation of a Context-Free Grammar (CFG) to Chomsky Normal 
    Form (CNF) converter. CNF is a simplified version of CFG where each 
    production rule is either in the form of A -> BC or A -> a. This specific
    implementation also includes steps for removing cycles, unit productions, 
    and unproductive/non-terminal symbols. Let's break down the code 
    intosections and comment it accordingly:


This class is used to convert a Context Free Grammar (CFG) to 
    Chomsky Normal Form (CNF). 
The initialisation method (__init__) sets up the initial values 
    for the input grammar (p) and 
    the set of non-terminal variables (Vn). Additionally, it computes 
    the ASCII codes for the non-terminal 
    variables in the CFG and stores them in unavailable_tokens.

'''
class CNFConvertor:
    def __init__(self, p, Vn):
        self.p = p   # Productions of the grammar
        self.Vn = Vn  # Non-terminals of the grammar
        # unavailable tokens that cannot be used for new non-terminals
        self.unavailable_tokens = [ord(x) for x in self.Vn]

    '''
The RemoveEpsilon method removes the epsilon (empty string) productions from the grammar. It follows 
these steps:
    - Step 1: Identify all non-terminals that produce ε.
    - Step 2: Generate all possible combinations of non-terminals that can produce ε.
    - Step 3: Generate new productions to replace non-terminals that produce ε.
    - Step 4: Update the grammar with the new productions.
    - Step 5: Remove the non-terminals that consisted only of an epsilon transition from the production 
    dictionary and the non-terminal list.
This method ultimately returns the updated production dictionary.
'''
    def RemoveEpsilon(self):

        # Step 1: Identify all non-terminals that produce ε.
        eps_producing = set()
        for nt, prods in self.p.items():
            if "" in prods:
                eps_producing.add(nt)

        # Step 2: Generate all possible combinations of non-terminals that can produce ε.
        eps_combinations = [[]]
        for nt in eps_producing:
            for i in range(len(eps_combinations)):
                eps_combinations.append(eps_combinations[i] + [nt])

        # Step 3: Generate new productions to replace non-terminals that produce ε.
        new_productions = {}
        for nt, prods in self.p.items():
            new_productions[nt] = []
            for prod in prods:
                for combination in eps_combinations:
                    new_prod = prod
                    for c in combination:
                        new_prod = new_prod.replace(c, "")
                    if new_prod != prod and new_prod not in new_productions[nt]:
                        new_productions[nt].append(new_prod)

        # Step 4: Update the grammar with the new productions.
        for nt, prods in new_productions.items():
            for prod in prods:
                if prod != "" and prod not in self.p[nt]:
                    self.p[nt].append(prod)
            if "" in self.p[nt]:
                self.p[nt].remove("")

        # Step 5: Remove the element if it consisted only of an epsilon transition
        to_be_popped = []
        for key in self.p:
            if self.p[key] == []:
                for key1 in self.p:
                    for state in self.p[key1]:
                        if key in state:
                            self.p[key1].remove(state)

                to_be_popped.append(key)

        # Remove it from dictionary and from nonterminals lists
        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)

        return self.p

    # Remove any possible cycle that forms
    '''
The RemoveCycles method is used to eliminate any possible cycles in the grammar. It does this by 
checking for any non-terminal that leads to itself, and if it finds such a case, it substitutes the 
recursive non-terminal with its corresponding productions.
'''
    def RemoveCycles(self):

        for key in self.p:
            for state in self.p[key]:
                if len(state) == 1 and state.isupper():

                    for state1 in self.p[state]:
                        if state1 == key:

                            for state2 in self.p[state]:
                                if state2 != key:
                                    self.p[key].append(state2)

                            self.p[state] = []
                            break

    '''
The RemoveUnitProd method is a recursive function that removes unit productions from the grammar. 
A unit production is in the form A -> B, where A and B are non-terminals. The function achieves this by 
substituting the non-terminal on the right-hand side with its corresponding productions.
'''
    def RemoveUnitProd(self,key):

        for state in self.p[key]:
            self.RemoveCycles()
            # Check for unit productions
            if len(state) == 1 and state.isupper():
                # If unit prod is detected, start iterating over next production
                for state1 in self.p[state]:
                    if len(state1) == 1 and state1.isupper():
                        self.RemoveUnitProd(state)

                    self.p[key].append(state1)
                # Remove the Renaming
                self.p[key].remove(state)

    '''
The RemoveUnproductive method removes the unproductive symbols from the grammar. An unproductive symbol 
is a non-terminal that does not produce any terminal symbol string. This method eventually returns the 
updated production dictionary.
'''
    def RemoveUnproductive(self):

        to_be_popped = []

        for key in self.p:
            terminals = 0
            for state in self.p[key]:
                if state.islower():
                    terminals += 1

            if terminals == 0:
                to_be_popped.append(key)

        for key in to_be_popped:
            self.p.pop(key)
            self.Vn.remove(key)

        return self.p

    '''
The Cleanup method is used to eliminate any inaccessibles nodes from the grammar. An inaccessible node 
is a non-terminal that cannot be reached from the start symbol. The method also removes any transitions 
that would lead to any previously removed non-terminals.
'''
    def Cleanup(self):

        # Firstly, remove any transitions that would lead to any previously removed non-terminals
        for key in self.p:
            for state in self.p[key]:
                for letter in state:
                    if letter.isupper() and letter not in self.Vn:
                        self.p[key].remove(state)


        # Then check and remove any inaccesible nodes
        # nont is non-terminal
        for nont in self.Vn:
            encounters = 0
            for key in self.p:
                if key != nont:
                    for state in self.p[key]:
                        if nont in state:
                            encounters += 1

            if encounters == 0:
                if nont in self.p:
                    self.p.pop(nont)
                self.Vn.remove(nont)

        return self.p

    # Checks if a state should be modified or not
    '''
The Modifiable method checks if a state in the grammar should be modified or not. This is based on the 
CNF rules, which stipulate that each production should either be of the form A -> BC or A -> a, where 
A, B, and C are non-terminals and a is a terminal. The method returns True if the state is modifiable 
and False otherwise.
'''
    def Modifiable(self,state):

        if len(state) == 1 and state.islower():
            return False

        if len(state) == 2 and state.isupper():
            return False

        return True

    '''
The Transform method is the main method that transforms the grammar into CNF. It does this by ensuring 
each production is either in the form A -> BC or A -> a. It checks each state and if it's modifiable 
according to the Modifiable method, it splits it into two new states. New non-terminals are generated 
if necessary, while avoiding those already present in the grammar. Duplicates are also removed to keep 
the grammar clean.
'''
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

            # removing duplicates
            for key in self.p:
                self.p[key] = list(dict.fromkeys(self.p[key]))

