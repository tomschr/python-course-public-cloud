# From https://levelup.gitconnected.com/metaphysics-2036b38fa711

class TypeSafe(type):
    def __init__(cls, name, bases, attrs):
        for key, type in cls.__annotations__.items():
            default = getattr(cls, key, None)
            setattr(cls, key, TypedProperty(key, type, default))


class TypedProperty:
    def __init__(self, key, type, default):
        self.key = key
        self.type = type
        self.default = default

    def __get__(self, instance, cls):
        if instance is None:
            return self
        # If the value is not defined, fall back to the default
        if self.key not in instance.__dict__:
            instance.__dict__[self.key] = self.default
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise AttributeError('{self.key} must be '
                                 '{self.type.__name__}')
        instance.__dict__[self.key] = value

    # If the value is deleted, reset it to the default
    def __delete__(self, instance):
        instance.__dict__[self.key] = self.default


class A(metaclass=TypeSafe):
    x: int = 1
    y: int = 2


if __name__ == "__main__":
    a = A()
    print(a)
    print(vars(a))
    print(A.__annotations__)
