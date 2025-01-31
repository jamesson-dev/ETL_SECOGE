# Secoge

bibliotecas baixadas

```bash
pip install requests
pip install pyodbc
pip install pandas
```

## executando o primeiro script de  teste para verificar o banco de dados SQL Server

![image.png](image.png)

---

executando o segundo script de teste, realizando a gravaçao dos dados no banco de dados SQL Server.

![image.png](image%201.png)

![image.png](image%202.png)

---

Modelo que utilizei para criar a tabela no SQLServer

![image.png](image%203.png)

execucao final, script automatizado

![image.png](image%204.png)

modelo gerado com pandas no excel

![image.png](image%205.png)

---

# Dados utilizados:

Escolhi dados de futebol por ter afinidade, nao encontrei o do meu time do coraçao entao peguei outro qualquer mas pude aplicar alguns filtros de qualidade nos dados

link dos dados:

[https://www.sofascore.com/pt/football/match/sao-paulo-botafogo/iOsGO#id:12117350](https://www.sofascore.com/pt/football/match/sao-paulo-botafogo/iOsGO#id:12117350)

escolhi esses dados por gostar de esportes e apostas esportivas, pude ter uma base de como funciona as estatisticas de futebol, claro que nao apliquei nenhuma tecnica de machine lerarning, mas pude verificar os dados e tratalos.

# Extraçao e Transformação:

apliquei um laço de repetiçao para extrair todas as informacoes que eu queria, salvei tudo num dataframe do pandas e apliquei algumas transformacoes no pandas mesmo.

# Consultas:

sobre as bibliotecas utilizadas:

`requests; pyodbc; pandas`

escolhi pois sao simples de utilizar, tem bastante documentacao e tambem foi indicacao do desafio.

request faz requisicoes bem simples na web, foi onde eu pude aplicar o scraping atraves da WEB atraves do HTML.

pyodbc foi o mais complicados entre todos as bibliotecas, mas conseguir apos varias tentivas de conectar com o SQLServer. Depois da barreira inicial se torna uma lib bem simples e facil de aplicar.

O pandas ja utilizo a algum tempo foi onde eu pude resolver alguns porblemas para tratar os dados e foi uma parte bem tranquila.

# Consideraçoes finais:

no inicio preferia realizar o projeto no colab por ser mais pratico, porem foram surgindo problemas com instabilidade e por ser uma ferramenta web, no final acabei optando pelo bom e velho VSCode, que numca me deixa na mao e quando tem algum problema consigo resolver sem muitas dificuldades. Tambem pensei em utilizar o pySpark mas como era um volume de dados pequeno nao valia o esforço, o pandas foi otimo nessa situação.
