######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *


####################### Route program ########################
def Route3(): 
	
    PortView_Battery()
    
    ### Πορέια προς χάρτη & βούρτσα ###
    MoveStraight_Distance (600,400,725,True,True,Stop.BRAKE)
    
    ### Χάρτης ###
    PointTurn_Angle (300, 300, -45, True, Stop.BRAKE)
    MoveStraight_Distance (450,300,150,True,True,Stop.BRAKE)
    rightArm.run_time(400, 700, then=Stop.BRAKE, wait=True)
    MoveStraight_Distance (300,300,-200,True,True,Stop.BRAKE)
    
    ### Πινέλο ###