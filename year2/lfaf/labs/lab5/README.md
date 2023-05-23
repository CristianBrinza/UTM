
<h4 align="center">LFAF FCIM UTM </h4>
<h1 align='center'> 
░█▒░▒█▀▒▄▀▄▒█▀<br>
▒█▄▄░█▀░█▀█░█▀
</h1>

<h3 align="center" >Course: Formal Languages & Finite Automata</h3>
<h1 align="center">Parser & Building an Abstract Syntax Tree</h1>
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
Laboratory work nr. 5
</h1>

<p align="center"><i>my variant : </i><b> Variant 3</b></p>


## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

---

## Implementation description:


While  laboratory work 3 had similar functionality, it did not depend on regular expressions. In this specific lab, a new strategy is introduced to enhance the Lexer class by incorporating a technique known as 'regex_tokenize.' This innovative method harnesses the power of the 're' library in Python to categorize tokens by employing regular expressions. This novel approach expands the capabilities of the Lexer class and introduces a fresh perspective to the task at hand.


First of all, the categorization of tokens.
---
<div class="markdown prose w-full break-words dark:prose-invert light" bis_skin_checked="1"><p>The language comprises three significant components, namely Suite, Test, and Order, each serving distinct purposes within the script. The Suite functions as the "header" of the script, the Test consists of predefined functions that necessitate testing within the script, and the Order specifies the precise execution sequence of the tests.</p><p>To ensure the correctness of the Abstract Syntax Tree (AST) in various scenarios, different behaviors need to be implemented. Consequently, several private methods have been developed, namely __create_suite, __create_tests (which relies on __create_params), and __create_order.</p><p>Moreover, an additional method named __convert_constant_to_type has been incorporated. This particular method facilitates the conversion of a specific token, recognized as a constant, into the required type for the interpreter.</p></div>

---


<p>The <code>Parser</code> class has an initializer method (<code>__init__</code>) that takes a list of <code>tokens</code> as input. Tokens represent the basic units of the programming language's syntax. The initializer initializes various instance variables, such as <code>tokens</code>, <code>current_token_index</code>, and <code>current_token</code>, which are used to keep track of the parsing process.</p>

```python

class Parser:
    def __init__(self, tokens):
        # tokens are the list of tokens which is input to the parser
        self.tokens = tokens
        # the current_token_index is used to keep track of the current token being parsed
        self.current_token_index = 0
        # the current_token stores the current token being parsed
        self.current_token = None
```

<p>The <code>parse</code> method is the entry point to the parsing process. It calls the <code>advance</code> method to move to the next token and then calls the <code>parse_program</code> method to parse the entire program.</p>

```python
    def parse(self):
        # parse() method is the entry point to the parsing process
        self.advance()
        self.parse_program()

```

<p>The <code>advance</code> method moves the parser to the next token in the list of tokens. It updates the <code>current_token_index</code> and <code>current_token</code> variables accordingly.</p>

```python
    def advance(self):
        # advance() is used to move to the next token in the list
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
            self.current_token_index += 1

```

<p>The <code>match</code> method checks if the current token matches the expected token type. If it does, it advances to the next token using the <code>advance</code> method. If not, it raises a <code>SyntaxError</code> with an appropriate error message.</p>

```python
    def match(self, expected_type):
        # match() is used to check if the current token matches the expected token type
        print(self.current_token)
        if self.current_token[0] == expected_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected token of type '{expected_type}', but found '{self.current_token[0]}'")
```


<p>The <code>parse_program</code> method is responsible for parsing the entire program. It calls several other methods in a specific order to parse different sections of the program, such as the input section, output section, RAM section, and assignment operation.</p>

```python
    def parse_program(self):
        # parse_program() is used to parse the entire program
        self.parse_input_section()
        self.parse_output_section()
        self.parse_ram_section()
        self.match('keywords')  # BEGIN
        self.parse_assignment()
        self.match('keywords')  # END

```

<p>The <code>parse_input_section</code>, <code>parse_output_section</code>, <code>parse_ram_section</code>, and <code>parse_assignment</code> methods are responsible for parsing their respective sections of the program. They use the <code>match</code> method to ensure that the tokens are in the expected order and types.</p>

