def bencode():
    pass


def decode():
    pass


def test_bencode_string():
    assert bencode("hello") == "5:hello"
    assert bencode("bencode") == "7:bencode"
    assert bencode("") == "0:"
    print("Test string: Passed")


def test_bencode_integer():
    assert bencode(42) == "i42e"
    assert bencode(0) == "i0e"
    assert bencode(-42) == "i-42e"
    print("Test integer: Passed")


def test_bencode_list():
    assert bencode(["hello", "world"]) == "l5:hello5:worlde"
    assert bencode([]) == "le"
    assert bencode([42, "hello"]) == "li42e5:helloe"
    print("Test list: Passed")


def test_bencode_dict():
    assert bencode({"key": "value"}) == "d3:key5:valuee"
    assert bencode({}) == "de"
    assert bencode({"num": 42, "str": "hello"}) == "d3:numi42e3:str5:helloe"
    print("Test dict: Passed")


# Let's also test nested structures
def test_bencode_nested():
    assert bencode([42, ["hello", "world"], {"key": "value"}]) == "li42el5:hello5:worlde3:key5:valueee"
    assert bencode({"list": [42, "hello"], "dict": {"key": "value"}}) == "d4:dictd3:key5:valuee4:listi42e5:helloee"
    print("Test nested: Passed")


def main() -> None:
    test_bencode_string()
    test_bencode_integer()
    test_bencode_list()
    test_bencode_dict()
    test_bencode_nested()


if __name__ == "__main__":
    main()
