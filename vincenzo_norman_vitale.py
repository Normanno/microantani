from microbit import *

# vincenzonorman@gmail.com
while true :
    microbit.compass.calibrate()
    while microbit.compass.is_calibrate() is False
        microbit.compass.calibrate()
    heading = microbit.compass.heading()
    if(heading > 315 and  heading <= 45)
        microbit.display.scroll("nord");
    else if(heading > 45 and  heading <= 135)
        microbit.display.scroll("est");
    if(heading > 135 and  heading <= 225)
       microbit.display.scroll("sud");
    else if (heading > 225 and  heading <= 315)
       microbit.display.scroll("ovest")
