from game.casting.actor import Actor
import random

speed = 10


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        #this one is not so useful
        self._message = ""
        #this one is what allows you to do scores (in tandem with actor.py)
        self._identity = ""
        
        self.frame_counter = 0
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def set_identity(self, x):
        """specifies the identity of the artifact as either a rock or a gem:
        x = 0 is rocks
        x = 1 is gems
        (Can be modified from actor.py)
        
        """
        self._identity = x

    def get_identity(self):
        """Get's the artifact's identity
        Returns:
            string: selected number for identification
        
        """
        return self._identity

    def drop(self):
        self._position._y += speed

    def reset(self):
        y = random.randint(1, 5 - 1)
        ypos = y * 30
        self._position._y = int(0 - ypos)
        x = random.randint(1, 60 - 1)
        pos = x
        pos = x * 30
        self._position._x = pos