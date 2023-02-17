from grammar import Grammar
from finite_automaton import FiniteAutomaton


def generate_strings(grammar, n):
    valid_strings = grammar.generate_strings(n)
    for i, string in enumerate(valid_strings):
        print(f"{i + 1}. {string}")

    
        

        



def check_string(automaton, string):
    if automaton.accepts(string):
        print(f'The string "{string}" is accepted by the automaton.')
    else:
        print(f'The string "{string}" is not accepted by the automaton.')


if __name__ == '__main__':
    grammar = Grammar(
        non_terminals={'S', 'D', 'R'},
        terminals={'a', 'b', 'c', 'd', 'f'},
        productions={
            'S': ['aS', 'bD', 'fR'],
            'D': ['cD', 'dR', 'd'],
            'R': ['bR', 'f'],
        },
        start_symbol='S',
    )

    automaton = FiniteAutomaton(
        states={'q0', 'q1', 'q2', 'q3'},
        alphabet={'a', 'b', 'c', 'd', 'f'},
        transitions={
            ('q0', 'a'): 'q0',
            ('q0', 'b'): 'q1',
            ('q1', 'c'): 'q2',
            ('q1', 'd'): 'q3',
            ('q2', 'c'): 'q2',
            ('q2', 'd'): 'q3',
            ('q3', 'b'): 'q1',
            ('q3', 'f'): 'q0',
        },
        start_state='q0',
        final_states={'q0'},
    )

    while True:
        print('\nWhat would you like to do?')
        print('1. Generate valid strings from the grammar')
        print('2. Check if a string is accepted by the automaton')
        print('3. Quit')

        choice = input('\nEnter your choice: ')

        if choice == '1':
            n = int(input('\nHow many valid strings do you want to generate? '))
            generate_strings(grammar, n)

        elif choice == '2':
            string = input('\nEnter a string to check: ')
            check_string(automaton, string)

        elif choice == '3':
            print('\nGoodbye!')
            break

        else:
            print('\nInvalid choice. Please enter 1, 2, or 3.')
