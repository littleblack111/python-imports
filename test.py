from socketserver import ThreadingUnixStreamServer
from stdlib import *

# TODO: try to make user no need to press any key to continue when doing input(test)
# TODO: finish this up

def tests():
    # print class 'ascii'
    print(ascii)
    print(dir(ascii))
    # print subclasses
    print(ascii.color)
    print(ascii.cursor)
    
    print(i2str([1,2,"as"]))
    
    # test color convertion
    print(rgb2hex(128, 128, 128))
    print(rgb2ascii(128, 128, 128))
    print(hex2rgb("#FF0000"))
    print(hex2ascii("#FF0000"))
    print(ascii2hex(20))
    print(ascii2rgb(20))

    printf("Hello from printf")

    testlist = [1,2,3,4,5,6,7,8,9,10]
    testlist2 = [10,20,30,40,50,60,70,80,90,100]
    print(f"testlist: {testlist}, testlist2: {testlist2}, shufflejoin: {shufflejoinlst(testlist, testlist2)}")
    del testlist, testlist2

    teststr = "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
    print(f"ori string: {teststr}, limitstring(10 char): {limitstring(teststr, 10)}")
    del teststr

    aprintf("Hello from aprintf")

    printinfo("Hello from printinfo")

    printwarning("Hello from printwarning")

    printerror("Hello from printerror")

    ainputf("Hello from ainputf (press any key to continue)")

    askinput("Hello from askinput (press any key to continue)")

    print("countdown for 3 seconds")
    countdown(3)

    #aloading("hello from aloding")

    # TODO: make aloading() in threading

    bgexec(print, "hello from bgexec")

    # def testhandler():
    #     print("Hello from testhandler")
    #     exit(100) # for testing purposes
    # import signal
    # sigcatch(sig="SIGINT", error="catched kill signal", handler=testhandler)
    # del testhandler, signal

    # TODO: fix this "TypeError: Please input @sig as a int(signal number, like 15) or str(signal name, like SIGTERM", tried signal.SIGINT, or str(signal name, like SIGTERM)

if __name__ == "__main__":
    tests()
else:
    print("Tests from test.py")