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
        self.__events = []; #Event objects
        self.__contacts = []; #Contact objects
        self.__event_attendees = []; #EventAttendee objects
        self.__event_uid = 0;
        self.__contact_uid= 0;
    
    # getters (5 methods)
    @property
    def events(self):
        return self.__events; #should return an entire list made up of Event objects

    @property
    def contacts(self):
        return self.__contacts; #should return an entire list made up of Contact objects

    @property
    def event_attendees(self):
        return self.__event_attendees;

    @property
    def event_uid(self):
        return self.__event_uid;

    @property
    def contact_uid(self):
        return self.__contact_uid;

    # setters (5 methods)
    @events.setter
    def events(self, new_events): #this is NOT the method to append an Event to a list. This will replace the list with whatever is passed
        self.__events = new_events;
    
    @contacts.setter
    def contacts(self, new_contacts): #this is NOT the method to append a Contact to a list. This will replace the list with whatever is passed
        self.__contacts = new_contacts;
    
    @event_attendees.setter
    def event_attendees(self, new_event_attendees): #this is NOT the method to append an EventAttendee to a list. This will replace the list with whatever is passed
        self.__event_attendees = new_event_attendees;

    @event_uid.setter
    def event_uid(self, new_event_uid):
        self.__event_uid = new_event_uid;

    @contact_uid.setter
    def contact_uid(self, new_contact_uid):
        self.__contact_uid = new_contact_uid;

    # other methods (6 methods)
    def add_event(self, d:dict):
        new_event = Event(d); #creates a new event, new_event
        self.__events.append(new_event); #appends said event to the event list
        self.__event_uid = self.__event_uid + 1; #increment Event UID counter
        self._sort_events(); #this should call the pre-defined function. If not, try removing an underscore.
    
    def add_contact(self, d:dict):
        new_contact = Contact(d); #creates a new Contact object, new_contact
        self.__contacts.append(new_contact); #appends the newly created contact to the contact list
        self.__contact_uid = self.__contact_uid + 1; #increment Contact UID counter
        self._sort_contacts();

    def is_attending(self, c:Contact, e:Event):
        #this cannot be the best way to implement this, but I had a difficult time
        #visualizing it in my mind, so this will work for now.
        """
        This essentially just checks for the existence of an EventAttendee object
        which is *for the same event as 'e'*, and is *in the same Contact object as 'c'*
        """
        for object in self.__event_attendees: 
            if (object.contact_object == c) and (object.event_object == e):
                return True;
        return False;

    def add_event_attendee(self, c:Contact, e:Event):
        if self.is_attending(c, e):
            pass
        else:
            new_event_attendee = EventAttendee(c, e);
            self.__event_attendees.append(new_event_attendee);
    
    def uid_to_event(self, uid:int):
        for e in self.__events:
            if e.UID == uid:
                return e;
            else:
                return None;

    def uid_to_contact(self, uid:int):
        for c in self.__contacts:
            if c.UID == uid:
                return c;
            else:
                return None;
    
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