# Analise de dados covid com python
 <p>Há um mês atrás eu estava estudando na plataforma Youtube e encontrei um rapaz chamada
 Walisson Silva e ele cria conteudos de tecnologia e linguagem de programação, e eu
 acabei assistindo tres aulas referente a analise de dados com python, aprendi muito
 com ele e eu dou todos os créditos a ele e deixarei aqui os dados para que possam assim
 como eu aprender mais
</p>
<b>canal Walisson Silva no Youtube<b>

<h2> Incremento no projeto </h2>

<p>Então pessoal como estou terminando o curso de ADS e o python está em minha grade e gosto
me aprofundei um pouco e fiz algumas melhorias para meu uso só que como eu estou com o meu
repositorio aqui , eu resolvi postar para que outras pessoas possam ter a mesma oportunidade
que eu de aprender e entender cada vez mais essa ferramenta poderosa que é o python.

O projeto ao qual eu me inspirei trabalha com dados abertos de covid em que precisa acessar
os dados via online e baixar para o computador, então eu resolvi criar algo que maximize e de
mais liberdade para o desenvolvedor. aluno ou entusiasta espero que gostem.
</p>

<b>Classes utilizadas</b>

        import pandas as pd

        from urllib.request import urlretrieve

        import matplotlib.pyplot as plt

        %matplotlib inline

<p>Para o projeto se fez necessário o uso do pandas para criar o dataframe para manipulação dos dados,
bem como as bibliotecas urllin.resquest para a conexão e download da base de dados, e também a biblioteca
matplotlib para plotar os graficos dos dados.
<br>

<h2> DCovid.py </h2>

<h1>Classe ObsCovid </h1>

crie uma instancia da classe ObsCovid

    id_obj.ObsCovid(dados)

<i>Parametros dados</i>

- Refere-se ao tipo de dado que está se busca :

"Confirmados" - Casos confirmados

"Óbito" - Obitos registrados com confirmação de covid

"Curados" - Registro de pessoas curadas

<i>A Classe ObsCovid possui 3 metodos valiosos</i>

id_obj.Salvar_Dados() - Metodo responsável por salvar o nossa base de dados do servidor para o mesmo local
                        onde o codigo fonte estiver.

    
id_obj.Pais(nomedoPaís) - Metodo responsável por carregar a base de dados de acordo com o que se pede
                          e pegar as datas e ocorrência no país procurado e plotar em um grafico.

    
 id_obj.PaisEx(nomedopaís, inicio, fim) - Metodo responsável por carregar a base de dados de acordo com o que se pede
                                        e pegar as datas e ocorrência no país procurado e plotar em um grafico tendo limites inicio e final, por exemplo eu quero apresentar somente 20 registros obedecendo o número de registros de ocorrências
</p>

<h2>Observação</h2>
<p>
Vou postar um projeto utilizando essa classe nesse fim de semana para demonstrar seu uso e mais uma vez agradeço ao
Walisson Silva pela oportunidade.
</p>