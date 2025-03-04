- Parte 1 - Fundamentos
    - Revisao de tipos de dados e estruturas
      - Tipos de dados
         - Dinâmico e tipado
           - decimal
           - string
           - None
           - https://realpython.com/python-data-types/
           - https://docs.python.org/3/library/datatypes.html
      - Estrutura de dados
         - Lists e Dicts
            - collections
         - Serialização e deserialização
            - JSON
      - Utilizando estruturas
        - enumerate e zip
        - sorted
        - list compreension
        - items(), keys, values
      - datetime, dateutils, format, enum
    - Caracteristicas
      - pitfalls
        - GIL
          - asyncio
          - redis, celery, etc
          - dask, numpy, tensorflow, cython
        - dinâmico/otimização
          - dificuldade de otimizar compilação
          - nuitka
          - Pypy
          - cálculos vetorizados e Cython
        - na prática, pouco impacto (Pareto)
      - vantagens
        - baterias incluidas
        - pip/conda --> loja de aplicativos
          - (baterias incluidas e acessorios a um clique)
          - venv e modular evita dependency hell
          - rodar pip freeze, criar venv, pip install, update, ==, >=, activate, deactivate, etc. 
        - import this
        - dinamico
        - conciso e coeso
        - fluidez
        - Porque Python
          - Produtividade
            - maximizar recurso
          - Usabilidade e simplicidade
            - focar no problema de negócio
          - Concisão
            - menos código, menos bugs
          - Recurso humano >> recurso computacional
            - economia inteligente
          - Comunidade
            - Principio de Linus
            - "Mercado"
    - Arquitetura
      - clean code
      - modulos e microservicos
      - cookiecutter
      - pip (muito mais que baterias incluidas)
      - setuptools
      - setup.py
      - venv
      - (pyenv, pipenv -- novidades)
      - tox
      - CI/CD
      - TDD
      - pytest, unittest, behave
      - flake8, black
      - code complexity (clean code)
      - code coverage
      - documentação (sphinx autodoc)
      - Design Patterns simplificados
      - Reflexão, introspecção, dinâmica
        - "tudo" é classe/objeto
        - multiparadigma
            - POO
                - Mixins
            - funcional
                - map, filter, etc
        - função como parâmetro
        - ponteiros de função e objeto
        - herança multipla, mixins
        - do some magic - getattr e setattr
        - https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
        - https://teamtreehouse.com/community/how-usermixin-and-class-inheritance-work
        - https://realpython.com/oop-in-python-vs-java/
      - pitfalls (sem almoço grátis)
        - Code completion e check
        - runtime error (sem compilação)
        - workarounds
            - type hints e mypy
            - testes unitarios e de qualidade
      - PEPs 
    - Persistência/ORM
      - open, write
      - pickle
      - json
      - SQLAlchemy
    - Desenvolvimento web
      - Tutorial Flask
      - Prática pequeno projeto web
- Parte 2 - Aplicações
    - Desenvolvimento web
      - Tutoriais What The Flask e Flask Mega Tutorial
      - Livro Obey the testing goat
      - Terminar um projeto Flask maior, com Persistência, Flask-Admin, testes, etc
      - https://www.toptal.com/flask/flask-production-recipes
    - Desenvolvimento API
      - Padrão Open API
      - swagger-ui
      - connexion
      - marshmallow-sqlalchemy
    - Consumindo APIs/sites
      - biblioteca requests
- Parte 3 - "Hackaton"
    - Colocando tudo junto
      - Configurando um projeto CI/CD com Git, Heroku, Travis, unittest e tox
      - Usa os conceitos da Parte 1 e 2 em um projeto prático
- Parte 4 - Ciência de Dados
    - Manhã - introdução e exercícios
    - Pandas
    - numpy
    - sklearn
    - keras/tensorflow 2.0
- Parte 5 - Ciência de Dados
    - Manhã - introdução e exercícios
        - Pandas/numpy
          - conceitos
          - DataFrame
          - Series
          - Filtros
          - Slicing
          - Apply
          - dummies
        - sklearn
         - conceitos
         - Tutorial oficial sklearn
        - statsmodels
    - Tarde - exercícios
       - combinando sklearn e pandas em um mini projeto
       - utilizando Pandas e Hue no Receita Data
- Parte 6 - Projeto AJNA
    - Manhã
        - Tutorial oficial keras/tensorflow 2.0
        - Exploração rápida dos módulos do AJNA e das bases de dados
    - Tarde
        - Treinar e publicar modelo para AJNA
        - Publicar um FiltroAuditoria no AJNA
        - Publicar uma tela no AJNA
