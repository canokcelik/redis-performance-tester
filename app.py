import redis
import random
import string
import os

REDIS_HOST=os.environ['REDIS_HOST']
REDIS_PASSWORD=os.environ['REDIS_PASSWORD']

r=redis.Redis(host=REDIS_HOST,password=REDIS_PASSWORD,port=6379,db=0)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_int():
    c=random.randint(100,1000)
    return int(c)

n=0

while n<10000:
    key = get_random_string(get_random_int())
    value = get_random_string(get_random_int())
    r.set(key,value)
    #print(key," - ",value)
    n+=1
