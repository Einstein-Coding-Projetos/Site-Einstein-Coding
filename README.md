# Site Einstein Coding 
Repositório destinado a elaboração do projeto do site institucional da entidade Einstein Coding, voltada para soluções de tecnologia e programação na área da saúde.

## Objetivo
Criar um site institucional funcional e responsivo para apresentar:
- A gestão atual e o hall da fama das gestões passadas;
- Nossos projetos e parcerias;
- Notícias, avisos e código social;
- Sobre nós;
- Contato;
- Área de login para membros e visitantes (a longo prazo).

---

## Estrutura do Projeto

```
EinsteinCoding-Site2025/
│
├── /frontend/                    
│   ├── /templates/             
│   │   ├── base.html
│   │   ├── home.html
│   │   └── gestao.html
│   └── /static/                  
│       ├── /css/
│       │   └── style.css
│       ├── /js/
│       │   └── script.js
│       └── /imgs/
│           ├── logo.png
│           └── equipe2025.jpg
│
├── /backend/                     
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   └── apps.py
│
├── /database/                    
│   └── migrations/               
│       └── __init__.py
│
├── manage.py                     
├── requirements.txt
└── README.md

```

---

## Equipe
**Scrum Master:** Maria Eduarda Taveiros Martins Costa

**Product Owner:** Henrique Machiaveli Martins

**Desenvolvedores:** Ana Beatriz Mamede Pampalon, Antonio Elias Faiçal Junior, Carolina Scilingo, Maria Vitória de Moura Coutinho e Bruna Sanches Paloni

---

## Mapa mental do Projeto

![Mapa mental do site Einstein Coding 2025](https://github.com/mariatmcosta/EinsteinCoding-Site2025/blob/main/frontend/static/imgs/miro.png?raw=true)


---

## Especificações Técnicas do Projeto: Site da Entidade Einstein Coding

```
Arquitetura:
  Modelo: "Cliente-Servidor em 3 camadas"
  Camadas:
    - Presentation (Frontend): "Interface com o usuário (HTML5, CSS3, JS ou NextJS futuramente)"
    - Application (Backend): "Camada de lógica e comunicação com o banco de dados (Django)"
    - Database: "Camada de armazenamento de dados (PostgreSQL)"
  Justificativa:
    A arquitetura de três camadas garante modularidade, segurança e
    escalabilidade, permitindo que novas funcionalidades sejam adicionadas
    sem reestruturar o sistema.

Frameworks:
  Frontend:
    Nome: "HTML5, CSS3 e JavaScript"
    Opcional_futuro: "NextJS"
    Motivo:
      Fornece uma base simples para o desenvolvimento inicial e permite
      migração futura para frameworks mais robustos, caso necessário.
  Backend:
    Nome: "Django (Python)"
    Motivo:
      Framework completo e seguro, com suporte nativo a banco de dados,
      autenticação e escalabilidade.
  Observação:
    O Django foi escolhido por sua robustez e facilidade de integração com o PostgreSQL.
    O Flask foi descartado devido à necessidade de montagem manual de componentes.

Banco_de_Dados:
  Tipo: "Relacional (SQL)"
  Nome: "PostgreSQL"
  Justificativa:
    Banco relacional maduro, compatível com Django, ideal para aprendizado
    e projetos escaláveis. Oferece integridade referencial e suporte a consultas complexas.
  Alternativas_Consideradas:
    - "MySQL"
    - "MongoDB (não relacional, descartado neste momento)"
  Status: "Escolhido e adotado para o desenvolvimento"

Ferramentas:
  Versionamento: "Git + GitHub (pull Requests, branches e commits controlados)"
  Documentação: "README.md e issues no GitHub"
  Gerenciamento_de_Projeto: "GitHub Projects / Scrum (Sprints organizadas)"
  Design_e_Planejamento: "Miro (mapas mentais, fluxos e wireframes) e Canva"
  Ambiente_de_Desenvolvimento: "Visual Studio Code"
  Controle_de_Dependências: "pip / virtualenv (Python)"
  Sistema_Operacional: "macOS e Windows (configurações padronizadas via requirements.txt)"

Levantamento_de_Requisitos:
  Funcionais:
    - "O sistema deve apresentar informações institucionais sobre o grupo Einstein Coding."
    - "O sistema deve permitir navegação entre páginas."
    - "O sistema deve possuir layout responsivo."
    - "O sistema deve permitir exibição de imagens e ícones da entidade."
    - "O sistema deve permitir atualização manual de conteúdos estáticos."
    - "O sistema deve permitir integração futura com módulo de login autenticado."
    - "O sistema deve permitir inclusão futura de páginas dinâmicas (projetos, artigos, eventos)."
    - "O sistema deve aceitar expansão para formulários de contato com coleta de dados de visitantes."

  Nao_Funcionais:
    - "O sistema deve ser desenvolvido em Django, garantindo modularidade e segurança."
    - "O banco de dados deve ser PostgreSQL, assegurando integridade e compatibilidade com o backend."
    - "O código deve seguir boas práticas de versionamento no GitHub, com commits e revisões via Pull Request."
    - "O sistema deve manter separação clara entre frontend, backend e banco de dados."
    - "O sistema deve apresentar desempenho estável e tempo de resposta adequado."

```


---

## Como rodar o projeto localmente

Seguindo boas práticas para projetos Django colaborativos (usando venv e requirements.txt):

Siga as instruções abaixo para configurar e executar o projeto no seu ambiente local.
1) Verificando instalação, no bash:
   ```
   python --version
   git --version
   pip --version
   ```
