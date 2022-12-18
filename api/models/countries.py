from enum import Enum
import peewee as p

from utils.db import EnumField

from . import PeeweeBaseModel


class ContinentTypeEnum(EnumField):
    class EnumClass(str, Enum):
        AFRICA = "Africa"
        ANTARCTICA = "Antarctica"
        ASIA = "Asia"
        EUROPE = "Europe"
        OCEANIA = "Oceania"
        NORTH_AMERICA = "North America"
        SOUTH_AMERICA = "South America"

    field_type = "e_continent"


class Countries(PeeweeBaseModel):
    id = p.TextField()
    name = p.TextField()
    continent = ContinentTypeEnum()
