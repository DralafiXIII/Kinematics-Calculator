# Name: Sean Settgast
# Project for Programming with Python
# Project Title: Kinematic Calculator

import math
from decimal import Decimal, getcontext
getcontext().prec = 10 # <-- This is the number of decimal places it will round up from

def num_check(statement):
    while True:
        number = input(statement + "\n\n(enter 'quit' at any time to exit the program)\n>> ")
        try:
            number = number.lower()
        except:
            pass
        if number == 'quit' or number == 'q':
            quit()
        try:
            number = float(number)
        except:
            print('**THE VALUE ENTERED IS NOT VALID. PLEASE TRY AGAIN.**\n')
            continue
        if number != 1 and number != 2:
            print('**THE VALUE ENTERED IS NOT VALID. PLEASE TRY AGAIN.**\n')
            continue
        print()
        return number
    
def num_check2(statement):
    while True:
        number = input(statement + "\n(if you don't have this value or this is a/the value you're looking for,\nleave this blank and hit 'ENTER')\n>> ")
        try:
            number = number.lower()
        except:
            pass
        if number == 'quit' or number == 'q':
            quit()
        try:
            number = float(number)
        except:
            if number == '':
                pass
            else:
                print('**THE VALUE ENTERED IS NOT VALID. PLEASE TRY AGAIN.**\n')
                continue
        print()
        return number

def num_check3(statement):
    while True:
        number = input(statement + "\n(if you don't have this value or this is a/the value you're looking for,\nleave this blank and hit 'ENTER')\n>> ")
        try:
            number = number.lower()
        except:
            pass
        if number == 'quit' or number == 'q':
            quit()
        try:
            if number.find(',') == -1 and number.find(':') != -1: 
                times = number.split(sep=':')
                if len(times) == 2:
                    number = int(times[0])*60+float(times[1])
                elif len(times) == 3:
                    number = int(times[0])*3600+int(times[1])*60+float(times[2])
                elif len(times) == 4:
                    number = int(times[0])*86400+int(times[1])*3600+int(times[2])*60+float(times[3])
            elif number.find(',') != -1:
                if number.find(':') == -1:
                    times = number.split(sep=',')
                    number = int(times[0])+float(times[1])/1000
                elif number.find(':') != -1:
                    times = number.split(sep=':')
                    times2 = times[len(times) - 1].split(sep=',')
                    del(times[len(times) - 1])
                    times = times + times2
                    if len(times) == 3:
                        number = int(times[0])*60+int(times[1])+float(times[2])/1000
                    elif len(times) == 4:
                        number = int(times[0])*3600+int(times[1])*60+int(times[2])+float(times[3])/1000
                    elif len(times) == 5:
                        number = int(times[0])*86400+int(times[1])*3600+int(times[2])*60+int(times[3])+float(times[4])/1000
            else:
                number = float(number)
        except:
            if number == '':
                pass
            else:
                print('**THE VALUE ENTERED IS NOT VALID. PLEASE TRY AGAIN.**\n')
                continue
        print()
        return number

def num_check4(statement):
    while True:
        number = input(statement + "\n\n>> ")
        try:
            number = number.lower()
        except:
            pass
        if number == 'quit' or number == 'q':
            quit()
        try:
            number = float(number)
        except:
            print('**THE VALUE ENTERED IS NOT VALID. PLEASE TRY AGAIN.**\n')
            continue
        if number != 1 and number != 2:
            print('**THE VALUE ENTERED IS NOT VALID. PLEASE TRY AGAIN.**\n')
            continue
        print()
        return number

def sec_to_time(dt): # Modify to append
    try:
        if dt >= 86400:            
            days = math.floor(dt / 86400)
            dt = float(Decimal(dt) - Decimal(86400) * Decimal(days))
            hrs = math.floor(dt / 3600)
            dt = float(Decimal(dt) - Decimal(3600) * Decimal(hrs))
            mins = math.floor(dt / 60)
            dt = float(Decimal(dt) - Decimal(60) * Decimal(mins))
            return (days,hrs,mins,dt)
        elif dt >= 3600:
            hrs = math.floor(dt / 3600)
            dt = float(Decimal(dt) - Decimal(3600) * Decimal(hrs))
            mins = math.floor(dt / 60)
            dt = float(Decimal(dt) - Decimal(60) * Decimal(mins))
            return (hrs,mins,dt)
        elif dt >= 60:
            mins = math.floor(dt / 60)
            dt = float(Decimal(dt) - Decimal(60) * Decimal(mins))
            return (mins,dt)
        else:
            return dt
    except:
        pass

