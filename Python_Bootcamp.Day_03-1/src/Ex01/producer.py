import redis
import random

r = redis.Redis(
    host="127.0.0.1",
    port=8000,
    decode_responses=True
)

counter = 0
while counter < 5:
    json_message = '{{"metadata": {{"from": {},"to": {}}},"amount": {}}}' \
            .format(
                random.randrange(1000000000, 9999999999),
                random.randrange(1000000000, 9999999999),
                random.randrange(-10000, 99999))
    r.publish('channel_1', json_message)
    counter += 1
r.publish("channel_1", '{"metadata": {"from": 1111111111,"to": \
           2222222222},"amount": 100}')
