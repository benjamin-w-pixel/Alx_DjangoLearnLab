## API Authentication

1. Obtain a token:
   POST /api/api-token-auth/
   Body: {"username": "yourusername", "password": "yourpassword"}

2. Use the token in headers:
   Authorization: Token yourtokenhere

Permissions:
- Book endpoints require authentication for write operations
- Read operations are available to all users