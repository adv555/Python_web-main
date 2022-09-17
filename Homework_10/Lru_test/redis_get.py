import time

from Lru_test.redis_client import client


def set_value():
    sleep = 3.0
    value = client.set('key3', 'value3', ex=3)
    print("After set", value)
    print("Get", client.get('key3'))
    time.sleep(sleep)
    print(f'{sleep} second later', client.get('key3'))


if __name__ == '__main__':
    set_value()