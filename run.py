import time, sys

from danmu import DanMuClient


def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

if len(sys.argv) != 3:
    print "arguments invalid!"
    exit(1)

danmu_plat = {
    'douyu': 'https://www.douyu.com/',
    'panda': 'http://www.panda.tv/'
}

plat_url = danmu_plat[sys.argv[1]]+str(sys.argv[2])
print 'live url:',plat_url

dmc = DanMuClient(plat_url)
if not dmc.isValid():
    print('Url not valid')
    exit(1)

@dmc.danmu
def danmu_fn(msg):
    pp('[%s] %s' % (msg['NickName'], msg['Content']))

@dmc.gift
def gift_fn(msg):
    pp('[%s] sent a gift!' % msg['NickName'])

@dmc.other
def other_fn(msg):
    pp('Other message received')

dmc.start(blockThread=True)
