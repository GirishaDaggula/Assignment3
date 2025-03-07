from app import calculate_area  

def test_area():
    assert calculate_area(5) == 25  


def test_area_with_student_id():
    assert calculate_area(33) == 33 ** 2  

def test_area_failure():
    assert calculate_area(5) == 30  

