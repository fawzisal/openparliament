from django.conf import settings

from google.oauth2 import id_token
from google.auth.exceptions import GoogleAuthError

from parliament.accounts.models import User
from parliament.utils.views import JSONView

def google_info_from_token(token):
    idinfo = id_token.verify_token(token, settings.GOOGLE_CLIENT_ID)
    if idinfo['aud'] != settings.GOOGLE_CLIENT_ID:
        raise GoogleAuthError('aud dont match')
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise GoogleAuthError("Wrong issuer.")
    return idinfo

def get_user_from_google_token(token):
    idinfo = google_info_from_token(token)
    assert idinfo['email']
    assert idinfo['email_verified']
    user, created = User.objects.get_or_create(email=idinfo['email'].lower().strip())
    if not user.name:
        user.name = idinfo['name']
        user.save()
    return user

class GoogleLoginEndpointView(JSONView):

    def post(self, request):
        user = get_user_from_google_token(request.POST.get('token'))
        user.log_in(request)
        return {'email': user.email}
