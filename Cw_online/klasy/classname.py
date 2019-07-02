
class A:
    pass


class B:
    pass


class C:
    pass


A = A()
B = B()
C = C()

'''
class ClassName:

    @classmethod
    def get_name(cls, obj):
        cls.obj = type (obj)
        return cls.obj


print(ClassName.get_name(A))
'''


class ClassName:

    def __init__(self, obj):
        self.obj = type (obj)

    def __str__(self):
        return str(self.obj)   


print(ClassName(A))

