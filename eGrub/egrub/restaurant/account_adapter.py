from allauth.account.adapter import DefaultAccountAdapter

# Disable alluth 'Signup', see ACCOUNT_ADAPTER in settings.py
class NoNewUsers(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False    