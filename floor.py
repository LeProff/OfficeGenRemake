#!/usr/bin/python3

import random
from room import Room
from svglib import SVG


class Floor:

    def __init__(self, grid: list[list], config: dict) -> None:
        self.floor = grid
        self.rooms = []
        self.joined_rooms = []
        self.config = config

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
        dimentions = self.get_dimentions()
        for y in range(dimentions[1]):
            for x in range(dimentions[0]):
                if random.randint(0, 1) == 0:
                    if room.place_vertical(self, (x, y)):
                        self.rooms.append(room)
                        return True
                    elif room.place_horizontal(self, (x, y)):
                        self.rooms.append(room)
                        return True
                else:
                    if room.place_horizontal(self, (x, y)):
                        self.rooms.append(room)
                        return True
                    elif room.place_vertical(self, (x, y)):
                        self.rooms.append(room)
                        return True
        return False

    def fill_empty_space(self) -> None:
        '''
        Fills empty space on the floor
        '''
        pass

    def check_full(self) -> bool:
        '''
        Checks if the floor is full

        Returns:
            bool: If the floor is full
        '''
        dimentions = self.get_dimentions()
        for y in range(dimentions[1]):
            for x in range(dimentions[0]):
                if self.get_tile((x, y)) == 0:
                    return False
        
        return True

    def connect_rooms(self) -> None:
        '''
        Connects all rooms on the floor
        '''
        pass

    def find_connected_rooms(self, room: Room) -> list:
        '''
        Finds all connected rooms to an initial room

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
        dimentions = self.get_dimentions()
        for y in range(dimentions[1]):
            for x in range(dimentions[0]):
                special_id = -1
                if self.get_tile((x, y)) == 2:
                    special_id = 2
                elif self.get_tile((x, y)) == 4:
                    special_id = 4
                elif self.get_tile((x, y)) == 5:
                    special_id = 5

                if special_id != -1:
                    room = Room(-special_id, False, self.config)
                    room.special = True
                    room.special_id = special_id
                    room.add_point((x, y))
                    self.rooms.append(room)

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
        return ""

    def __str__(self) -> str:
        return ""