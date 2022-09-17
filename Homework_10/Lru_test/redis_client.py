import redis

client = redis.Redis(host='localhost', port=6379, db=2)


if __name__ == '__main__':
    # client.set('foo', 'bar')
    # client.set('key', 'value')
    client.set('key2', 'value2')
    print(client.get('key2'))
