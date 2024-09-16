from datetime import date, timedelta

# Nome, data de nascimento, CPF, contato, endereço,

class Leito():
    def __init__(self):
        self.leitos = []
        self.data = date.today()
        
    def _novo_leito(self, identificador:str):#permite diminuir ou aumentar quantidade
        try:    
            leito = {
                'data_inicial':self.data,
                'data_final':None,
                'nome':None,
                'data_de_nascimento':None,
                'cpf':None,
                'contato':None,#SMS?
                'endereco':None,
                'status':'livre',
                'identificador':identificador,
            }
            self.leitos.append(leito)
            
        except Exception as erro:
            print(f'Erro: {erro}')
    
    def cadastrar_paciente(self):
        for leito in  self.leitos:
            if leito['status'] == 'livre':
                leito['nome'] = input('Nome: ')
                leito['data_de_nascimento'] = input('Insira a data de nascimento: ')
                leito['cpf'] = input('CPF: ')
                leito['contato'] = input('Contato: ')
                leito['endereco'] = input('endereco: ')
                leito['status'] = 'ocupado'
                print(f'\nPaciente cadastrado no leito {leito['identificador']}')
                return
        return
            
    def _consulta_finalizada(self, identificador):
        for leito in self.leitos:
            if leito['identificador'] == identificador and leito['status'] == 'ocupado':
                print(f'\nPaciente: {leito['nome']}')
                print(f'CPF: {leito['cpf']}')
                escolha = input('Esta consulta esta finalizada(s/n)? ')
                if escolha == 'n':
                    print('\nOperação Cancelada')
                    return 
        
                if escolha == 's':
                    leito['nome'] = None,
                    leito['data_de_nascimento'] = None
                    leito['cpf'] = None
                    leito['contato'] = None
                    leito['endereco'] = None
                    leito['status'] = 'livre'
                    print(f'\nLeito {leito['identficador']} livre!')
                    return
        return
                
    def _leitos_livres(self):
        for leito in self.leitos:
            if leito['status'] == 'livre':
                print(f'\nLeito {leito['identificador']} {leito['status']}')
                return
        print('\nNão existem leitos diponiveis')
        return    
    
    def _leitos_ocupados(self):
        for leito in self.leitos:
            if leito['status'] == 'ocupado':
                print(f'\nLeito {leito['identificador']} {leito['status']}')
    
        return    
    # A fazer
    def _carregar_dados(self,leitos):
        #adicionar leitos após fechamento do programa
        for leito in leitos:
            self.leitos.append(leito)
        return    
    
#quando o programa é finaizado todos os dadossão resetados
if __name__=='__main__':
    #leitos
    leito = Leito()
    for i in range(1,10):
        leito._novo_leito(identificador=str(i))
        
    while True:
        print('\n1. cadastrar paciente')
        print('2. Consulta finalizada')
        print('3.Ver leitos diponiveis')
        print('4. ver leitos ocupados')
        print('0. sair')
        escolha = input('Digite: ')
        
        if escolha == '1':
            leito.cadastrar_paciente()
        elif escolha == '2':
            identificador = input('\nInsira o identificador: ')
            leito._consulta_finalizada(identificador=identificador)
        elif escolha == '3':
            leito._leitos_livres()
        elif escolha == '4':
            leito._leitos_ocupados()
        elif escolha=='0':
            break
            