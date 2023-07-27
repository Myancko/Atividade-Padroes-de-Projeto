import os

class SiteNameHandler ():
    
    def validate(self, name : str):
        if name[0:25] == "[SPOTIFY-DOWNLOADER.COM] " or name[0:25] == "[SPOTIFY DOWNLOADER.COM]": 
            return True
        
        return False
    
    def action(self, name): 
        old_name = name
        new_name = name[25:]
        return new_name