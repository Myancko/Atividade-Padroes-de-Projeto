import os

class LowerCaseHandler ():
    
    def validate(self, name):
        
        space = True
        new_name = ''
        
        for char in name:
            
            if space and char == '(' or  char == '[' or char == '{' or char == '-' or char == '_':
                continue
            
            elif space and char.islower():
               return True
            
            elif char == ' ':
                space = True
             
        return False
    
    def action(self, name): 
        
        space = True
        new_name = ''
        for char in name:
            
            if space and char == '(' or char == '[' or char == '{' or char == '-' or char == '_':
                new_name += char
                continue
            
            elif space and char.islower():
                new_name += char.upper()
                space = False
                continue
            
            elif char == ' ':
                new_name += char
                space = True
                continue
            
            space = False
            new_name += char
                
        return new_name