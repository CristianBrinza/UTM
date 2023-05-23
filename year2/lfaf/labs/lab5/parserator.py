
# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab5 | variant 3

import networkx as nx
import matplotlib.pyplot as plt

# This class Parser is used to parse a set of tokens from a language
class Parser:
    def __init__(self, tokens):
        # tokens are the list of tokens which is input to the parser
        self.tokens = tokens
        # the current_token_index is used to keep track of the current token being parsed
        self.current_token_index = 0
        # the current_token stores the current token being parsed
        self.current_token = None

    def parse(self):
        # parse() method is the entry point to the parsing process
        self.advance()
        self.parse_program()

    def advance(self):
        # advance() is used to move to the next token in the list
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
            self.current_token_index += 1

    def match(self, expected_type):
        # match() is used to check if the current token matches the expected token type
        print(self.current_token)
        if self.current_token[0] == expected_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected token of type '{expected_type}', but found '{self.current_token[0]}'")

    def parse_program(self):
        # parse_program() is used to parse the entire program
        self.parse_input_section()
        self.parse_output_section()
        self.parse_ram_section()
        self.match('keywords')  # BEGIN
        self.parse_assignment()
        self.match('keywords')  # END

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

    def parse_output_section(self):
        # parse_output_section() is used to parse the output section of the program
        self.match('keywords')  # OUTPUT
        while self.current_token[0] == 'variables':
            self.match('variables')  # Q
            self.match('numeric')  # 011
            self.match('separators')  # .
            self.match('variables')  # M
            self.match('numeric')  # 011
            self.match('separators')  # ;

    def parse_ram_section(self):
        # parse_ram_section() is used to parse the RAM section of the program
        self.match('keywords')  # RAM
        while self.current_token[0] == 'contacts':
            self.match('contacts')  # CN01
            self.match('logic gates')  # .AND
            self.match('variables')  # I
            self.match('numeric')  # 011
            self.match('separators')  # .
            self.match('variables')  # Q
            self.match('numeric')  # 011
            self.match('separators')  # .
            self.match('contacts')  # CN04
            self.match('separators')  # .
            self.match('logic gates')  # NOT
            self.match('variables')  # Q
            self.match('numeric')  # 011
            self.match('separators')  # .
            self.match('variables')  # I
            self.match('numeric')  # 011
            self.match('separators')  # ;

    def parse_assignment(self):
        # parse_assignment() is used to parse the assignment operation in the program
        if self.current_token[0] == 'variables':
            self.match('variables')  # I
            self.match('numeric')  # 011
            self.match('operators')  # :=
            self.match('logic gates')  # NOT
            self.match('variables')  # I
            self.match('numeric')  # 011

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
