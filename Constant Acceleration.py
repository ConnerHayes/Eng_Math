import math

axis = int(input("Which axis do you need? 0 for x, 1 for y, 2 for z: "))
if axis == 0:
    print("0 = x position, 1 = final x velocity, 2 = initial velocity, 3 = acceleration, 4 = time")
    variables_wanted_x = int(input("What variable are you looking for? "))
    print("What are your current variables? Enter 0 for unknown value! \n Also make sure the units are correct! \n")
    x1 = float(input("What is the initial x position? "))
    x2 = float(input("What is the final x position? "))
    v1 = float(input("What is the initial velocity? "))
    v2 = float(input("What is the final velocity? "))
    a = float(input("what is the acceleration? "))
    t = float(input("How long did it take? "))
    delta_x = x2 - x1
    v_bar = (v1 * v2)/2  # Both velocities are given.

    if variables_wanted_x == 0:  # Position of x-axis
        if v_bar > 0:
            delta_x = v_bar * t
            print("X-Position is \u0394", delta_x)
        elif v2 > 0:
            delta_x = ((v1 + v2) / 2) * t
            print("X-Position is \u0394", delta_x)
        else:
            delta_x = (v1 * t) + .5 * (a * (t ** 2))
            print("X-Position is \u0394", delta_x)

    elif variables_wanted_x == 1:  # Final velocity of x-axis
        if t > 0:
            v2 = v1 + (a * t)
            print("X-Final velocity is ", v2)
        else:
            v2_squared = (v1 ** 2) + (2 * a * delta_x)
            v2 = math.sqrt(v2_squared)
            print("X-Final velocity is ", v2)

    elif variables_wanted_x == 2:  # Initial velocity of x-axis
        if t > 0:
            v1 = (a * t) / v2
            print("X-Initial velocity is ", v1)
        elif v2 == 0:
            v1 = (delta_x - (.5 * (a * (t ** 2)))) / t
            print("X-Initial velocity is ", v1)
        elif t == 0:
            v1_squared = (v2 ** 2) - (2 * a * delta_x)
            v1 = math.sqrt(v1_squared)
            print("X-Initial velocity is ", v1)
        else:
            v1 = ((delta_x / t) * 2) - v2
            print("X-Initial velocity is ", v1)

    elif variables_wanted_x == 3:  # Acceleration of x-axis
        if delta_x > 0:
            if v2 == 0:
                a = ((delta_x - (v1 * t)) * 2) / (t ** 2)
                print("Acceleration is ", a)
            else:
                v2v1_squared = math.sqrt(v2 - v1) ** 2
                a = v2v1_squared / (2 * delta_x)
                print("Acceleration is ", a)
        elif delta_x == 0:
            a = (v2 - v1) / t
            print("Acceleration is ", a)
        else:
            print("Something wrong here mate. Try again! ")

    elif variables_wanted_x == 4:  # Time taken in x-axis
        if delta_x == 0:
            t = (v2 - v1) / a
            print("Time taken is ", t)
        elif a == 0:
            t = delta_x / (2 / (v1 + v2))
            print("Time taken is ", t)
        elif v2 == 0:
            t = (delta_x - (.5 * (a * (t ** 2)))) / v1
            print("Time taken is ", t)
        else:
            print("Something wrong here mate. Try again! ")

