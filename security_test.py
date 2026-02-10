import os

def verify_password(input_password):
    # This is a hardcoded password (Codacy should flag this as a security risk)
    if input_password == os.environ.get("ADMIN_PASSWORD"):
        print("Access Granted")
    else:
        print("Access Denied")