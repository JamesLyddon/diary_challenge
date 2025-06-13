from lib.contact import *

"""
Given a name and number as strings
We can create a contact
"""
# contact = Contact("Pete", "570-560-7834")
# contact.name # => "Pete"
# contact.number # => "570-560-7834"

def test_initialisation():
    contact = Contact('Pete', '570-560-7834')
    assert isinstance(contact, Contact)
    assert contact.name == 'Pete'
    assert contact.number == '570-560-7834'