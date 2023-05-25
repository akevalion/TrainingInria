
class EmptyList(Exception):
    pass

def test_something():
    assert 1 == 1

def compute_average(numbers: list) -> float:
    
    if not numbers:
        raise EmptyList()
    return sum(numbers) / len(numbers)

def test_compute_average_of_empty_list():
    try:
        compute_average([])
        raise Exception("Should not run with empty list")
    except EmptyList:
        # its ok to have an error
        pass 

def test_compute_average_of_numbers():
    result = compute_average([1, 2, 3, 4, 5])
    assert result == 3 