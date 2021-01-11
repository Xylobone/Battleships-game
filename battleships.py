#see the readme.md file for description and data 


'''
class ship:
    def __init__(self, row, column, horizontal, length, hits):
        self.length = 0
        self.row = 0
        self.column = 0
        self.horizontal = False
        self.length = 0
        self.hits = ()


# (0row, 1column, 2horizontal, 3length, 4hits)


'''

import random
fleet = []

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
    for i in fleet: 

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
            if (((shiprow - 1) <= row <= (shiprow + length + 1)) and ((column - 1) <= shipcolumn <= (column + 1))):
                return False

        else:
            # If it pases these conditions then the function will return that the square specified is in open sea.
            return True
        


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    
    # For loop to iterate through each ship in list (fleet) 
    for i in fleet:
        # if the ship is horizontal then we must check is_open_sea along column value (iterate through x axis)
        if horizontal == True:
            for j in range(0, length + 1):
                if is_open_sea(row, column + j, fleet) == False:
                    return False
        
        # if the ship is vertical then we must check is_open_sea along row value (iterate through y axis)
        elif horizontal == False:
            for k in range(0, length + 1):
                if is_open_sea(row + k, column, fleet) == False:
                    return False
        else:
            return True
            

def place_ship_at(row, column, horizontal, length, fleet):

    # Creating a new ship. 0 is a placeholder for set of tuples that will be the hits
    # Since we have to remake tuples whenever we edit them I thought this was a suitable solution
    fleet.append((row, column, horizontal, length, 0))


def randomly_place_all_ships():

    numberofships = 0

    # Placing battleship
    randomhorizontal = random.randint(0, 1)

    if randomhorizontal == 1:
        randomrow = random.randint(0, 9)
        randomcolumn = random.randint(0, 6)
        place_ship_at(randomrow, randomcolumn, True, 4, 0, fleet1)

    elif randomhorizontal == 0:
        randomrow = random.randint(0, 6)
        randomcolumn = random.randint(0, 9)
        place_ship_at(randomrow, randomcolumn, False, 4, 0, fleet1)
    
    numberofships = numberofships + 1
    

    # Placing Cruisers
    while (1 < numberofships < 3):
            
        randomhorizontal = random.randint(0, 1)
        
        if randomhorizontal == 1:

            randomrow = random.randint(0, 9)
            randomcolumn = random.randint(0, 7)
            if ok_to_place_ship_at(randomrow, randomcolumn, True, 3, fleet1) == True:
                place_ship_at(randomrow, randomcolumn, True, 3, 0, fleet1)
                numberofships = numberofships + 1

        elif randomhorizontal == 0:
            
            randomrow = random.randint(0, 7)
            randomcolumn = random.randint(0, 9)
            if ok_to_place_ship_at(randomrow, randomcolumn, False, 3, fleet1) == True:
                place_ship_at(randomrow, randomcolumn, False, 3, 0, fleet1)
                numberofships = numberofships + 1

    # Placing destroyers
    while 3 <= numberofships < 6:

        randomhorizontal = random.randint(0, 1)

        if randomhorizontal == 1:

            randomrow = random.randint(0, 9)
            randomcolumn = random.randint(0, 8)
            if ok_to_place_ship_at(randomrow, randomcolumn, True, 2, fleet1) == True:
                place_ship_at(randomrow, randomcolumn, True, 2, 0, fleet1)
                numberofships = numberofships + 1

        elif randomhorizontal == 0:
            
            randomrow = random.randint(0, 8)
            randomcolumn = random.randint(0, 9)
            if ok_to_place_ship_at(randomrow, randomcolumn, False, 2, fleet1) == True:
                place_ship_at(randomrow, randomcolumn, False, 2, 0, fleet1)
                numberofships = numberofships + 1
    
    while numberofships < 10:
        
        randomhorizontal = random.randint(0, 1)

        if randomhorizontal == 1:

            randomrow = random.randint(0, 9)
            randomcolumn = random.randint(0, 8)
            if ok_to_place_ship_at(randomrow, randomcolumn, True, 1, fleet1) == True:
                place_ship_at(randomrow, randomcolumn, True, 1, 0, fleet1)
                numberofships = numberofships + 1

        elif randomhorizontal == 0:
            
            randomrow = random.randint(0, 8)
            randomcolumn = random.randint(0, 9)
            if ok_to_place_ship_at(randomrow, randomcolumn, False, 1, fleet1) == True:
                place_ship_at(randomrow, randomcolumn, False, 1, 0, fleet1)
                numberofships = numberofships + 1
# (0row, 1column, 2horizontal, 3length, 4hits)
def check_if_hits(row, column, fleet):
    
    for i in fleet:
        
        shiplength = fleet[i][3]
        shiphorizontal = fleet[i][2]
        shiprow = fleet[i][0]
        shipcolumn = fleet[i][1]

        if shiphorizontal == True:
            if row != shiprow:
                return False
            elif ((shipcolumn <= column <= (shipcolumn + shiplength)):
                return True
        
        elif shiphorizontal == False:
            if column != shiprow:
                return False
            elif ((shiprow) <= row <= (shiprow + shiplength)):
                return True

def hit(row, column, fleet):
    

def are_unsunk_ships_left(fleet):

    # 0 means all ships are sunk
    allshipssunk = 0

    for i in fleet:
        if is_sunk(fleet[i]) == False:
            # Will add 1 if it finds an unsunk ship
            allshipssunk = allshipssunk + 1
    
    # It requires all ships to be sunk for allshipssunk to be 0
    if unsunkships == 0:
        return False 
    else:
        return True


            



def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and column to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
