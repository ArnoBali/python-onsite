# https://www.python-course.eu/python3_class_and_instance_attributes.php

class Count(object):
    num = 0
    def __init__(self):
        # 'print(Count)' returns what object a 'Count' object is, which
        # is the same as asking for 'print(type(self))' therefore:
        Count.num += 1  # is same as: type(self).num += 1

# the class attribute 'num' is 1
i = Count()
print(i.num)

# the class attribute 'num' is 2 for both instances
j = Count()
print(j.num)
print(i.num)

# the class attribute 'num' is now 3 for all instances
k = Count()
print(i.num)
print(j.num)
print(k.num)

# etc.
