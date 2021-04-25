import re

# importing RegEx to take inputs in desired format
directions = []  # Taking all the directions after place statement in a list
final_position = []  # Updating all the x,y,z co-ordinates in this list
placing, x, y, z = list(re.split(r'[, ]', input()))
x_coordinate = int(x)
y_coordinate = int(y)


def taking_input_from_user():
    # Taking Input from user and input validation
    global x_coordinate
    global y_coordinate
    global directions
    global z
    if (placing == 'PLACE') and (0 <= x_coordinate < 5) and (0 <= y_coordinate < 5) and \
            (z == 'NORTH' or 'EAST' or 'SOUTH' or 'WEST'):
        while True:
            user_input = input()  # user inputs after place statement
            if user_input == 'REPORT':
                break
            if user_input.startswith('PLACE'):
                # Taking PLACE function in middle of directions
                directions = []
                directions.append(user_input)
                list_to_string = ''.join([str(elm) for elm in directions]) \
                    # modifying input to validate and update x,x,z coordinates
                if (0 <= int(list_to_string[6]) < 5) and (0 <= int(list_to_string[8]) < 5) and \
                        (z == 'NORTH' or 'EAST' or 'SOUTH' or 'WEST'):
                    x_coordinate = int(list_to_string[6])
                    y_coordinate = int(list_to_string[8])
                    z = list_to_string[10:]
                else:
                    print(f"Re-Run the program and input the values in Correct Format")
                    exit()
                user_input = input()
            if not user_input == 'REPORT':
                directions.append(user_input)
            else:
                break
    else:
        print(f"Re-Run the program and input the values in Correct Format")
        exit()


def down_limit():
    # Making sure the robot doesn't fall of the table to south-side
    global y_coordinate
    if 0 <= y_coordinate < 5:
        pass
    else:
        y_coordinate += 1


def upper_limit():
    # Making sure the robot doesn't fall of the table to north-side
    global y_coordinate
    if 0 <= y_coordinate < 5:
        pass
    else:
        y_coordinate -= 1


def right_limit():
    # Making sure the robot doesn't fall of the table to the east-side
    global x_coordinate
    if 0 <= x_coordinate < 5:
        pass
    else:
        x_coordinate -= 1


def left_limit():
    # Making sure the robot doesn't fall of the table to the west-side
    global x_coordinate
    if 0 <= x_coordinate < 5:
        pass
    else:
        x_coordinate += 1


def left_rotation():
    # This function rotates the robot 90 deg counter-clockwise
    global z
    if z == 'NORTH':
        z = 'WEST'
    elif z == 'WEST':
        z = 'SOUTH'
    elif z == 'SOUTH':
        z = 'EAST'
    elif z == 'EAST':
        z = 'NORTH'


def right_rotation():
    # This function rotates the robot 90 deg clockwise
    global z
    if z == 'NORTH':
        z = 'EAST'
    elif z == 'WEST':
        z = 'NORTH'
    elif z == 'SOUTH':
        z = 'WEST'
    elif z == 'EAST':
        z = 'SOUTH'


def moving_robot():
    # This function can move and rotate the robot w.r.t the input given
    global x_coordinate
    global y_coordinate
    global z
    global final_position
    for next_move in directions:  # looping through the directions so that we can calculate each step
        if next_move == 'MOVE' and z == 'NORTH':
            y_coordinate += 1
            upper_limit()
        elif next_move == 'MOVE' and z == 'EAST':
            x_coordinate += 1
            right_limit()
        elif next_move == 'MOVE' and z == 'SOUTH':
            y_coordinate -= 1
            down_limit()
        elif next_move == 'MOVE' and z == 'WEST':
            x_coordinate -= 1
            left_limit()
        elif next_move == 'LEFT':
            left_rotation()
        elif next_move == 'RIGHT':
            right_rotation()
    final_position.append(x_coordinate)
    final_position.append(y_coordinate)
    final_position.append(z)


if __name__ == "__main__":
    taking_input_from_user()
    moving_robot()
    print(f"{final_position[0]},{final_position[1]},{final_position[2]}")  # printing out final position of Robot
