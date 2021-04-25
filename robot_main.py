import re

# importing RegEx to take inputs in desired format
directions = []  # Taking all the directions after place statement in a list
final_position = []   # Updating all the x,y,z co-ordinates in this list
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


def moving_robot():
    # This function can move and rotate the robot w.r.t the input given
    global x_coordinate
    global y_coordinate
    global z
    global final_position
    for next_move in directions:  # looping through the directions so that we can calculate each step
        if next_move == 'MOVE' and z == 'NORTH':
            y_coordinate += 1
        elif next_move == 'MOVE' and z == 'EAST':
            x_coordinate += 1
        elif next_move == 'MOVE' and z == 'SOUTH':
            y_coordinate -= 1
        elif next_move == 'MOVE' and z == 'WEST':
            x_coordinate -= 1
        elif next_move == 'LEFT':
            continue
        elif next_move == 'RIGHT':
            continue

    final_position.append(x_coordinate)
    final_position.append(y_coordinate)
    final_position.append(z)


if __name__ == "__main__":
    taking_input_from_user()
    moving_robot()
