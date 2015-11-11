from django.utils.crypto import get_random_string


def generate_local_settings(file_path):
    """Generate local_settings file

    Args:
        file_path (str): Path to local_settings.py
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, chars)

    settings = (
        'SECRET_KEY = "{0}"'.format(secret_key),
    )

    with open(file_path, 'w+') as local_settings:
        local_settings.write('\n'.join(settings) + '\n')
