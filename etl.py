import pyodbc
import pandas as pd
import requests

url = 'https://www.sofascore.com/api/v1/event/12117350/statistics'

# Simulador de navegador chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    all_data = []

    for match_stat in data['statistics']:
        period = match_stat['period']

        for group in match_stat['groups']:
            group_name = group['groupName']

            for item in group['statisticsItems']:
                stat_name = item.get('name')
                home_value = item.get('home')
                away_value = item.get('away')

                all_data.append({
                    'Period': period,
                    'Group': group_name,
                    'Statistic': stat_name,
                    'Home': home_value,
                    'Away': away_value 
                })

# criando dataframe a parti dos dados coletados
df = pd.DataFrame(all_data)

# Renomeando colunas
df = df.rename(columns={
    'Away': 'Visitante', 
    'Home': 'Casa', 
    'Statistic': 'Statistica', 
    'Group': 'Grupo', 
    'Period': 'Periodo'
})

# salvando dados em arquvo xlsx
excel_file = 'futebol_stats.xlsx'
df.to_excel(excel_file, index=False)

#iniciando conecxao com banco de dados SqlServer 
def conect_bd(driver='ODBC Driver 17 for SQL Server', server='DESKTOP-AG11Q8P', database='SECOGE', username=None, password=None, trusted_connection='yes'):
    # Indented block within the function
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection};'
    print(connectionString)

    conexao = pyodbc.connect(connectionString)
    cursor = conexao.cursor()
    print('Conectado com sucesso')
    print('conexao: ', conexao)
    print('cursor: ', cursor)

    return conexao, cursor

conexao, cursor = conect_bd()

# Inserindo cada linha do DataFrame na tabela SQL
try:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO futebol_statistica (Visitante, Casa, Statistica, Grupo, Periodo) VALUES (?, ?, ?, ?, ?)", 
                       row['Visitante'], row['Casa'], row['Statistica'], row['Grupo'], row['Periodo'])
    conexao.commit()
except pyodbc.DatabaseError as e:
    print(e)
    conexao.rollback()
finally:
    # print(cursor.execute('SELECT id from futebol').fetchall())
    conexao.close()

