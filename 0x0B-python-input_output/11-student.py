#!/usr/bin/python3
'''
-class Student that defines a student by: (based on 9-student.py)
-Public instance attributes:
    -first_name
    -last_name
    -age
-Instantiation with first_name, last_name and age:
 def __init__(self, first_name, last_name, age):
-Public method def to_json(self, attrs=None):
 that retrieves a dictionary representation of a Student instance
 (same as 8-class_to_json.py):
-If attrs is a list of strings, only attribute names contained in
 this list must be retrieved.
-Otherwise, all attributes must be retrieved
-Public method def reload_from_json(self, json):
 that replaces all attributes of the Student instance:
    -You can assume json will always be a dictionary
    -A dictionary key will be the public attribute name
    -A dictionary value will be the value of the public attribute
-You are not allowed to import any module
'''


class Student:
    '''
    this class create the class student
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        myDict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__:
                myDict[i] = self.__dict__[i]
        return myDict

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
        return self.__dict__
