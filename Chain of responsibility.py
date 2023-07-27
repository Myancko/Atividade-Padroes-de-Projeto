import os
from Validadores import  LowerCaseHandler, SpaceHandler, SiteNameHandler


class Validacao:
    
    def __init__(self):
        
        self.chain = [
            SiteNameHandler(),
            SpaceHandler(),
            LowerCaseHandler(),
        ]
        self.request_status = ''
        
    def change_name (self, folder_path):
        
        for handler in self.chain:

            for song in os.listdir(folder_path):

                if handler.validate(song): 
                    os.rename( folder_path+song, folder_path+handler.action(song))
                    self.request_status = True
            
            """ if self.request_status == True:
                
                return print('As Musicas foram processadas') """
            
        if self.request_status == True:
            
            return print('As Musicas foram processadas')
        
        return print('Nem um dos Validadores foram capazes de realizar o processo')

                
renomear_musicas = Validacao()
renomear_musicas.change_name('./spotfy_playlist/')