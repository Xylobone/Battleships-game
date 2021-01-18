#see the readme.md file for description and data 

import random

def is_sunk(ship):
    if ship[3] == len(ship[4]):
        return True
    else:
        return False

def ship_type(ship):
    # Checks length value and returns a string
    if ship[3] == 1:
        return "submarine"
    elif ship[3] == 2:
        return "destroyer"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 4:
        return "battleship"

def is_open_sea(row, column, fleet):
    # Iterates through each ship in fleet
    for i in range(len(fleet)): 

        # Creating variables to make it easier to code conditions
        # 'ship' variables refer to the values of the ship being compared to user row and column values
        shiplength = fleet[i][3]
        shiphorizontal = fleet[i][2]
        shiprow = fleet[i][0]
        shipcolumn = fleet[i][1]

        if shiphorizontal == True:
            # Returns false if the row and column values are adjacent to the current ship
            if (((row - 1) <= shiprow <= (row + 1)) and ((shipcolumn - 1) <= column <= (shipcolumn + shiplength + 1))):
                return False

        elif shiphorizontal == False:
            # Returns false if the row and column values are adjacent to the current ship
            if (((shiprow - 1) <= row <= (shiprow + shiplength + 1)) and ((column - 1) <= shipcolumn <= (column + 1))):
                return False

        else:
            # If it pases these conditions then the function will return that the square specified is in open sea.
            return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    
    # For loop to iterate through each ship in list (fleet) 
    for i in range(len(fleet)):
        # if the ship is horizontal then we must check is_open_sea along column value (iterate through x axis)
        if horizontal == True:
            for j in range(0, length + 1):
                if is_open_sea(row, column + j, fleet) == False:
                    return False
            return True
        
        # if the ship is vertical then we must check is_open_sea along row value (iterate through y axis)
        elif horizontal == False:
            for k in range(0, length + 1):
                if is_open_sea(row + k, column, fleet) == False:
                    return False
            return True
        else:
            return True
            

def place_ship_at(row, column, horizontal, length, fleet):

    # Creating a new ship. 0 is a placeholder for set of tuples that will be the hits
    # Since we have to remake tuples whenever we edit them I thought this was a suitable solution
    fleet.append((row, column, horizontal, length, {}))

# (0row, 1column, 2horizontal, 3length, 4hits)
def check_if_hits(row, column, fleet):
    
    for i in range(len(fleet)):
        
        shiplength = fleet[i][3]
        shiphorizontal = fleet[i][2]
        shiprow = fleet[i][0]
        shipcolumn = fleet[i][1]
        
        if shiphorizontal == True:
            if (row == shiprow) and (shipcolumn <= column <= (shipcolumn + shiplength)):
                return True

        elif shiphorizontal == False:
            if (column == shipcolumn) and (shiprow <= row <= (shiprow + shiplength)):
                return True

    # If the function reaches this part without return True then then it must not be a hit.
    # This is because it would have exited the function already with a True return otherwise
    return False

def hit(row, column, fleet):
    
    # Since ship is not specified in the function, it will
    # search through fleet for the ship that is hit and then
    # return the tuple containing the fleet and ship
    for i in range(len(fleet)):
        shiplength = fleet[i][3]
        shiphorizontal = fleet[i][2]
        shiprow = fleet[i][0]
        shipcolumn = fleet[i][1]
        shiphits = set(fleet[i][4])
            
        #Finding out which ship is hit
        if shiphorizontal == True:
            if (row == shiprow) and ((shipcolumn) <= column <= (shipcolumn + shiplength)):
                shiphits.add((row, column))
                fleet[i] = (shiprow, shipcolumn, True, shiplength, shiphits)
                return (fleet, fleet[i])

        
        elif shiphorizontal == False:
            if (column == shipcolumn) and ((shiprow) <= row <= (shiprow + shiplength)):
                shiphits.add((row, column))
                fleet[i] = (shiprow, shipcolumn, False, shiplength, shiphits)
                return (fleet, fleet[i])

def are_unsunk_ships_left(fleet):

    # 0 means all ships are sunk
    allshipssunk = 0

    for i in range(len(fleet)):
        if is_sunk(fleet[i]) == False:
            # Will add 1 if it finds an unsunk ship
            allshipssunk = allshipssunk + 1
    
    # It requires all ships to be sunk for allshipssunk to be 0
    if allshipssunk == 0:
        return False 
    else:
        return True

