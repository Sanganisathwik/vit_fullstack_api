# BFHL REST API

A Flask-based REST API that processes arrays and returns categorized results.

## Features

- **POST** endpoint `/bfhl` that processes input arrays
- Categorizes data into even numbers, odd numbers, alphabets, and special characters
- Calculates sum of numbers
- Creates concatenated string with alternating caps in reverse order
- Returns user information including user_id, email, and roll number

## API Endpoint

### POST /bfhl

Processes an array and returns categorized results.

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Examples

### Example A
**Input:** `["a", "1", "334", "4", "R", "$"]`
**Output:** 
- odd_numbers: `["1"]`
- even_numbers: `["334", "4"]`
- alphabets: `["A", "R"]`
- special_characters: `["$"]`
- sum: `"339"`
- concat_string: `"Ra"`

### Example B
**Input:** `["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]`
**Output:**
- odd_numbers: `["5"]`
- even_numbers: `["2", "4", "92"]`
- alphabets: `["A", "Y", "B"]`
- special_characters: `["&", "-", "*"]`
- sum: `"103"`
- concat_string: `"ByA"`

### Example C
**Input:** `["A", "ABcD", "DOE"]`
**Output:**
- odd_numbers: `[]`
- even_numbers: `[]`
- alphabets: `["A", "ABCD", "DOE"]`
- special_characters: `[]`
- sum: `"0"`
- concat_string: `"EoDdCbAa"`

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## Deployment

The application is configured for deployment on platforms like Heroku, Railway, or Render with the provided `Procfile`.

## Technologies Used

- Python 3.x
- Flask
- Flask-CORS
- Gunicorn (for production) 