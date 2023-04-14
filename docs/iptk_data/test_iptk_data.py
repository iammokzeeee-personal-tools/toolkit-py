import iptk_data as data


normalize = data.Normalize
present = data.Present()

# TEST NORMALIZE CLASS #

# Test normalize string
def test_normalize_string():
    assert normalize.string('Ø [Phase]') == 'o phase'
    assert normalize.string("Héllø Wórld!") == 'hello world'
    assert normalize.string("HELLO WORLD") == 'hello world'
    assert normalize.string('hello world') == 'hello world'
    print('No exceptions for Normalize.string()')

test_normalize_string()

def test_normalize_num():
    return

test_normalize_num()

def test_normalize_flt():
    return

test_normalize_flt()

# TEST PRESENT CLASS #

# Test present title
def test_present_title():
    assert present.title("Héllø Wórld!") == 'Hello World'
    assert present.title("HELLO WORLD") == 'Hello World'
    assert present.title('hello world') == 'Hello World'
    print('No exceptions for Present.title()')

test_present_title()