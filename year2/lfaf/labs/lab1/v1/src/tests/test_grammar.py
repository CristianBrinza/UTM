from src.grammar import Grammar

def test_generate_string():
    g = Grammar()
    assert g.generate_string('a') == 'a'
    assert g.generate_string('b') == 'b'
    assert g.generate_string('c') == 'c'
    assert g.generate_string('d') == 'd'
    assert g.generate_string('f') == 'f'
    assert g.generate_string('S') in ['a', 'bD', 'fR', 'aS', 'bDcD', 'bDdR', 'bDd', 'fRbR', 'fRf']

def test_generate_valid_strings():
    g = Grammar()
    strings = g.generate_valid_strings(5)
    assert len(strings) == 5
    for string in strings:
        assert set(string).difference(set(g.VT)) == set()

