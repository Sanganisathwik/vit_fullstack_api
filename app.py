from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

def is_number(s):
    """Check if a string represents a number"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_integer(s):
    """Check if a string represents an integer"""
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_alphabet(s):
    """Check if a string contains only alphabets"""
    return s.isalpha()

def is_special_character(s):
    """Check if a string is a special character"""
    return len(s) == 1 and not s.isalnum()

def process_array(data):
    """Process the input array and return categorized results"""
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    sum_numbers = 0
    all_alphabets = []
    
    for item in data:
        if is_number(item):
            if is_integer(item):
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
                sum_numbers += num
        elif is_alphabet(item):
            alphabets.append(item.upper())
            all_alphabets.extend(list(item))
        elif is_special_character(item):
            special_characters.append(item)
    
    # Create concatenated string with alternating caps in reverse order
    if all_alphabets:
        # Reverse the list and create alternating caps
        reversed_alphabets = all_alphabets[::-1]
        concat_string = ""
        for i, char in enumerate(reversed_alphabets):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
    else:
        concat_string = ""
    
    return {
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(sum_numbers),
        "concat_string": concat_string
    }

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        # Get JSON data from request
        request_data = request.get_json()
        
        if not request_data or "data" not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Missing 'data' field in request"
            }), 400
        
        data = request_data["data"]
        
        if not isinstance(data, list):
            return jsonify({
                "is_success": False,
                "error": "'data' must be an array"
            }), 400
        
        # Process the array
        result = process_array(data)
        
        # Create response with user information
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Example user ID
            "email": "john@xyz.com",  # Example email
            "roll_number": "ABCD123",  # Example roll number
            "odd_numbers": result["odd_numbers"],
            "even_numbers": result["even_numbers"],
            "alphabets": result["alphabets"],
            "special_characters": result["special_characters"],
            "sum": result["sum"],
            "concat_string": result["concat_string"]
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": f"An error occurred: {str(e)}"
        }), 500

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "BFHL API is running",
        "endpoint": "/bfhl",
        "method": "POST",
        "description": "Process arrays and return categorized results"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
