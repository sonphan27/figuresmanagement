import hashlib

from . import PeeweeBaseModel
import peewee as p

class Users(PeeweeBaseModel):
    id = p.BigAutoField()
    name = p.TextField()
    password = p.TextField()
    active = p.BooleanField()

    @classmethod
    def create_(cls, payload):
        if "password" in payload:
            payload["password"] = generate_password(payload["password"])
        user = Users.create(**payload)
        return user


def generate_password(password):
    # adding 5gz as password
    postfix = "erugif"
    # Adding salt at the last of the password
    database_password = password + postfix
    # Encoding the password
    hashed = hashlib.md5(database_password.encode())
    return hashed.hexdigest()