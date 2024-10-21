from enum import Enum
from core.address_builder import AddressBuilder

class Gender(Enum):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'X' 
    
class CommunicationChannel(Enum):
    EMAIL = 'E'
    SMS = 'S'
    MAIL = 'M'
    
class Honorific(Enum):
    MISTER = {
        'en': 'Mr.', 'fr': 'M.', 'es': 'Sr.', 'it': 'Sig.', 'pt': 'Sr.', 'nl': 'Dhr.'
    }
    MISSUS = {
        'en': 'Mrs.', 'fr': 'Mme', 'es': 'Sra.', 'it': 'Sig.ra', 'pt': 'Sra.', 'nl': 'Mevr.'
    }
    MISS = {
        'en': 'Miss', 'fr': 'Mlle', 'es': 'Srta.', 'it': 'Sig.na', 'pt': 'Srta.', 'nl': 'Juf.'
    }
    DOCTOR = {
        'en': 'Dr.', 'fr': 'Dr', 'es': 'Dr.', 'it': 'Dott.', 'pt': 'Dr.', 'nl': 'Dr.'
    }
    ESQUIRE = {
        'en': 'Esq.', 'fr': 'Me', 'es': 'Abg.', 'it': 'Avv.', 'pt': 'Dr.', 'nl': 'Mr.'
    }
    PROFESSOR = {
        'en': 'Prof.', 'fr': 'Pr', 'es': 'Prof.', 'it': 'Prof.', 'pt': 'Prof.', 'nl': 'Prof.'
    }
    OTHER = {
        'en': 'Mx', 'fr': 'Mx', 'es': 'Mx', 'it': 'Mx', 'pt': 'Mx', 'nl': 'Mx'
    }
    
    def get_honorific(self, lang='en'):
        """Get the honorific in the specified language (default is 'en')."""
        return self.value.get(lang, self.value['en'])

class IdentityBuilder(dict):    
    def __init__(self):
         super().__init__()

    def add_name(self, name):
        self['name'] = name
        return self
    
    def add_surname(self, surname):
        self['surname'] = surname
        return self

    def add_middlename(self, middlename):
        self['middlename'] = middlename
        return self
    
    def add_honorific(self, honorific: Honorific, lang):
        self['honorific'] = honorific.get_honorific(lang)
        return self
    
    def add_gender(self, gender: Gender):
        self['gender'] = gender.value
        return self
    
    def add_birthday(self, birthday):
        self['birthday'] = birthday
        return self
    
    def add_phone_number(self, phoneNumber):
        self['phoneNumber'] = phoneNumber
        return self

    def add_email(self, email):
        self['email'] = email
        return self
    
    def add_is_email_verified(self, isEmailVerified=False):
        if not isinstance(isEmailVerified, bool):
            isEmailVerified = 'false'    
        self['isEmailVerified'] = str(isEmailVerified).lower()
        return self
    
    def add_username(self, username):
        self['username'] = username
        return self
    
    def add_password(self, password):
        self['password'] = password
        return self
    
    def add_is_active(self, isActive=False):
        if not isinstance(isActive, bool):
            isActive = 'false'
        self['isActive'] = str(isActive).lower()
        return self
    
    def add_language(self, language):
        self['language'] = language
        return self
    
    def add_communication_channel(self, communicationChannel: CommunicationChannel):
        self['communicationChannel'] = communicationChannel.value
        return self
    
    def add_company(self, company):
        self['company'] = company
        return self

    def add_address(self, address: AddressBuilder):
        self['address'] = address
        return self

    def build(self):
        return self
    
# builder = IdentityBuilder()
# identity = builder.add_name("John Doe").add_email("john@example.com").add_address("123 Rue de la Paix").build()