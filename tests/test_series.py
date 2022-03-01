from math_series.series import fibonacci,lucas,sum_series


def test_fibonacci01():
    actual = fibonacci(1)
    excepted = 1
    assert  actual == excepted


def test_fibonacci02():
    actual = fibonacci(5)
    excepted = 5
    assert  actual == excepted

def test_fibonacci03():
    actual = fibonacci(3)
    excepted = 2
    assert  actual == excepted


def test_lucas01():
    actual = lucas(0)
    excepted = 2
    assert  actual == excepted

def test_lucas02():
    actual = lucas(1)
    excepted = 1
    assert  actual == excepted

def test_lucas03():
    actual = lucas(4)
    excepted = 7
    assert  actual == excepted

def test_sum_series01():
    actual = sum_series(5)
    excepted = 5
    assert  actual == excepted

def test_sum_series02():
    actual = sum_series(4,2,1)
    excepted = 7
    assert  actual == excepted