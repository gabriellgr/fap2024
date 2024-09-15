### PI (FAP)

- class Leito: 
    - parâmetros:
    - **identificador:** Pode ser uma sequencia de numeros ou mesmo uma codificação para cada leito
    - **data:** Data atual no formato date (YYYY-MM-DD)
    - **manha:** Uma lista inicialmente vazia para posteriromente adicionar as informações necessárias
    - **tarde:** Uma lista inicialmente vazia para posteriromente adicionar as informações necessárias
    - **noite:** Uma lista inicialmente vazia para posteriromente adicionar as informações necessárias
 
```
from datetime import date

class Leito():
    def __init__(self,identificador:str,data:date,manha:list,tarde:list,noite:list):
        self.identificador = identificador
        self.manha  = manha
        self.tarde = tarde
        self.noite = noite
        self.data = data
        self.DATA = date.today()

```

- Adicionar uma pessoa para ocupar o leito
    - Se o comprimento da lista for maior que 0 siginifica que existe agendamento então é verificado se não há conflito.
    caso contrário a lista **self.tarde** recebe o primeiro item da lista, que também é uma lista.
    
```
def agendar_tarde(self):
        data = self.DATA#input('DATA: ')
        nome = input('nome: ')
        
        if len(self.tarde ) > 0:
            for agenda in self.tarde:
                if not data in agenda:
                    self.tarde.append([data, nome])
        else:
            self.tarde.append([data, nome])
```
- Todos os parâmetros:
    - retorna todos os parâmetros
```
 def ver_ocupacao(self):
        return self.identificador,self.manha,self.tarde,self.noite,self.data
```

- Criando uma lista de objetos tipo Leito():
    - O identificador de cada será uma sequência de numeros do tipo string

```
lista_de_leitos = []

#criando 199 leitos:
for criar_leito in range(1,200,1):
    leito = Leito(identificador=f'{criar_leito}',data = date.today(),manha=[],tarde=[],noite=[])
    lista_de_leitos.append(leito)

```
- Agendamento:
    - Buscando o leito com identificador 150 (número no formato string), e adicionado uma pessoa para usar no horário da tarde.

    ```
    for ver_leitos in lista_de_leitos:
        if ver_leitos.identificador == '150':
            ver_leitos.agendar_tarde()

    ```

 -  Varrendo horários todos os horários manhâ, tarde e noite:
```
for ver_leitos in lista_de_leitos:
    print('\nMANHA:',ver_leitos.manha)
    print('TARDE:',ver_leitos.tarde)
    print('NOITE:',ver_leitos.noite,'\n')

```
