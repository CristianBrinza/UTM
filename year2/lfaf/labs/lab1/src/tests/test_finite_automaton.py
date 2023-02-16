from grammar import Grammar
from finite_automaton import FiniteAutomaton

def test_check_string():
    g = Grammar()
    fa = FiniteAutomaton(g)
    assert fa.check_string('acd') == True
    assert fa.check_string('bdr') == True
    assert fa.check_string('ff') == True
    assert fa.check_string('bcdf') == False
    assert fa.check_string('abd') == False
