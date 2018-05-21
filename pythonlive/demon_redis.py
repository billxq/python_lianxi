import redis

r = redis.Redis(host='10.148.60.61',port=6379,db=1)
print(r.ping())