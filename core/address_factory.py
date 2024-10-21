
import random
from faker import Faker
from core.address_builder import AddressBuilder, AddressType

class AddressFactory:
    @staticmethod
    def create_address(locale="fr_FR"):
        """Factory method to create address based on locale"""
        if locale == 'fr_FR':
            return FrenchAddress()
        elif locale == 'es_ES':
            return SpanishAddress()
        elif locale == 'it_IT':
            return ItalianAddress()
        elif locale == 'pt_PT':
            return PortugueseAddress()
        elif locale == 'nl_NL':
            return DutchAddress()
        elif locale == 'en_GB':
            return BritishAddress()
        elif locale == 'en_US':
            return AmericanAddress()
        else:
            return DefaultAddress()

class FrenchAddress:
    def generate(self):
        builder = AddressBuilder()
        fake = Faker(['fr_FR'])
        address = (builder.add_type(random.choice(list(AddressType)))
                   .add_street_number(fake.building_number())
                   .add_complement_street_number(random.choice(['bis', 'ter', 'quater']) if random.random() > 0.8 else '')
                   .add_street_type(random.choice(['boulevard', 'avenue', 'rue', 'place', 'chemin']))
                   .add_street_name(fake.street_name().split(' ', 1)[1])
                   .add_complement_location('Batiment 1')
                   .add_complement_identification('')
                   .add_complement_address('BP 12345')
                   .add_postal_code(fake.postcode())
                   .add_locality(fake.city())
                   .add_region(fake.region())
                   .add_country('France'))
        return address

class SpanishAddress:
    def generate(self):
        # Generate Address data
        pass

class ItalianAddress:
    def generate(self):
        # Generate Address data
        pass

class SpanishAddress:
    def generate(self):
        # Generate Address data
        pass

class PortugueseAddress:
    def generate(self):
        # Generate Address data
        pass

class DutchAddress:
    def generate(self):
        # Generate Address data
        pass

class BritishAddress:
    def generate(self):
        # Generate Address data
        pass

class AmericanAddress:
    def generate(self):
        # Generate Address data
        pass

class DefaultAddress:
    def generate(self):
        # Generate Address data
        pass

# Address = AddressFactory.create_Address('fr_FR')
# Address.generate()