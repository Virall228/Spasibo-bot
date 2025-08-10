# Простая in-memory блокировка пользователей
blocked_users = set()

def is_blocked(user_id: int) -> bool:
    return user_id in blocked_users

def block_user(user_id: int):
    blocked_users.add(user_id)

def unblock_user(user_id: int):
    blocked_users.discard(user_id)