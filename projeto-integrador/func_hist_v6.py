from leito_v6 import Leito
#data de entrada e saída de cada internação, o diagnóstico e o tratamento recebido.
class Historico():
    def __init__(self):
        self.historico = []
        
    def _historico(self, identificador):
        s = 1
        while True:
            nome = input('Nome: ')
            cpf = input('CPF: ')
            data_inicial = input('Data inicial de internação: ')
            data_final = input('Data final: ')
            descricao = input('Descrição da internação: ')
            diagnostico = input('Diagnostico da internação: ')
            tratamento = input('Descreva o tratamento recebido ')
            
            internacao = {
                'data_incial':data_inicial,
                'data_final':data_final,
                'descricao':descricao,
                'diagnostico':diagnostico,
                'tratamento':tratamento,
            }
            
            historico = {
                'nome':nome,
                'cpf':cpf,
                'internacoes':[internacao],
                'identificador':identificador,
            }
        
            self.historico.append(historico)
            break
        
    def _ver_internacoes(self, identificador: str):
        for hist in self.historico:
            if hist['identificador'] == identificador:
                for internacoes in hist['internacoes']:
                    for chave, valor in internacoes.items():
                        print('\n',chave,valor)
                        
    #Adiciona uma nova internação ao histórico, caso necessário
    def _adicionar_internacao(self,identificador):
        for hist in self.historico:
            if hist['identificador'] == identificador:
                data_inicial = input('Data inicial de internação: ')
                data_final = input('Data final: ')
                descricao = input('Descrição da internação: ')
                diagnostico = input('Diagnostico da internação: ')
                tratamento = input('Descreva o tratamento recebido ')
                internacao = {
                'data_incial':data_inicial,
                'data_final':data_final,
                'descricao':descricao,
                'diagnostico':diagnostico,
                'tratamento':tratamento,
                }   
                hist['internacoes'].append(internacao)
    
if __name__=='__main__':
    h = Historico()
    identificador = '1'
    h._historico(identificador=identificador)
    h._ver_internacoes(identificador=identificador)
    h._adicionar_internacao(identificador=identificador)
    h._ver_internacoes(identificador=identificador)