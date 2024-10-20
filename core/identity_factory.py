import random
from faker import Faker
from unidecode import unidecode
from core.address_factory import AddressFactory
from core.identity_builder import IdentityBuilder

class IdentityFactory:
    @staticmethod
    def create_identity(locale="fr_FR"):
        """Factory method to create identity based on locale"""
        if locale == 'fr_FR':
            return FrenchIdentity()
        elif locale == 'es_ES':
            return SpanishIdentity()
        elif locale == 'it_IT':
            return ItalianIdentity()
        elif locale == 'pt_PT':
            return PortugueseIdentity()
        elif locale == 'nl_NL':
            return DutchIdentity()
        elif locale == 'en_GB':
            return BritishIdentity()
        elif locale == 'en_US':
            return AmericanIdentity()
        else:
            return DefaultIdentity()

class FrenchIdentity:
    def generate(self, unique_usernames=None):
        # Generate French identity data
        while True:
            locale = 'fr_FR'
            builder = IdentityBuilder()
            fake = Faker([locale])
            gender = random.choice(['M', 'F'])
            if gender == 'M':
                surname = fake.first_name_male()
                middlename = fake.first_name_male() if random.random() > 0.6 else '' # 40% chance of having a middlename
                honorific = 'M'
            else:
                surname = fake.first_name_female()
                middlename = fake.first_name_female() if random.random() > 0.6 else '' # 40% chance of having a middlename
                honorific = 'Mme'
            name = fake.last_name().lower()
            username = f"{unidecode(name.lower()).replace(' ', '-')}.{unidecode(surname.lower()).replace(' ', '-')}{random.randint(1000, 9999)}"
            # Ensure the username is unique using manager.dict() as a set
            if username not in unique_usernames:
                unique_usernames[username] = None  # Add username to the set
                break
        email = f"{username}@yopmail.com"
        address = AddressFactory.create_address(locale)
        identity = (builder.add_surname(surname)
                    .add_middlename(middlename)
                    .add_name(name)
                    .add_honorific(honorific)
                    .add_gender(gender)
                    .add_username(username)
                    .add_email(email)
                    .add_communication_channel('E')
                    .add_is_active('true')
                    .add_is_email_verified('true')
                    .add_language('fr')
                    .add_address(address.generate()))
        
        return identity

class SpanishIdentity:
    def generate(self):
        # Generate identity data
        pass

class ItalianIdentity:
    def generate(self):
        # Generate identity data
        pass

class SpanishIdentity:
    def generate(self):
        # Generate identity data
        pass

class PortugueseIdentity:
    def generate(self):
        # Generate identity data
        pass

class DutchIdentity:
    def generate(self):
        # Generate identity data
        pass

class BritishIdentity:
    def generate(self):
        # Generate identity data
        pass

class AmericanIdentity:
    def generate(self):
        # Generate identity data
        pass

class DefaultIdentity:
    def generate(self):
        # Generate identity data
        pass

# identity = IdentityFactory.create_identity('fr_FR')
# identity.generate()