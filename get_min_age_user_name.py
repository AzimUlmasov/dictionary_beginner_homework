def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """

    min_age = []
    i = 99
    for age in data:
        if i > age["age"]:
            i = age["age"]
            min_age = age
    return min_age["name"]