# Index

- [x] Display Contacts Menu
    - [x] Importing Data
    - [x] Last Date of Contact
- [x] Create Contact Menu
- [x] Create Event Menu
- [ ] Display Events Menu
    - [ ] Add Attendee
    - [ ] Current Attendees
        - [x] Memo
    - [ ] Add a SECOND attendee

## Things changed:
- Contact.py
    - Changed `@property` to `@last_contact.setter` for `last_contact`'s setter
- Event.py
- EventAttendee.py
    - Lines 18, 38-39, 50-52: Changed `event_object` to `event`
    - Lines 17, 34-35, 46-48: Changed `contact_object` to `contact`
- EventManager.py
    - Line 110: Changed `c.UID` to `c.uid` because the getter for `Contact` UIDs is lowercase, not caps. Might need to change<br> line 103 as well, because it does the same thing for but for the `Event` class
    - Line 103: Changed `e.UID` to `e.uid` because the getter for `Event` UIDs is lowercase, not caps.
    - Line 90: Changed `contact_object` to `contact` and `event_object` to `event`
- SearchContacts.py