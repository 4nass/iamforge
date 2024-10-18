class AddressBuilder(dict):
    def __init__(self):
         super().__init__()

    def add_type(self, type='home'):
        self['type'] = type
        return self

    def add_street_number(self, streetNumber):
        self['streetNumber'] = streetNumber
        return self

    def add_complement_street_number(self, complementStreetNumber):
        self['complementStreetNumber'] = complementStreetNumber
        return self
    
    def add_street_type(self, streetType):
        self['streetType'] = streetType
        return self

    def add_street_name(self, streetName):
        self['streetName'] = streetName
        return self

    def add_complement_location(self, complementLocation):
        self['complementLocation'] = complementLocation
        return self
    
    def add_complement_identification(self, complementIdentification):
        self['complementIdentification'] = complementIdentification
        return self
    
    def add_complement_address(self, complementAddress):
        self['complementAddress'] = complementAddress
        return self
    
    def add_postal_code(self, postalCode):
        self['postalCode'] = postalCode
        return self
    
    def add_locality(self, locality):
        self['locality'] = locality
        return self
    
    def add_region(self, region):
        self['region'] = region
        return self
    
    def add_country(self, country):
        self['country'] = country
        return self

    def build(self):
        return self