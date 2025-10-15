# User Registration API

## Endpoints

### POST /api/register
- **Request Body:**
  - For Email-Password Registration:
    - `email`: User's email address
    - `password`: User's password
  - For Google OAuth Registration:
    - `googleToken`: Google OAuth token

- **Responses:**
  - `201 Created`: Returns user details on success.
  - `400 Bad Request`: Returns error messages for invalid inputs.

### POST /api/auth/google
- **Request Body:**
  - `idToken`: Google ID token

- **Responses:**
  - `201 Created`: Returns user details on success.
  - `400 Bad Request`: Returns error messages for invalid inputs.

## Database Schema
- **Users Table:**
  - `id`: Primary Key, Auto Increment
  - `email`: Unique, String
  - `password_hash`: String, for email-password method
  - `google_id`: String, nullable, for Google OAuth
  - `created_at`: Timestamp
  - `updated_at`: Timestamp

## Testing
- Run tests using `pytest` to ensure functionality.