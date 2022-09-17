import redis
import requests
from redis_lru import RedisLRU

CLIENT = redis.StrictRedis(host="localhost", port=6379, password=None)

cache = RedisLRU(CLIENT, default_ttl=300)


@cache
def to_get_data(link):
    print(f'Request by url:{link}')
    answer = requests.get(link)
    return answer.text


if __name__ == '__main__':
    while True:
        user_input = input('Enter url or "exit" to end:\n')
        if user_input.lower() == 'exit':
            break
        get_data = to_get_data(user_input)
