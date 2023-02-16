# ░█▒░▒█▀▒▄▀▄▒█▀  c. LFAF | FAF | FCIM | UTM | Spring 2023
# ▒█▄▄░█▀░█▀█░█▀  FAF-212 Cristian Brinza lab1


from src.grammar import Grammar
from src.finite_automaton import FiniteAutomaton

if __name__ == '__main__':
    g = Grammar()
    print(g.generate_valid_strings(5))

    fa = FiniteAutomaton(g)
    print(fa.check_string('acd'))
    print(fa.check_string('bdr'))
    print(fa.check_string('ff'))
    print(fa.check_string('bcdf'))
    print(fa.check_string('abd'))

# To run the tests, you can use the following command from the project root directory:
#     python -m unittest discover -s tests