elif axis == 1:
    print("0 = y position, 1 = final y velocity, 2 = initial velocity, 3 = acceleration, 4 = time")
    variables_wanted_y = int(input("What variable are you looking for? "))
    print("What are your current variables? Enter 0 for unknown value! \n")
    y1 = float(input("What is the initial y position? "))
    y2 = float(input("What is the final y position? "))
    v1 = float(input("What is the initial velocity? "))
    v2 = float(input("What is the final velocity? "))
    a = float(input("What is the acceleration? "))
    t = float(input("How long did it take? "))
    delta_y = y2 - y1
    v_bar = (v1 * v2) / 2  # Both velocities are given.

    if variables_wanted_y == 0:  # Position of y-axis
        if v_bar > 0:
            delta_y = v_bar * t
            print("Y-Position is \u0394", delta_y)
        elif v2 > 0:
            delta_y = ((v1 + v2) / 2) * t
            print("Y-Position is \u0394", delta_y)
        else:
            delta_y = (v1 * t) + .5 * (a * (t ** 2))
            print("Y-Position is \u0394", delta_y)

    elif variables_wanted_y == 1:  # Final velocity of y-axis
        if t > 0:
            v2 = v1 + (a * t)
            print("Y-Final velocity is ", v2)
        else:
            v2_squared = (v1 ** 2) + (2 * a * delta_y)
            v2 = math.sqrt(v2_squared)
            print("Y-Final velocity is ", v2)

    elif variables_wanted_y == 2:  # Initial velocity of y-axis
        if t > 0:
            v1 = (a * t) / v2
            print("Y-Initial velocity is ", v1)
        elif v2 == 0:
            v1 = (delta_y - (.5 * (a * (t ** 2)))) / t
            print("Y-Initial velocity is ", v1)
        elif t == 0:
            v1_squared = (v2 ** 2) - (2 * a * delta_y)
            v1 = math.sqrt(v1_squared)
            print("Y-Initial velocity is ", v1)
        else:
            v1 = ((delta_y / t) * 2) - v2
            print("Y-Initial velocity is ", v1)

    elif variables_wanted_y == 3:  # Acceleration of y-axis
        if delta_y > 0:
            if v2 == 0:
                a = ((delta_y - (v1 * t)) * 2) / (t ** 2)
                print("Acceleration is ", a)
            else:
                v2v1_squared = math.sqrt(v2 - v1) ** 2
                a = v2v1_squared / (2 * delta_y)
                print("Acceleration is ", a)
        elif delta_y == 0:
            a = (v2 - v1) / t
            print("Acceleration is ", a)
        else:
            print("Something wrong here mate. Try again! ")

    elif variables_wanted_y == 4:  # Time taken in y-axis
        if delta_y == 0:
            t = (v2 - v1) / a
            print("Time taken is ", t)
        elif a == 0:
            t = delta_y / (2 / (v1 + v2))
            print("Time taken is ", t)
        elif v2 == 0:
            t = (delta_y - (.5 * (a * (t ** 2)))) / v1
            print("Time taken is ", t)
        else:
            print("Something wrong here mate. Try again! ")

elif axis == 2:
    print("0 = y position, 1 = final y velocity, 2 = initial velocity, 3 = acceleration, 4 = time")
    variables_wanted_z = int(input("What variable are you looking for? "))
    print("What are your current variables? Enter 0 for unknown value! \n")
    z1 = float(input("What is the initial z position? "))
    z2 = float(input("What is the final z position? "))
    v1 = float(input("What is the initial velocity? "))
    v2 = float(input("What is the final velocity? "))
    a = float(input("What is the acceleration? "))
    t = float(input("How long did it take? "))
    delta_z = z2 - z1
    v_bar = (v1 * v2) / 2  # Both velocities are given.

    if variables_wanted_z == 0:  # Position of z-axis
        if v_bar > 0:
            delta_z = v_bar * t
            print("Z-Position is \u0394", delta_z)
        elif v2 > 0:
            delta_z = ((v1 + v2) / 2) * t
            print("Y-Position is \u0394", delta_z)
        else:
            delta_z = (v1 * t) + .5 * (a * (t ** 2))
            print("Y-Position is \u0394", delta_z)

    elif variables_wanted_z == 1:  # Final velocity of z-axis
        if t > 0:
            v2 = v1 + (a * t)
            print("Z-Final velocity is ", v2)
        else:
            v2_squared = (v1 ** 2) + (2 * a * delta_z)
            v2 = math.sqrt(v2_squared)
            print("Z-Final velocity is ", v2)

    elif variables_wanted_z == 2:  # Initial velocity of z-axis
        if t > 0:
            v1 = (a * t) / v2
            print("Z-Initial velocity is ", v1)
        elif v2 == 0:
            v1 = (delta_z - (.5 * (a * (t ** 2)))) / t
            print("Z-Initial velocity is ", v1)
        elif t == 0:
            v1_squared = (v2 ** 2) - (2 * a * delta_z)
            v1 = math.sqrt(v1_squared)
            print("Z-Initial velocity is ", v1)
        else:
            v1 = ((delta_z / t) * 2) - v2
            print("Z-Initial velocity is ", v1)

    elif variables_wanted_z == 3:  # Acceleration of z-axis
        if delta_z > 0:
            if v2 == 0:
                a = ((delta_z - (v1 * t)) * 2) / (t ** 2)
                print("Acceleration is ", a)
            else:
                v2v1_squared = math.sqrt(v2 - v1) ** 2
                a = v2v1_squared / (2 * delta_z)
                print("Acceleration is ", a)
        elif delta_z == 0:
            a = (v2 - v1) / t
            print("Acceleration is ", a)
        else:
            print("Something wrong here mate. Try again! ")

    elif variables_wanted_z == 4:  # Time taken in z-axis
        if delta_z == 0:
            t = (v2 - v1) / a
            print("Time taken is ", t)
        elif a == 0:
            t = delta_z / (2 / (v1 + v2))
            print("Time taken is ", t)
        elif v2 == 0:
            t = (delta_z - (.5 * (a * (t ** 2)))) / v1
            print("Time taken is ", t)
        else:
            print("Something wrong here mate. Try again! ")

else:
    print("You put in the wrong input try again!")
