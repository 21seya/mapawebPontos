import folium
import pandas as pd

# as coordenadas do mapa aqui é do Brasil
map = folium.Map([-15.77972, -47.92972], zoom_start=4)

#ler os um arquivo em json
arq_json = 'Brasil.json'
#ler dados em csv
dados = pd.read_csv('Indicadores_de_Qualidade_de_Água_2001_a_2014__Média_do_Último_Ano_da_Série_de_Fósforo_Total.csv',sep=',')

lat = dados['LATITUDE'][:2405].values
lon = dados['LONGITUDE'][:2405].values
coord = []
for la,lo in zip(lat,lon):
    folium.Marker([la,lo],popup='<i>'+dados['UF']+'/'+dados['ENTIDADE_R']+'/'+dados['CORPO_DAGU']+'</i><br/>Rios poluidos:'+str(dados['AMBIENTE']),
    tooltip=dados['UF']+'/'+dados['ENTIDADE_R']+'/'+dados['CORPO_DAGU']).add_to(map)
    coord.append(['UF'])

    #columns=['UF','NU1FOSFORO','ME1FOSFORO','MI1FOSFORO','MA1FOSFORO','SD1FOSFORO','LATITUDE','LONGITUDE'],
  
#cria o map no html
map.save('mapa.html')