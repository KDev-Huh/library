from . import redis_client

def save_borrowed_book(borrower: str, title: str):
    try:
        print(redis_client.ping())  # True 나오면 OK
        key = f"borrower:{borrower}:books"
        print(key)
        redis_client.sadd(key, title)
        return True
    except Exception as e:
        print(e)
        return False


def return_book(borrower, title):
    redis_key = f"borrower:{borrower}:books"
    redis_client.srem(redis_key, title)
    return True