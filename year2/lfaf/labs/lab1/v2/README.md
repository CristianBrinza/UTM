
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
Laboratory work nr. 1
</h1>

<p align="center"><i>my variant : </i><b> Variant 3</b></p>

```
VN={S, D, R}, 
VT={a, b, c, d, f},
P={ 
    S → aS
    S → bD
    S → fR
    D → cD
    D → dR
    R → bR
    R → f
    D → d
}
```

## Theory
Def:

- **Language** - a means of communicating information, by using visual or audio interpretations of words.
- **Formal language** -  a set of strings based on an alphabet that are generated with the help of a grammar.
- **String** - a combination of symbols generated with the help of rules from the production set.
- **Grammar** - an entity defined by four elements: the set of non-terminal symbols, the set of terminal symbols, the start symbol, and the set of production rules.
- **Automation** - an abstract computational device. It contains the states, an alphabet, transition functions for each state, the initial and final states.
- **Finite automaton** - an automaton with finite amounts of states and transitions.


## Objectives:

1. Understand what a language is and what it needs to have in order to be considered a formal one.
2. Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:
    - Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);
    - Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;
    - Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;
3. According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    - Implement a type/class for your grammar;
    - Add one function that would generate 5 valid strings from the language expressed by your given grammar;
    - Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    - For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;
<br><br>

## Implementation description

<div class="markdown prose w-full break-words dark:prose-invert light"><p>Here's a breakdown of the code and what it does:</p><p><code>grammar.py</code>:</p><ul><li><p><code>class Grammar</code>: this is the main class representing the grammar. It has three attributes:</p><ul><li><code>VN</code>: a set of non-terminal symbols</li><li><code>VT</code>: a set of terminal symbols</li><li><code>P</code>: a set of productions</li></ul></li><li><p><code>__init__(self)</code>: this is the constructor for the <code>Grammar</code> class. It initializes the three attributes of the grammar.</p></li><li><p><code>add_production(self, production)</code>: this method adds a production to the set of productions for the grammar.</p></li><li><p><code>generate_string(self, symbol)</code>: this method generates a random string of terminals from the given symbol. If the symbol is a terminal, it simply returns the symbol. If the symbol is a non-terminal, it applies one of the productions that has the symbol on the left-hand side, and recursively generates strings for each symbol on the right-hand side.</p></li><li><p><code>generate_valid_strings(self, n)</code>: this method generates <code>n</code> valid strings for the grammar. It does this by repeatedly calling <code>generate_string()</code> starting from the start symbol until a valid string is produced. It then adds the string to a list of valid strings, and continues until <code>n</code> strings have been generated.</p></li></ul><p><code>finite_automaton.py</code>:</p><ul><li><p><code>class FiniteAutomaton</code>: this is the main class representing the finite automaton. It has four attributes:</p><ul><li><code>states</code>: a set of states</li><li><code>alphabet</code>: a set of input symbols</li><li><code>transition</code>: a dictionary representing the transition function</li><li><code>start_state</code>: the start state for the automaton</li></ul></li><li><p><code>__init__(self, grammar)</code>: this is the constructor for the <code>FiniteAutomaton</code> class. It takes a grammar as input, and uses it to construct the automaton.</p></li><li><p><code>add_transition(self, state, symbol, next_state)</code>: this method adds a transition to the transition function for the automaton.</p></li><li><p><code>check_string(self, string)</code>: this method checks if the given string can be obtained via state transitions from the start state. It does this by iterating through each symbol in the string, and using the transition function to determine the next state for each symbol. If the final state is an accepting state, it returns <code>True</code>, otherwise it returns <code>False</code>.</p></li></ul><p><code>tests/test_grammar.py</code>:</p><ul><li><p><code>test_generate_string()</code>: this test checks that <code>generate_string()</code> produces the expected output for a given symbol.</p></li><li><p><code>test_generate_valid_strings()</code>: this test checks that <code>generate_valid_strings()</code> produces the expected number of valid strings for the grammar.</p></li></ul><p><code>tests/test_finite_automaton.py</code>:</p><ul><li><code>test_check_string()</code>: this test checks that <code>check_string()</code> correctly identifies whether a given string can be obtained via state transitions from the start state.</li></ul>
<p><code>main.py</code>:</p><p>This is a simple <code>main</code> script that demonstrates how to use the <code>Grammar</code> and <code>FiniteAutomaton</code> classes. It first creates a new <code>Grammar</code> object, adds the productions for the grammar, and then generates 5 valid strings for the grammar. It then creates a new <code>FiniteAutomaton</code> object using the grammar, and checks if the first generated string is accepted by the automaton.</p>
<br>

```
python -m unittest discover -s tests
```

<p>When you run this script, it will print out the 5 valid strings that were generated, and whether the first string is accepted by the automaton.</p>


## Conclusions / Screenshots / Results

<div class="markdown prose w-full break-words dark:prose-invert light"><p>&nbsp;&nbsp;&nbsp;&nbsp; In conclusion, we have implemented a Python program that generates valid strings for a given context-free grammar and converts the grammar to a finite automaton. The program includes several classes, methods, and unit tests to ensure correct functionality.</p><p>&nbsp;&nbsp;&nbsp;&nbsp; The <code>Grammar</code> class represents a context-free grammar with non-terminal and terminal symbols and productions. It includes methods to generate valid strings for the grammar and to add productions to the grammar.</p><p>&nbsp;&nbsp;&nbsp;&nbsp; The <code>FiniteAutomaton</code> class represents a finite automaton with states, input symbols, transition function, and a start state. It includes methods to add transitions to the transition function and to check if a given string is accepted by the automaton.</p><p>&nbsp;&nbsp;&nbsp;&nbsp; We also included a <code>main</code> script that demonstrates how to use the <code>Grammar</code> and <code>FiniteAutomaton</code> classes to generate valid strings for the grammar and check if they are accepted by the automaton. Additionally, we provided unit tests for the <code>Grammar</code> and <code>FiniteAutomaton</code> classes to ensure their functionality.</p><p>&nbsp;&nbsp;&nbsp;&nbsp; Overall, this program provides a useful tool for generating valid strings for a given context-free grammar and checking if they are accepted by a finite automaton, which has a wide range of applications in various fields, such as natural language processing, programming languages, and computer science.</p></div>

<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="resources/Screenshot%202023-02-17%20233744.png"/>
</p>