# https://levelup.gitconnected.com/descriptors-aplenty-33fb3cacea21

class TypedProperty:
    def __init__(self, type):
        self.type = type

    def __set_name__(self, cls, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        # If it wasn't assigned, resolve to a default value:
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = self.type()
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise AttributeError(f'{self.name} must be '
                                 f'{self.type.__name__}')
        instance.__dict__[self.name] = value


class A:
   x = TypedProperty(int)

   def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    a = A(2)
    print(a.x)
    a.x = 10
    print(a.x)
    a.x = "Hello"
