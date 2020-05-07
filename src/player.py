# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name: str, current_room:Room, items:[] = []):
        self.name = name
        self.current_room = current_room
        self.items = []
    def __str__(self):
        return f'{self.name} is at {self.current_room}'



        