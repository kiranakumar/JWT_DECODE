# JWT_DECODE
This script is a Python utility for decoding and inspecting JWT (JSON Web Tokens). It allows you to extract and view the header and payload information from a JWT without verifying its signature. Additionally, it checks for the expiration time (exp field) and determines if the token is still valid.
# Key Features:

JWT Decoding:
The script decodes the header and payload of a JWT.
The output is displayed in a human-readable format with each key-value pair printed on separate lines.

Expiration Validation:
If the JWT includes an exp (expiration) claim, the script checks if the token is still valid by comparing it to the current time.
If the token has expired, the script informs you when it expired.

Custom Formatting:
The output starts with a bold-style heading "JWT_DECODE" that is simulated using uppercase letters and asterisks.
Additional spacing is added after the command to improve readability and structure.

# Usage
Command-Line Input:

python jwt_check_expiration.py <your_jwt_token>

# Output Format:
*******************************
          JWT_DECODE           
*******************************


Decoded JWT Header:
alg: HS256
typ: JWT

Decoded JWT Payload:
sub: 1234567890
name: John Doe
iat: 1516239022
exp: 1672412312

Token is valid. It will expire at Sat Dec 30 12:58:32 2023.
-------------------------------------------------------------------
