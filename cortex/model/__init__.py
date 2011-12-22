import redis
import json

import cv 
import SimpleCV as scv
import numpy as np
import re

#connect to redis
def init_model(config):
  (redis_host, redis_port, redis_db) = re.match("redis://(\w+):(\d+)/(\d)", config['redis.url']).groups()
  return redis.Redis(host=redis_host, port=int(redis_port), db=int(redis_db))
  

