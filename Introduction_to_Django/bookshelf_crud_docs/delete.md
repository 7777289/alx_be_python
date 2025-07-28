# Delete Operation

This demonstrates how to delete a Book record using Django ORM.

## Delete a specific book

```python
from bookshelf.models import Book

# Get the book by ID
book = Book.objects.get(id=1)

# Delete the book
book.delete()
Book.objects.all()
# Output: <QuerySet []> if the book was deleted successfully
