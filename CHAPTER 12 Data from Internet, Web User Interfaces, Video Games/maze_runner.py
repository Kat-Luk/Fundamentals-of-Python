import numpy as np

def main():
    maze = np.array([["S", ".", ".", "#", "."],
                     ["#", "#", ".", "#", "."],
                     [".", ".", ".", ".", "."],
                     [".", "#", "#", "#", "#"],
                     [".", ".", ".", ".", "E"]])
    
    player_position_r = 0
    player_position_c = 0
    print(f"Start position: ({player_position_r}, {player_position_c})")
    while True:
        move = input("Move (N/S/E/W): ")
        
        new_r = player_position_r
        new_c = player_position_c
        
        if move == "N":
            new_r = player_position_r - 1
        elif move == "S":
            new_r = player_position_r + 1
        elif move == "E":
            new_c = player_position_c + 1
        elif move == "W":
            new_c = player_position_c - 1
        
        if new_r < 0 or new_r >= 5 or new_c < 0 or new_c >= 5:
            print("You can't go there!")
            continue
        
        next_cell = maze[new_r, new_c]
        
        if next_cell == "#":
            print("There is a wall there!")
        elif next_cell == "E":
            maze[player_position_r, player_position_c] = "."
            player_position_r = new_r
            player_position_c = new_c
            maze[player_position_r, player_position_c] = "S"
            print(f"Current position: ({player_position_c}, {player_position_r})")
            print ("You found the exit! You win!")
            return
        else:
            maze[player_position_r, player_position_c] = "."
            player_position_r = new_r
            player_position_c = new_c
            maze[player_position_r, player_position_c] = "S"
            print(f"Current position: ({player_position_c}, {player_position_r})")
if __name__ == "__main__":
    main()
