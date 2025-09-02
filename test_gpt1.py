from gpt1 import Book

def test_book_initialization():
    # Test with valid inputs
    book = Book("1984", "George Orwell", 19.49)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.price == 19.49

    # Test with missing arguments
    try:
        Book("1984")
    except TypeError:
        print("Passed: Missing arguments test")

    # Test with invalid data types
    try:
        Book(1984, 123, "Price")
    except ValueError:
        print("Passed: Invalid data types test")

def test_apply_coupon():
    # Test applying coupon with price attribute
    book = Book("1984", "George Orwell", 100)
    book.apply_coupon(10)
    assert book.price == 90

def test_display_info():
    # Test display_info method
    book = Book("1984", "George Orwell", 19.49)
    book.display_info()  # Should print the correct information

if __name__ == "__main__":
    test_book_initialization()
    test_apply_coupon()
    test_display_info()
    print("All tests passed.")
