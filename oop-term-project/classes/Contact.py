import json


class Contact:

    #constructor to pull data in from json dictionary
    def __init__(self, d: dict):
        #there is most definitely a cleaner way to implement this, but i'm unsure the level of creative freedom we're allowed

        #UID
        if(d.get("UID") == ""):
            self.__uid == "-1"
        else:
            self.__uid = d.get("UID");
        
        #firstname
        if(d.get("FirstName") == ""):
            self.__firstname = "--"
        else:
            self.__firstname = d.get("FirstName");

        #lastname
        if(d.get("LastName") == ""):
            self.__lastname = "--"
        else:
            self.__lastname = d.get("LastName");

        #email
        if(d.get("EmailAddress") == ""):
            self.__lastname = "--"
        else:
            self.__email = d.get("EmailAddress");

        #department
        if(d.get("Dept") == ""):
            self.__lastname = "--"
        else:
            self.__department = d.get("Dept");
        
        #title
        if(d.get("Title") == ""):
            self.__lastname = "--"
        else:
            self.__title = d.get("Title");
        
        #phone
        if(d.get("Phone") == ""):
            self.__lastname = "--"
        else:
            self.__phone = d.get("Phone");
        
        #building
        if(d.get("Building") == ""):
            self.__lastname = "--"
        else:
            self.__building = d.get("Building");
        
        #mail_code
        if(d.get("POBox") == ""):
            self.__lastname = "--"
        else:
            self.__mail_code = d.get("POBox");

        #last_contact
        self.__last_contact = "";

    def __str__(self) -> str:
        """
        Dunder method that defines what happens when you print a Contact object.
        :return: String defining the object
        """
        return f"{self.__firstname} {self.__lastname}\nTitle: {self.__title}\nEmail: {self.__email}\nDepartment: " \
               f"{self.__department}\nPhone: {self.__phone}\nBuilding: {self.__building}\nLDC: {self.__last_contact}"

    def __eq__(self, other: 'Contact') -> bool:  # Using quotes around the type allows for typing of this class here
        """
        Dunder method that defines whether two Contact objects are equal based on their attributes.
        :param other: Another contact object.
        :return: Equality evaluation.
        """
        return self.__uid == other.uid and \
            self.__firstname == other.firstname and \
            self.__lastname == other.lastname and \
            self.__email == other.email and \
            self.__department == other.department and \
            self.__title == other.title and \
            self.__phone == other.phone and \
            self.__building == other.building and \
            self.__mail_code == other.mail_code and \
            self.__last_contact == other.last_contact
    
    """begin getters"""
    @property
    def uid(self):
        return self.__uid;
    
    @property
    def firstname(self):
        return self.__firstname;

    @property
    def lastname(self):
        return self.__last_name;
    
    @property
    def email(self):
        return self.__email;

    @property
    def department(self):
        return self.__department;
    
    @property
    def title(self):
        return self.__title;
    
    @property
    def phone(self):
        return self.__phone;
    
    @property
    def building(self):
        return self.__building;
    
    @property
    def mail_code(self):
        return self.__mail_code;
    
    @property
    def last_contact(self):
        return self.__last_contact;

    """setter for last_contact var"""
    @property
    def last_contact(self, last_contact:str):
        self.__last_contact = last_contact;