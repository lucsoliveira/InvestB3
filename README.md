<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />

   <h1 align="center">
       NotificaB3
</h1>
  <p align="center">
    Sistema de notificação de oportunidades de negociação de ações da B3: receba notificações em seu email sobre o preço de suas ações favoritas com valores de compra e venda desejados.
  </p>

<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre</a>
      <ul>
        <li><a href="#built-with">Feito com</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Instruções</a>
      <ul>
        <li><a href="#prerequisites">Pré requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
        <li><a href="#understanding">Entendendo o código</a></li>
      </ul>
    </li>
    <li><a href="#usage">Uso</a></li>
    <li><a href="#license">Licença</a></li>
    <li><a href="#contact">Contato</a></li>
    <li><a href="#acknowledgements">Créditos</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<a id="about-the-project"></a>

## Sobre

O sistema NotificaB3 é um projeto desenvolvido para participação do desafio da empresa INOA. Em suma, este projeto é um sistema de monitoramento de ações da B3, cuja finalidade é monitorar os limites inferior e superior de uma ação, criados pelo usuário, e notifica-lo, via email, caso o preço atual da ação cruze esses valores limites. A seguir estão algumas das funcionalidades do NotificaB3:

* Dados confiáveis das ações, sendo as informações quantitativas de cada ação obtidas através da API do Yahoo Finances;
* O sistema pode possuir vários usuários e cada usuário pode ter vários alertas;
* Tela inicial com formulário de busca de ações que possui sugestões juntamente com o setor de operação;
* Front-end com formulários de configuração de notificação via email dos limites superior e inferior, além do intervalo de notificação, para a ação desejada;
* Front-end com tela única com dados estatísticos da ação, gráfico de histórico de preço dos últimos 5 anos da ação e notícias relacionadas a ela;
* Sistema de notificação inteligente: o aplicativo "notificator", que roda em background, só notifica o usuário caso o dia e a hora atuais estejam no intervalo de funcionamento da B3; além disso, o sistema possui um verificador de ultimo envio de notificação, enviando uma nova notificação somente se a nova notificação ocorra 30 minutos após a ultima notificação enviada;
* Navegação simples e intuitiva: basta procurar uma ação, clicar em "acompanhar", delimitar os limites e pronto. O sistema irá notificá-lo caso a ação atinja esses limites;
* Email de notificação simples e objetivo.

A tela inicial do front-end do sistema tem a finalidade de servir de ferramenta de busca para uma ação em específico, além de mostrar os alertas de ações criados pelo usuário.

![Tela Alert][alert-screen-screenshot]

Abaixo é possível observar uma imagem da tela "stock", onde contém informações sobre uma única ação e um gráfico com o histórico de valor dela.

![Tela Stock][stock-screen-screenshot]

Um exemplo de email de notificação de compra:
```sh
[ASSUNTO] [NOTIFICAB3] Compre a ação: XXXX
[MENSAGEM] Olá, Lucas! 
Essa é uma mensagem de aviso para compra da ação: XXXX. 
O Valor atual dela está em: (BRL) 9.91 e seu limite para compra foi de: (BRL) 10.0 .
```

<!-- BUILT WITH -->
<a id="built-with"></a>

### Feito com

