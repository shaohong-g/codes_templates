try:
    from TestPackage.one import *
    # raise ImportError # (TESTING)
except ImportError:
    try:
        print("Module 'TestPackage.one.py' not found")
        from one import *
    except ImportError:
        print("Import Error: one.py not found")
        exit(1)


class two_test:
    def print():
        return "two_test"
        print("two_test")

    def print_other():
        return test_function()

class two_another_test:
    def __init__(self):
        self.attribute = "two_attribute" 

    def print(self):
        return f"Printing attribute: {self.attribute}"
        print(f"Printing attribute: {self.attribute}")
    
    def print_other(self):
        one_instance = another_test()
        return one_instance.print()


def two_test_function():
    print("two_test_function")
    print(f"Print from other modules: {test_function()}")


if __name__ == "__main__":
    two_instance = two_another_test()

    print("Test 1.1:")
    print(f"Expected output: two_test, Actual output: {two_test.print()}")
    print("Test 1.2:")
    print(f"Expected output: test_function, Actual output: {two_test.print_other()}")

    print("Test 2.1:")
    print(f"Expected output: 'Printing attribute: two_attribute', Actual output: '{two_instance.print()}'")
    print("Test 2.2:")
    print(f"Expected output: 'Printing attribute: attribute', Actual output: '{two_instance.print_other()}'")

    print("Test 3:")
    two_test_function()