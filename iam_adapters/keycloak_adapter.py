from iam_adapters.iam_adapter import IAMAdapter
from mantelo import KeycloakAdmin

class KeycloakAdapter(IAMAdapter):
    def format_identity(self, identity):
        """Format an identity object for Keycloak"""
        keycloak_identity = {
            "firstName": identity["name"],
            "lastName": identity["surname"],
            "username": identity["username"],
            "enabled": identity["isActive"],
            "email": identity["email"],
            "credentials": [{"value": identity["password"],"type": "password",}],
            "attributes": {
                "locale": [identity["language"]],
                # Add more Keycloak-specific attributes
            }
        }
        return keycloak_identity
    
    def connect(self):
        from mantelo import KeycloakAdmin
        keycloak_config = self.config["keycloak"]
        self.admin = KeycloakAdmin.from_username_password(
            server_url=keycloak_config['admin_url'],
            username=keycloak_config['username'],
            password=keycloak_config['password'],
            realm_name=keycloak_config['realm'],
            client_id=keycloak_config['client_id'],
            client_secret_key=keycloak_config['client_secret']
        )

    def create_keycloak_user(self, identity, realm):
        formatted_identity = self.format_identity(identity)
        # Call the Keycloak API or simulate creation (e.g., REST API or Keycloak Admin API)
        print(f"Creating user in realm {realm}: {formatted_identity}")
        
    def assign_roles(self, identity, roles):
        print(f"Assigning roles {roles} to: {identity}")
        pass
    
    def assign_groups(self, identity, groups):
        print(f"Assigning roles {groups} to: {identity}")
        pass

    def deactivate_user(self, identity):
        pass
    
    def get_user_id(self, username):
        pass
    
    def get_user(self, userID):
        pass
    
    def update_user(self, userID, payload):
        pass

    def delete_user(self, userID):
        pass
