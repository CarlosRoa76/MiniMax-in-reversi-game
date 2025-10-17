class Token:
    
    COLORS = ('B', 'W')
    def __init__(self, color):
        if color not in self.COLORS:
            raise ValueError(f"Invalid color {color}. Valid colors are B and W.")
        
        self.color = color
        
    def flip(self):
        self.color = 'W' if self.color == 'B' else 'B'

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.__str__()



class StackToken:
    def __init__(self, color):
        self.color = color
        self.tokens = [Token(color) for _ in range(32)]
        
    def pop(self):
        if not self.is_empty():
            return self.tokens.pop()
        else:
            return None

    def is_empty(self):
        return len(self.tokens) == 0
    
    def size(self):
        return len(self.tokens)
    
    def __str__(self):
        return f"Color: {self.color}, Tokens: {len(self.tokens)}"
    
    def __repr__(self):
        return f"StackToken(color={self.color}, size={len(self.tokens)})"
    
      
if __name__ == "__main__":
    t = Token('B')
    print(t.color)  # Output: B
    
    t.flip()
    print(t.color)  # Output: W

    t.flip()
    print(t.color)  # Output: B

    t.flip()
    print(t.color)  # Output: W
    
