
<h4 align="center">LFAF FCIM UTM </h4>
<h1 align='center'> 
░█▒░▒█▀▒▄▀▄▒█▀<br>
▒█▄▄░█▀░█▀█░█▀
</h1>
<h4 align="center">Technical University of Moldova  </h4>
<h4 align="center">FCIM   |   UTM   |   Spring 2023</h4>
<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="https://utm.md/wp-content/uploads/2020/12/logo-sigla.png" />
</p>
</br><p align=right>  
p. Formal Languages & Finite Automata
</p>
<p align=right>  
c. I. Cojuhari <br>
lab. V. Drumea
</p>
</br><p align=center>  
Chisinau 2023
</p>
<hr></br>
<h3><b> Course grading: </b></h3>

- Laboratories tasks 15%
- Individual work tasks 15%
- Mid-term evaluation (2) 15+ 15%
- Final exam 40%
</br></br>
<p align=right>  
c. LFAF | FCIM UTM Spring 2023 | 3-104 | 08.02.2023
</p>


<h2> Important </h2>

<table>
<tr>
<td><b> Sign</b> </td>
<td><b> Name</b> </td>
<td><b> Exemple</b> </td>
</tr>
<tr>
<td>&#8512;</td>
<td>alfabet</td>
<td>&#8512;={0,1}</td>
</tr>
<tr>
<td></td>
<td>string</td>
<td>010101010</td>
</tr>
<tr>
<td>&epsilon;</td>
<td>empty string</td>
<td>⅀ = ε <i>or</i> |w|=0 <i>or</i> w=ε </td>
</tr>
<tr>
<td>w</td>
<td>length</td>
<td>|w|=3</td>
</tr>
<tr>
<td>G</td>
<td>grammar</td>
<td></td>
</tr>
<tr>
<td>V<sub>T</sub></td>
<td>finite set of<b> non-terminal symbols</b> </td>
<td rowspan="2">V<sub>T</sub> &#8745; V<sub>T</sub> = &#248;</td>
</tr>
<tr>
<td>V<sub>N</sub></td>
<td>finite set of<b> terminal symbols</b> </td>

</tr>
<tr>
<td>S</td>
<td>start symbol;</td>
<td></td>
</tr>
<tr>
<td>P</td>
<td>is a finite set of productions of rules</td>
<td></td>
</tr>
<tr>
<td>CS</td>
<td>Context-Sensitive</td>
<td></td>
</tr>
<tr>
<td>CF</td>
<td>Context-Free</td>
<td></td>
</tr>



</table>
<br>
<hr>
<br>


- **Language** - a means of communicating information, by using visual or audio interpretations of words.
- **Formal language** -  a set of strings based on an alphabet that are generated with the help of a grammar.
- **String** - a combination of symbols generated with the help of rules from the production set.
- **Grammar** - an entity defined by four elements: the set of non-terminal symbols, the set of terminal symbols, the start symbol, and the set of production rules.
- **Automation** - an abstract computational device. It contains the states, an alphabet, transition functions for each state, the initial and final states.
- **Finite automaton** - an automaton with finite amounts of states and transitions.



<br><br>

<h2 align="center">Powers of an alphabet</h2>

- If  ⅀ is an alphabet, we can express the set of all strings of a
certain length from that alphabet by using an exponential
notation.
- ⅀<sup>k</sup> is defined to be the set of strings of length <b>k</b>, each of
whose symbols is in ⅀.
  - ⅀<sup>0</sup> = { ε }
  - ⅀<sup>1</sup> = { 0, 1, 2 }
  - ⅀<sup>2</sup> = { 00, 01, 02, 10, 11, 12, 20, 21, 22 }
  - ⅀<sup>3</sup> = { 000, 001, 002, ... 222 }
- The set of words over an alphabet ⅀ is denoted
by ⅀<sup>&#42;</sup><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⅀<sup>&#42;</sup>  = { a<sub>1</sub>, ... a<sub>n</sub> | a<sub>1</sub>, a<sub>2</sub>, ... a<sub>n</sub> &#8712; ⅀ , n &#8805; 0 } 
- The set of nonempty words over ⅀ is denoted by
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⅀<sup>+</sup>  = ⅀<sup>&#42;</sup> / { ε } 
- The concatenation of the word w<sub>1</sub>
and w<sub>2</sub>
is
denoted by<b><i> w<sub>1</sub>w<sub>2</sub></i></b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; w<sub>1</sub> = 01, w<sub>2</sub> = 11 -> w<sub>1</sub>w<sub>2</sub> = 0111 ,  w<sub>2</sub>w<sub>1</sub> = 1101
- A notation we will commonly use to define languages is by a
“set-former”:
 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 L={ w | something about w }
<br><br>

<h2 align="center">Grammar</h2>
A grammar G is an ordered quadruple
G=(V<sub>N</sub>
, V<sub>T</sub>
, P, S) 

EXAMPLE:

-  Let G = (V<sub>N</sub>
, V<sub>T</sub>
, S, P),
- where V<sub>N</sub>
= {S, A}
-  V<sub>T</sub>
= {a},
- S is a start symbol
- P = {S → aS, S → a}. 
 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 S → aS → <b>a</b>aS → <b>aa</b>aa → <b><i>stop</i></b> 
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  S → a → <b><i>stop</i></b> 
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
   S → aS → <b>a</b>aS → <b>aa</b>a → <b><i>stop</i></b> 
     <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
   S → aS → <b>a</b>aS → <b>aaa</b>S → <b>aaa</b>a | &#8730;

<br><br>
<h2 align="center">Chomsky Classification</h2>

- <b> Type 0</b>. Recursively enumerable languages.
 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Only restriction on rules: left-hand side cannot be the empty
string ( * Ø → ... . )
-  <b> Type 1</b>. Context-Sensitive languages - <i> Context-Sensitive (CS) </i>
rules.
- <b> Type 2</b>. Context-Free languages -<i> Context-Free (CF) rules </i>
- <b> Type 3</b>. Regular languages -<i> Non-Context-Free (CF) rules </i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
0 ⊇ 1 ⊇ 2 ⊇ 3
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
a ⊇ b meaning a properly includes b (a is a superset of b),
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
i.e. b is a proper subset of a or b is in a

<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="documetation_resources/lfaf001.png" />
</p>
<br><br>
<h2 align="center">Types of Grammars -
Chomsky hierarchy of languages</h2><br>
<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="documetation_resources/lfaf002.png" />
</p>
<br><br>
<h2 align="center">Derivation Trees</h2>
A derivation in the language generated by a
<b>grammar</b> can be represented graphically using an
ordered rooted tree, called a <b>derivation (or parse)
tree</b>:

- the <b>root</b> represents the starting symbol,
- <b>internal</b> represent nonterminals,
- <b>leaves</b> represent terminals, and
- the <b>children of a vertex</b> are the symbols on the
right side of a production, in order from left to
right, where the symbol represented by the
parent is on the left-hand side.

Example:

<p align=center>                           
  <img align=center style="height: 30%;
  width: 30%; " src="documetation_resources/lfaf003.png" />
</p>