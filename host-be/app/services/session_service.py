sessions_db = {}
session_id_counter = 1


def create_session(user_id: int):
    global session_id_counter
    session = {
        "session_id": session_id_counter,
        "user_id": user_id
    }
    sessions_db[session_id_counter] = session
    session_id_counter += 1
    return session
