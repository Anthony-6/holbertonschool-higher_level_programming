#!/usr/bin/python3
'''
this program import json and os module to make it work
'''
import json
import os
'''
Class Base:
-private class attribute __nb_objects = 0
-class constructor: def __init__(self, id=None)::
-if id is not None, assign the public instance attribute id with this
argument value -you can assume id is an integer and you don’t need to
test the type of it-
-otherwise, increment __nb_objects and assign the new value to the public
 instance attribute id
-This class will be the “base” of all other classes in this project. The goal
 of it is to manage
 id attribute in all your future classes and to avoid duplicating the same code
 (by extension, same bugs)
'''


class Base():
    '''
    main class for the programm that inherit from
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        this function test if id is none and create a public instance if not
        none
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        this function check if list dictionnaries is empty or not and
        dumps list dictionnaries
        '''
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        this function check if the list of object is empty or not and
        write the list into a file
        '''
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as myFile:
            if list_objs is None:
                return myFile.write(cls.to_json_string(None))
            else:
                myList = []
                for i in list_objs:
                    myList.append(i.to_dictionary())
                return myFile.write(cls.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        '''
        check if the json string is empty or not and loads the string
        if not
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        this function create a dictionnary with object of square or
        rectangle
        '''
        if cls.__name__ == 'Square':
            dummyVar = cls(1)
        if cls.__name__ == 'Rectangle':
            dummyVar = cls(1, 1)
        dummyVar.update(**dictionary)
        return dummyVar

    @classmethod
    def load_from_file(cls):
        '''
        open a file and check if a file exist or not and create
        the file with needed information if true
        '''
        if os.path.exists(cls.__name__+'.json') is False:
            return []
        else:
            with open(cls.__name__+'.json', 'r', encoding='utf-8') as myFile:
                myList = cls.from_json_string(myFile.read())
                dummyList = []
                for i in range(len(myList)):
                    dummyVar = cls.create(**myList[i])
                    dummyList.append(dummyVar)
                return dummyList
