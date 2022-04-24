from flaskeddit.models import AppUser


def get_user(username):
    """
    Gets a user by name from the database.
    """
    return AppUser.query.filter_by(username=username).first()
