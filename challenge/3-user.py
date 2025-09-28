#!/usr/bin/python3
"""
Correct User class with proper password hashing & validation.

- set_password(clear_text): stores a salted hash (never the clear text)
- is_valid_password(clear_text): returns True iff the hash matches

No external libraries; uses hashlib + per-user salt.
"""

from hashlib import sha256
from os import urandom


class User:
    def __init__(self, email: str):
        self.email = email
        # Store salt and hashed password as bytes
        self.__password_salt = None
        self.__password_hash = None

    def set_password(self, password):
        """Set a new password by storing a salted hash."""
        if not isinstance(password, str) or password == "":
            # reject invalid inputs
            self.__password_salt = None
            self.__password_hash = None
            return
        # generate 16-byte random salt
        self.__password_salt = urandom(16)
        # hash(salt || utf8(password))
        self.__password_hash = sha256(self.__password_salt + password.encode("utf-8")).digest()

    def is_valid_password(self, password) -> bool:
        """Return True iff password matches the stored salted hash."""
        if (
            not isinstance(password, str)
            or self.__password_salt is None
            or self.__password_hash is None
        ):
            return False
        test_hash = sha256(self.__password_salt + password.encode("utf-8")).digest()
        return test_hash == self.__password_hash


# Self-tests: should be silent when everything is correct
if __name__ == "__main__":
    u = User("test@example.com")

    # Initially invalid
    assert u.is_valid_password("anything") is False

    # After setting a password
    u.set_password("Holberton!")
    assert u.is_valid_password("Holberton!") is True
    assert u.is_valid_password("holberton!") is False

    # Reset password and ensure old no longer works
    u.set_password("NewPass123")
    assert u.is_valid_password("NewPass123") is True
    assert u.is_valid_password("Holberton!") is False
