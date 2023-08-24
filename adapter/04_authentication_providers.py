class GoogleAuth:
    def google_login(self, user_email):
        return f"Google authentication for {user_email}"

class FacebookAuth:
    def facebook_sign_in(self, user_id):
        return f"Facebook sign-in for user ID {user_id}"

class TwitterAuth:
    def twitter_authenticate(self, username):
        return f"Twitter authentication for {username}"

class AuthAdapter:
    def __init__(self, auth_provider):
        self.auth_provider = auth_provider

    def authenticate_user(self, user_identifier):
        if isinstance(self.auth_provider, GoogleAuth):
            return self.auth_provider.google_login(user_identifier)
        elif isinstance(self.auth_provider, FacebookAuth):
            return self.auth_provider.facebook_sign_in(user_identifier)
        elif isinstance(self.auth_provider, TwitterAuth):
            return self.auth_provider.twitter_authenticate(user_identifier)


if __name__ == "__main__":
    # Usage
    google_auth = GoogleAuth()
    facebook_auth = FacebookAuth()
    twitter_auth = TwitterAuth()

    google_adapter = AuthAdapter(google_auth)
    facebook_adapter = AuthAdapter(facebook_auth)
    twitter_adapter = AuthAdapter(twitter_auth)

    print(google_adapter.authenticate_user("alice@gmail.com"))    # Output: Google authentication for alice@gmail.com
    print(facebook_adapter.authenticate_user("123456789"))      # Output: Facebook sign-in for user ID 123456789
    print(twitter_adapter.authenticate_user("user123"))         # Output: Twitter authentication for user123
