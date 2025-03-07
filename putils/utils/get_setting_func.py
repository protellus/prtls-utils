from django.conf import settings

def get_setting(setting_name, default_value=None):
    """
    Retrieves a setting from the Django settings, with an option to provide a default value
    if the setting is not found.

    :param setting_name: The name of the setting to retrieve.
    :param default_value: The value to return if the setting is not found.
    :return: The value of the setting, or the default value if the setting is not found.
    """
    return getattr(settings, setting_name, default_value)
