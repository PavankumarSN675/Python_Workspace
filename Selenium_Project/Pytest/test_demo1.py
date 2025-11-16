import pytest

@pytest.mark.login
def test_demo1():
    a = 2
    b = 3
    assert a+1 == b, "Test passed successfully"
    assert a == b, "Test failed as a is not equal to b"

def test_demo2():
    name = 'pavan'
    assert name.upper() == "PAVAN"

@pytest.mark.login
def test_demo3():
    assert True

def test_demo4():
    assert False

@pytest.mark.login
def test_demo5():
    assert 100 == 100

def test_demo6():
    assert 'pavan' == 'PAVAN'

@pytest.mark.login
def test_login():
    assert 'pavan' == 'pavan'