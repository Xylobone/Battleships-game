import pytest
from battleships import *

def test_is_sunk1():
    ship = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(ship) == True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    ship = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert ship_type(ship) == "cruiser"

def test_ship_type2():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    assert ship_type(ship) == "battleship"
    #add at least one test for ship_type by the deadline of session 7 assignment
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    fleet1 = [ship]
    result = is_open_sea(1, 2, fleet1)
    assert result == True
    #add at least one test for open_sea by the deadline of session 7 assignment
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():
    #(row, column, horizontal, length, fleet)
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    result = ok_to_place_ship_at(3, 5, True, 3, fleet1)
    assert result == True
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    #(row, column, horizontal, length, fleet)
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    assert len(place_ship_at(1, 9, True, 2, fleet1)) == 3
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    #(row, column, fleet)
    fleet1 = [ship, ship2]
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    check_if_hits(6,7, fleet1)
    assert check_if_hits(6,7, fleet1)== True
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    #(row, column, fleet)
    ship = (2, 3, False, 4, {(2,3), (3,3)})
    fleet1 = [ship]
    shiphit = hit(4, 3, fleet1)
    assert shiphit == (ship, fleet1)
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    ship = (2, 3, False, 4, {(2,3), (3,3), (4,3)})
    ship2 = (6, 7, False, 3, {(6,6), (6,5)})
    fleet1 = [ship, ship2]
    assert are_unsunk_ships_left == True
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline