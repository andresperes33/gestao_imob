from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('username')

        if not username or not password:
            return None

        UserModel = get_user_model()

        user = (
            UserModel.objects.filter(email=username).first()
            or UserModel.objects.filter(username=username).first()
        )

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None
