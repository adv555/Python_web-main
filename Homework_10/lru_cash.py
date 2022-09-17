import functools
import json
import redis
from redis_lru import RedisLRU
from tabulate import tabulate

client = redis.Redis(
    host='localhost',
    port=6379,
    db=3
)
cache = RedisLRU(client)

print(client.client_info())
# client.flushdb()

for _key in client.scan_iter():
    print('KEY: ', _key.decode())

    _value = client.get(_key)
    print('VALUE: ', _value.decode())


class LruCache:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        key = args[0]
        if client.exists(key):
            value_json = client.get(key).decode('utf-8')
            value = json.loads(value_json)
            table_data = [
                ['First name', 'Last name', 'Email', 'Phone'],
                [value['first_name'], value['last_name'], value['email'], value['phone']]
            ]
            print(tabulate(table_data, headers='firstrow', tablefmt='grid'))
        else:
            value = self.func(*args, **kwargs)
            value_json = json.dumps(value)
            client.set(key, value_json)
            table_data = [
                ['First name', 'Last name', 'Email', 'Phone'],
                [value['first_name'], value['last_name'], value['email'], value['phone']]
            ]
            print(tabulate(table_data, headers='firstrow', tablefmt='grid'))


