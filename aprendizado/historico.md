ANOTAÇÕES AO LONGO DO DESENVOLVIMENTO DO PROJETO

--------------------------------------------------------------
                          07/12/2021 
--------------------------------------------------------------

------- Strings

https://docs.python.org/3.10/tutorial/introduction.html

In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:

Pegar dois ou mais caracteres de string
>>>
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'

Note that since -0 is the same as 0, negative indices start from -1.

-------------------- Listas
 squares = [1, 4, 9, 16, 25]

square + retangule # para concatenar
cubes.append(216)  # add the cube of 6 ##adicionar um valor ao final


---------------------iF
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')

---------------------FOR

https://docs.python.org/3.10/tutorial/controlflow.html

>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
##

lista = ['a', 'b', 'c', 'd']

for i in range(len(lista)):
    print(i, lista[i])

----------------------------- FUNÇÕES
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)


----------------------- utilizando o PIP

pip install ipython[notebook]

para executar: ipython notebook

--------------------------------------------------------------
                          08/12/2021 
--------------------------------------------------------------

#No Python tudo é referência. Para evitar alteração numa lista pode-se fazer o seguinte:

def g(x):
	x = x[:] #copia toda a lista
	x.append(51) #adiciona ao final
	return x

x(lista), lista
#printa a lista alterada e, depois, a lista original

#tuplas são sequências imutáveis
tupla = ('A', 'b', 3.13, ['1','2','3'])
#ou pode escrever sem os parenteses
tupla = 'A', 'b', 3.13, ['1','2','3']

##### dicionarios são listas com indices #######
dicionario = {'nome': 'Lucas', 'idade': 23, 'interesses': []}
print(dicionario)

print('\nAcrescentando valor ao dicionário >>>')

dicionario['interesses'].append('Desenvolvimento')
dicionario['interesses'].append('Livros')
dicionario['interesses'].append('Rock')
print(dicionario)

print('\nRemovendo ultimo valor da lista do dicionário >>>')
dicionario['interesses'].pop()
print(dicionario)

print('\nAlterando valor do indice nome >>>')
dicionario['nome'] = 'Lucas de Oliveira'
print(dicionario)


##Orientação a objetos
Dados -> possuem somente valor
Objetos -> possuem valor, identidade e tipo

Variáveis locais definidas no corpo da classe são os atributos da classe.
Se na instância não houver um atributo procurado, a busca se dá na própria classe. É como se a instância só tivesse dados próprios quando estes forem acrescidos após a instânciação.

o "self" equivale ao "this" de outras linguagens

#classe

class Carro:
    portas = 2

    def __init__(self, nome):
        self.nome = nome

# herança
class Ferrari(Carro):
    def __init__(self, modelo):
        super().__init__('Ferrari')
        self.modelo = modelo

# DJANGO 

Django é um framework web de desenvolvimento alto nível escrito em Python que possibilita rápido desenvolvimento e design pragmático.

## MTV

- Model:
- Template:
- View:

- Um Raio-X do Django - Henrique Bastos - Palestra: https://www.youtube.com/watch?v=K62z2lVHS_M

 Em Django, não é recomendado começar pelos modelos. O Django é utilizado para fazer backoffice de sites que contem conteúdos.
 Estrutura recomendada para os projetos:

repo/
	manage.py
	myproject/
		__init__.py
		settings.py
		urls.py
		wsgi.pi
		myapp/
			__init__.py
			models.py
			tests.py
			views.py

