import iptk_data as data


normalize = data.Normalize()
present = data.Present()

# TEST NORMALIZE CLASS #

def test_normalize():
    assert normalize.normalize("Héllø Wórld!") == 'hello world'
    print(normalize.normalize('19850603', data_type='date'))
    assert normalize.normalize('19850603', data_type='date') == '1985/06/03'
    print('No exceptions for Normalize.normalize()')

# Test normalize date

def test_normalize_date():
    assert normalize.date('19850603')
    print('No exceptions for normalize.date()')

# Test normalize string
def test_normalize_string():
    assert normalize.string('Ø [Phase]') == 'o phase'
    assert normalize.string("Héllø Wórld!") == 'hello world'
    assert normalize.string("HELLO WORLD") == 'hello world'
    assert normalize.string('hello world') == 'hello world'
    print('No exceptions for Normalize.string()')


def test_normalize_num():
    return



def test_normalize_flt():
    return


# TEST PRESENT CLASS #

# Test present title
def test_present_title():
    assert present.title("Héllø Wórld!") == 'Hello World'
    assert present.title("HELLO WORLD") == 'Hello World'
    assert present.title('hello world') == 'Hello World'
    assert present.title('hello AND world') == 'Hello & World'
    assert present.title('hello AND AND world') == 'Hello & and World'
    assert present.title('Hello OF world') == 'Hello of World'
    assert present.title('synthpop') == 'Synthpop'
    print('No exceptions for Present.title()')

if __name__ == "__main__":
    test_normalize()
    test_normalize_date()
    test_normalize_string()
    test_normalize_num()
    test_normalize_flt()

    #Test Present
    test_present_title()

