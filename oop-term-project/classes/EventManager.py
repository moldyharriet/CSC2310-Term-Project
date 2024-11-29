from classes.EventAttendee import EventAttendee
from classes.Event import Event
from classes.Contact import Contact

'''
This file is where the bulk of your work will be done. 
I have listed each category of method you will need to create in the comments.
I have also listed how many methods will appear in each category.
'''

class EventManager:
    """
    This class is meant to manage the Events, Contacts, and Event_Attendees.
    This class also directly communicates with the GUI as the GUI "has" an EventManager object (aggregation).
    This class has a list of Event objects, a list of Contact objects, and a list of EventAttendee objects.
    """
    # constructor (1 method)
    def __init__(self):
        #for the time being, these are all private attributes. 
        #TODO: might need to change these to protected/public
        self.__event_list:Event = [];
        self.__contact_list:Contact = [];
        self.__eventattendee_list:EventAttendee = [];
        self.__event_uid:int = 0;
        self.__contact_uid:int = 0;
    
    # getters (5 methods)
    @property
    def event_list(self):
        return self.__event_list; #should return an entire list made up of Event objects

    @property
    def contact_list(self):
        return self.__contact_list; #should return an entire list made up of Contact objects

    @property
    def eventattendee_list(self):
        return self.__eventattendee_list;

    @property
    def event_uid(self):
        return self.__event_uid;

    @property
    def contact_uid(self):
        return self.__contact_uid;

    # setters (5 methods)
    @property
    def event_list(self, new_event_list): #this is NOT the method to append an Event to a list. This will replace the list with whatever is passed
        self.__event_list = new_event_list;
    
    @property
    def contact_list(self, new_contact_list): #this is NOT the method to append a Contact to a list. This will replace the list with whatever is passed
        self.__contact_list = new_contact_list;
    
    @property
    def eventattendee_list(self, new_eventattendee_list): #this is NOT the method to append an EventAttendee to a list. This will replace the list with whatever is passed
        self.__eventattendee_list = new_eventattendee_list;

    # other methods (6 methods)

    # pre-existing methods (2 methods; they are already here; no need to touch them)

    def _sort_contacts(self) -> None:
        """
        Sort contacts by their last name
        :returns: None
        """
        # sort the list by lastname (alphabetically)
        self.contacts.sort(key=lambda x: x.lastname)

    def _sort_events(self) -> None:
        """
        Sort the stored events by date
        :returns: None
        """
        self.events.sort(key=lambda x: x.date, reverse=False)
