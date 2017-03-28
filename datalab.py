import pandas as pd

# # Path to the object in Google Cloud Storage that you want to copy
# sample_gcs_object = 'gs://brazil_data/1746data.csv'

# # Copy the file from Google Cloud Storage to Datalab
# !gsutil cp $sample_gcs_object '1746data.csv'

# Read the file into a pandas DataFrame
tp = pd.read_csv('1746data.csv', sep='|', iterator=True, chunksize=10000, encoding = "ISO-8859-1")
#latin1
df = pd.concat(tp, ignore_index=True)

df.head()
# Data dictionary
{'id_categoria_fk' : {'Informações':'1', 'Serviço':'2', 'Denúncia': '3', 'Reclamação': '4', 'Elogio': '5', 'Crítica': '6', 'Sugestão': '7'},
 'id_origem_fk' : {'Teleatendimento': '1', 'E-mail': '2', 'Chat':'3', 'Fax': '4', 'Carga':'5', 'SISO': '6', 'Departamental': '8', 'SMS': '10',
                   'Aplicativo Móvel': '11', 'Presencial': '12', 'Aplicativo Web': '13', 'Nave do conhecimento': '15', 'Carioca Digital': '16',
                   'Whatsapp': '17', '1746 Móvel': '18'},
 
    
}


drop_cols = ['categoria','origem']

# pd.to_datetime(df['data_abertura'],infer_datetime_format=True)
df['data_abertura'] =  pd.to_datetime(df['data_abertura'], format='%Y-%m-%d %H:%M:%S')
df['data_fechamento'] =  pd.to_datetime(df['data_abertura'], format='%Y-%m-%d %H:%M:%S')
df['data_atualizacao'] =  pd.to_datetime(df['data_abertura'], format='%Y-%m-%d %H:%M:%S')
df['nascimento'] =  pd.to_datetime(df['data_abertura'], format='%Y-%m-%d %H:%M:%S')
df['dt_classificacao'] =  pd.to_datetime(df['data_abertura'], format='%Y-%m-%d %H:%M:%S')