from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author - MUST HAVE THESE EXACT QUERIES"""
    author = Author.objects.get(name=author_name)  # First required pattern
    books = Book.objects.filter(author=author)    # Second required pattern
    return books

def get_books_in_library(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Test demonstration
def test_queries():
    # Setup test data
    test_author = Author.objects.create(name="Test Author")
    Book.objects.create(title="Test Book 1", author=test_author)
    Book.objects.create(title="Test Book 2", author=test_author)
    
    # Execute and print the required query
    print("Books by author:")
    books = get_books_by_author("Test Author")
    for book in books:
        print(f"- {book.title}")

if __name__ == "__main__":
    test_queries()