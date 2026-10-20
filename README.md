# RMSYS

Aplicação desktop desenvolvida em Python com interface gráfica criada com [Flet](https://flet.dev/). O projeto tem como objetivo praticar uma arquitetura em camadas inspirada em MVC, com interfaces, factories e DAOs para separar a interface do usuário das regras da aplicação e do acesso a dados.

> **Status do projeto:** em desenvolvimento. O cadastro de usuários é o módulo mais desenvolvido. A tela de clientes está preparada visualmente, mas sua integração funcional ainda está em construção. O suporte a bancos diferentes também está em evolução.

## Funcionalidades

- Tela de autenticação com usuário e senha.
- Tela principal com menu de navegação.
- Cadastro de usuários com operações de inclusão, alteração, exclusão lógica, consulta e pesquisa, conforme as rotinas implementadas.
- Pesquisa e exibição de usuários em uma tabela.
- Separação entre View, Controller, Model, Entity e DAO.
- Uso de interfaces e factories para organizar a criação dos componentes.
- Camada de conexão preparada para SQLite e com implementação inicial para MySQL.

## Tecnologias

- **Python** — linguagem da aplicação.
- **Flet** — interface gráfica.
- **SQLite via ODBC** — banco utilizado como configuração padrão no arquivo `config.ini`.
- **pyodbc** — conexão ODBC com SQLite.
- **MySQL Connector/Python** — dependência prevista para a conexão MySQL.

## Arquitetura e estrutura

A estrutura principal do projeto é organizada da seguinte forma:

```text
RMSYS/
├── Controller/
│   ├── Factory/
│   ├── Interface/
│   └── ControllerUsuario.py
├── Enums/
│   └── Enums.py
├── Model/
│   ├── DAO/
│   │   ├── Factory/
│   │   ├── Interface/
│   │   ├── MySql/
│   │   └── Sqlite/
│   ├── Entity/
│   ├── Factory/
│   ├── Interface/
│   ├── ModelConexaoMySQL.py
│   ├── ModelConexaoSqlite.py
│   └── ModelUsuario.py
├── Utils/
├── View/
│   ├── Componentes/
│   ├── ViewAutenticacao.py
│   ├── ViewCliente.py
│   ├── ViewPrincipal.py
│   └── ViewUsuario.py
├── config.ini
└── Main.py
```

### Responsabilidade das camadas

- **View:** monta as telas e recebe as ações do usuário. `ViewCadastroBase` concentra comportamentos comuns às telas de cadastro.
- **Controller:** recebe as solicitações da View e coordena as operações por meio do Model.
- **Model:** concentra a lógica de aplicação e delega operações de persistência ao DAO.
- **Entity:** representa os dados do domínio, como a entidade `EntityUsuario`.
- **DAO:** encapsula as operações de acesso ao banco de dados.
- **Interfaces:** definem contratos para reduzir o acoplamento entre componentes.
- **Factory:** centraliza a criação de objetos, como conexão, DAO e Controller.
- **Utils:** reúne funções auxiliares usadas pelo sistema.

## Requisitos

- Windows (a configuração de banco de dados incluída utiliza um caminho local do Windows).
- Python compatível com a versão do Flet e das dependências utilizadas no projeto.
- Driver ODBC **SQLite3 ODBC Driver** instalado para a conexão SQLite.
- Um banco SQLite acessível no caminho definido em `config.ini`.

O projeto compactado contém uma pasta `.venv` e arquivos gerados pelo Python/IDE. Eles são específicos do ambiente de desenvolvimento e não devem ser necessários para instalar o projeto em outra máquina. Recomenda-se não versionar `.venv`, `__pycache__`, arquivos `.pyc` e configurações locais da IDE.

## Instalação e execução

### 1. Obtenha o código

Clone o repositório ou baixe o código-fonte e extraia os arquivos em uma pasta local.

### 2. Crie um ambiente virtual

No terminal, dentro da pasta do projeto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação do ambiente, você pode executar os comandos usando o interpretador diretamente, por exemplo `.\.venv\Scripts\python.exe`.

### 3. Instale as dependências

Instale os pacotes utilizados pelo projeto:

```powershell
python -m pip install --upgrade pip
python -m pip install flet pyodbc mysql-connector-python pandas
```

O código atual contém uma importação de `pandas` em um módulo DAO. Se essa importação for removida durante a limpeza do código, o pacote poderá deixar de ser necessário. Verifique também as versões compatíveis com seu ambiente.

### 4. Configure o banco de dados

Edite o arquivo `config.ini`. A configuração padrão é semelhante a esta:

```ini
[DATABASE]
TIPO=SQLITE

[SQLITE]
DATABASE=C:\Bancos\SQLite\RMSYSDB.db

[MYSQL]
HOST=localhost
PORT=3306
DATABASE=rmsys
USER=root
PASSWORD=altere_esta_senha

[POSTGRESQL]
HOST=localhost
PORT=5432
DATABASE=rmsys
USER=postgres
PASSWORD=altere_esta_senha
```

Ajuste o caminho do SQLite para um arquivo de banco existente e acessível na sua máquina. Confirme que o driver ODBC SQLite está instalado e que sua arquitetura (32 ou 64 bits) é compatível com a instalação do Python.

**Importante:** não mantenha senhas reais no repositório. Use valores locais e mantenha um arquivo de configuração com credenciais fora do controle de versão. O PostgreSQL aparece na configuração, mas o código analisado ainda não oferece suporte completo a esse banco. A implementação MySQL também está incompleta e deve ser tratada como experimental.

### 5. Execute a aplicação

Na raiz do projeto:

```powershell
python Main.py
```

A janela da aplicação deverá abrir na tela de autenticação. O acesso depende de existir no banco um usuário compatível com a estrutura esperada pelo sistema.

## Banco de dados

O projeto usa uma camada de conexão e DAOs separados por banco. A configuração selecionada é lida de `config.ini`.

| Banco | Situação observada no código |
|---|---|
| SQLite | Opção padrão; contém DAO para usuários e conexão via ODBC. |
| MySQL | Há classes de conexão e DAO, mas a implementação do DAO não está completa. |
| PostgreSQL | Há uma seção no arquivo de configuração e um valor no enum, mas não há implementação de conexão/DAO identificada na estrutura analisada. |

A criação automática das tabelas não está habilitada no fluxo principal: a chamada de preparação do SQLite em `Main.py` está comentada. Garanta que o banco e as tabelas necessários existam antes de executar a aplicação.

## Estado dos módulos

- **Autenticação:** tela implementada; utiliza o Controller de usuários.
- **Usuários:** tela de cadastro baseada no componente comum e operações delegadas ao Controller/Model/DAO.
- **Clientes:** a tela está esboçada, mas o menu informa que o módulo está em construção e não abre um fluxo funcional.
- **MySQL e PostgreSQL:** suporte incompleto; não considerar pronto para uso sem concluir e testar as implementações.

## Pontos de atenção para evolução

1. **Consultas parametrizadas:** substituir SQL montado por interpolação de strings por parâmetros preparados. Isso reduz o risco de SQL injection e evita problemas com aspas e caracteres especiais.
2. **Senhas:** armazenar hashes seguros de senha (por exemplo, Argon2id ou bcrypt), nunca senhas em texto puro. Revisar também a rotina de autenticação.
3. **Transações e recursos:** garantir que conexões e cursores sejam fechados com segurança mesmo quando ocorrer uma exceção.
4. **Tratamento de erros:** padronizar mensagens para o usuário e registrar detalhes técnicos em logs, sem expor informações sensíveis.
5. **Configuração e segredos:** retirar credenciais do arquivo versionado e disponibilizar um `config.example.ini` sem senhas reais.
6. **Testes:** adicionar testes para Controller, Model e DAO, incluindo autenticação, validação, inclusão, alteração, exclusão lógica e pesquisa.
7. **Dependências:** manter um `requirements.txt` com versões testadas e documentar a versão do Python utilizada.
8. **Higiene do repositório:** evitar versionar `.venv`, caches, arquivos compilados, arquivos de workspace da IDE e bancos com dados pessoais ou credenciais.

## Próximos passos sugeridos

- Concluir a implementação do cadastro de clientes.
- Completar e testar o DAO MySQL e implementar PostgreSQL somente se fizer parte do escopo.
- Criar ou documentar o script de criação/atualização do esquema do banco.
- Parametrizar todas as consultas SQL.
- Implementar armazenamento seguro de senhas.
- Adicionar testes automatizados e um arquivo `requirements.txt`.
- Adicionar `.gitignore` para arquivos locais e artefatos gerados.

## Contribuição

Sugestões e melhorias são bem-vindas. Para contribuir:

1. Crie um fork do repositório.
2. Crie uma branch para sua alteração.
3. Faça commits pequenos e descritivos.
4. Execute os testes disponíveis e valide a alteração localmente.
5. Abra um pull request descrevendo o problema e a solução.

## Licença

Nenhuma licença foi identificada nos arquivos analisados. Antes de redistribuir ou reutilizar o projeto, defina uma licença e inclua o arquivo `LICENSE`.
