 ######################## Pybricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *
from Route1 import *
from Route2 import *
from Route3 import *
from Route4 import *
# from Route5 import *
# from Route6 import *
# from Route7 import *
# from Route8 import *
# from Route9 import *
# from Route10 import *
######################## Total route ########################

CURRENT_ROUTE = 1
MAX_ROUTE = 4 # modify accordingly

######################## Main program ########################

while True:
    Hub_DisplayNum(CURRENT_ROUTE)

    if Button.LEFT in hub.buttons.pressed():
        if CURRENT_ROUTE > 1:
            CURRENT_ROUTE -= 1
        wait(200)

    elif Button.RIGHT in hub.buttons.pressed():
        if CURRENT_ROUTE < MAX_ROUTE:
            CURRENT_ROUTE += 1
        wait(200)

    elif Button.CENTER in hub.buttons.pressed():
        # add your route here
        if CURRENT_ROUTE == 1:
            Route1()
        elif CURRENT_ROUTE == 2:
            Route2()
        elif CURRENT_ROUTE == 3:
            Route3()
        elif CURRENT_ROUTE == 4:
            Route4()
        # elif CURRENT_ROUTE == 5:
        #     Route5()    
        # elif CURRENT_ROUTE == 6:
        #     Route6()  
        # elif CURRENT_ROUTE == 7:
        #     Route7()    
        # elif CURRENT_ROUTE == 8:
        #     Route8() 
        # elif CURRENT_ROUTE == 9:
        #     Route9() 
        # elif CURRENT_ROUTE == 10:
        #     Route10() 
        
        # auto-run next route
        if CURRENT_ROUTE < MAX_ROUTE:
            CURRENT_ROUTE += 1
            







