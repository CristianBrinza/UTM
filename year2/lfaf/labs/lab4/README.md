
<h4 align="center">LFAF FCIM UTM </h4>
<h1 align='center'> 
░█▒░▒█▀▒▄▀▄▒█▀<br>
▒█▄▄░█▀░█▀█░█▀
</h1>

<h3 align="center" >Course: Formal Languages & Finite Automata</h3>
<h1 align="center">Intro to formal languages. Regular grammars. Finite Automata.</h1>
<h4 align="center">Technical University of Moldova  </h4>
<h4 align="center">FCIM   |   UTM   |   Spring 2023</h4><br><br>


<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="https://utm.md/wp-content/uploads/2020/12/logo-sigla.png" />
</p>
</br><p align=right>  
p. Formal Languages and Finite Automata
</p>
<p align=right>  
lab. V. Drumea
</p>
<p align="right" > student FAF-212, Cristian Brinza</p>
</br><p align=center>  
Chisinau 2023
</p>
<hr></br></br></br>

<h1 align='center'> 
Laboratory work nr. 4
</h1>

<p align="center"><i>my variant : </i><b> Variant 3</b></p>

```
p = {
    'S' : ['dB', 'A'],
    'A' : ['d', 'dS', 'aAdAB'],
    'B' : ['aC', 'aS', 'AC'],
    'C' : [''],
    'E' : ['AS']
}

vn = ['S', 'A', 'B', 'C', 'E']
vt = ['a', 'd']
a = vt
```




## Objectives:

1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

---

## Laboratory notes:
A Python dictionary, the type of data that will be mainly used, the grammar looks like this:

```python
# Defining a dictionary representing a context-free grammar
p = {
    'S' : ['dB', 'A'],
    'A' : ['d', 'dS', 'aAdAB'],
    'B' : ['aC', 'aS', 'AC'],
    'C' : [''],
    'E' : ['AS']
}

# Defining the non-terminals and terminals of the grammar
vn = ['S', 'A', 'B', 'C', 'E']
vt = ['a', 'd']
a = vt
```
Note: the epsilon is noted simply as an empty string "".

Unit tests will be implemented for each of the methods responsible for
each step in the CNF conversion. For unit tests, the 'unittest' module
in python will be used.

---

## Implementation description:
This laboratory builds on previous work.

To be more concise, 
the Grammar class type object is created to intake the grammar. 

Additionally,
a new method in the <b>Grammar</b> class that using this given grammar, returns
a new type of object, from a new class:

```python
    def ConvertCNF(self):
        # Create convertor instance
        chomsky_form = CNFConvertor(self.P, self.Vn)
```
```python
        # Remove Epsilon-transitions
        chomsky_form.RemoveEpsilon()
```
```python
        # Remove unit productions, key by key
        for key in chomsky_form.p:
            chomsky_form.RemoveUnitProd(key)
```
```python
        # Remove unproductive symbols:
        chomsky_form.RemoveUnproductive()
```
```python
        # Remove inaccesible, and cleanup the grammar
        chomsky_form.Cleanup()
```
```python
        # Obtain the final Chomsky form
        chomsky_form.Transform()
```
```python
        return chomsky_form
```
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

The new aforementioned class is basically a CNF converter, containing the
methods necessary for each of the CNF conversion steps. These methods are 
called in the code above.

### Step 1. Removing epsilon-transitions:
First one to be used is the method that removes the epsilon-transitions,
and possibly the most difficult to implement. In the end, the method can
be broken down in 5 steps:

```python
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
```
It should be noted that to iterate over all possible combinations, the
'itertools' library was used.

## Unit testing:
```python
    def test_eps_rem(self):
        self.assertEqual(self.cnf_grammar.RemoveEpsilon(),correct_1,'The epsilon was not removed correctly')
```
The correct_1 variable, against which the result of the method is compared
was computed by hand, using the standard rules, and looking like this:
```python

vn = ['S','A','B','C','D','X']
vt = ['a','b']
p = {
'S' : ['dB','A'],
'A' : ['d','dS', 'aAdAB'],
'B' : ['aC','aS','AC'],
'C' : [''],
'E' : ['AS']
}
a = vt

correct = {
    'S' : ['d', 'DB', 'DS', 'FG'],
    'A' : ['d', 'DS', 'FG'],
    'B' : ['a', 'd', 'HS', 'DS', 'FG'],
    'D' : ['d'],
    'F' : ['HA'],
    'G' : ['DI'],
    'H' : ['a'],
    'I' : ['AB']
}
```


As can be seen, the test result was successful, and just to be sure, here
is the result returned by the method:

### Step 2. Removing Unit Productions:
Next in line, is the method that clears any renaming in the grammar.
This method works a little bit different, going through the grammar
line-by-line, recursively if necessary (i.e. if it detects one unit producton
and a second one when it tries to remove it).

```python
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
```

As it removes the renaming, the method transfers all the states associated
with the removed state, while constantly keeping an eye on any possible
cycles forming. If any cycles forms, it is removed using another method:

```python
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
```

#### Unit testing:
Due to it going through the grammar line-by-line, it cannot be tested 
individually, hence the result returned by the  RemoveUnitProd() method 
will be tested through the ConvertCNF() method.

Again, the correct result was computed by hand:

```python
correct_2 = {
    'S' : ['AXaD', 'AaD'],
    'A' : ['aX', 'bX', 'a', 'b'],
    'X' : ['BX', 'b', 'AXaD', 'AaD'],
    'B' : ['AXaD', 'AaD'],
    'C' : ['Ca'],
    'D' : ['aD', 'a']
}
```

```python
    def test_unit_rem(self):
        self.assertEqual(self.reg_grammar.ConvertCNF(),correct_2,'The unit production removal was not correct')
```
#### Test results:
```commandline
...\python.exe "...\_jb_unittest.py" --path .../testing.py
Testing started at 3:34 PM ...
Launching unittests with arguments python -m unittest ...//unittest.py in cristianbrinza@Cristians-MacBook-Pro UTM 

Ran 1 test in 0.002s

OK

Process finished with exit code 0
```
### Step 3. Removing non-productive symbols:
```python
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
```
The Algorithm is simple, it just checks if the transitions has any terminals,
if it doesn't, it gets popped from the grammar.


### Step 4. Unreachable states removal and cleanup:
```python
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
```
This method checks for any unreachable states, but before that it cleans
up any states left that contain any non-terminal removed in the previous
step.


### Step 5. Transforming it into Chomsky Normal Form:

Obtaining the final form by splitting the string in half, and looking in
another dictionary if the new state was already created, otherwise a new
state is given, in the form of a capital letter from the latin alphabet.



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

Here be the final result.

```commandline
S : ['d', 'DB', 'DS', 'FG']
A : ['d', 'DS', 'FG']
B : ['a', 'd', 'HS', 'DS', 'FG']
D : ['d']
F : ['HA']
G : ['DI']
H : ['a']
I : ['AB']
```
