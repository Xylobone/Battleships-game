import pytest
import random
from battleships import *


def test_is_sunk1():
    ship = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(ship) == True    

def test_is_sunk2():
    ship = (1, 1, False, 4, {})
    assert is_sunk(ship) == False  

def test_is_sunk3():
    ship = (9, 5, True, 1, {(9, 5)})
    assert is_sunk(ship) == True  

def test_is_sunk4():
    ship = (5, 5, False, 2, {(6, 5)})
    assert is_sunk(ship) == False  

def test_is_sunk5():
    ship = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    assert is_sunk(ship) == True  

def test_ship_type1():
    ship = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert ship_type(ship) == "cruiser"

def test_ship_type2():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    assert ship_type(ship) == "battleship"

def test_ship_type3():
    ship = (1, 1, False, 1, {})
    assert ship_type(ship) == "submarine"

def test_ship_type4():
    ship = (5, 5, False, 2, {(6, 5)})
    assert ship_type(ship) == "destroyer"

def test_ship_type5():
    ship = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    assert ship_type(ship) == "battleship"

def test_is_open_sea1():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    fleet1 = [ship]
    result = is_open_sea(1, 2, fleet1)    
    assert result == False

def test_is_open_sea2():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    fleet1 = [ship]
    result = is_open_sea(8, 9, fleet1)    
    assert result == True

def test_is_open_sea3():
    ship = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    fleet1 = [ship]
    result = is_open_sea(4, 5, fleet1)    
    assert result == False

def test_is_open_sea4():
    ship = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    fleet1 = [ship]
    result = is_open_sea(4, 9, fleet1)    
    assert result == False

def test_is_open_sea5():
    ship = (5, 5, False, 2, {(6, 5)})
    fleet1 = [ship]
    result = is_open_sea(7, 8, fleet1)    
    assert result == True

def test_ok_to_place_ship_at1():
    ship = (3, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    assert ok_to_place_ship_at(1, 1, True, 1, fleet1) == True

def test_ok_to_place_ship_at2():
    ship = (3, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    assert ok_to_place_ship_at(3, 3, True, 1, fleet1) == False

def test_ok_to_place_ship_at3():
    ship = (3, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    assert ok_to_place_ship_at(3, 3, True, 1, fleet1) == False

def test_ok_to_place_ship_at4():
    ship = (3, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    ship3 = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    fleet1 = [ship, ship2, ship3]
    assert ok_to_place_ship_at(5, 4, True, 2, fleet1) == False

def test_ok_to_place_ship_at5():
    ship = (3, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    ship3 = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    fleet1 = [ship, ship2, ship3]
    assert ok_to_place_ship_at(7, 7, True, 3, fleet1) == False


def test_place_ship_at1():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    place_ship_at(1, 9, True, 2, fleet1)
    assert fleet1[2] == (1, 9, True, 2, {})

def test_place_ship_at2():
    fleet1 = []
    place_ship_at(8, 8, True, 2, fleet1)
    assert fleet1[0] == (8, 8, True, 2, {})
    
def test_place_ship_at3():
    ship = (3, 3, False, 4, {(2,3), (3,3), (4,3)})
    fleet1 = [ship, ship2, ship3]
    place_ship_at(5, 6, True, 3, fleet1)
    assert fleet1[0] == (5, 6, True, 3, {})


def test_place_ship_at4():
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2, ship3]
    place_ship_at(2, 3, True, 2, fleet1)
    assert fleet1[0] == (2, 3, True, 2, {})


def test_place_ship_at5():
    ship3 = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    fleet1 = [ship, ship2, ship3]
    place_ship_at(0, 0, False, 1, fleet1)
    assert fleet1[0] == (0, 0, False, 1, {})

def test_randomly_place_all_ships():
    # Printing fleet and length of fleet to check the contents of the fleet during testing
    randomly_place_all_ships()
    print(fleet1)
    print(len(fleet1))
    assert len(fleet1) == 10

def test_check_if_hits1():
    #(row, column, fleet)
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(7,7), (8,7)})
    ship3 = (1, 1, True, 1)
    fleet1 = [ship, ship2, ship3]
    check_if_hits(1,1, fleet1)
    assert check_if_hits(1, 1, fleet1) == True

def test_hit1():
    #(row, column, fleet)
    ship = (2, 3, False, 4, {(3,3)})
    fleet1 = [ship]
    shiphit = hit(2, 3, fleet1)
    assert shiphit == (fleet1, (2, 3, False, 4, {(2,3), (3,3)}))

def test_hit2():
    #(row, column, fleet)
    ship = (2, 3, False, 4, {})
    fleet1 = [ship]
    shiphit = hit(2, 3, fleet1)
    assert shiphit == (fleet1, (2, 3, False, 4, {(2,3)}))

def test_hit3():
    #(row, column, fleet)
    ship = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})
    fleet1 = [ship]
    shiphit = hit(4, 8, fleet1)
    assert shiphit == (fleet1, (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)}))

def test_hit4():
    #(row, column, fleet)
    ship = (4, 6, True, 4, {(4, 6), (4, 7), (4, 8)})
    fleet1 = [ship]
    shiphit = hit(4, 9, fleet1)
    assert shiphit == (fleet1, (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})

def test_hit5():
    #(row, column, fleet)
    ship = (4, 6, True, 4, {(4, 6)})
    fleet1 = [ship]
    shiphit = hit(4, 7, fleet1)
    assert shiphit == (fleet1, (4, 6, True, 4, {(4, 6), (4, 7), (4, 8), (4, 9)})

    
def test_are_unsunk_ships_left1():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6, 7), (7, 7)})
    ship3 = (9, 9, True, 1, {(9, 9)})
    fleet1 = [ship, ship2]
    assert are_unsunk_ships_left(fleet1) == True