#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    liste = []
    for i in range(0, list_lenght):
        try:
            liste.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            liste.append(0)
            printf("division by 0")
        except TypeError:
            liste.append(0)
            print("wrong type")
        except IndexError:
            liste.append(0)
            print("out of range")
        finally:
            continue
    return liste
