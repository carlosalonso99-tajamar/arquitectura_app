# Entidades de dominio
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def validate(self):
        if "@" not in self.email:
            raise ValueError("Invalid email address")
