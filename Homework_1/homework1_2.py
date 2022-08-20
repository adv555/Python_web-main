class Meta(type):
    children_number = 0

    def __new__(mcs, name, bases, attrs):
        attrs["class_number"] = mcs.children_number
        mcs.children_number += 1
        return super().__new__(mcs, name, bases, attrs)


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data





assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
