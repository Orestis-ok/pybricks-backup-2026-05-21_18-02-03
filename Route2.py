######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route2(): 

    PortView_Battery()
    
    ### Πορέια προς βόρειο τοίχο μπορστά από χάρτη ###
    MoveSteering_Seconds(300, -50, 100)
    MoveStraight_Distance (600,600,800,True,True,Stop.BRAKE)
    PointTurn_Angle (300, 300, 180, True, Stop.BRAKE)
    MoveStraight_Distance (600,600,-300,True,True,Stop.BRAKE)
    MoveStraight_Distance (600,600,60,True,True,Stop.BRAKE)
    PointTurn_Angle (500, 400, -105, True, Stop.BRAKE)
    
    ### Προσεκτική & τρενάκι ###
    MoveStraight_Distance (400,300,100,True,True,Stop.BRAKE)
    leftArm.run_time(-800,1000, then=Stop.BRAKE, wait=False)
    rightArm.run_time(500, 1000, then=Stop.BRAKE, wait=True)
    
	### Επιστροφή στην βάση ###
    MoveStraight_Distance (250,200,-100,True,True,Stop.BRAKE)
    PointTurn_Angle (300, 300, 100, True, Stop.BRAKE)
    MoveStraight_Distance (800,600,800,True,True,Stop.BRAKE)

