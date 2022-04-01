import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
%matplotlib inline

class ObsCovid():
    identif = ""
    sarq = ""
    S_local = None
    def __init__(self,ident):
        if (ident == 'Confirmados'):
            self.identif = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
            self.sarq = "casos_confirmados.csv"
    
        if (ident == 'Óbito'):
            self.identif = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
            self.sarq = "Obitos.csv"
            
        if (ident == 'Curados'):
            self.identif = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
            self.sarq = "curados.csv"
    
    def Salvar_Dados(self):
        urlretrieve(self.identif, self.sarq)
    
      
    def Pais(self,nome):
        dataframe_covid = pd.read_csv(self.sarq) 
        dataframe_covid.head()
        dataframe_covid.drop(['Lat','Long'], axis=1, inplace=True)
        country = dataframe_covid.groupby('Country/Region').sum()
        s_local = country.loc[nome]
        s_local =  s_local[s_local > 0]
        self.S_local = s_local
        tamanho = len(s_local)
        plt.figure(figsize=(14,8))
        plt.bar(s_local.index[0:tamanho], s_local.values[0:tamanho])
        plt.title('Primeiro caso data :{} '.format(s_local.index[0]))

    def PaisEx(self,nome, inic, fim):
        
        dataframe_covid = pd.read_csv(self.sarq) 
        dataframe_covid.head()
        dataframe_covid.drop(['Lat','Long'], axis=1, inplace=True)
        country = dataframe_covid.groupby('Country/Region').sum()
        s_local = country.loc[nome]
        
        s_local =  s_local[s_local > 0]
        self.S_local = s_local
        plt.figure(figsize=(14,8))
        plt.xticks(rotation=60)
        plt.bar(s_local.index[int(inic):fim], s_local.values[inic:fim])
        plt.title('Primeiro caso data :{} - {} - {}'.format(s_local.index[0], self.sarq, s_local.values[int(fim)]))
        plt.show()