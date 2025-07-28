# Retrieve Operation

This demonstrates how to retrieve Book records from the database using Django ORM.

## Retrieve all books
```python
from bookshelf.models import Book

books = Book.objects.all()
print(books)
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
book = Book.objects.get(id=1)
print(book)
# Output: 1984 by George Orwell (1949)
books_by_orwell = Book.objects.filter(author="George Orwell")
print(books_by_orwell)
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
