class IAMFactory:
    @staticmethod
    def get_adapter(iam_solution):
        """Factory method to get the correct IAM Adapter"""
        if iam_solution == 'keycloak':
            from iam_adapters.keycloak_adapter import KeycloakAdapter
            return KeycloakAdapter()
        elif iam_solution == 'okta':
            from iam_adapters.okta_adapter import OktaAdapter
            return OktaAdapter()
        elif iam_solution == 'aws_cognito':
            from iam_adapters.aws_cognito_adapter import CognitoAdapter
            return CognitoAdapter()
        elif iam_solution == 'microsoft_entra_id':
            from iam_adapters.microsoft_entra_id_adapter import EntraIDAdapter
            return EntraIDAdapter()
        else:
            raise ValueError(f"Unsupported IAM solution: {iam_solution}")
