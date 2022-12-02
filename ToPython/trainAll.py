from threading import Thread

def start():
    if i == 0:
        import BlotzBig;
    elif i == 1:
        import BoltzConv;
    elif i == 2:
        import BoltzSmall
    elif i == 3:
        import BoltzTiny
    elif i == 4:
        import GreedyBig
    elif i == 5:
        import GreedyConv;
    elif i == 6:
        import GreedySmall;
    elif i == 7:
        import GreedyTiny;

for x in range(0,8):
    i = x
    th = Thread(target=start)
    th.start()