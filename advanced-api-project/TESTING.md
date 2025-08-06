# API Testing Documentation

## Test Structure
- CRUD operation tests
- Authentication/permission tests
- Filtering/Search/Ordering tests
- Error case testing

## How to Run Tests
```bash
python manage.py test api --verbosity=2
```

## Test Cases

### Book API Endpoints
| Test Case | Description | Expected Status |
|-----------|-------------|-----------------|
| test_book_list | GET book list | 200 OK |
| test_book_create_authenticated | POST book (authenticated) | 201 Created |
| test_book_create_unauthenticated | POST book (unauthenticated) | 403 Forbidden |
| test_filter_by_year | Filter by publication year | 200 OK |

## Interpretation
- **200**: Successful request
- **201**: Resource created
- **204**: Resource deleted
- **403**: Permission denied
