import pytest

from caesar import encode


@pytest.mark.timeout(1.0)  # this checks whether the solution is fast enough
def test_only_non_letters():  # test functions should start with test and then describe clearly what will be tested
    if False in [encode("123456789", 10) == "123456789", encode("304%%#$9023)", 1) == "304%%#$9023)",
                 encode(" 495>/.,", 34) == " 495>/.,"]:  # if any of those functions returns False...
        pytest.fail(f"Numbers and symbols should remain the same.")  # ...then the test will fail with this error message/reason


@pytest.mark.timeout(1.0)
def test_examples():
    if False in [encode("i like turtles", 6) == "o roqk zaxzrky",
                 encode("o roqk zaxzrky", 20) == "i like turtles",
                 encode("example", 1) == "fybnqmf",
                 encode("don't change", 0) == "don't change",
                 encode("the quick brown fox jumps over the lazy dog.", 7) == "aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn."]:  # if any of those functions returns False...
        pytest.fail(f"Trying to encode a regular string with a small shift.")  # ...then the test will fail


@pytest.mark.timeout(1.0)
def test_empty_string():
    if encode("", 5) != "":  # if empty string input doesn't return an empty string, then the test will fail
        pytest.fail("Trying to encode an empty string.")


@pytest.mark.timeout(1.0)
def test_non_letters():
    if encode("hmm... wh4t, oh what?!?‽", 4) != "lqq... al4x, sl alex?!?‽":
        pytest.fail("Trying to encode a string of letters and symbols.")


@pytest.mark.timeout(1.0)
def test_key_zero():
    if encode("this is a message", 0) != "this is a message":
        pytest.fail("Trying to encode a string with a shift of 0.")


@pytest.mark.timeout(1.0)
def test_big_key():
    if encode("rendime saarele sauna", 100) != "najzeia owwnaha owqjw":
        pytest.fail("Trying to encode a string with a shift bigger than the length of the alphabet.")

