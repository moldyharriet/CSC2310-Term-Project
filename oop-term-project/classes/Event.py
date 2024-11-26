
class Event:

    def __init__(self, d:dict):
        #name
        if(d.get("Name") == ""):
            self.__name = "--";
        else:
            self.__name = d.get("Name");
        
        #uid
        if(d.get("UID") == ""):
            self.__uid = "-1";
        else:
            self.__uid = d.get("UID");
    
        #date
        if(d.get("Date") == ""):
            self.__date = "--";
        else:
            self.__date = d.get("Date");

        #start_time
        if(d.get("StartTime") == ""):
            self.__start_time = "--";
        else:
            self.__start_time = d.get("StartTime");

        #location
        if(d.get("Location") == ""):
            self.__location = "--";
        else:
            self.__location = d.get("Location");

        #duration
        if(d.get("Duration") == ""):
            self.__duration = "--";
        else:
            self.__duration = d.get("Duration");

    # This function defines what happens when you print the object as text i.e., print(Event)
    def __str__(self) -> str:
        """
        python has a few ways of streamlining concatenation of strings.
        each time there's a {} in the string that represents a variable.
        notice at the end of the string, ".format()"
        the variables passed into this function will replace each {} (in order)
        """
        return "Event: {}\nDate: {}\nStart time: {}\nDuration: {} hours\nLocation: {}" \
            .format(self.name, self.date, self.start_time, self.duration, self.location)

    def __eq__(self, other: 'Event') -> bool:
        return self.__name == other.name and \
            self.__uid == other.uid and \
            self.__date == other.date and \
            self.__start_time == other.start_time and \
            self.__location == other.location and \
            self.__duration == other.duration
    
    """begin getters"""
    @property
    def name(self):
        return self.__name;

    @property
    def uid(self):
        return self.__uid;

    @property
    def date(self):
        return self.__date;

    @property
    def start_time(self):
        return self.__start_time;

    @property
    def location(self):
        return self.__start_time;

    @property
    def duration(self):
        return self.__duration;
