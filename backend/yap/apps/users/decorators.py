from functools import WRAPPER_ASSIGNMENTS, wraps

from .models import User
from .serializers import TokenSerializer


def allow_guest_mode():
    """
    View decorator that will create a guest user
    and set it's token in response header,
    if there is no user in request.

    Example:
    @guest_user()
        def view(request, ...):
            ....

    For class-based views use:
    @method_decorator(guest_user())
        def get(self, request, ...):
            ...

    Returns:
        [Reponse] : response with token in header, if guest user was created
    """

    def decorator(func):
        @wraps(func, assigned=WRAPPER_ASSIGNMENTS)
        def inner(request, *args, **kwargs):
            # If there is no user, create a guest
            if not request.user.pk:
                user = User.objects.create_guest_user()
                request.user = user

            response = func(request, *args, **kwargs)

            # If user is guest, add token to response header
            if request.user.is_guest:
                token = TokenSerializer().get_token(user)
                response["Token"] = str(token.access_token)

            return response

        return inner

    return decorator
