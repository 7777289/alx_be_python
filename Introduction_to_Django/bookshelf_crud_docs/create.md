# Create Operation

This demonstrates how to create a new Book record using the Django ORM.

```python
from bookshelf.models import Book

# Creating a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Verifying the creation
print(book)
# Output: 1984 by George Orwell (1949)
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
