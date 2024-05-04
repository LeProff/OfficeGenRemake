#!/usr/bin/python3

from math import nan
from multiprocessing import Value

from room import Room
from svglib import SVG


class Floor:

    def __init__(self, grid: list[list], config: dict) -> None:
        self.floor = grid
        self.rooms = []
        self.joined_rooms = []

    def set_tile(self, point: tuple, value) -> bool:
        '''
        Sets a tile on the floor

        Args:
            point (tuple): Point to set (x, y)
            value: Value to set

        Returns:
            bool: If the tile was set
        '''
        # returns false if the x position is out of bounds
        if point[0] < 0 or point[0] >= len(self.floor[0]):
            return False
        
        # returns false if the y position is out of bounds
        if point[1] < 0 or point[1] >= len(self.floor):
            return False
        
        # sets the tile and returns true
        self.floor[point[1]][point[0]] = value
        return True

    def get_tile(self, point: tuple):
        '''
        Gets a tile on the floor

        Args:
            point (tuple): Point to get (x, y)

        Returns:
            value: Value of the tile
        '''
        # returns false if the x position is out of bounds
        if point[0] < 0 or point[0] >= len(self.floor[0]):
            return None
        
        # returns false if the y position is out of bounds
        if point[1] < 0 or point[1] >= len(self.floor):
            return None
        
        # sets the tile and returns true
        return self.floor[point[1]][point[0]]

    def get_dimentions(self) -> tuple:
        '''
        Gets the dimentions of the floor

        Returns:
            tuple: Tuple of the dimentions (width, height)
        '''
        return (len(self.floor[0]), len(self.floor))

    def place_room(self, room: Room) -> bool:
        '''
        Places a room on the floor

        Args:
            room (Room): Room to place

        Returns:
            bool: If the room was placed
        '''
        pass

    def fill_empty_space(self) -> None:
        '''
        Fills empty space on the floor
        '''
        pass

    def connect_rooms(self) -> None:
        '''
        Connects all rooms on the floor
        '''
        pass

    def find_connected_rooms(self, room: Room) -> list:
        '''
        Finds all connected rooms to a room

        Args:
            room (Room): Room to find connections to

        Returns:
            list: List of connected rooms
        '''
        pass

    def add_specialty_rooms(self) -> None:
        '''
        Adds specialty rooms to the floor
        '''
        pass

    def output(self, path: str) -> None:
        '''
        Outputs the floor to a file

        Args:
            path (str): Path to output to
        '''
        pass

    def draw_envelope(self, svg: SVG) -> None:
        '''
        Draws the envelope of the floor

        Args:
            svg (SVG): SVG to draw on
        '''
        pass

    def draw_rooms(self, svg: SVG) -> None:
        '''
        Draws the rooms on the floor

        Args:
            svg (SVG): SVG to draw on
        '''
        pass

    def draw_doors(self, svg: SVG, room: Room) -> None:
        '''
        Draws the doors on the floor

        Args:
            svg (SVG): SVG to draw on
            room (Room): Room to draw doors for
        '''
        pass

    def check_wall(self, point1: tuple, point2: tuple) -> bool:
        '''
        Checks if the wall is capable of having a door

        Args:
            point1 (tuple): First point
            point2 (tuple): Second point

        Returns:
            bool: If there is a wall
        '''
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass