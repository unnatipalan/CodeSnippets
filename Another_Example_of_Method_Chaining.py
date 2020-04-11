#!/usr/bin/env python
# -*- coding: utf-8 -*-

# method_chaining.py
# Jim Bagrow
# Last Modified: 2016-12-05

"""
Method chaining (or cascading) is a technique for making many calls to an
object with less code. Each method should return a reference to the object
itself (in Python this reference is called `self`). Then, instead of writing:
    A.method1()
    A.method2()
You can write:
    A.method1().method2()
This works because A.method1(), while it may perform some internal task,
returns A itself. So, in a sense, A.method1() is equal to A.
Below is a silly Python example.
"""


class Jarvis():

    def __init__(self, data):
        self.data = data

    def train_sum(self, newX):
        self.data = [x + newX for x in self.data]

        return self  # This is what allows chaining

    def train_prod(self, beta):
        self.data = [x * beta for x in self.data]
        return self


# initialize the object:
jv = Jarvis([1, 2, 3, 4])

# use its methods
jv.train_sum(2)
jv.train_prod(10)
print(jv.data)

# the same thing with method chaining:
jv = Jarvis([1, 2, 3, 4])

print(jv.train_sum(2).train_prod(10).data)