# text color code
class color:
    ### ASCII
    #\33[0m   # remove all attribute
    #\33[1m   # control brightness
    #\33[4m   # underline
    #\33[5m   # blink
    #\33[7m   # reverse
    #\33[8m   # disappear
    #\33[30m -- \33[37m   # foreground
    #\33[40m -- \33[47m   # background
    #\33[nA   # upper cursor n line
    #\33[nB   # lower cursor n line
    #\33[nC   # righter cursor n line
    #\33[nD   # lefter cursor n line
    #\33[y;xH # set cursor x/y
    #\33[2J   # clear screen
    #\33[K    # clear from cursor to end
    #\33[s    # save cursor pos
    #\33[u    # recover saved cursor pos
    #\33[?25l # hide cursor
    #\33[?25h # show cursor
    #\033[1m  # bold
    #\033[0m  # un-bold
    #\033[0m  # reset \033[2m 

    reset = "\33[0m"

    black = "\033[30m" # black
    red = "\033[31m" # red
    green = "\033[32m" # green
    yellow = "\033[33m" # yellow
    blue = "\033[34m" # blue
    purple = "\033[35m" # purple
    cyan = "\033[36m" # cyan
    gray = "\033[37m" # gray

    lblack = "\033[1;30m" # light-black
    lred = "\033[1;31m" # light-red
    lgreen = "\033[1;32m" # light-green
    lyellow = "\033[1;33m" # light-yellow
    lblue = "\033[1;34m" # light-blue
    lpurple = "\033[1;35m" # light-purple
    lcyan = "\033[1;36m" # light-cyan
    white = "\033[1;37m" # white

# convert iterable into string
def istr(value):
    return str(''.join(map(str, value)))

# print but formatly without newline and will flush stream
def printf(*value: str):
    print(str(istr(value)), end='', flush=True)

# mixly(shuffle) join a list to another
def shufflejoin(str1: str, str2: str, *others):
    from random import shuffle
    tmpstr = str1 + str2
    if others:
        for o in others:
            tmpstr += o

    tmpstrlst = list(tmpstr)
    shuffle(tmpstrlst)
    return ''.join(tmpstrlst)

# limit string to how much charactor it can use, and delete other then that
def limitString(string: str, limit: int):
    if len(string) > limit:
        return string[0:limit]
    else:
        return string

# animated print
def aprintf(*value: str, end=None):
    from time import sleep
    waitime = 0.01
    value = istr(list(value))
    ani=True
    if len(value) >= 8*16:
        ani = ainputf("Print string is bigger, fast animation(Y/n: ")
        if ani.lower() == 'y':
            ani=False
    for i in value:
        printf(i)
        if ani:
            sleep(waitime)
    if end == None:
        printf('\n')
    else:
        printf(end)

def printinfo(str: str, outputter=aprintf, ccolor=color.green, selection=False):
    if selection:
        outputter(f"{ccolor}[+] {str}{color.reset}")
    else:
        outputter(f"{ccolor}[*] {str}{color.reset}")

def printwarning(str: str, outputter=aprintf, ccolor=color.yellow):
    outputter(f"{ccolor}[!] {str}{color.reset}")

def printerror(str: str, outputter=aprintf, ccolor=color.red):
    outputter(f"{ccolor}[#] {str}{color.reset}")

def ainputf(str: str, end='', ccolor=color.purple):
    aprintf(f"{ccolor}{str}", f"{end}{color.reset}", end=end)
    return input()

def askinput(str: str, inputter=ainputf, ccolor=color.blue):
    inputter(f"{ccolor}[?] {str}{color.reset}")

# animated countdown from @timeoutsec
def countdown(timeoutsec: int):
    from time import sleep
    timeoutsec = timeoutsec
    for _ in range(timeoutsec-1):
        printf(timeoutsec)
        for _ in range(3):
            printf('.')
            sleep(0.8/3)
        timeoutsec -= 1
        sleep(0.2)
    print(1)

# animated loading with @msg
def aloading(msg="Loading...", stop=False):
    from itertools import cycle
    from time import sleep
    for c in cycle(['|', '/', '-', '\\']):
        if stop:
            break
        printf(f"\r[{c}] {msg}")
        sleep(0.1)

# automated execute @func in background with @arg
def bgexec(func, arg=False, stop=False):
    from threading import Thread
    if stop:
        try:
            t.join()
        except AttributeError:
            raise AttributeError("Thread is not started")
        except UnboundLocalError:
            raise UnboundLocalError("Thread is not started")
    else:
        if arg:
            t = Thread(target=func, args=arg).start()
        else:
            t = Thread(target=func).start()
