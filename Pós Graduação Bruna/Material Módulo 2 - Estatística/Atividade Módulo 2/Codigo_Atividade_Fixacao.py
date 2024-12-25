
############################################################################################################
###########         Atividade de Fixação - Análise Estatística de Dados #####################################
   #############                      #################################
############################################################################################################

#Os pacotes a serem importados devem estar instalados

#Forma o conjunto de dados historico contendo vinte locacoes sorteadas aleatoriamente do banco de dados e a armazena
#em um data frame chamado dados

import pandas as pd
import matplotlib.pyplot as plt

# Dados em um dicionário
dados = {
    "Preco": [368.384514890573, 446.850186825816, 414.72765691978, 434.291090918223, 
              436.652686535348, 457.65797344255, 490.694346597566, 474.881781399868, 
              458.462395897205, 412.719412673294, 448.799032112411, 352.040747235864, 
              449.461858221104, 416.150953927119, 416.499426750268, 551.315803331779, 
              462.126789471159, 515.957335395508, 467.598697162974, 339.548470369391],
    "Portas": ["duas_portas", "quatro_portas", "duas_portas", "quatro_portas", "quatro_portas", 
               "duas_portas", "quatro_portas", "duas_portas", "quatro_portas", "duas_portas", 
               "quatro_portas", "quatro_portas", "duas_portas", "quatro_portas", "duas_portas", 
               "quatro_portas", "quatro_portas", "duas_portas", "quatro_portas", "quatro_portas"],
    "Ar_Condicionado": ["sem_ar_condicionado", "com_ar_condicionado", "com_ar_condicionado", 
                        "com_ar_condicionado", "com_ar_condicionado", "com_ar_condicionado", 
                        "com_ar_condicionado", "com_ar_condicionado", "com_ar_condicionado", 
                        "com_ar_condicionado", "com_ar_condicionado", "sem_ar_condicionado", 
                        "com_ar_condicionado", "com_ar_condicionado", "com_ar_condicionado", 
                        "com_ar_condicionado", "com_ar_condicionado", "com_ar_condicionado", 
                        "com_ar_condicionado", "sem_ar_condicionado"],
    "Quadrimestre": ["segundo_quadrimestre", "segundo_quadrimestre", "segundo_quadrimestre", 
                     "segundo_quadrimestre", "segundo_quadrimestre", "terceiro_quadrimestre", 
                     "primeiro_quadrimestre", "primeiro_quadrimestre", "terceiro_quadrimestre", 
                     "segundo_quadrimestre", "terceiro_quadrimestre", "segundo_quadrimestre", 
                     "terceiro_quadrimestre", "segundo_quadrimestre", "segundo_quadrimestre", 
                     "primeiro_quadrimestre", "terceiro_quadrimestre", "primeiro_quadrimestre", 
                     "primeiro_quadrimestre", "segundo_quadrimestre"],
    "Idade_Locatario": [23, 18, 28, 21, 18, 21, 18, 20, 25, 29, 18, 33, 20, 21, 18, 21, 18, 20, 25, 29],
    "Quilometragem": [957.442780544097, 829.533278217768, 923.300215829467, 871.519116905113, 
                      930.704105677958, 554.696695914233, 501.941059782271, 665.435074822519, 
                      568.24079543466, 930.704105677958, 554.696695914233, 829.533278217768, 
                      665.435074822519, 871.519116905113, 930.704105677958, 351.547138218644, 
                      501.941059782271, 447.872006186523, 568.24079543466, 930.704105677958],
    "Dolar": [4.41147933990862, 5.63014407874318, 8.80557934010615, 4.260591319988649, 
              6.93416279643155, 1.61130694543154, 2.57813244655973, 4.66666728709914, 
              1.6846066723224, 7.33872353619711, 4.52300814589177, 2.96689816205009, 
              9.91448182957733, 8.55577847959413, 5.93424935955983, 5.55775429484673, 
              6.94475470863839, 4.74330294976712, 4.723306965757987, 4.7010894862212]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Exibir o DataFrame
print(df)




# Histograma do preço, só para ter uma idea
plt.figure(figsize=(10, 6))
plt.hist(df['Preco'], bins=10, edgecolor='black')
plt.title('Histograma do Preço')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

#1 Boxplot do preço
plt.figure(figsize=(10, 6))
plt.boxplot(df['Preco'], vert=True)
plt.title('Boxplot do Preço')
plt.xlabel('Preço')
plt.show()


#2 Plota boxplot com Preço por Quadrimestre
import seaborn as sns

sns.boxplot(x='Quadrimestre', y='Preco', data=df)
plt.show()



#3 Estatísticas descritivas do preço
descricao = df['Preco'].describe()
print(descricao)


#4 Não necessitam de código

#5 Dicas

#O pacote scipy.stats tem várias distribuições, como a normal
from scipy.stats import norm

#A normal tem dois parâmetros, média e desvio padrão
mean = 2500
sd = 170

#O comando norm.cdf(x, mean, sd) calcula a probabilidade acumulada da normal entre -infinito e x

# Calculando as probabilidades acumuladas
probabilidade_ate_2600 = norm.cdf(2600, mean, sd)
probabilidade_ate_2400 = norm.cdf(2400, mean, sd)

# Se eu quero a probabilidade acumulada entre 2400 e 2600, devo fazer a diferença
diferenca_probabilidade = probabilidade_ate_2600 - probabilidade_ate_2400

print(diferenca_probabilidade)

#Adaptar o código para o problema dado



