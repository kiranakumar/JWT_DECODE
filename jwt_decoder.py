import json
import base64
import argparse
import time

# Decode JWT without verification
def decode_jwt(token):
    try:
        # Add some space and print a heading
        print("\n\n")
        print("*******************************")
        print("          JWT_DECODE           ")
        print("*******************************")
        print("\n")

        header, payload, signature = token.split('.')

        decoded_header = base64.urlsafe_b64decode(header + '==').decode('utf-8')
        decoded_payload = base64.urlsafe_b64decode(payload + '==').decode('utf-8')

        header_json = json.loads(decoded_header)
        payload_json = json.loads(decoded_payload)

        print("Decoded JWT Header:")
        for key, value in header_json.items():
            print(f"{key}: {value}")

        print("\nDecoded JWT Payload:")
        for key, value in payload_json.items():
            print(f"{key}: {value}")

        # Validate expiration if the 'exp' claim exists
        if 'exp' in payload_json:
            expiration_time = payload_json['exp']
            current_time = time.time()

            if current_time < expiration_time:
                print(f"\nToken is valid. It will expire at {time.ctime(expiration_time)}.")
            else:
                print(f"\nToken has expired. Expiration time was {time.ctime(expiration_time)}.")
        else:
            print("\nToken does not contain an expiration ('exp') field.")
    
    except Exception as e:
        print("Error decoding token:", str(e))

# Set up command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode a JWT token and check its expiration.")
    parser.add_argument("jwt_token", help="The JWT token to decode and check expiration")

    args = parser.parse_args()

    # Decode JWT and check expiration
    decode_jwt(args.jwt_token)
