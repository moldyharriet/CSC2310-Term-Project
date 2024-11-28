from classes.Contact import Contact
from classes.Event import Event

"""
This class represents a tuple of 1 Event and 1 Contact object, meaning the Contact is attending the Event.
This is its own class because there will be attributes associated to a contact attending an event, e.g.
whether they need a parking pass, special accommodations, etc. 

For now, the "memo" attribute is a catch-all for these, but in the future, more attributes will be added.
"""


class EventAttendee:

    #constructor
    def __init__(self, c:Contact, e:Event):
        self.__contact_object = c;
        self.__event_object = e;
        self.__memo = "";

    # This function defines what happens when you print the object as text, i.e. print(event_attendee)
    # PRINTS IN THE FORM "John Smith attending Data Science League Meeting"
    def __str__(self):
        """
        python has a few ways of streamlining concatenation of strings.
        each time there's a {} in the string that represents a variable.
        notice at the end of the string, ".format()"
        the variables passed into this function will replace each {} (in order)
        """
        return "{} {}\nattending\n{}".format(self.contact.firstname, self.contact.lastname, self.event.name)
    
    #begin getters
    @property
    def contact_object(self):
        return self.__contact_object;

    @property
    def event_object(self):
        return self.__event_object;

    @property
    def memo(self):
        return self.__memo;

    #begin setters
    @contact_object.setter
    def contact_object(self, c:Contact):
        self.__contact_object = c;

    @event_object.setter
    def event_object(self, e:Event):
        self.__event_object = e;

    @memo.setter
    def memo(self, m:str):
        self.__memo = m;