def zpad(val, n):
    val = str(val)
    bits = val.split('.')
    return "%s.%s" % (bits[0].zfill(n), bits[1])

print("Sean's Basic Kinematics Calculator v1.2")
print("=======================================\n")
print("A quick blurb on how to use this:")
print("You do have to have a basic knowledge on how")
print("kinematics works. Some problems will have to")
print("be done in segments or legs rather than having")
print("things such as the overall initial velocity")
print("and the overall final velocity, etc., and you")
print("will have to add the collective t values or")
print("dx values on your own. If you do problems in")
print("legs, write down the values you will need to")
print("add.")
input()
print("Value definitions will be explained as you")
print("proceed through the script. Type 'q' or 'quit'")
print("at anytime to quit the script. Otherwise, let's")
print("get moving!")
input()

while True:

    vi = 0.0 # m/s
    vf = 0.0 # m/s
    vix = 0.0 # m/s
    vfx = 0.0 # m/s
    viy = 0.0 # m/s
    vfy = 0.0 # m/s
    dt = 0.0 # s
    dx = 0.0 # m
    dy = 0.0 # m
    ax = 0.0 # m/s^2
    ay = -9.8 # m/s^2
    theta = 0.0 # °
    # ac = 0.0 # m/s <-- Is this even necessary?
    
    mmenu = num_check('What are you trying to figure out?\n1 = 1D Motion\n2 = 2D Motion')

    if mmenu == 1:
        mmenu = num_check('Is the motion horizontal or vertical?\n1 = Horizontal\n2 = Vertical')
        if mmenu == 1:
            vix = num_check2('What was the initial horizontal velocity (Vix)?')
            vfx = num_check2('What was the final horizontal velocity (Vfx)?')
            dt = num_check3('How long did it last (dt)?\n\nAccepted formats:\n# of seconds\nMinutes and seconds (mm:ss)\nHours, minutes, and seconds (hh:mm:ss)\nDays, hours, minutes, and seconds (dd:hh:mm:ss)\n')
            dx = num_check2('How much of a horizontal distance did it travel (dx)?')
            ax = num_check2('What was the horizontal acceleration (ax)?')
            i = 0
            while i != 6:
                if vix == '':
                    try:
                        if type(vfx) == float and type(ax) == float and type(dt) == float:
                            vix = float(Decimal(vfx) - Decimal(ax) * Decimal(dt))
                        elif type(dx) == float and type(ax) == float and type(dt) == float:
                            vix = float(Decimal((Decimal(dx) - (Decimal(ax) * pow(Decimal(dt), 2) / 2))) / Decimal(dt))
                        elif type(vfx) == float and type(ax) == float and type(dx) == float:
                            vix = float(Decimal(math.sqrt(pow(Decimal(vfx), 2) - 2 * Decimal(ax) * Decimal(dx))))
                        elif i == 5 and vix == '':
                            vix = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        vix = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass
                        
                if vfx == '':
                    try:
                        if type(vix) == float and type(ax) == float and type(dt) == float:
                            vfx = float(Decimal(vix) + Decimal(ax) * Decimal(dt))
                        elif type(vix) == float and type(ax) == float and type(dx) == float and dx != 0.0:
                            vfx = float(Decimal(math.sqrt(pow(Decimal(vix), 2) + 2 * Decimal(ax) * Decimal(dx))))
                        elif i == 5 and vfx == '':
                            vfx = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        vfx = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if dt == '':
                    try:
                        if type(vix) == float and type(vfx) == float and type(ax) == float and ax != 0.0:
                            dt = float(Decimal(abs( - ((Decimal(vix) - Decimal(vfx)) / Decimal(ax)))))
                        elif type(dx) == float and type(vix) == float and type(ax) == float and ax != 0.0:
                            dt = float(Decimal(abs(( - Decimal(vix) - Decimal(math.sqrt(pow(Decimal(vix), 2) + 2 * Decimal(ax) * Decimal(dx)))) / Decimal(ax))))
                        elif i == 5 and dt == '':
                            dt = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        dt = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if dx == '':
                    try:
                        if type(vix) == float and type(ax) == float and type(dt) == float:
                            dx = float(Decimal(vix) * Decimal(dt) + (Decimal(ax) * pow(Decimal(dt), 2)) / 2)
                        elif type(vix) == float and type(vfx) == float and type(ax) == float and ax != 0.0:
                            dx = float(Decimal((pow(Decimal(vfx), 2) - pow(Decimal(vix), 2)) / (2 * Decimal(ax))))
                        elif i == 5 and dx == '':
                            dx = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        dx = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if ax == '':
                    try:
                        if type(vix) == float and type(vfx) == float and type(dt) == float:
                            ax = float(Decimal((Decimal(vfx) - Decimal(vix)) / Decimal(dt)))
                        elif type(vix) == float and type(dx) == float and type(dt) == float:
                            ax = float(Decimal( - ((2 * Decimal(vix)) / Decimal(dt)) + ((2 * Decimal(dx)) / pow(Decimal(dt), 2))))
                        elif type(vix) == float and type(vfx) == float and type(dx) == float:
                            ax = float(Decimal((pow(Decimal(vfx), 2) - pow(Decimal(vix), 2)) / (2 * Decimal(dx))))
                        elif i == 5 and ax == '':
                            ax = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        ax = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if type(vix) == float and type(vfx) == float and type(dt) == float and type(dx) == float and type(ax) == float:
                    i = 6
                else:
                    i += 1

            if type(vix) != float:
                print('Vix =',vix)
            else:
                print('Vix = ',float(Decimal(vix) - Decimal(1) + Decimal(1)),'m/s',sep='')
            if type(vfx) != float:
                print('Vfx =',vfx)
            else:
                print('Vfx = ',float(Decimal(vfx) - Decimal(1) + Decimal(1)),'m/s',sep='')
            if type(dt) != float:
                print('dt =',dt)
            else:
                dt = sec_to_time(dt)
                try:
                    if len(dt) == 4:
                        if dt[1] == 0.0 and dt[2] == 0.0 and dt[3] == 0.0:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day',sep='')
                            else:
                                print('dt = ',dt[0],' days',sep='')
                        elif dt[1] == 0.0 and dt[2] == 0.0:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day, ',dt[3],'s',sep='')
                            else:
                                print('dt = ',dt[0],' days, ',dt[3],'s',sep='')
                        elif dt[1] == 0.0:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day, ',dt[2],':',zpad(dt[3],2),sep='')
                            else:
                                print('dt = ',dt[0],' days, ',dt[2],':',zpad(dt[3],2),sep='')
                        else:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day, ',dt[1],':','%02d' % (dt[2],),':',zpad(dt[3],2),sep='')
                            else:
                                print('dt = ',dt[0],' days, ',dt[1],':','%02d' % (dt[2],),':',zpad(dt[3],2),sep='')
                    elif len(dt) == 3:
                        print('dt = ',dt[0],':','%02d' % (dt[1],),':',zpad(dt[2],2),sep='')
                    elif len(dt) == 2:
                        print('dt = ',dt[0],':',zpad(dt[1],2),sep='')
                except:
                    print('dt = ',float(Decimal(sec_to_time(dt))),'s',sep='')
                    pass
            if type(dx) != float:
                print('dx =',dx)
            else:
                print('dx = ',float(Decimal(dx) - Decimal(1) + Decimal(1)),'m',sep='')
            if type(ax) != float:
                print('ax =',ax)
            else:
                print('ax = ',float(Decimal(ax) - Decimal(1) + Decimal(1)),'m/s^2',sep='')
            print()
            
            mmenu = num_check4('Would you like to do another one?\n\n1 = Yes\n2 = No')
            if mmenu == 1:
                continue
            elif mmenu == 2:
                quit()

        if mmenu == 2:
            viy = num_check2('What was the initial vertical velocity (Viy)?')
            vfy = num_check2('What was the final vertical velocity (Vfy)?')
            dt = num_check3('How long did it last (dt)?\n\nAccepted formats:\n# of seconds\nMinutes and seconds (mm:ss)\nHours, minutes, and seconds (hh:mm:ss)\nDays, hours, minutes, and seconds (dd:hh:mm:ss)\n')
            dy = num_check2('How much of a vertical distance did it travel (dy)?')
            print('ay = -9.8m/s^2')
            print("Vertical acceleration is simply set to Earth's gravity rounded,")
            print('which is -9.8m/s^2. If you actually need to specify it,')
            print('that is currently beyond the scope of this program.')
            print('STAY TUNED FOR UPDATES!')
            input()
            i = 0
            while i != 6:
                if viy == '':
                    try:
                        if type(vfy) == float and type(ay) == float and type(dt) == float:
                            viy = float(Decimal(vfy) - Decimal(ay) * Decimal(dt))
                        elif type(dy) == float and type(ay) == float and type(dt) == float:
                            viy = float(Decimal((Decimal(dy) - (Decimal(ay) * pow(Decimal(dt), 2) / 2)) / Decimal(dt)))
                        elif type(vfy) == float and type(ay) == float and type(dy) == float:
                            viy = float(Decimal(math.sqrt(pow(Decimal(vfy), 2) - 2 * Decimal(ay) * Decimal(dy))))
                        elif i == 5 and viy == '':
                            viy = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        viy = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass
                            
                if vfy == '':
                    try:
                        if type(viy) == float and type(ay) == float and type(dt) == float:
                            vfy = float(Decimal(viy) + Decimal(ay) * Decimal(dt))
                        elif type(viy) == float and type(ay) == float and type(dy) == float:
                            vfy = float(Decimal(math.sqrt(pow(Decimal(viy), 2) + 2 * Decimal(ay) * Decimal(dy))))
                        elif i == 5 and vfy == '':
                            vfy = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        vfy = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if dt == '':
                    try:
                        if type(viy) == float and type(vfy) == float and type(ay) == float and ay != 0.0:
                            dt = float(Decimal(abs( - ((Decimal(viy) - Decimal(vfy)) / Decimal(ay)))))
                        elif type(dy) == float and type(viy) == float and type(ay) == float and ay != 0.0:
                            dt = float(Decimal(abs(( - Decimal(viy) - Decimal(math.sqrt(pow(Decimal(viy), 2) + 2 * Decimal(ay) * Decimal(dy)))) / Decimal(ay))))
                        elif i == 5 and dt == '':
                            dt = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        dt = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if dy == '':
                    try:
                        if type(viy) == float and type(ay) == float and type(dt) == float:
                            dy = float(Decimal(viy) * Decimal(dt) + (Decimal(ay) * pow(Decimal(dt), 2)) / 2)
                        elif type(viy) == float and type(vfy) == float and type(ay) == float and ay != 0.0:
                            dy = float(Decimal((pow(Decimal(vfy), 2) - pow(Decimal(viy), 2))) / (2 * Decimal(ay)))
                        elif i == 5 and dy == '':
                            dy = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                    except:
                        dy = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                        pass

                if type(viy) == float and type(vfy) == float and type(dt) == float and type(dy) == float:
                    i = 6
                else:
                    i += 1
                    
            if type(viy) != float:
                print('Viy =',viy)
            else:
                print('Viy = ',float(Decimal(viy) - Decimal(1) + Decimal(1)),'m/s',sep='')
            if type(vfy) != float:
                print('Vfy =',vfy)
            else:
                print('Vfy = ',float(Decimal(vfy) - Decimal(1) + Decimal(1)),'m/s',sep='')
            if type(dt) != float:
                print('dt =',dt)
            else:
                dt = sec_to_time(dt)
                try:
                    if len(dt) == 4:
                        if dt[1] == 0.0 and dt[2] == 0.0 and dt[3] == 0.0:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day',sep='')
                            else:
                                print('dt = ',dt[0],' days',sep='')
                        elif dt[1] == 0.0 and dt[2] == 0.0:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day, ',dt[3],'s',sep='')
                            else:
                                print('dt = ',dt[0],' days, ',dt[3],'s',sep='')
                        elif dt[1] == 0.0:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day, ',dt[2],':',zpad(dt[3],2),sep='')
                            else:
                                print('dt = ',dt[0],' days, ',dt[2],':',zpad(dt[3],2),sep='')
                        else:
                            if dt[0] == 1.0:
                                print('dt = ',dt[0],' day, ',dt[1],':','%02d' % (dt[2],),':',zpad(dt[3],2),sep='')
                            else:
                                print('dt = ',dt[0],' days, ',dt[1],':','%02d' % (dt[2],),':',zpad(dt[3],2),sep='')
                    elif len(dt) == 3:
                        print('dt = ',dt[0],':','%02d' % (dt[1],),':',zpad(dt[2],2),sep='')
                    elif len(dt) == 2:
                        print('dt = ',dt[0],':',zpad(dt[1],2),sep='')
                except:
                    print('dt = ',float(Decimal(sec_to_time(dt))),'s',sep='')
                    pass
            if type(dy) != float:
                print('dy =',dy)
            else:
                print('dy = ',float(Decimal(dy) - Decimal(1) + Decimal(1)),'m',sep='')
            print('ay = ',float(Decimal(ay)),'m/s^2',sep='')
            print()
            
            mmenu = num_check4('Would you like to do another one?\n\n1 = Yes\n2 = No')
            if mmenu == 1:
                continue
            elif mmenu == 2:
                quit()
            
    elif mmenu == 2:
        vi = num_check2('What was the initial velocity (Vi)?')
        theta = num_check2('What was the measure of the angle (theta) at which the object/projectile\nwas launched?')
        if type(vi) != float or type(theta) != float:
            vix = num_check2('What was the initial horizontal velocity (Vix)?')
            viy = num_check2('What was the initial vertical velocity (Viy)?')
        else:
            vix = ''
            viy = ''
        vf = num_check2('What was the final velocity (Vf)?')
        vfx = num_check2('What was the final horizontal velocity (Vfx)?')
        vfy = num_check2('What was the final vertical velocity (Vfy)?')
        dt = num_check3('How long did it last (dt)?\n\nAccepted formats:\n# of seconds\nMinutes and seconds (mm:ss)\nHours, minutes, and seconds (hh:mm:ss)\nDays, hours, minutes, and seconds (dd:hh:mm:ss)\n')
        dx = num_check2('How much of a horizontal distance did it travel (dx)?')
        dy = num_check2('How much of a vertical distance did it travel (dy)?')
        print('ax = 0.0m/s^2')
        print('ay = -9.8m/s^2')
        print("In the case of projectiles/launched objects, there is only acceleration\nat the point of launch, after which since there's no horizontal force\nacting upon the object, the horizontal acceleration is 0.0m/s^2.\nVertical acceleration is simply set to Earth's gravity rounded,\nwhich is -9.8m/s^2. All of this assumes no air/drag resistance.")
        input()
        i = 0
        while i != 6:
            if viy == '':
                try:
                    if type(vfy) == float and type(ay) == float and type(dt) == float:
                        viy = float(Decimal(vfy) - Decimal(ay) * Decimal(dt))
                    elif type(dy) == float and type(ay) == float and type(dt) == float:
                        viy = float(Decimal((Decimal(dy) - (Decimal(ay) * pow(Decimal(dt), 2) / 2))) / Decimal(dt))
                    elif type(vfy) == float and type(ay) == float and type(dy) == float:
                        viy = float(Decimal(math.sqrt(pow(Decimal(vfy), 2) - 2 * Decimal(ay) * Decimal(dy))))
                    elif type(vi) == float and type(theta) == float:
                        viy = float(Decimal(vi) * Decimal(math.sin(math.radians(Decimal(theta)))))
                    elif type(vix) == float and type(theta) == float:
                        viy = float(Decimal(vix) * Decimal(math.tan(math.radians(Decimal(theta)))))
                    elif i == 5 and viy == '':
                        viy = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    viy = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass
                        
            if vfy == '':
                try:
                    if type(viy) == float and type(ay) == float and type(dt) == float:
                        vfy = float(Decimal(viy) + Decimal(ay) * Decimal(dt))
                    elif type(viy) == float and type(ay) == float and type(dy) == float and dy != 0.0:
                        vfy = float(Decimal(math.sqrt(pow(Decimal(viy), 2) + 2 * Decimal(ay) * Decimal(dy))))
                    elif type(vf) == float and type(vfx) == float:
                        vfy = float(Decimal(math.sqrt((Decimal(vf) + Decimal(vfx)) * (Decimal(vf) - Decimal(vfx)))))
                    elif i == 5 and vfy == '':
                        vfy = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    vfy = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if dt == '':
                try:
                    if type(viy) == float and type(vfy) == float and type(ay) == float and ay != 0.0:
                        dt = float(Decimal(abs( - ((Decimal(viy) - Decimal(vfy)) / Decimal(ay)))))
                    elif type(dy) == float and type(viy) == float and type(ay) == float and ay != 0.0:
                        dt = float(Decimal(abs(( - Decimal(viy) - Decimal(math.sqrt(pow(Decimal(viy), 2) + 2 * Decimal(ay) * Decimal(dy)))) / Decimal(ay))))
                    elif type(dx) == float and type(vix) == float:
                        dt = float(Decimal(dx) / Decimal(vix))
                    elif i == 5 and dt == '':
                        dt = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    dt = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if dy == '':
                try:
                    if type(viy) == float and type(ay) == float and type(dt) == float:
                        dy = float(Decimal(viy) * Decimal(dt) + (Decimal(ay) * pow(Decimal(dt), 2)) / 2)
                    elif type(viy) == float and type(vfy) == float and type(ay) == float and ay != 0.0:
                        dy = float(Decimal((pow(Decimal(vfy), 2) - pow(Decimal(viy), 2))) / (2 * Decimal(ay)))
                    elif i == 5 and dy == '':
                        dy = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    dy = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if vix == '':
                try:
                    if type(vfx) == float and type(ax) == float and type(dt) == float:
                        vix = float(Decimal(vfx) - Decimal(ax) * Decimal(dt))
                    elif type(dx) == float and type(ax) == float and type(dt) == float:
                        vix = float(Decimal((Decimal(dx) - (Decimal(ax) * pow(Decimal(dt), 2) / 2))) / Decimal(dt))
                    elif type(vfx) == float and type(ax) == float and type(dx) == float:
                        vix = float(Decimal(math.sqrt(pow(Decimal(vfx), 2) - 2 * Decimal(ax) * Decimal(dx))))
                    elif type(vi) == float and type(theta) == float:
                        vix = float(Decimal(vi) * Decimal(math.cos(math.radians(Decimal(theta)))))
                    elif type(viy) == float and type(theta) == float:
                        vix = float(Decimal(viy) * Decimal(math.cos(math.radians(Decimal(theta)))) / Decimal(math.sin(math.radians(Decimal(theta)))))
                    elif i == 5 and vix == '':
                        vix = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    vix = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if vfx == '':
                try:
                    if type(vix) == float and type(ax) == float and type(dt) == float:
                        vfx = float(Decimal(vix) + Decimal(ax) * Decimal(dt))
                    elif type(vix) == float and type(ax) == float and type(dx) == float:
                        vfx = float(Decimal(math.sqrt(pow(Decimal(vix), 2) + 2 * Decimal(ax) * Decimal(dx))))
                    elif type(vf) == float and type(vfy) == float:
                        vfx = float(Decimal(math.sqrt((Decimal(vf) + Decimal(vfy)) * (Decimal(vf) - Decimal(vfy)))))
                    elif i == 5 and vfx == '':
                        vfx = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    vfx = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if dx == '':
                try:
                    if type(vix) == float and type(ax) == float and type(dt) == float:
                        dx = float(Decimal(vix) * Decimal(dt) + (Decimal(ax) * pow(Decimal(dt), 2)) / 2)
                    elif type(vix) == float and type(vfx) == float and type(ax) == float and ax != 0.0:
                        dx = float(Decimal((pow(Decimal(vfx), 2) - pow(Decimal(vix), 2))) / (2 * Decimal(ax)))
                    elif i == 5 and dx == '':
                        dx = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    dx = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if vf == '':
                try:
                    if type(vfy) == float and type(vfx) == float:
                        vf = float(Decimal(math.sqrt(pow(Decimal(vfy), 2) + pow(Decimal(vfx), 2))))
                    elif i == 5 and vf == '':
                        vf = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    vf = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if vi == '':
                try:
                    if type(viy) == float and type(vix) == float:
                        vi = float(Decimal(math.sqrt(pow(Decimal(viy), 2) + pow(Decimal(vix), 2))))
                    elif type(viy) == float and type(theta) == float:
                        vi = float(Decimal(viy) / Decimal(math.sin(Decimal(theta))))
                    elif type(vix) == float and type(theta) == float:
                        vi = float(Decimal(vix) / Decimal(math.cos(Decimal(theta))))
                    elif i == 5 and vi == '':
                        vi = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    vi = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if theta == '':
                try:
                    if type(vi) == float and type(viy) == float:
                        theta = float(Decimal(math.degrees(math.asin(Decimal(viy) / Decimal(vi)))))
                    elif type(vi) == float and type(vix) == float:
                        theta = float(Decimal(math.degrees(math.acos(Decimal(vix) / Decimal(vi)))))
                    elif i == 5 and theta == '':
                        theta = 'NO SOLUTION; NOT ENOUGH DATA TO SOLVE!'
                except:
                    theta = 'MATH ERROR; POSSIBLE INCORRECT AMOUNTS ENTERED FOR VARIABLES!'
                    pass

            if type(theta) == float and type(viy) == float and type(vfy) == float and type(dt) == float and type(dy) == float and type(vix) == float and type(vfx) == float and type(dx) == float and type(vf) == float:
                i = 6
            else:
                i += 1
            
    if type(theta) != float:
        print('theta =',theta)
    else:
        print('theta = ',float(Decimal(theta) - Decimal(1) + Decimal(1)),'°',sep='')
    if type(vi) != float:
        print('Vi =',vi)
    else:
        print('Vi = ',float(Decimal(vi) - Decimal(1) + Decimal(1)),'m/s',sep='')
    if type(vix) != float:
        print('Vix =',vix)
    else:
        print('Vix = ',float(Decimal(vix) - Decimal(1) + Decimal(1)),'m/s',sep='')
    if type(viy) != float:
        print('Viy =',viy)
    else:
        print('Viy = ',float(Decimal(viy) - Decimal(1) + Decimal(1)),'m/s',sep='')
    if type(vf) != float:
        print('Vf =',vf)
    else:
        print('Vf = ',float(Decimal(vf) - Decimal(1) + Decimal(1)),'m/s',sep='')
    if type(vfx) != float:
        print('Vfx =',vfx)
    else:
        print('Vfx = ',float(Decimal(vfx) - Decimal(1) + Decimal(1)),'m/s',sep='')
    if type(vfy) != float:
        print('Vfy =',vfy)
    else:
        print('Vfy = ',float(Decimal(vfy) - Decimal(1) + Decimal(1)),'m/s',sep='')
    if type(dt) != float:
        print('dt =',dt)
    else:
        dt = sec_to_time(dt)
        try:
            if len(dt) == 4:
                if dt[1] == 0.0 and dt[2] == 0.0 and dt[3] == 0.0:
                    if dt[0] == 1.0:
                        print('dt = ',dt[0],' day',sep='')
                    else:
                        print('dt = ',dt[0],' days',sep='')
                elif dt[1] == 0.0 and dt[2] == 0.0:
                    if dt[0] == 1.0:
                        print('dt = ',dt[0],' day, ',dt[3],'s',sep='')
                    else:
                        print('dt = ',dt[0],' days, ',dt[3],'s',sep='')
                elif dt[1] == 0.0:
                    if dt[0] == 1.0:
                        print('dt = ',dt[0],' day, ',dt[2],':',zpad(dt[3],2),sep='')
                    else:
                        print('dt = ',dt[0],' days, ',dt[2],':',zpad(dt[3],2),sep='')
                else:
                    if dt[0] == 1.0:
                        print('dt = ',dt[0],' day, ',dt[1],':','%02d' % (dt[2],),':',zpad(dt[3],2),sep='')
                    else:
                        print('dt = ',dt[0],' days, ',dt[1],':','%02d' % (dt[2],),':',zpad(dt[3],2),sep='')
            elif len(dt) == 3:
                print('dt = ',dt[0],':','%02d' % (dt[1],),':',zpad(dt[2],2),sep='')
            elif len(dt) == 2:
                print('dt = ',dt[0],':',zpad(dt[1],2),sep='')
        except:
            print('dt = ',float(Decimal(sec_to_time(dt))),'s',sep='')
            pass
    if type(dx) != float:
        print('dx =',dx)
    else:
        print('dx = ',float(Decimal(dx) - Decimal(1) + Decimal(1)),'m',sep='')
    if type(dy) != float:
        print('dy =',dy)
    else:
        print('dy = ',float(Decimal(dy) - Decimal(1) + Decimal(1)),'m',sep='')
    print('ax = ',float(Decimal(ax)),'m/s^2',sep='')
    print('ay = ',float(Decimal(ay)),'m/s^2',sep='')
    print()
    print('NOTE- If you were looking for theta by leaving it blank, calculated\ntheta uses arcsine and arccosine converted from radians for its\ncalculations. For this reason, the value of calculated theta is an\napproximation.\n')
   
    mmenu = num_check4('Would you like to do another one?\n\n1 = Yes\n2 = No')
    if mmenu == 1:
        continue
    elif mmenu == 2:
        quit()
