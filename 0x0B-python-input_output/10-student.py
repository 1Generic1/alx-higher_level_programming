#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ defines student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_nmae = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        json_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_data[attr] = getattr(self, attr)
        return json_data
