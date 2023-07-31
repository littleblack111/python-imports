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

def printf(str):
    print(str, end='', flush=True)

def shufflejoin(str1: str, str2: str, str3=None, str4=None, str5=None):
    from random import shuffle
    if str3:
        if str4:
            if str5:
                 tmpstr = str1 + str2 + str3 + str4 + str5
            else:
                tmpstr = str1 + str2 + str3 + str4
        else:
            tmpstr = str1 + str2 + str3
    else:
        tmpstr = str1 + str2

    tmpstrlst = list(tmpstr)
    shuffle(tmpstrlst)
    return ''.join(tmpstrlst)

def limitString(string: str, limit: int):
    if len(string) > limit:
        return string[0:limit]
    else:
        return string

def aprintf(str, end=None):
    from time import sleep
    waitime = 0.01
    str = list(str)
    for i in str:
        printf(i)
        sleep(waitime)
    if end == None:
        printf('\n')
    else:
        printf(end)

def countdown(timeoutsec: int): # animated count down 3 seconds
    from time import sleep
    timeoutsec = timeoutsec
    for _ in range(timeoutsec-1):
        printf(timeoutsec)
        for _ in range(timeoutsec):
            printf('.')
            sleep(0.8/3)
        timeoutsec -= 1
        sleep(0.2)
    print(1)
