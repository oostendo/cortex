#!/usr/bin/python

import SimpleCV
import redis as rd

def castParam(field, data):
  return str(data)

def getDefaults():
  return { 'redis-server': "localhost",
    'redis-port': 6379,
    'redis-db': 0,
    'triggerurl': "http://localhost/frame/index" }
     

def usage():
  print "USAGE python loadFrame.py [parameters] file1 file2 ..."
  print "--redis-host=hostname - Redis server to upload to"
  print "--redis-port=#### - Redis port"
  print "--redis-db=# - Redis database"
  print "--triggerurl - URL fetch after import"
  print "--help - Show usage"

def main(argv):
  params = getDefaults()
  options = [p + "=" for p in params.keys()]
  options.append("help")
  try:
    opts, args = getopt.getopt(argv[1:], '', options)
  except getopt.GetoptError:
    usage()
    sys.exit(2)

  for o, a in opts:
    o = o[2:] #chop off leading dashes 
    if o == 'help':
      usage()
      sys.exit(0)
    params[o] = castParam(o,a)
 
  
  rd = new redis.Redis(host=params['redis-server'], port=params['redis-port'], db=params['redis-db'] );

  for img in args:
    img_file = open(img, 'r')
    rd.set(img, img_file.read)
   
  try:
    urllib.urlopen(params['triggerurl'] + "/" + args.join(","))
  except:
    print "hm, that didn't work" 



if __name__ == "__main__":
  main(sys.argv)
