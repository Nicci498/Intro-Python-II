# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

        # def next_room(self, cmd):
        #     if hasattr(self, f'{cmd}_to'):
        #         return getattr(self, f'{cmd}_to')
        #     else: 
        #         return f"You wanted to go {cmd}, but the footing that way is treacherous. Turn back now."

 