def main():

    fleet1 = []
    def randomly_place_all_ships():

        numberofships = 0
        # Placing battleship
        randomhorizontal = random.randint(0, 1)

        if randomhorizontal == 1:
            randomrow = random.randint(0, 9)
            randomcolumn = random.randint(0, 6)
            place_ship_at(randomrow, randomcolumn, True, 4, fleet1)

        elif randomhorizontal == 0:
            randomrow = random.randint(0, 6)
            randomcolumn = random.randint(0, 9)
            place_ship_at(randomrow, randomcolumn, False, 4, fleet1)
        
        numberofships = numberofships + 1

        # Placing Cruisers
        while (1 <= numberofships < 3):
                
            randomhorizontal = random.randint(0, 1)
            
            if randomhorizontal == 1:

                randomrow = random.randint(0, 9)
                randomcolumn = random.randint(0, 7)
                if ok_to_place_ship_at(randomrow, randomcolumn, True, 3, fleet1) == True:
                    place_ship_at(randomrow, randomcolumn, True, 3, fleet1)
                    numberofships = numberofships + 1

            elif randomhorizontal == 0:
                
                randomrow = random.randint(0, 7)
                randomcolumn = random.randint(0, 9)
                if ok_to_place_ship_at(randomrow, randomcolumn, False, 3, fleet1) == True:
                    place_ship_at(randomrow, randomcolumn, False, 3, fleet1)
                    numberofships = numberofships + 1

        # Placing destroyers
        while 3 <= numberofships < 6:

            randomhorizontal = random.randint(0, 1)

            if randomhorizontal == 1:

                randomrow = random.randint(0, 9)
                randomcolumn = random.randint(0, 8)
                if ok_to_place_ship_at(randomrow, randomcolumn, True, 2, fleet1) == True:
                    place_ship_at(randomrow, randomcolumn, True, 2, fleet1)
                    numberofships = numberofships + 1

            elif randomhorizontal == 0:
                
                randomrow = random.randint(0, 8)
                randomcolumn = random.randint(0, 9)
                if ok_to_place_ship_at(randomrow, randomcolumn, False, 2, fleet1) == True:
                    place_ship_at(randomrow, randomcolumn, False, 2, fleet1)
                    numberofships = numberofships + 1
        
        # Placing Submarines
        while 6 <= numberofships < 10:
            
            randomhorizontal = random.randint(0, 1)

            if randomhorizontal == 1:

                randomrow = random.randint(0, 9)
                randomcolumn = random.randint(0, 9)
                if ok_to_place_ship_at(randomrow, randomcolumn, True, 1, fleet1) == True:
                    place_ship_at(randomrow, randomcolumn, True, 1, fleet1)
                    numberofships = numberofships + 1

            elif randomhorizontal == 0:
                
                randomrow = random.randint(0, 9)
                randomcolumn = random.randint(0, 9)
                if ok_to_place_ship_at(randomrow, randomcolumn, False, 1, fleet1) == True:
                    place_ship_at(randomrow, randomcolumn, False, 1, fleet1)
                    numberofships = numberofships + 1

    randomly_place_all_ships()

    # Printing fleet1 to check values
    for items in fleet1:
        print(items)


    # Creating the text-based base grid in which provides the visualisation for the game.
    # A list of ten lists, which will become a 10x10 grid in the terminal.
    # Inspiration comes from the project description, which I thought was a very effective way of representing game state.
    
    # The visualisation displays:
    # Rows and column numbers
    # state of each square, with statuses inluding: unknown, miss, hit.
    # If a ship is sunk it will display its type indicated by the first character (e.g. B for Battleship)

    grid = [[" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
            [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "]]
    
    # Function to show columns and rows
    def row_and_column_display(grid):
        rows = len(grid)
        columns = len(grid[0])

        display = ("    " + "  ".join(str(i) for i in range(rows)) + "\n" + "   " + " ".join( ' ―' for i in range(columns)) + '\n')
        
        for i, row in enumerate(grid):
            display = display + (str(i)+ " |" + ''.join(str(item) for item in row) + '\n')
        return display


    game_over = False
    shots = 0
    print("***** Welcome to battleships. *****\n")
    while not game_over:
        
        # Printing the grid display. This is updated every time a new co-ordinate is entered.
        print(row_and_column_display(grid))

        # Handling execptions. the application should only except a signle digit followed by a space
        # followed by another single digit.
        while True:
            try:
                loc_str = (input("Please enter a row and column to shoot, separated by a space: ")) 
                if  len(loc_str) < 3 or len(loc_str) > 3:
                    raise ValueError
                if not loc_str[1] == " ":
                    raise ValueError
                if not loc_str[0].isdigit() == True:
                    raise ValueError
                if not loc_str[2].isdigit() == True:
                    raise ValueError
            except ValueError:
                print("That wasn't a valid input, please enter your row and column again separated by a space: ")
                continue 
            else:
                break
    
        loc_str = loc_str.split()
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])

        shots += 1

        if check_if_hits(current_row, current_column, fleet1) == True:
            print("--- You have a hit! ---")
            (fleet1, ship_hit) = hit(current_row, current_column, fleet1)
            
            # Replacing hit spot with " * " which indicates a hit
            grid[current_row][current_column] = " * "

            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
                
                # Turning a set of tuples into a list of tuples
                sunk_ship_hits = list(ship_hit[4])
                # Turning a list of tuples into a list of lists
                sunk_ship_hits_lists = [list(x) for x in sunk_ship_hits]
                
                #Iterates through the list of hits
                for i in range(len(sunk_ship_hits_lists)):
                    # Takes items in coordinate pairs and amends their position in the grid.
                    row_edit = sunk_ship_hits_lists[i][0]
                    column_edit = sunk_ship_hits_lists[i][1]
                    if ship_hit[3] == 4:
                        grid[row_edit][column_edit] = " B "
                    elif ship_hit[3] == 3:
                        grid[row_edit][column_edit] = " C "
                    elif ship_hit[3] == 2:
                        grid[row_edit][column_edit] = " D "
                    elif ship_hit[3] == 1:
                        grid[row_edit][column_edit] = " S "
                        
        else:
            print("--- You have missed! ---")

            # Misses are indicated by a " - " on the grid
            grid[current_row][current_column] = " - "

        if not are_unsunk_ships_left(fleet1): game_over = True

    #Game over message with shots required and final game board
    print("Game over - all ships suck! You required", shots, "shots. \n")
    print("Here is the Final Gameboard: \n")
    print(row_and_column_display(grid))


if __name__ == '__main__': #keep this in
   main()
