from datetime import date

class Leito():
    def __init__(self,identificador:str,data:date,manha:list,tarde:list,noite:list):
        self.identificador = identificador
        self.manha  = manha
        self.tarde = tarde
        self.noite = noite
        self.data = data
        self.DATA = date.today()
    
    def _leito(self):
        return self.identificador
    
    def ver_ocupacao(self):
        return self.identificador,self.manha,self.tarde,self.noite,self.data
    
    def agendar_manha(self):    
        data = self.DATA#input('DATA: ')
        nome = input('nome: ')
        
        if len(self.manha) > 0:
            for agenda in self.manha:
                if not data in agenda:
                    self.manha.append([data, nome])
        else:
            self.manha.append([data, nome])
            
        return None

    def agendar_tarde(self):
        data = self.DATA#input('DATA: ')
        nome = input('nome: ')
        
        if len(self.tarde ) > 0:
            for agenda in self.tarde:
                if not data in agenda:
                    self.tarde.append([data, nome])
        else:
            self.tarde.append([data, nome])
            
        return None
    
    def agendar_noite(self):
        data = self.DATA#input('DATA: ')
        nome = input('nome: ')
        
        if len(self.noite) > 0:
            for agenda in self.noite:
                if not data in agenda:
                    self.noite.append([data, nome])
        else:
            self.noite.append([data, nome])
        
        return None
    
    def agenda_da_manha(self):
        return self.manha
    
    def agenda_da_tarde(self):
        return self.tarde
    
    def agenda_da_noite(self):
        return self.noite


        
lista_de_leitos = []

#criando 199 leitos:
for criar_leito in range(1,200,1):
    leito = Leito(identificador=f'{criar_leito}',data = date.today(),manha=[],tarde=[],noite=[])
    lista_de_leitos.append(leito)


for ver_leitos in lista_de_leitos:
    if ver_leitos.identificador == '150':
        ver_leitos.agendar_tarde()
        
for ver_leitos in lista_de_leitos:
    print('\nMANHA:',ver_leitos.manha)
    print('TARDE:',ver_leitos.tarde)
    print('NOITE:',ver_leitos.noite,'\n')

#Teste de adicionamento de horário

                
        
        
