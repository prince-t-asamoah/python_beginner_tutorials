# Run pytest or python -m nose2 or python -m unittest discover -s {test_source} test command to run tests


def test_sum_list():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    print("List sum test passed successfully")


def test_sum_tuple():
    assert sum((1, 2, 3)) == 6, "Should be 6"
    print("Tuple sum test passed successfully")

# Test function performance using pytest benchmark test runner
def test_my_function(benchmark):
    benchmark(test_sum_list)