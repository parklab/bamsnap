import bamsnap


def test_init_dict():
    assert bamsnap.util.init_dict({'k1':11}, 'k1') == {'k1':11}
    assert bamsnap.util.init_dict({'k1':11}, 'k2') == {'k1':11, 'k2':{}}
    assert bamsnap.util.init_dict({}, 'k3') == {'k3':{}}
    
def test_add_dict_value():
    assert bamsnap.util.add_dict_value({'k1':11}, 'k2', 1) == {'k1':11, 'k2':1}
    assert bamsnap.util.add_dict_value({'k1':11}, 'k1', 2) == {'k1':13}

def test_get_scale():
    assert bamsnap.util.get_scale(1000, 200, 30000) == 37.5
    assert bamsnap.util.get_scale(1000, 200, 1000) == 1.25

def test_convert_int_list():
    assert bamsnap.util.convert_int_list(['1','2','3']) == [1,2,3]
    assert bamsnap.util.convert_int_list(['1',2,'3']) == [1,2,3]
    assert bamsnap.util.convert_int_list(['-1','2','3']) == [-1,2,3]
    assert bamsnap.util.convert_int_list(['a','2','3']) == [2,3]

def test_comma():
    assert bamsnap.util.comma(3546) == '3,546'
    assert bamsnap.util.comma(123453546) == '123,453,546'
    assert bamsnap.util.comma(3546.02) == '3,546.02'

if __name__ == "__main__":
    test_init_dict()
    

