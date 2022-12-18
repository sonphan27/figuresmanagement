from enum import Enum
from typing import Optional, Type
from peewee import TextField


class _EnumFieldMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        # Set name of EnumClass to that of the main class,
        # so that it can be used directly as FastAPI's field definition
        # If not, there will be name conflict between different EnumClass
        if enum_class := attrs.get("EnumClass"):
            enum_class.__name__ = name

    def __getattr__(cls, key):
        # Add quick access to EnumClass members from EnumField
        if key in cls.EnumClass.__members__:
            return cls.EnumClass.__members__[key]

        raise AttributeError(key)


class EnumField(TextField, metaclass=_EnumFieldMeta):
    EnumClass: Optional[Type[Enum]] = None
    field_type: Optional[str] = None

    def __init__(self, *args, **kwargs):
        if not issubclass(self.EnumClass, Enum):
            raise ValueError("EnumClass is not defined in " + str(self.__class__))
        if not self.__class__.field_type:
            raise ValueError("field_type is not defined in " + str(self.__class__))
        super().__init__(*args, **kwargs)

    def adapt(self, value):
        # pylint: disable=isinstance-second-argument-not-valid-type
        return super().adapt(
            value.value if isinstance(value, self.EnumClass) else value
        )

    def python_value(self, value):
        try:
            return self.EnumClass(value)  # pylint: disable=not-callable
        except ValueError:
            return value


def f(query):
    """query first"""
    for result in list(query.dicts()):
        return result
    return None


def e(query):
    """query for all"""
    return list(query.dicts())
