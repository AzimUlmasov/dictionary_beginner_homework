def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    max_age = -1
    max_age_user_name = ''
    for user in data:
        if user["age"] > max_age:
            max_age = user["age"]
            max_age_user_name = user["name"]
    return max_age_user_name

