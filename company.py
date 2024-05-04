#!/usr/bin/python3

import random
import os

class Company:
    '''Company class for storing company information'''

    def __init__(self, config: dict) -> None:
        '''
        Constructor for Company
        
        Args:
            config (dict): Program configuration
        '''
        self.config = config
        self.name: str = ''
        self.description: str = ''
        self.departments: list = []
        self.deparment_ratios: dict = {}

    def load_data(self):
        '''
        Loads the company data from the data source

        Raises:
            ValueError: If the data source is invalid
        '''
        data_source = self.config['dataSource']

        # Added and if statement here if any more data sources want to be added. Ex: database, API, etc.
        if data_source == 'file':
            try:
                file = open('data/compantlist.txt', 'r')
                line = random.choice(file.readlines())
                parts = line.split(':')
                file.close()

                self.name = parts[0]
                self.description = parts[1]
                for i in range(2, len(parts)):
                    temp = parts[i].split(',')
                    self.departments.append(temp[0])
                    self.deparment_ratios.update({i - 2: float(temp[1])})

                self.departments.append('president')
                self.departments.append('meeting room')
            except FileNotFoundError:
                raise FileNotFoundError('Company data source file not found')
        else:
            raise ValueError('Invalid company data source')
        
    def load_envelope(self) -> str:
        '''
        Loads a random envelope for the company

        Returns:
            list[list[str]]: 2D list of envelope data
        '''
        envelopes = os.listdir('data/envelopes')
        if len(envelopes) == 0:
            raise FileNotFoundError('No envelopes found')
        
        envelope = random.choice(envelopes)
        return envelope
    
    def pick_floor_layout(self, envelope: str) -> list[list[int]]:
        layouts: list[str] = os.listdir(f'data/envelopes/{envelope}')
        if len(layouts) == 0:
            raise FileNotFoundError(f'No floor layouts found in envelope {envelope}')
        
        layout = random.choice(layouts)
        temp = open(f'data/envelopes/{envelope}/{layout}', 'r')
        
        width = int(temp.readline())
        height = int(temp.readline())
        grid =[[0 for x in range(width)] for y in range(height)]
        for i in range(height):
            line = temp.readline()
            for j in range(width):
                grid[i][j] = int(line[j])

        return grid
    
    def generate_floors(self):
        '''
        Generates all the floors for the company
        '''
        departments: list = []
        executives: list = []

        # Generate all the rooms that need to be placed.
        size = random.randint(self.config['minFloors'], self.config['maxFloors'])
        for i in range(len(self.departments) - 2):
            pass
        
    def __repr__(self) -> str:
        return f'Company({self.name}, {self.description})'
    