

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    def __str__(self):
        return f"User: {self.name} | Email: {self.email}"


