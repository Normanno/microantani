from microbit import *

# vincenzonorman@gmail.com
while true :
	compass.calibrate()
	while compass.is_calibrate() is False
		compass.calibrate()
	heading = compass.heading()
	if(heading > 315 and  heading < 45)
		display.scroll("nord");
	else if(heading > 45 and  heading < 135)
	    display.scroll("est");
	if(heading > 135 and  heading < 225)
	   display.scroll("sud");
	else
	   display.scroll("ovest")
