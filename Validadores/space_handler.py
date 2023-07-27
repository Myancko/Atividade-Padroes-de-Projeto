import os

class SpaceHandler ():
    
    def validate(self, name: str):

        for char in name: 
            if char == '-' or char == '_':

                return True
            
        return False
    
    def action(self, name):
        
        new_name = ''
        first_letter = True
        more_than_one = False
        for char in name: 
            
            if first_letter and char == '-' or first_letter and char == '_':
                char = ''
                more_than_one = True
            
            elif more_than_one and char == '-' or more_than_one and char == '_':
                char = ''
                first_letter =  False
                
            elif char == '-' or char == '_':
                char = ' '
                more_than_one = False
                first_letter =  False
                
            else:
                more_than_one = False
                first_letter =  False
                
            new_name = new_name + char


        return(new_name)
    