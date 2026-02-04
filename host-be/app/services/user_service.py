users_db = {}
user_id_counter = 1


def create_user(user_data):
    global user_id_counter
    user = {
        "id": user_id_counter,
        "name": user_data.name,
        "level": user_data.level,
        "preferences": user_data.preferences
    }
    users_db[user_id_counter] = user
    user_id_counter += 1
    return user


def get_user(user_id: int):
    return users_db.get(user_id)
