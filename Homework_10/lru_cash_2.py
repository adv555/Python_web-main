import json
from tabulate import tabulate
from redis_client import client
from redis_lru import RedisLRU

print(client.info())
client.flushdb()

for _key in client.scan_iter():
    print('KEY: ', _key.decode())

    _value = client.get(_key)
    print('VALUE: ', _value.decode())

cache = RedisLRU(client, default_ttl=300)


def print_data(value):
    table_data = [
        ['First name', 'Last name', 'Email', 'Phone'],
        [value['first_name'], value['last_name'], value['email'], value['phone']]
    ]
    print(tabulate(table_data, headers='firstrow', tablefmt='grid'))


class LruCache:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        key = args[0]
        if client.exists(key):
            value_json = client.get(key).decode('utf-8')
            value = json.loads(value_json)
            print_data(value)

        else:
            value = self.func(*args, **kwargs)
            value_json = json.dumps(value)
            client.set(key, value_json)
            print_data(value)


