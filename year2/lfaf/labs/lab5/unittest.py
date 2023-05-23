# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab4  | variant 3
import unittest
from cnf import CNFConvertor
from Grammar import RegularGrammar



'''
 Due to it going through the grammar line-by-line, it cannot be tested individually, hence the
 result returned by the RemoveUnitProd() method will be tested through the ConvertCNF() method.
'''

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

'''
The TestMethods class is defined, which inherits from the unittest.

TestCase class. The setUp method of this class is used to initialize 
two instances of the aforementioned classes, and assign them to instance 
variables named cnf_grammar and reg_grammar.
'''

# Define a class TestMethods that inherits from unittest.TestCase
class TestMethods(unittest.TestCase):
    
    
    # Define a method called setUp that initializes two instances of classes and assigns them to instance variables
    '''
    The setUp method is called before each test method is run and initializes 
      two objects: self.cnf_grammar and self.reg_grammar. These objects are instances
      of two different classes: CNFConvertor and RegularGrammar, respectively.
        The constructor for CNFConvertor takes two arguments p and vn, while the 
        constructor for RegularGrammar takes four arguments: vn, vt, p, and a.
    '''
    def setUp(self):
        # Assign an instance of CNFConvertor class to the instance variable cnf_grammar with two arguments p and vn
        self.cnf_grammar = CNFConvertor(p,vn)
        # Assign an instance of RegularGrammar class to the instance variable reg_grammar with four arguments vn, vt, p, and a
        self.reg_grammar = RegularGrammar(vn,vt,p,a)





#The four test methods each test a different method of the CNFConvertor class. 


    # Define a method called test_eps_rem that checks if a method called RemoveEpsilon returns the expected result
    '''
    The first test method, test_eps_rem, calls the RemoveEpsilon method of the 
      self.cnf_grammar object and checks that the result matches the expected output,
      which is stored in the variable correct. The RemoveEpsilon method removes all
      epsilon productions from the grammar. Epsilon productions are productions that 
      derive the empty string.
    '''
    def test_eps_rem(self):
        # Use the assertEqual method of the unittest.TestCase class to check if RemoveEpsilon() method of cnf_grammar instance returns correct output
        self.assertEqual(self.cnf_grammar.RemoveEpsilon(),correct,'The epsilon was not removed correctly')

    # Define a method called test_unit_rem that checks if a method called ConvertCNF returns the expected result
    '''
    The second test method, test_unit_rem, calls the ConvertCNF method of the self.reg_grammar 
    object and checks that the result matches the expected output. The ConvertCNF method converts 
    a regular grammar into a Chomsky Normal Form (CNF) grammar. CNF is a standard form 
    for context-free grammars, which has two types of productions: either a production 
    of the form A → BC or A → a, where A, B, and C are nonterminals and a is a terminal.
    '''
    def test_unit_rem(self):
        # Use the assertEqual method of the unittest.TestCase class to check if ConvertCNF() method of reg_grammar instance returns correct output
        self.assertEqual(self.reg_grammar.ConvertCNF(),correct,'The unit production removal was not correct')

    # Define a method called test_unpr_rem that checks if a method called RemoveUnproductive returns the expected result
    '''
    The third test method, test_unpr_rem, calls the RemoveUnproductive method of the
      self.cnf_grammar object and checks that the result matches the expected output. 
      The RemoveUnproductive method removes all unproductive nonterminals from the grammar.
      A nonterminal is unproductive if it cannot derive any terminal string.
    '''
    def test_unpr_rem(self):
        # Assign correct value to the p instance variable of cnf_grammar instance
        self.cnf_grammar.p = correct
        # Use the assertEqual method of the unittest.TestCase class to check if RemoveUnproductive() method of cnf_grammar instance returns correct output
        self.assertEqual(self.cnf_grammar.RemoveUnproductive(),correct,'The unprodoctive removal went wrong')

    # Define a method called test_cln that checks if a method called Cleanup returns the expected result
    '''
    The fourth test method, test_cln, calls the Cleanup method of the 
    self.cnf_grammar object and checks that the result matches the expected output. 
    The Cleanup method removes all unreachable nonterminals from the grammar. 
    A nonterminal is unreachable if it cannot be reached from the start symbol 
    of the grammar.
    '''
    def test_cln(self):
        # Assign correct value to the p instance variable of cnf_grammar instance
        self.cnf_grammar.p = correct
        # Use the assertEqual method of the unittest.TestCase class to check if Cleanup() method of cnf_grammar instance returns correct output
        self.assertEqual(self.cnf_grammar.Cleanup(),correct,'The cleanup went wrong!')



'''
In the first test method, called test_eps_rem, the RemoveEpsilon method 
of CNFConvertor instance is tested. The second test method, test_unit_rem, 
tests the ConvertCNF method of RegularGrammar instance. The third test method, 
test_unpr_rem, tests the RemoveUnproductive method of CNFConvertor instance. 
Finally, the fourth test method, test_cln, tests the Cleanup method of CNFConvertor 
instance.

The final if statement checks if this code is being run as the main program. 
If it is, the unittest.main() function is called, which runs the tests in the 
TestMethods class.
'''


# If this script is being run as the main program, execute unittest.main() function to run the tests in TestMethods class
if __name__ == '__main__':
    unittest.main()
