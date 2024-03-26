import redis
import logging
import json
import argparse


def pars_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("-e",
                        action="store_true",
                        help="Set flag e")
    parser.add_argument("list", type=str,
                        help="Set numbers to change")
    args = parser.parse_args()
    if args.e:
        return args.list
    else:
        print("Set flag -e and give numbers to change")


def change_numbers_if_need(message: dict[str, any], numbers: str):
    json_s = json.loads(message["data"])
    numbers = numbers.split(",")
    if json_s["amount"] > 0 and str(json_s["metadata"]["to"]) in numbers:
        json_s["metadata"]["from"], json_s["metadata"]["to"] = \
            json_s["metadata"]["to"], json_s["metadata"]["from"]
    return json_s


def redis_listen(numbers):
    r = redis.Redis(
        host="127.0.0.1",
        port=8000,
        decode_responses=True
    )

    p = r.pubsub()
    p.subscribe("channel_1")
    while True:
        message = p.get_message()
        if message and type(message["data"]) is str:
            logging.warning(change_numbers_if_need(message, numbers))


if __name__ == "__main__":
    redis_listen(pars_args())
