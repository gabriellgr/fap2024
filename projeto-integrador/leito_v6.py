from datetime import date, timedelta

# Nome, data de nascimento, CPF, contato, endereço,
'''**1. Cadastro de Pacientes**
- Informações Básicas: Nome, data de nascimento, CPF, contato, endereço, informações de emergência.
Histórico Médico: Doenças pré-existentes, medicamentos em uso, alergias.
Documentação: Anexar exames, laudos ou documentos médicos importantes.
Status do Paciente: Internado, em observação, em consulta, alta.
'''

class Leito():
    def __init__(self):
        self.leitos = []
        self.informacoes = []
        self.pacientes = []
        self.data = date.today()
       
    def _novo_leito(self, identificador:str):#permite diminuir ou aumentar quantidade 
        try:    
            leito = {
                'identificador':identificador,
                'manha':'livre',
                'tarde':'livre',
                'noite':'livre',  
                'data_inicial':None,
                'data_final':None,
            }#pensando que há:
            
            documentacao = 'stand by'#Em desenvolviemnto ...
            self.leitos.append(leito)
            
            
            return 
            
        except Exception as erro:
            print(f'Erro capturado: {erro}')
    
    
    '''
    Faz um "cadastro de paciente, viculando ele à um leito", é necessario fornecer
    o parâmetro identificador que corresponde ao leito que este paciente vai usar
    '''
    def _novo_paciente(self):
        
         #vendo se o numero/identificador corresponde a um leito
        identificador = input('Insira o numero do leito : ')
        lista_de_verificação= [str(leito['identificador']) for leito in self.leitos]
        
        if identificador not in lista_de_verificação:
            print(f'\nNão existe leito com identificador {identificador}, operação cancelada, tente novamente')
            return
        
        paciente = {
                'leito':identificador,#Insirir identificador do leito
                'nome':input('Nome: '),
                'cpf':input('CPF: '),
                'data_de_nascimento':input('Data de nascimento: '),
                'status_do_paciente':input('Status do paciente (estavel, instavel, critico): '),
            }

        identificacao_do_paciente = {#Um dicionario com a identificacao
            'nome':paciente['nome'],
            'cpf':paciente['cpf'],
        }
        
        medicamentos = []
        
        med = [medicamentos.append(input(f'\nInsira o nome de cada medicamento, um de cada vez {_}: ')) for _ in range(1,int(input('Quantos medicamentos são necessários?: '))+1)]
        alergias = input('\nEscreva aqui todas as alergias, caso existam: ')
        
        info_paciente ={#Aqui  sobre
            'data_inicial':self.data,#data a qual comecou a internação
            'data_final':None,#data a qual saiu da internação
            'endereco':input('Endereco: '),
            'contato':input('Numero de telefone: '),
            'medicamentos_em_uso':medicamentos,
            'alergias': alergias,
            'identificacao':identificacao_do_paciente,# A trabalhar ...
            }    

        #funcao para agendar ou entrar logo
        self.pacientes.append(paciente)
        self.informacoes.append(info_paciente)
        
        print('1.Agendar cirurgia')
        print('2.marcar para manhã')
        print('3.marcar para tarde')
        print('4.marcar para noite')
        consulta = input('Digite: ')
        if consulta == '1':
            self.agendar_cirurgia()
        if consulta == '2':
            self.agendar_horario('manha', identificador=identificador)
        if consulta == '3':
            self.agendar_horario('tarde', identificador=identificador)
        if consulta == '4':
            self.agendar_horario('noite', identificador=identificador)

        
    def ver_pacientes(self):
        if self.pacientes:
            for paciente in self.pacientes:
                for leito in self.leitos:
                    if leito['identificador'] == paciente['leito']:
                        print(f'Paciente: {paciente["nome"]}, no leito: {leito['identificador']}')
        else:
            print('\nNão existem pacientes, por enquanto')
            
        return
    
    
    #informações dos pacientes
    def ver_paciente(self, identificador):
        if self.pacientes:
            for paciente in self.pacientes:
                for leito in self.leitos:
                    if leito['identificador'] == paciente['leito'] == identificador:
                        print(f'Paciente: {paciente["nome"]}, no leito: {leito['identificador']}')
                        print(f'CPF: {paciente['cpf']}, data de nascimento: {paciente['data_de_nascimento']}, status: {paciente['status_do_paciente'], }')
                        return
                    
        else:
            print('\nNão existem pacientes, por enquanto')   
        return
    
    def ver_info(self, identificador):
        for info in self.informacoes:
            for paciente in self.pacientes:
                if info['identificacao'] == {'nome':paciente['nome'], 'cpf':paciente['cpf']}:
                    for chave, valor in info.items():
                        print(chave, valor)
                        
        print('Não encontrado ou não existente')    
        return
    
    #Um dia todo
    def _consulta_agendada(self):
        for leito in self.leitos:
            if leito['manha'] == 'livre' and leito['tarde'] == 'livre' and leito['noite'] == 'livre':
                print(f'o Leito {leito["identificador"]} está diponível.')
                return leito['identificador']
            
    def _consulta_manha(self):
        for leito in self.leitos:
            if leito['manha'] == 'livre':
                print(f'o Leito {leito["identificador"]} está diponível para o horário da manhã.')
                return leito['identificador']
            
    def _consulta_tarde(self):
        for leito in self.leitos:
            if leito['tarde'] == 'livre':
                print(f'o Leito {leito["identificador"]} está diponível para o horário da tarde.')
                return leito['identificador']
            
    def _consulta_noite(self):
        for leito in self.leitos:
            if leito['tarde'] == 'livre':
                print(f'o Leito {leito["identificador"]} está diponível para o horário da noite.')
                return leito['identificador']
        
    def ver_leitos_livres(self):
        existe = True
        for leito in self.leitos:
            if leito['manha'] == 'livre' or leito['tarde'] == 'livre' or leito['noite'] =='livre':
                print(f'Leito {leito['identificador']} está {leito['manha']} pela manhã')
                print(f'Leito {leito['identificador']} está {leito['tarde']} pela tarde')
                print(f'Leito {leito['identificador']} está {leito['noite']} pela noite')
                existe = False
            elif leito['manha'] == 'agendado' or leito['tarde'] == 'agendado' or leito['noite'] =='agendado':
                print(f'Leito {leito['identificador']} está {leito['manha']} pela manhã data: {leito['data_inicial']}')
                print(f'Leito {leito['identificador']} está {leito['tarde']} pela tarde data: {leito['data_inicial']}')
                print(f'Leito {leito['identificador']} está {leito['noite']} pela noite data: {leito['data_inicial']}')
                existe = False
        if existe:
            print('\nTodos os leitos estão em uso no momento')
        return
    
    '''
    recebe como paramentro: "manha" ou "tarde" ou "noite"
    agenda cirurgias nos três horários
    identificador: É o número correspondente ao leito, que é mostrado no inicio
    com prints, da função: ver_leitos_livres()
    '''
    
    def agendar_horario(self, horario:str, identificador):
        data = ('Digite a data para agendar: ')
        
        if horario == 'manha':
            for leito in self.leitos:
                if leito['identificador'] == identificador and leito['manha'] == 'agendado' or leito['identificador'] == identificador and leito['tarde'] == 'livre':
                    leito['manha'] = 'agendado'
                    leito['data_inicial'] = data
                    print('\nTudo pronto!')
                    return
                
                elif leito['tarde'] == 'ocupado':
                    print(f'\nJá existe agendamento para esse leito neste horário')
                    return
                    
        elif horario == 'tarde':
            for leito in self.leitos:
                if leito['identificador'] == identificador and leito['tarde'] == 'agendado' or leito['identificador'] == identificador and leito['tarde'] == 'livre':
                    leito['tarde'] = 'agendado'
                    leito['data_inicial'] = data
                    print('\nTudo pronto!')
                    return
                
                elif leito['noite'] == 'ocupado':
                    print(f'\nJá existe agendamento para esse leito neste horário')
                    return
                
        if leito['identificador'] == identificador and leito['tarde'] == 'agendado' or leito['identificador'] == identificador and leito['tarde'] == 'livre':
            for leito in self.leitos:
                if leito['identificador'] == identificador and leito['noite'] == 'agendado' or leito['identificador'] == identificador and leito['noite'] == 'livre':
                    leito['noite'] ='agendado'
                    leito['data_inicial'] = data
                    print('\nTudo pronto!')
                    return
                elif leito['noite'] == 'ocupado':
                    print(f'\nJá existe agendamento para esse leito neste horário')
                    return
    #Procurando e retoronando um leito que esteja disponivel integralmente
    def leitos_para_agendar(self):
        for leito in self.leitos:
            if leito['manha'] == 'livre' and leito['tarde'] == 'livre' and leito['noite'] =='livre':
                return leito['identificador']
            
        print('\nTodos os leitos estão ocupados')
        return False
            
    #datas agendadas
    def datas_agendadas(self):
        for leito in self.leitos:
            if leito['manha'] =='agendado' or leito['tarde'] =='agendado' or leito['noite'] =='agendado':
                for chave,valor in leito:
                    print(chave,valor)
                    
        print('\nNão existe')
        return

    def agendar_cirurgia(self):
        print('Agendas marcadas:',self.datas_agendadas())
        data = input('Insira a data para agendar: ')
        for leito in self.leitos:
            if leito['data_inicial'] == None:#Ou seja, se não foi agendado nenhmua consulta neste leito
                leito['data_inicial'] = data
                leito['manha'] = 'agendado'
                leito['tarde'] = 'agendado'
                leito['noite'] = 'agendado'
                print(f'Agendado para data {data}')
                return
            
        print('\nNão existem leitos para agendar hoje')
        return
            
    def _ver_leitos_ocupados(self):
        existe = True
        for leito in self.leitos:
            if leito['data_inicial']:
                print(f'Leito: {leito['identificador']}, manhã:{leito['manha']}, tarde: {leito['tarde']}, noite:  {leito['noite']} ')
                existe = False
        if existe:
            print('\nNenhum leito em uso')   
        return
    
#quando o programa é finaizado todos os dadossão resetados
leito = Leito()
for l in range(1,20):
    leito._novo_leito(str(l))#o argumento é uma string
if __name__=='__main__':
    
    while True:
        print('\n1.Novo paciente')
        print('2.Ver leitos agendados')
        print('3.ver leitos diponiveis')
        print('4.ver pacientes')#ver todos os pacientes na lista de pacientes
        print('5.ver paciente')#paciente em especifico
        print('6.Informações do paciente')#informações adicionais 
        print('7.sair')
        
        escolha = input('Escolha: ')
        
        if escolha =='1':
            leito._novo_paciente()
        elif escolha =='2':
            leito._ver_leitos_ocupados()
        elif escolha=='3':
            leito.ver_leitos_livres()
        elif escolha =='4':
            leito.ver_pacientes()
        elif escolha =='5':
            leito.ver_paciente(input('Identificador: '))
        elif escolha =='6':
            leito.ver_info(input('identificador do paciente (numero...): '))
        elif escolha =='7':
            break