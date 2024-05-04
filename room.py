#!/usr/bin/python3

from floor import Floor


class Room:

    def __init__(self, department: int, executive: bool, config: dict) -> None:
        self.points: list[tuple] = []
        self.corners: list[tuple] = []
        self.floor = None
        self.people = 1
        self.department = department
        self.executive = executive
        self.special = False
        self.special_id = 0
        self.config = config

    def add_point(self, point: tuple) -> None:
        '''
        Adds a point to the room

        Args:
            points (tuple): Point to add
        '''
        self.points.append(point)

    def get_dimentions(self) -> tuple:
        '''
        Gets the dimentions of the room

        Returns:
            tuple: Tuple of the dimentions
        '''
        pass

    def check(self, point: tuple, size: tuple) -> bool:
        '''
        Checks if the room can fit the object

        Args:
            point (tuple): Point to check
            size (tuple): Size of the object

        Returns:
            bool: If the room can fit
        '''
        pass

    def place_vertical(self, floor: Floor, point: tuple) -> bool:
        '''
        Places the room vertically

        Args:
            floor (Floor): Floor to place
            point (tuple): Point to place

        Returns:
            bool: If the room was placed
        '''

        # put check here and return false if it fails
        pass

    def place_horizontal(self, floor: Floor, point: tuple) -> bool:
        '''
        Places the room horizontally

        Args:
            floor (Floor): Floor to place
            point (tuple): Point to place

        Returns:
            bool: If the room was placed
        '''

        # put check here and return false if it fails
        pass

    def fill_up(self, floor: Floor, point: tuple) -> None:
        '''
        Fills up the room

        Args:
            floor (Floor): Floor to fill
            point (tuple): Point to fill
        '''
        pass

    def fill_down(self, floor: Floor, point: tuple) -> None:
        '''
        Fills down the room

        Args:
            floor (Floor): Floor to fill
            point (tuple): Point to fill
        '''
        pass

    def fill_left(self, floor: Floor, point: tuple) -> None:
        '''
        Fills left the room

        Args:
            floor (Floor): Floor to fill
            point (tuple): Point to fill
        '''
        pass

    def fill_right(self, floor: Floor, point: tuple) -> None:
        '''
        Fills right the room

        Args:
            floor (Floor): Floor to fill
            point (tuple): Point to fill
        '''
        pass

    def get_corners(self) -> list[tuple]:
        '''
        Gets the corners of the room

        Returns:
            list[tuple]: List of the corners
        '''
        pass

    def check_if_corner(self, point: tuple) -> str:
        '''
        Checks if the point is a corner

        t = top
        b = bottom
        l = left
        r = right

        Args:
            point (tuple): Point to check

        Returns:
            str: Corner type
        '''
        pass

    def get_top_left_corner(self) -> tuple:
        '''
        Gets the top left corner

        Returns:
            tuple: Top left corner
        '''
        pass