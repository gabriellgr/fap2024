# Sistema de Gestão de Leitos Hospitalares

Este código Python implementa um sistema básico para gerenciar leitos em um hospital. Ele permite:

* **Criar leitos:** Define um número inicial de leitos com identificadores numéricos.
* **Registrar pacientes:** Cadastra pacientes com informações como nome, CPF, data de nascimento, status, medicamentos em uso, alergias e informações de contato.
* **Agendar consultas:** Permite agendar consultas em diferentes horários (manhã, tarde, noite) em leitos específicos.
* **Gerenciar status de leitos:** Mostra quais leitos estão ocupados e livres, com detalhes sobre os horários e datas agendadas.
* **Visualizar informações:** Exibe informações sobre pacientes e seus respectivos leitos.


## Classes e Funções

### Classe `Leito`

* **`__init__()`:**
    * Inicializa uma lista de leitos (`self.leitos`), uma lista de informações sobre pacientes (`self.informacoes`), uma lista de pacientes (`self.pacientes`) e a data atual (`self.data`).

* **`_novo_leito(self, identificador:str)`:**
    * Cria um novo leito com o identificador fornecido.
    * Inicializa o status do leito como "livre" para os horários da manhã, tarde e noite.
    * Define as datas inicial e final como `None`.
    * Adiciona o novo leito à lista `self.leitos`.

* **`_novo_paciente(self)`:**
    * Solicita ao usuário o identificador do leito, nome, CPF, data de nascimento e status do paciente.
    * Verifica se o identificador do leito é válido (se existe).
    * Cria um dicionário `paciente` com as informações do paciente e o identificador do leito.
    * Cria um dicionário `identificacao_do_paciente` para armazenar nome e CPF.
    * Coleta informações sobre medicamentos em uso e alergias do paciente.
    * Cria um dicionário `info_paciente` com informações adicionais, incluindo a data inicial da internação, endereço, contato, medicamentos e alergias.
    * Adiciona os dicionários `paciente` e `info_paciente` às listas `self.pacientes` e `self.informacoes`, respectivamente.
    * Permite agendar a consulta em diferentes horários (manhã, tarde, noite) ou agendar uma cirurgia.

* **`ver_pacientes(self)`:**
    * Exibe os nomes dos pacientes e os identificadores dos seus leitos.

* **`ver_paciente(self, identificador)`:**
    * Busca um paciente pelo identificador do leito e exibe suas informações.

* **`ver_info(self, identificador)`:**
    * Exibe informações adicionais sobre o paciente com o identificador fornecido.

* **`_consulta_agendada(self)`:**
    * Retorna o identificador do leito que está livre para todos os horários (manhã, tarde e noite).

* **`_consulta_manha(self)`:**
    * Retorna o identificador do leito que está livre para o horário da manhã.

* **`_consulta_tarde(self)`:**
    * Retorna o identificador do leito que está livre para o horário da tarde.

* **`_consulta_noite(self)`:**
    * Retorna o identificador do leito que está livre para o horário da noite.

* **`ver_leitos_livres(self)`:**
    * Exibe o status dos leitos (livre ou ocupado) e as datas agendadas.

* **`agendar_horario(self, horario:str, identificador)`:**
    * Agenda uma consulta no horário especificado em um leito com o identificador fornecido.

* **`leitos_para_agendar(self)`:**
    * Retorna o identificador do primeiro leito encontrado que está livre para todos os horários.

* **`datas_agendadas(self)`:**
    * Exibe as datas agendadas para cada leito.

* **`agendar_cirurgia(self)`:**
    * Agenda uma cirurgia em um leito disponível, ocupando todos os horários (manhã, tarde, noite).

* **`_ver_leitos_ocupados(self)`:**
    * Exibe os leitos ocupados com seus horários e datas agendadas.


## Execução do Programa

* O código inicializa 20 leitos com identificadores numéricos.
* O programa apresenta um menu com opções:
    * **Novo paciente:** Cadastra um novo paciente.
    * **Ver leitos agendados:** Exibe os leitos ocupados.
    * **Ver leitos diponiveis:** Exibe os leitos livres.
    * **Ver pacientes:** Exibe todos os pacientes cadastrados.
    * **Ver paciente:** Exibe informações de um paciente específico.
    * **Informações do paciente:** Exibe informações adicionais sobre um paciente específico.
    * **Sair:** Encerra o programa.

## Observações

* O código utiliza dicionários para armazenar informações sobre leitos e pacientes.
* As datas são armazenadas como objetos `date` do módulo `datetime`.
* A funcionalidade de anexar documentação médica ainda está em desenvolvimento.
* O programa é simples e pode ser expandido com funcionalidades adicionais, como:
    * Gerar relatórios.
    * Implementar uma interface gráfica.
    * Integrar com um banco de dados.
