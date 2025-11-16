import random

"""" User entity class """
class User:
    """" Constructor """
    def __init__(self, uid: int, uname: str, password: str = "welcome"):
        self.uid = uid
        self.uname = uname
        self.password = password

    def __str__(self):
        """ Magic method: print object"""
        return f'Username: {self.uname} (id: {self.uid}, pw: {self.password}´)'

# Testing User entity med kommandoen `python user.py`
if __name__ == "__main__":
    # Create and print random user (username) 1
    uid = random.randint(1_000, 9_999)
    # Create random user name and password from uid
    random_user = User(uid, f"user_{uid}", f"user_{uid}")
    print('Printing random user')
    print(random_user)

    # Create and print random user (username) 2
    uid = random.randint(1_000, 9_999)
    # Create random user name and password from uid
    random_user = User(uid, f"user_{uid}", f"user_{uid}")
    print('Printing random user')
    print(random_user)
