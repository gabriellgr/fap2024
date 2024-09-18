from leito_v6 import Leito
from datetime import date


class Agendar():
    def __init__(self) -> None:
        pass
    
    def agendar(self, identificador:str, lista_de_leitos: Leito):
        
        if lista_de_leitos:
            for leito in lista_de_leitos:
                if leito['status'] == 'livre':
                    leito['status'] = 'agendado'
                    print('\nAgendado!')
                    
                    return
            print('\nSem leitos diponíveis')
            return
        else:
            print('\nNão existe')    