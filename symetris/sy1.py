from cryptography.fernet import Fernet as fernet

def generate_key():
    """
    -- Generate key --
    """

    key = fernet.generate_key()
    print(key)

generate_key()