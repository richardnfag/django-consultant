# Challenge Django Consultant

Esse repositorio é uma implementação de [Challenge Django Consultant](https://github.com/DigitalsysTecnologia/challenge-django-consultant)


### Requisitos

Certifique-se que tenha as seguintes ferramentas instaladas:

- Docker (https://docs.docker.com/engine/install/)  
- Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  


### Configuração e execução

1. Clone esse repositório

```bash
git clone https://github.com/richardnfag/django-consultant.git
```

2. Navegue até o repositório do projeto:

```bash
cd django-consultant
```

3. Execute o seguinte comando para iniciar os container da aplicação:

```
docker-compose up -d
```



4. Após a inicialização dos containers execute o seguinte comando:

```bash
docker-compose run --rm backend make example
```

Esse comando irá configurar o ambiente necessário para testar a aplicação

5. Após o ambiente de exemplo estar configurado pode-se acessar o formulário para submição da proposta de emprestimo atravéz de localhost:3000.   
Tente acessar: http://localhost:3000/

![Formulário de Proposta](docs/images/formulario_proposta.jpeg)

O ambiente de administração também já foi previamente configurado no exemplo.   
Acesse: http://localhost:8000/admin utilizando o usuário `admin` com a senha `admin`

![Tela de Login do Django Admin](docs/images/admin_login.jpeg)

6. Dentro da tela de Admin é possivel gerenciar as propostas assim como os campos customizáveis

![Tela de Admin](docs/images/admin.jpeg)

![Tela dos campos customizáveis](docs/images/listagem_campos.jpeg)

![Tela de propostas](docs/images/listagem_propostas.jpeg)

7. A aprovação de cada proposta pode ser gerenciado conforme os requisitos do projeto.

![Tela de proposta pendente](docs/images/proposta_pendente.jpeg)

![Tela de proposta aprovada](docs/images/proposta_aprovada.jpeg)

![Tela de proposta negada](docs/images/proposta_negada.jpeg)

![Tela de proposta negada pelo provedor](docs/images/proposta_negada_pelo_provedor.jpeg)


8. Para visualizar a cobertura de testes execute o seguinte comando:

```bash
docker-compose run --rm backend make coverage
```

```
Name                               Stmts   Miss  Cover
------------------------------------------------------
backend/__init__.py                    2      0   100%
backend/celery.py                      6      0   100%
backend/settings.py                   27      1    96%
backend/urls.py                        3      0   100%
loans/__init__.py                      0      0   100%
loans/admin.py                        65      0   100%
loans/apps.py                          4      0   100%
loans/migrations/0001_initial.py       6      0   100%
loans/migrations/__init__.py           0      0   100%
loans/models.py                       34      0   100%
loans/tasks.py                        21      0   100%
loans/tests/__init__.py                0      0   100%
loans/tests/conftest.py               14      0   100%
loans/tests/test_admin.py             53      0   100%
loans/tests/test_models.py            14      0   100%
loans/tests/test_tasks.py             35      0   100%
loans/tests/test_views.py             29      0   100%
loans/urls.py                          3      0   100%
loans/views.py                        33      0   100%
------------------------------------------------------
TOTAL                                349      1    99%
```

### Tecnologias Utilizadas

- [**Python**](https://www.python.org/)  
- [**Django**](https://www.djangoproject.com/)  
- [**Django Rest Framework**](https://www.django-rest-framework.org/)  
- [**Celery**](https://docs.celeryq.dev/en/stable/index.html)  
- [**RabbitMQ**](https://www.rabbitmq.com/)  
- [**PostgreSQL**](https://www.postgresql.org/)  
- [**Docker**](https://www.docker.com/)  
- [**Pytest**](https://docs.pytest.org/)  
- [**Next.js**](https://nextjs.org/)  


### Estrutura de diretórios

```sh
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── Makefile
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── backend
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── pytest.ini
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── example.json
│   ├── loans
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── tasks.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   ├── test_admin.py
│   │   │   ├── test_models.py
│   │   │   ├── test_tasks.py
│   │   │   └── test_views.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
├── docs
│   ├── images
├── docker-compose.yml
├── frontend
│   ├── Dockerfile
│   ├── README.md
│   ├── app
│   │   ├── components
│   │   │   ├── LoanProposalForm.tsx
│   │   │   ├── LoanProposalMenu.tsx
│   │   │   └── LoanProposalPanel.tsx
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   ├── page.module.css
│   │   └── page.tsx
│   ├── next-env.d.ts
│   ├── next.config.js
│   ├── node_modules
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   └── tsconfig.json
```
