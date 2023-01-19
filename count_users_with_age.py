def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    count = 0
    for ages in data:
        if ages['age'] == age:
            count += 1
    return count

# data = [
#   {
#     'name': 'John', 
#     'age': 35
#   },
#   {
#     'name':'Mary', 
#     'age': 20
#   }
#   ]

# age = 38

# print(count_users_with_age(data, age))