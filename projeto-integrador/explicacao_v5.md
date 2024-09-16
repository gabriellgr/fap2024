## Sistema de Gerenciamento de Leitos: Uma Explicação Detalhada

Este código Python implementa um sistema básico para gerenciar leitos em um ambiente hospitalar. Vamos analisá-lo passo a passo para que você possa entender como funciona e utilizá-lo com facilidade.

**1. Importações e Definição da Classe `Leito`**

```python
from datetime import date, timedelta

# Nome, data de nascimento, CPF, contato, endereço,

class Leito():
    def __init__(self):
        self.leitos = []
        self.data = date.today()
```

* **`from datetime import date, timedelta`**: Importa as funções `date` e `timedelta` do módulo `datetime` para trabalhar com datas.
* **`class Leito():`**: Define a classe `Leito` que encapsula a lógica do sistema de gerenciamento.
* **`__init__(self)`**: O construtor da classe. Inicializa a lista `self.leitos` (onde serão armazenados os dados dos leitos) e a variável `self.data` com a data atual.

**2. Criação de Novos Leitos (`_novo_leito`)**

```python
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
```

* **`_novo_leito(self, identificador:str)`**:  Método para criar um novo leito.
* **`identificador:str`**:  Parâmetro que define o identificador do leito (ex: "1", "2", etc.).
* **`leito = { ... }`**:  Cria um dicionário com as informações do leito:
    * **`'data_inicial'`:** Data de criação do leito (data atual).
    * **`'data_final'`:** Data em que o leito ficou livre (inicialmente `None`).
    * **`'nome'`, `'data_de_nascimento'`, `'cpf'`, `'contato'`, `'endereco'`:** Informações do paciente (inicialmente `None`).
    * **`'status'`:** Define se o leito está "livre" ou "ocupado".
    * **`'identificador'`:** O identificador único do leito.
* **`self.leitos.append(leito)`**: Adiciona o novo leito à lista `self.leitos`.
* **`except Exception as erro:`**:  Gerencia possíveis erros durante a criação do leito.

**3. Cadastrar Paciente (`cadastrar_paciente`)**

```python
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
```

* **`cadastrar_paciente(self)`**: Método para cadastrar um paciente em um leito livre.
* **`for leito in self.leitos:`**: Itera sobre todos os leitos na lista.
* **`if leito['status'] == 'livre':`**: Verifica se o leito está disponível.
* **`leito['nome'] = input('Nome: ') ...`**:  Coleta os dados do paciente via entrada do usuário.
* **`leito['status'] = 'ocupado'`**: Define o status do leito como ocupado.
* **`print(f'\nPaciente cadastrado no leito {leito['identificador']}')`**:  Informa o usuário que o paciente foi cadastrado.
* **`return`**: Sai do método após cadastrar o paciente.

**4. Consultar Consulta Finalizada (`_consulta_finalizada`)**

```python
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
```

* **`_consulta_finalizada(self, identificador)`**:  Método para registrar que uma consulta foi finalizada em um leito específico.
* **`identificador`:** Parâmetro com o identificador do leito.
* **`for leito in self.leitos:`**: Itera sobre todos os leitos.
* **`if leito['identificador'] == identificador and leito['status'] == 'ocupado':`**: Verifica se o leito corresponde ao identificador e se está ocupado.
* **`print(f'\nPaciente: {leito['nome']}') ...`**:  Exibe os dados do paciente.
* **`escolha = input('Esta consulta esta finalizada(s/n)? ')`**:  Solicita confirmação ao usuário se a consulta está finalizada.
* **`if escolha == 'n':`**: Se a resposta for "n", a operação é cancelada.
* **`if escolha == 's':`**: Se a resposta for "s", os dados do paciente são removidos do leito, e o status é definido como "livre".

**5. Verificar Leitos Livres e Ocupados (`_leitos_livres`, `_leitos_ocupados`)**

```python
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
```

* **`_leitos_livres(self)`**:  Método para exibir os leitos livres.
* **`_leitos_ocupados(self)`**: Método para exibir os leitos ocupados.
* **`for leito in self.leitos:`**:  Itera sobre todos os leitos.
* **`if leito['status'] == 'livre' / 'ocupado':`**:  Verifica se o status do leito corresponde ao tipo de leito que se deseja exibir.
* **`print(f'\nLeito {leito['identificador']} {leito['status']}')`**:  Exibe o identificador e o status do leito.

**6. Carregar Dados (`_carregar_dados`)**

```python
    # A fazer
    def _carregar_dados(self,leitos):
        #adicionar leitos após fechamento do programa
        for leito in leitos:
            self.leitos.append(leito)
        return    
```

* **`_carregar_dados(self,leitos)`**:  Método para carregar dados de leitos (ainda não implementado). 
* **`for leito in leitos:`**: Itera sobre os dados dos leitos a serem carregados.
* **`self.leitos.append(leito)`**: Adiciona os leitos carregados à lista de leitos. 

**7. Execução Principal (`if __name__=='__main__':`)**

```python
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
```

* **`if __name__=='__main__':`**: Bloco de código que é executado somente quando o script é executado diretamente (não como um módulo importado).
* **`leito = Leito()`**:  Cria um objeto da classe `Leito`.
* **`for i in range(1,10):`**: Cria 9 novos leitos com identificadores de 1 a 9.
* **`while True:`**: Loop infinito para interagir com o usuário.
* **`print('\n1. cadastrar paciente') ...`**:  Exibe um menu de opções.
* **`escolha = input('Digite: ')`**:  Coleta a escolha do usuário.
* **`if escolha == '1': ... elif escolha == '2': ...`**:  Executa a ação correspondente à escolha do usuário.
* **`elif escolha=='0':`**:  Sai do loop e finaliza o programa.

**Observações:**

* O código ainda não possui a implementação de salvamento de dados. Se o programa for fechado, todos os dados serão perdidos.
* A função `_carregar_dados` é uma sugestão para implementar o carregamento de dados de um arquivo ou outro local.
* O sistema pode ser expandido com outras funcionalidades como:
    * Gerenciar datas de internação e alta dos pacientes.
    * Permitir a visualização de informações detalhadas sobre cada paciente.
    * Adicionar mecanismos de segurança para acesso aos dados.

Espero que esta explicação detalhada tenha ajudado você a entender o funcionamento do sistema de gerenciamento de leitos! 
