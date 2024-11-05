#Introdução a biblioteca pandas
import pandas as pd

#Criar um DataFrame a partir de um dicionário
data = {    
    'nome': ['joao', 'maria', 'pedro'],
    'idade': ['19', '52', '23'],
    'cidade': ['Sp', 'Rj', 'Curitiba']
    }
df = pd.DataFrame(data)
print("DataFrame criada: \n", df)


#Ler dados de um arquivo CSV
df_csv = pd.read_csv('clientes.csv')
print("\nDataframe lidodo CSV: \n", df_csv.head())

#Selecionar a coluna 'Cidade'
cidades = df['cidade']
print("\nCidades: \n", cidades)

#Filtrar clientes com idade com maior que 30
filtro = df_csv[df_csv['idade']> 30]
print("\nClientes com idade maior que 30:\n", filtro)