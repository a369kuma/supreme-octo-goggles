from gpt1 import Book, EBook, AudioBook

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
    # Test display_info method for Book
    book = Book("1984", "George Orwell", 19.49)
    book.display_info()  # Should print the correct information

def test_ebook_initialization():
    # Test with valid inputs
    ebook = EBook("Digital Fortress", "Dan Brown", 9.99, 2.5)
    assert ebook.title == "Digital Fortress"
    assert ebook.author == "Dan Brown"
    assert ebook.price == 9.99
    assert ebook.file_size == 2.5

def test_ebook_display_info():
    # Test display_info method for EBook
    ebook = EBook("Digital Fortress", "Dan Brown", 9.99, 2.5)
    ebook.display_info()  # Should print the correct information

def test_audiobook_initialization():
    # Test with valid inputs
    audiobook = AudioBook("Becoming", "Michelle Obama", 14.99, 19.5)
    assert audiobook.title == "Becoming"
    assert audiobook.author == "Michelle Obama"
    assert audiobook.price == 14.99
    assert audiobook.duration == 19.5

def test_audiobook_display_info():
    # Test display_info method for AudioBook
    audiobook = AudioBook("Becoming", "Michelle Obama", 14.99, 19.5)
    audiobook.display_info()  # Should print the correct information

if __name__ == "__main__":
    test_book_initialization()
    test_apply_coupon()
    test_display_info()
    test_ebook_initialization()
    test_ebook_display_info()
    test_audiobook_initialization()
    test_audiobook_display_info()
    print("All tests passed.")