* [Python 3.10](https://www.python.org/)
* [Django 4.0](https://www.djangoproject.com/)
* [Semantic UI](https://semantic-ui.com/)

<!-- GETTING STARTED -->
<a id="getting-started"></a>

## Instalação

Comece a instalação verificando e instalando os softwares que são pré-requisitos deste projeto. Após isso, clone o repositório em sua máquina e, depois, efetue todas as configurações necessárias seguindo o tópico "Configurando o projeto".

<!-- PREREQUISITES -->
<a id="prerequisites"></a>

### Pré requisitos

O projeto necessita dos seguintes softwares:

* git
* python3
* django 4.0
* pip3

<!-- INSTALLATION -->
<a id="installation"></a>

### Configurando o projeto

O primeiro passo é clonar este repositório em seu computador. Comece rodando o comando:

```sh
git clone https://github.com/lucsoliveira/NotificaB3 && cd NotificaB3
```

Após clonar este repositório em seu *workspace*, é necessário criar um ambiente virtual "venv" e realizar a ativação deste ambiente. Para mais detalhes, acesse a documentação: [Criação de ambientes virtuais — documentação Python 3.10.1](https://docs.python.org/pt-br/3/library/venv.html).

Com o ambiente *venv* criado, instale as dependências do arquivo "requirements.txt", executando o seguinte comando dentro da pasta "./NotificaB3":

```sh
pip install -r requirements.txt
```

Com todas as dependências instaladas, efetue a migração do banco de dados com o seguinte comando:

```sh
py ./manage.py migrate
```

Como é a primeira inicialização do sistema, recomenda-se a criação de um usuário administrador. Para tanto, basta executar o comando:

```sh
py ./manage.py createsuperuser
```

Agora é necessário criar e configurar as variáveis do arquivo .env do sistema. Há um arquivo de exemplo dentro da pasta "core", nomeado como ".env_example". O arquivo de exemplo contém as seguintes constantes:

```Python
# Yahoo Finances API
URL_SERVER_API='yh-finance.p.rapidapi.com'
URL_SERVER_API_KEY='yourkey'

# Email Config
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='youremail@gmail.com'
EMAIL_HOST_PASSWORD='yourpass'
EMAIL_PORT=587
EMAIL_USE_SSL=False
EMAIL_USE_TLS=True
```

Para a parte da API dos dados de ações da B3, é necessário configurar o "URL_SERVER_API_KEY". Você pode obter uma chave *freemium* dessa API clicando [aqui](https://rapidapi.com/apidojo/api/yahoo-finance1/). Após colocar sua chave da API Yahoo Finances, é necessário realizar a configuração dos parâmetros para envio de email. Em caso de dúvidas, você pode acessar este tutorial (caso use o gmail): [Fazer login com senhas de app - Ajuda da Conta do Google](https://support.google.com/accounts/answer/185833?hl=pt-BR)

Por fim, basta salvar o arquivo como ".env" somente, dentro da pasta "core".

### Entendendo o código

O sistema foi dividido em uma aplicação central, chamada "Core", e várias outras aplicações (todas estas dentro da pasta "./apps"). Eis a funcionalidade de cada uma das aplicações:

* Core: aplicação central que contem os arquivos principais do sistema: settings.py, .env e urls.py;
* Alert: aplicação que possui a view da página "Meus Alertas" e chama a funcionalidade em background da aplicação "Notificator";
* Notificator: aplicação que roda em background e executa as rotinas de notificação de negociação de ações na B3; as rotinas de notificação estão presentes no arquivo "jobs.py";
* Market: aplicação que contém a view "Market", onde está presente uma tabela dinâmica que faz uma listagem das ações da B3 e seus respectivos setores;
* Stock: aplicação com a view "Stock Single" onde, através da comunicação com a aplicação API, faz uma listagem de todos os dados da ação, além de trazer um gráfico com o histórico de até 5 anos do preço de uma ação. Nessa view também há um módulo de criação de uma notificação (formulário com inputs);
* API: aplicação que faz a comunicação com a API do Yahoo Finances e uma API pública para listagem das ações da B3. Suas views retornam valores do tipo JSON.
* User: aplicação que faz uso da biblitoeca de autenticação padrão do Django para obtenção e manipulação de usuários.

Os templates das views estão na pasta "templates" e os arquivos .js para tornar as views mais dinâmicas estão na pasta "static".

<!-- USAGE -->
<a id="usage"></a>

## Executando o projeto

Após realizar o passo-a-passo do tópico anterior, basta executar a aplicação com o comando:

```sh
py ./manage.py runserver --noreload
```

Onde o "--noreload" é um parâmetro necessário para se evitar que os *jobs* em *background* se dupliquem ao atualizar automaticamente após cada alteração do código (se for alterado algo, é necessário executar o comando acima novamente).

Pode-se acessar o front-end do projeto em [127.0.0.1:8000](127.0.0.1:8000) e logar no sistema com o seu usuário. Com o usuário e senha criados nos passos anteriores, recomenda-se a inserção de um "First Name" para o usuário. Isso pode ser feito através do painel administrativo do Django, acessado em 127.0.0.1:8000/admin . Isso é necessário, pois os emails a serem enviados pelo notificador utilizam o primeiro nome do usuário.

Agora é só buscar suas ações favoritas e criar seus alertas nos intervalos desejados :)

<!-- LICENSE -->
<a id="license"></a>

## Licença

Distribuído sob a MIT License.

<!-- CONTACT -->
<a id="contact"></a>

## Contato

Lucas de Oliveira | [LinkedIn](https://www.linkedin.com/in/engenheiro-lucas-oliveira/) 

<!-- ACKNOWLEDGEMENTS -->
<a id="acknowledgements"></a>

## Créditos

* [Django](https://www.djangoproject.com/)

* [Semantic UI](https://semantic-ui.com/)

* [Rapid API](https://rapidapi.com/)

* [Yahoo! Finance](https://finance.yahoo.com/)

* [Apex Chart](https://apexcharts.com/)

  

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-url]: https://github.com/lucsoliveira/NotificaB3/graphs/contributors

[forks-url]: https://github.com/lucsoliveira/NotificaB3/network/members

[stars-url]: https://github.com/lucsoliveira/NotificaB3/stargazers

[issues-url]: https://github.com/lucsoliveira/NotificaB3/issues

[linkedin-url]: https://github.com/lucsoliveira/NotificaB3

[alert-screen-screenshot]: ./NotificaB3/static/images/alert.gif
[stock-screen-screenshot]: ./NotificaB3/static/images/stock.gif
