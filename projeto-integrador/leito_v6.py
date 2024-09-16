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
        self.infos = []
        self.pacientes = []
        self.data = date.today()
    
    def _novo_leito(self, identificador:str):#permite diminuir ou aumentar quantidade 
        try:    
            leito = {
                'status':'livre',
                'identificador':identificador,
            }#pensando que há:
            paciente = {
                'nome':None,
                'cpf':None,
                'data_de_nascimento':None,
                'status_do_paciente':None,
                'identificador':identificador,
            }

            info_paciente ={
                'data_inicial':self.data,
                'data_final':None,
                'nome':None,
                'endereco':None,
                'contato':None,
                'historico_medico':None,
                'medicamentos_em_uso':[],
                'alergias':None,
                'identificador':identificador,#O mesmo para focar mais prático de manipular
            }
            #identicador
            documentacao = 'stand by'
            self.leitos.append(leito)
            self.pacientes.append(paciente)
            self.infos.append(info_paciente)
            
            return 
            
        except Exception as erro:
            print(f'Erro: {erro}')
    
    def cadastrar_paciente(self):
        if len(self.leitos) > 0:
            for leito in  self.leitos:
                if leito['status'] == 'livre':
                    leito['status'] = 'ocupado'
                    for paciente in self.pacientes:#Buscando o paciente com mesmo código de identificação
                        if paciente['identificador'] == leito['identificador']:
            
                            nome = input('Insira o nome: ').title()
                            
                            paciente['nome'] = nome
                            paciente['cpf'] = input('CPF: ')
                            paciente['data_de_nascimento'] = input('Insira a data de nascimento: ')
                            paciente['status'] = input('Status de saúde (estavel,instavel,critico): ')
                            
                            print('1.Informações completas')
                            print('2. cadastro rápido')
                            escolha = input('Cadastro rápido')
                            
                            for info in self.infos:#buscando as informações através do mesmo identificador 
                                    if info['identificador'] == paciente['identificador'] == leito['identificador']:
                                        
                                        
                                        if escolha =='1':
                                            info['nome'] = nome
                                            info['endereco'] = input('Endereço do paciente: ')
                                            info['contato'] = input('Contato: ')
                                            info['historico_medico'] = input('Histórico médico: '),
                
                                            medicamentos = int(input('Quantos medicamentos o paciente necessita? '))
                                            info['medicamentos_em_uso'] = [input(f'Digite o nome do medicamento {_}: ') for _ in range(medicamentos)] 
                                            
                                            alergias = input('O paciente apresenta alguma alergia (s/n)? ').lower()
                                            
                                            if alergias =='s':
                                                info['alergias'] = input('Insira quais alergias: ')
                                            elif alergias == 'n':
                                                info['alergias'] = 'Não possui nenhuma alergia'
                                                
                                        elif escolha =='2' :
                                            info['nome'] = nome
                                            info['endereco'] = input('Endereço do paciente: ')
                                            info['contato'] = input('Contato: ')
                                            
                                        print(f'Paciente: {nome}, Identificação: {info['identificador']}, leito: {leito['identificador']}')
                                        return
          
        return
    
    def _leitos_ocupados(self):
        existe = False
        for leito in self.leitos:
            if leito['status'] == 'ocupado':
                print(f'\nLeito {leito['identificador']} {leito['status']}')
                existe = True
        if not existe:
            print(f'\nNão existem pacientes ocupando leitos')
        return    
    
    
    def ver_paciente(self, identificador):
        for paciente in self.pacientes:
            if paciente['identificador'] == identificador:
                print(f'Paciente: {paciente['nome']}')
                print(f'CPF: {paciente['cpf']}')
                print(f'Data de nascimento: {paciente['data_de_nascimento']}')
                print(f'Status do paciente: {paciente['status_do_paciente']}')
                return   
        print('\nNão encontrado')
        return
    
    # A fazer
    def _carregar_dados(self,leitos):        
        for leito in leitos:
            self.leitos.append(leito)
        print('\nProcesso finalizado!')
        return   
#quando o programa é finaizado todos os dadossão resetados
if __name__=='__main__':
    #leitos
    leito = Leito()
    for i in range(1,10):
        leito._novo_leito(identificador=str(i))
        
    while True:
        print('\n1. cadastrar paciente')
        print('2. ver leitos ocupados')
        print('3. ver paciente')
        print('0. sair')
        escolha = input('Digite: ')
        
        if escolha == '1':
            leito.cadastrar_paciente()
        elif escolha == '2':
            leito._leitos_ocupados()
        elif escolha =='3':
            identificador = input('identificador: ')
            leito.ver_paciente(identificador=identificador)
        elif escolha=='0':
            break
    
print('\nPrograma encerrado')