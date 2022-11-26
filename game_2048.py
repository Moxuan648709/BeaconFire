import function_2048

matrix = function_2048.start_game()
function_2048.print_mat(matrix)

status = function_2048.get_current_state(matrix)

while status == 'continues':
    cmd = input("Enter command: ")

    # Use a while loop to handle invalid input command.
    while cmd not in ['w', 's', 'a', 'd']:
        print("This command is invalid, please use the correct command key!")
        cmd = input("Enter command:")
    
    # Enter w to move up:
    if cmd == 'w':
        matrix, flag = function_2048.move_up(matrix) # move up function
        status = function_2048.get_current_state(matrix) # print current matrix
        
    # Enter s to move down
    elif cmd == 's':
        matrix, flag = function_2048.move_down(matrix) # move down function
        status = function_2048.get_current_state(matrix)
        
    # Enter a to move left
    elif cmd == 'a':
        matrix, flag = function_2048.move_left(matrix) # move left
        status = function_2048.get_current_state(matrix)
        
    # Enter d to move right
    elif cmd == 'd':
        matrix, flag = function_2048.move_right(matrix) # move right
        status = function_2048.get_current_state(matrix)

    function_2048.print_mat(matrix)
    if status == 'continues':
        function_2048.add_new_2(matrix)
    else:
        print(status)
        break
