class UserAlreadyExists(Exception):
    pass

class UserNotFound(Exception):
    pass


class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, email):
        if username in self.users:
            raise UserAlreadyExists("The username already exists.")

        if "@" not in email:
            raise ValueError("Invalid email format.")

        self.users[username] = {"email": email}
        return True

    def get_user(self, username):
        if username not in self.users:
            raise UserNotFound("User not found.")
        return self.users[username]

    def delete_user(self, username):
        if username not in self.users:
            raise UserNotFound("User not found.")
        del self.users[username]
        return True

    def update_email(self, username, new_email):
        if username not in self.users:
            raise UserNotFound("User not found.")
        if "@" not in new_email:
            raise ValueError("Invalid email format.")
        self.users[username]["email"] = new_email
        return True
