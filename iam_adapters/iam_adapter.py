class IAMAdapter:
    def __init__(self, config):
        self.config = config

    def connect(self):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def create_user(self, identity):
        raise NotImplementedError("This method should be implemented by subclasses")

    def assign_roles(self, identity, roles):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def assign_groups(self, identity, groups):
        raise NotImplementedError("This method should be implemented by subclasses")

    def deactivate_user(self, identity):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def get_user_id(self, username):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def get_user(self, userID):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def update_user(self, userID, payload):
        raise NotImplementedError("This method should be implemented by subclasses")

    def delete_user(self, identity):
        raise NotImplementedError("This method should be implemented by subclasses")
    