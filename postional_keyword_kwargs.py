#!/usr/bin/python

#using postional and dynamic keywords arguments
def format_customer(first_name,last_name,**kwargs):
    strLocation = ""
    for key, value in  kwargs.items():
        if key == "location":
            strLocation = "(" + value + ")"
            print(kwargs['location'])
            print(type(kwargs))
            print(kwargs)
    return first_name + " " + last_name + strLocation

#using postional and keyword argumaets
def format_customer1(first_name,last_name,location=None):
    if location:
        return '%s %s (%s)' % (first_name, last_name, location)
    else:
        return '%s %s' % (first_name, last_name)
