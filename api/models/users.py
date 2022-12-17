from . import PeeweeBaseModel
import peewee as p

class Users(PeeweeBaseModel):
  id = p.BigAutoField()
  name = p.TextField()
  active = p.BooleanField()
