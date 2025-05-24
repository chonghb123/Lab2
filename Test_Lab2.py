import Lab2 as Lab2

def test_min_max():
    input_arr = [1,2,3,4,5,6]
    test = [1,6]
    result = Lab2.find_min_max(input_arr)
    assert(result == test)
def test_average():
    input_arr = [1,2,3,4]
    test = 10/4
    result = Lab2.calc_average(input_arr)
    assert(result == test)
def test_median():
    input_arr = [1,2,3,4,5]
    test= 3
    result = Lab2.calc_median_temperature(input_arr)
    assert(result == test)

    