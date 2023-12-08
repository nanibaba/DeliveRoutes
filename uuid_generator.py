# uuid_generator.py
# This module contains a function to generate unique identifiers (UUIDs) using 
# the uuid4 method from the Python uuid library.

import uuid


def generateUUID():
    """
    Generate a random UUID (Universally Unique Identifier).

    Returns:
        UUID object: A randomly generated UUID.
    """
    return uuid.uuid4()