```python
    def parse_input_section(self):
        # parse_input_section() is used to parse the input section of the program
        self.match('keywords')  # INPUT
        while self.current_token[0] == 'variables':
            self.match('variables')  # I
            self.match('numeric')  # 011
            self.match('separators')  # .
            self.match('variables')  # Q
            self.match('numeric')  # 011
            self.match('separators')  # ;

    

    def display_ast(self):
        # display_ast() is used to visualize the Abstract Syntax Tree (AST) of the parsed program
        G = nx.DiGraph()

        # Create nodes for tokens
        for i, token in enumerate(self.tokens):
            token_type, token_value = token
            G.add_node(i, label=f"{token_type}\n{token_value}")

        # Create edges between tokens based on their order
        for i in range(len(self.tokens) - 1):
            G.add_edge(i, i + 1)

        # Find the indices of Begin, Input, Output, and Ram tokens
        begin_nodes = [node for node in G.nodes if self.tokens[node][1] == "BEGIN"]
        input_nodes = [node for node in G.nodes if self.tokens[node][1] == "INPUT"]
        output_nodes = [node for node in G.nodes if self.tokens[node][1] == "OUTPUT"]
        ram_nodes = [node for node in G.nodes if self.tokens[node][1] == "RAM"]

        # Connect the Input, Output, and Ram sections to the Begin node
        for begin_node in begin_nodes:
            for input_node in input_nodes:
                if input_node > begin_node:
                    G.add_edge(begin_node, input_node)
            for output_node in output_nodes:
                if output_node > begin_node:
                    G.add_edge(begin_node, output_node)
            for ram_node in ram_nodes:
                if ram_node > begin_node:
                    G.add_edge(begin_node, ram_node)

        # Calculate depths for each connected component
        depths = {}
        for component in nx.weakly_connected_components(G):
            component_depths = nx.shortest_path_length(G.subgraph(component), source=begin_nodes[0])
            depths.update(component_depths)

        # Sort the nodes based on depth
        sorted_nodes = sorted(G.nodes, key=lambda node: depths.get(node, 0))

        # Calculate the x-coordinate for each node based on depth
        x_coordinates = {node: i for i, node in enumerate(sorted_nodes)}

        # Calculate the y-coordinate for each node based on depth
        y_coordinates = {node: -depths.get(node, 0) for node in sorted_nodes}

        # Configure plot settings
        node_labels = nx.get_node_attributes(G, 'label')
        edge_labels = {(u, v): '' for u, v in G.edges()}
        plt.figure(figsize=(10, 6))

        # Draw graph
        nx.draw_networkx_nodes(G, pos={node: (x_coordinates[node], y_coordinates[node]) for node in G.nodes},
                               node_color='lightblue', node_size=1200)
        nx.draw_networkx_labels(G, pos={node: (x_coordinates[node], y_coordinates[node]) for node in G.nodes},
                                labels=node_labels, font_size=10, font_color='black')
        nx.draw_networkx_edges(G, pos={node: (x_coordinates[node], y_coordinates[node]) for node in G.nodes},
                               arrowsize=20, edge_color='gray', width=1.5)
        nx.draw_networkx_edge_labels(G, pos={node: (x_coordinates[node], y_coordinates[node]) for node in G.nodes},
                                     edge_labels=edge_labels, font_color='gray')

        # Display graph
        plt.axis('off')
        plt.show()


```


<ul><li>The Parser object is initialized with the input tokens in its <strong>init</strong> method.</li><li>To initiate the parsing process, the parse method is called.</li><li>By moving to the next token in the token list, the advance method is responsible for progressing.</li><li>In order to check if the current token matches the expected type, the match method is used. If a match is found, the parser advances to the next token; otherwise, a SyntaxError is raised.</li><li>The parse_program method is responsible for parsing the entire program. It ensures the presence of the "BEGIN" and "END" keywords and calls various section parsing methods.</li><li>The input section of the program, which includes variable declarations followed by a semicolon, is parsed by the parse_input_section method.</li><li>Similarly, the parse_output_section method handles the parsing of the output section, which also consists of variable declarations followed by a semicolon.</li><li>For parsing the RAM section of the program, which includes contact, logic gate, variable, and numeric tokens, the parse_ram_section method is utilized.</li><li>To parse an assignment statement, the parse_assignment method is used. It involves variables, numeric values, assignment operators, logic gates, and additional variables and numeric values.</li><li>The Parser class guarantees the correct order of token processing and adheres to the specified grammar rules. If a token of an unexpected type is encountered, a SyntaxError is raised to indicate the issue.</li></ul>



## Conclusion
Throughout the course of conducting this laboratory experiment, I successfully developed a basic Parser class designed to parse a specific section of my PBL project. While there is ample room for improvement within this implementation, it effectively parses uncomplicated code snippets. However, it would have been advantageous to enhance error handling capabilities and incorporate support for more intricate declarations and assignments. Parsing serves as a fundamental component of programming, playing a central role in the translation and execution of code. Leveraging the insights garnered from my `Parser` implementation, I am now able to seamlessly "transpile" this code into Python, offering a more streamlined alternative.


## References:

[1] [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)

[2] [parsing-grammar](https://www.thoughtco.com/parsing-grammar-term-1691583)

[3] [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

[4] [interpreterbook](https://interpreterbook.com/)