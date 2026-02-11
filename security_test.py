import os

def verify_password(input_password):
    # This is a hardcoded password (Codacy should flag this as a security risk)
    if input_password == os.environ.get("ADMIN_PASSWORD"):
        print("Access Granted")
    else:
        print("Access Denied")

        # ... (your existing code is up here) ...

# Add this check to run the test only when executing the file
if __name__ == "__main__":
    # 1. Simulate setting the secure environment variable
    os.environ["ADMIN_PASSWORD"] = "SuperSecret123"
    
    # 2. Call the function with the matching password
    print("Testing with correct password:")
    verify_password("SuperSecret123")

    # 3. Call the function with a WRONG password (to prove it fails)
    print("\nTesting with wrong password:")
    verify_password("HackerGuess")