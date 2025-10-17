from abc import ABC, abstractmethod

class Player(ABC):
    
    TYPE_ = None
    
    def __init__(self, name):
        self.name = name
        self._token_color = None
        self._tokens = None
        
    @abstractmethod
    def play(self):
        pass
    
    @property
    def token_color(self):
        return self._token_color    
    
    @property
    def tokens(self):
        return self._tokens
    
    @tokens.setter
    def tokens(self, tokens):
        self._tokens = tokens
        self._token_color = tokens.color