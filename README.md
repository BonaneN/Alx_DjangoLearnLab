1. Setting Up a New Django Project with Custom Serializers

Django Project Initialization

Learned to start a Django project and app from scratch.

Configured settings for REST framework integration.

Managed project structure for advanced API development.

Models and Database

Defined Django models (Author and Book) with proper field types.

Established a one-to-many relationship using ForeignKey.

Applied migrations to sync models with the database.

Custom Serializers

Created serializers for complex and nested data.

BookSerializer for the Book model.

AuthorSerializer with nested BookSerializer for related books.

Added custom validation (e.g., ensuring publication_year isn’t in the future).

Learned to handle serialization of related objects and nested structures.

Manual Testing

Used Django shell and admin to create, retrieve, and test model instances.

Validated data serialization and nested relationships.

2. Building Custom Views and Generic Views

Generic Views

Implemented CRUD operations with DRF’s generic views:

ListView, DetailView, CreateView, UpdateView, DeleteView.

Learned how generic views simplify repetitive CRUD logic.

URL Routing

Configured api/urls.py to map endpoints to views.

Ensured endpoint structure is RESTful (/books/, /books/<id>/).

Custom Behavior in Views

Learned to customize Create and Update views for validation.

Applied permission checks to restrict certain actions.

Permissions

Restricted Create, Update, and Delete to authenticated users.

Allowed read-only access for unauthenticated users.

Testing Views

Tested API endpoints using Postman or curl.

Verified CRUD functionality and permissions enforcement.

Documentation

Documented views, their purposes, and customization hooks.

3. Implementing Filtering, Searching, and Ordering

Filtering

Used DjangoFilterBackend to filter books by fields (title, author, publication_year).

Searching

Configured SearchFilter for text-based queries on title and author.

Ordering

Applied OrderingFilter to sort books by any field, e.g., title or publication_year.

Integration in Views

Updated BookListView to include filtering, search, and ordering.

Testing and Usage

Tested query parameters using Postman/curl.

Learned how to allow users to customize the data they receive.

Documentation

Provided instructions for API consumers on how to filter, search, and order results.

4. Writing Unit Tests for DRF APIs

Testing Fundamentals

Learned Django’s built-in test framework (based on unittest).

Configured a separate test database.

CRUD Test Cases

Created tests for:

Creating a book.

Retrieving book data.

Updating a book.

Deleting a book.

Functional Testing

Tested filtering, searching, and ordering functionality.

Verified response status codes and data integrity.

Permissions Testing

Ensured authentication and permissions worked as intended.

Running Tests

Executed tests with python manage.py test api.

Reviewed results and debugged failing tests.

Documentation

Documented testing strategy, test cases, and instructions for running tests.

Skills Gained Overall

Setting up and managing a Django REST Framework project.

Creating custom serializers, including nested relationships.

Using generic views to streamline CRUD operations.

Implementing filtering, searching, and ordering for API endpoints.

Applying authentication and permissions in DRF.

Writing comprehensive unit tests for API reliability.

Documenting models, serializers, views, and tests for maintainability.

Using API testing tools like Postman or curl.

Understanding the full workflow from project setup → development → testing → documentation.