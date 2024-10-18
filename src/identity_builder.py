from address_builder import AddressBuilder

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

    def add_email(self, email):
        self['email'] = email
        return self
    
    def add_is_email_verified(self, isEmailVerified=False):
        self['isEmailVerified'] = isEmailVerified
        return self
    
    def add_username(self, username):
        self['username'] = username
        return self
    
    def add_password(self, password):
        self['password'] = password
        return self
    
    def add_is_active(self, isActive=False):
        self['isActive'] = isActive
        return self
    
    def add_language(self, language):
        self['language'] = language
        return self
    
    def add_honorific(self, honorific):
        self['honorific'] = honorific
        return self
    
    def add_gender(self, gender):
        self['gender'] = gender
        return self
    
    def add_communication_channel(self, communicationChannel):
        self['communicationChannel'] = communicationChannel
        return self
    
    def add_company(self, company):
        self['company'] = company
        return self

    def add_address(self, addressType, streetNumber, complementStreetNumber, streetType, streetName, complementLocation, complementIdentification, complementAddress, postalCode, locality, region, country):
        builder = AddressBuilder()
        self['address'] = (builder.add_type(addressType).add_street_number(streetNumber).add_complement_street_number(complementStreetNumber).add_street_type(streetType).add_street_name(streetName).add_complement_location(complementLocation).add_complement_identification(complementIdentification).add_complement_address(complementAddress).add_postal_code(postalCode).add_locality(locality).add_region(region).add_country(country).build())
        return self

    def build(self):
        return self
    
# builder = IdentityBuilder()
# identity = builder.add_name("John Doe").add_email("john@example.com").add_address("123 Rue de la Paix").build()