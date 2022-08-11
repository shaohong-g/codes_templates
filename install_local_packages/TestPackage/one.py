import pkg_resources

class test:
    def print():
        return "test"
        # print("test")

class another_test:
    def __init__(self):
        self.attribute = "attribute" 

    def print(self):
        return f"Printing attribute: {self.attribute}"
        # print(f"Printing attribute: {self.attribute}")


def test_function():
    return "test_function"
    # print("test_function")


def test_data_files():
    import pandas as pd
    from IPython.display import display

    stream = pkg_resources.resource_stream(__name__, 'static/test.csv')
    df = pd.read_csv(stream)
    display(df)


if __name__ == "__main__":
    one_instance = another_test()

    print("Test 1:")
    print(f"Expected output: test, Actual output: {test.print()}")

    print("Test 2:")
    print(f"Expected output: 'Printing attribute: attribute', Actual output: '{one_instance.print()}'")

    print("Test 3:")
    print(f"Expected output: 'test_function', Actual output: '{test_function()}'")

    print("Test 4:")
    test_data_files()