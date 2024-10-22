from iam_adapters.iam_adapter import IAMAdapter

class EntraIDAdapter(IAMAdapter):
    def format_identity(self, identity):
        """Format an identity object for AWS Cognito"""
        aws_identity = {
            "Username": identity["username"],
            "UserAttributes": [
                {"Name": "email", "Value": identity["email"]},
                {"Name": "given_name", "Value": identity["name"]},
                {"Name": "family_name", "Value": identity["surname"]},
            ],
            # Add AWS Cognito-specific attributes
        }
        return aws_identity

    def create_cognito_user(self, identity, user_pool_id):
        """Simulate the creation of an AWS Cognito user"""
        formatted_identity = self.format_identity(identity)
        # Call the AWS Cognito API or simulate creation
        print(f"Creating user in pool {user_pool_id}: {formatted_identity}")