2) Clonar o repositório, no bash.
   Escolha uma pasta de trabalho e execute:
   ```
   git clone https://github.com/mariatmcosta/EinsteinCoding-Site2025.git
   cd EinsteinCoding-Site2025
   ```
3) Criar e ativar o ambiente virtual (isolado para o projeto):
   macOS/ Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
   Windows (PowerShell):
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   * Após ativar o ambiente virtual, você verá (venv) antes do seu usuário no         terminal.
4) Instalar as dependências com o ambiente virtual ativo:
   ```
   pip install -r requirements.txt
   ```
5) Configurar variáveis de ambiente (crie um arquivo .env na raiz do projeto para guardar informações sensíveis relacionadas com a conexão com o banco de dados após o banco estar conectado):
   ```
   SECRET_KEY=coloque_sua_chave_aqui
   DEBUG=True
   DATABASE_URL=postgres://usuario:senha@localhost:5432/einstein_coding
   ```
6) Executar as migrações do banco após configurado: 
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
7) Rodar o servidor local e iniciar o servidor de desenvolvimento Django:
   ```
   python manage.py runserver
   ```
   * O terminal deve exibir algo como:
     ```
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.
     ```
     Acesse o site no navegador
8) Desativar o ambiente virtual ao encerrar o trabalho:
   ```
   deactivate
   ```


---

## Como contribuir 
- Antes de começar uma nova tarefa, certifique-se de ter a versão mais recente do projeto:
  ```
  git pull origin main
  ```
- Crie uma nova branch (específica para a funcionalidade ou correção em que você vai trabalhar). O nome da branch deve ser curto e descritivo.
    ```
    git checkout -b feature/nome-da-feature
    ```
- Faça suas alterações
  Edite, crie ou modifique os arquivos necessários. É possível testar localmente rodando:
  ```
  python manage.py runserver
  ```
  Sempre garanta que o código funciona antes de prosseguir!
- Adicione e confirme suas alterações (commit)
  ```
  git add .
  git commit -m "O que foi feito"
  ```
- Envie a branch para o repositório remoto
  ```
  git push origin feature/nome-da-feature
  ```
- Abra um Pull Request (PR) no GitHub
  1) Vá até o repositório
  2) Clique em "Compare & pull request"
  3) Adicione um título claro e uma descrição breve do que foi feito
  4) Clique em "Create Pull Request"
  O Scrum Master ou outro membro revisará o PR antes da integração com a branch principal
- Aguarde a revisão
  Durante a revisào, corrija eventuais comentários e sugestões. Assim que aprovado, o PR será mesclado (merged) à branch principal (main).
- Limpeza (opcional)
  Após o merge, apague a branch local e remota para manter o repositório organizado:
  ```
  git branch -d feature/nome-da-feature
  git push origin --delete feature/nome-da-feature
  ```
- Boas práticas de colaboração:
  1) Faça commits pequenos e frequentes
  2) Sempre use branches diferentes da main
  3) Mantenha o código limpo, legível e comentado
  4) Descreva claramente o que foi feito no PR
  5) Antes de iniciar uma nova tarefa, sempre puxe as últimas alterações da main
