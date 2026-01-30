# Site Einstein Coding - 2025
Site institucional da Empresa Júnior Einstein Coding - 2025

Repositório oficial para o desenvolvimento do site da **Empresa Júnior Einstein Coding**, voltada para soluções de tecnologia e programação na área da saúde.

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

## Especificações Técnicas do Projeto
## Projeto: Site da Entidade Einstein Coding

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
