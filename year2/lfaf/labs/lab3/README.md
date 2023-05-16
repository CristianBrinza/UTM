
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
Laboratory work nr. 3
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
1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

---

## On Lexical Analysis and Scanners
For the purposes of this laboratory, lexical analysis means the
transformation of a sequence of characters into a series of lexical
tokens.
The program/algorithm that does this is called the lexer (or scanner),
and it is the main character of this here laboratory.

---
## Implementation description:
The class new 'Lexer' was created, that opens a text file where the 
code in the given language is.

For this particular example, the grammar used was the one developed
during the semester project, that can be accessed [here](https://github.com/inga-paladi/DSL-for-PLC/blob/master/src/Program.g4).

The particular code that will be used, looks like this:
```commandline
BEGIN
v
INPUT
I 011. Q 011;
OUTPUT
Q 011. M 011;
RAM
CN01.AND I 011. Q 011 . CN04.NOT Q 011. I 011;
I 011 := NOT I 011
END
```

How the algorithm works, is by mapping the grammar into a dictionary:
```python
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
```

From the code file, the algorithm separates the code into individual
words, by use of the '.split()' method, and splits them again if there
are any points or semicolons.

From there on, using the dictionary, the words are tokenized, according
to their keyes. If the word is numeric, it also tokenized, despite not
being in the dictionary.

If, however, the word is not in the grammar or a numeric one, it is
defined as 'unknown'.

The end result, i.e. the token list, for the provided code looks like
this:
```commandline
[['keywords', 'BEGIN'], ['unknown', 'v'], ['keywords', 'INPUT'], 
['variables', 'I'], ['numeric', '011'], ['separators', '.'], 
['variables', 'Q'], ['numeric', '011'], ['separators', ';'], 
['keywords', 'OUTPUT'], ['variables', 'Q'], ['numeric', '011'],
['separators', '.'], ['variables', 'M'], ['numeric', '011'], 
['separators', ';'], ['keywords', 'RAM'], ['contacts', 'CN01'], 
['separators', '.'], ['logic gates', 'AND'], ['variables', 'I'], 
['numeric', '011'], ['separators', '.'], ['variables', 'Q'], 
['numeric', '011'], ['separators', '.'], ['contacts', 'CN04'], 
['separators', '.'], ['logic gates', 'NOT'], ['variables', 'Q'], 
['numeric', '011'], ['separators', '.'], ['variables', 'I'], 
['numeric', '011'], ['separators', ';'], ['variables', 'I'], 
['numeric', '011'], ['operators', ':='], ['logic gates', 'NOT'], 
['variables', 'I'], ['numeric', '011'], ['keywords', 'END']]

```