Django App é um pacote Python que contem um módulo models.py. Ele não [e propriamente um módulo.

O fluxo de requisição da aplicação Django.
1. Request Middleware
2. Url Resolve (são as rotas do sistema)
3. View Middleware (recebe as views e os parâmetros que são executados)
4. View (execução do seu código de fato)
5. Template Response Middleware 
6. Response Middleware

URLConf:  módulo que contem uma variável urlpatterns que referencia uma sequencia de rotas associadas a views.

	urlpatterns = patterns('', url('time/plus/(\d{1,2}/$', time_ahead),)

acima é um exemplo de uma rota onde somara de 1 a 2 horas o tempo passado

Expressões Regulares: https://docs.python.org/pt-br/3/library/re.html

Views: um callable (objeto python que pode ser executado, ou seja, se comporta como uma função) que recebe uma instância de HttpRequest e retorna uma instância de HttpResponse

um exemplo em Django:

## codigo: utf-8
from django.http import HttpResponse

def myview(request):
	return HttpResponse('Olá, mundo!')

Boas práticas quanto as views:
- Muito grandes;
- Conversão de dados na view;
- Pilhas de decoradores ()
- Uso de funções auxiliares que instanciam o HttpResponse;
- Contextos de templates gigantes;

## Arquitetura dos Forms

Forms: responsável pelo pipeline de validação

Fields: valida dados da requisição e os converte para tipos Python

Widgets: representa o valor do field em html

Bounded: quando tem dados -> SubscriptionForm(request.POST)

Unbounded: sem dados -> SubscriptionForm()

## Models

Subscription: descreve a estrutura de uma tabela

Subscription(...) : corresponde à uma linha da tabela

Subscription.objects: manipula todas as linhas da tabela

Subscription.objects.all(): Acumula estados que serão usados pelo ORM para compilar uma query SQL

Model Fields: correlacionam atributos do modelo com colunas da tabela

## Template

{{ STATIC_URL }}

{{ subscription.name }}
{{ subscription.['name'] }}

Parecido com EJS.
## Hello World com Django
criar um projeto no PyCharm
Executar o comando no terminal:
pip install --pre django

django-admin startproject helloworld
cd .\helloworld

python manage.py migrate

#para executar o server
python manage.py runserver

### Projetos e aplicações

ref: https://docs.djangoproject.com/pt-br/4.0/intro/tutorial01/

Projetos contem várias aplicações.

Para iniciar uma nova aplicação dentro de um projeto, basta executar: 
py manage.py startapp polls

Primeira view:

- Criar polls/views.py
- Criar o arquivos urls.py dentro da aplicação
- referenciar a view dentro do arquivo anterior
- Apontar no URLconf do módulo principal o path com o include
- Executar a aplicação principal e acessar a nova rota, neste caso é '/polls'

--------------------------------------------------------------
                          09/12/2021 
--------------------------------------------------------------

# Iniciando o banco de dados

py manage.py migrate
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .tables (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

# Modelos do DB

- Mude seus modelos (em models.py).

- Rode python manage.py makemigrations para criar migrações para suas modificações

- Rode python manage.py migrate para aplicar suas modificações no banco de dados.

Um exemplo:

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

Para incluir a aplicação no nosso projeto, precisamos adicionar a referência à classe de configuração da aplicação na configuração INSTALLED_APPS . A classe PollsConfig está no arquivo polls/apps.py, então seu caminho pontuado é 'polls.apps.PollsConfig'. Edite o arquivo mysite/settings.py e adicione aquele caminho com notação de ponto a configuração INSTALLED_APPS. 

Para atualizar as tabelas do banco após uma criação de um modelo e alteração do installed_apps, basta rodar o comando:

py manage.py makemigrations polls

onde o "polls" refere-se aos modelos da aplicação ao qual foram atualizados.

O comando sqlmigrate recebe o nome da migração e o seu SQL.

...\> py manage.py sqlmigrate polls 0001

Agora rode o migrate novamente para criar essas tabelas dos modelos no seu banco de dados:

...\> py manage.py migrate

O comando migrate pega todas as migrações que ainda não foram aplicadas (Django rastreia quais foram aplicadas usando uma tabela especial em seu banco de dados chamada django_migrations) e aplica elas no seu banco de dados - essencialmente, sincronizando as alterações feitas aos seus modelos com o esquema no banco de dados.

É importante adicionar métodos __str__() aos seus modelos, não apenas para sua própria conveniência quando estiver lidando com o prompt interativo, mas também porque representações de objetos são usadas por todo interface administrativa gerada automaticamente pelo Django.

# Usuário administrador

py manage.py createsuperuser

# Criando Views

A URLconf maps URL patterns to views.

Em polls/views.py é definido a view

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

E em polls/urls.py é definido a rota que ligará com a view. Isso dentro de urlpatterns:

path('<int:question_id>/', views.detail, name='detail'),


Tudo que o Django espera é que a view devolva um HttpResponse. Ou uma exceção.

Criar uma pasta 'templates' dentro da aplicação. E dentro dessa pasta, criar uma pasta com o nome da aplicação e, dentro dela, um arquivo index.html

In other words, your template should be at polls/templates/polls/index.html

Depois, dentro de 'app/views.py' da aplicação alterar da seguinte forma: 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

Esse código carrega o template chamado polls/index.html e passa um contexto para ele. O contexto é um dicionário mapeando nomes de variáveis ​​para objetos Python.