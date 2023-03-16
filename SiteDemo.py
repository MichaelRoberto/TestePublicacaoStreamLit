# executar ==> streamlit run teste.py
# executar dentro do Prompt do Anaconda (funciona no DOS também) - tem que estar dentro da pasta da aplicação

import streamlit as st

# pip list
# streamlit 1.13.0


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import datetime
from pathlib import Path
import plotly
import plotly.figure_factory as ff
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
from prophet.plot import plot_cross_validation_metric
import cmdstanpy
'''


def homepage():
    st.title('CONCORRÊNCIA ENTRE PROCESSOS')
    st.write('')
    st.write('')    
    st.header('Análise do impacto de concorrências e comparativos entre processos concorrentes')
    #st.subheader('Predição Geral / Predição por Data')
    st.write('')
    st.write('')    
    st.markdown('## Conteúdo:')   
    st.markdown('#### Gráfico com os tempos originais')   
    st.markdown('#### Gráfico com os tempos preditos')   
    st.markdown('#### Gráfico com a predição por data específica')           
    st.markdown('#### Painel de configuração Treino/Teste')               
   

def aboutAjuda():
    st.header('ABOUT / AJUDA')
    st.markdown('# ')       
    st.markdown('##### O foco desta aplicação é funcionar como uma "ferramenta" para construção de um protótipo de avaliação de concorrências de processos.')      
    st.markdown('##### As principais funcionalidades são mostrar os períodos de processos concorrentes, seja geral ou com predições, além de escolher a massa Treino/Teste para avaliar o comportamento do modelo.')      
    st.markdown('#### ')      
    st.markdown('#### ')              

    
    # trabalhando com Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Gráfico com tempos originais", "Gráfico com tempos preditos",  "Gráfico com predição por data específica", "Painel de configuração Treino/Teste"])

    tab1.subheader("Gráfico com os tempos originais")
    tab1.write('Esta parte mostra o gráfico de todos os processos durante todo período existente.')
    tab1.write('')
    tab1.write('É possível "selecionar" trechos de períodos dando zoom para ver a concorrência com mais detalhes informativos sobre o início/fim de execução.')
    
    tab2.subheader("Gráfico com os tempos preditos")
    tab2.write('Esta parte mostra o gráfico de todos os processos levando em conta a proporção Treino/Teste para montar a proporção de datas que serão preditas.')
    tab2.write('')
    tab2.write('Proporções:')
    tab2.write('2/3 (67% Treino / 33% Teste)')
    tab2.write('3/4 (75% Treino / 25% Teste)')        
    tab2.write('9/10 (90% Treino / 10% Teste)')    
    tab2.write('')
    tab2.write('É possível "selecionar" trechos de períodos dando zoom para ver a concorrência com mais detalhes informativos sobre o início/fim de execução.')

    tab3.subheader("Gráfico com predição por data específica")
    tab3.write('Esta parte mostra somente o gráfico de processos apenas do dia escolhido em tela.')
    tab3.write('No caso da Rotina 01, é mostrado o período original e o período predito do modelo')    
    tab3.write('No caso da Rotina 04 (que em tese é a rotina afetada pela Rotina 01), é mostrado o período original e a predição da Rotina 04, levando em conta o horário de início digitado em tela')
    tab3.write('')    
    tab3.write('É possível "selecionar" trechos de períodos dando zoom para ver a concorrência com mais detalhes informativos sobre o início/fim de execução.')
        
    tab4.subheader("Painel de configuração Treino/Teste")
    tab4.write('Esta é a parte responsável pela configuração Treino/Teste de acordo com a proporção indicada.')
    tab4.write('')    
    tab4.write('Proporções:')
    tab4.write('2/3 (67% Treino / 33% Teste)')
    tab4.write('3/4 (75% Treino / 25% Teste)')        
    tab4.write('9/10 (90% Treino / 10% Teste)')    
    tab4.write('')
    tab4.write('Para cada proporção será mostrado o RMSE apurado.')    
    tab4.write('RMSE: Root Mean Squared Error / Raiz do Erro Quadrático Médio --> Quanto menor o valor, melhor')  
 

def main():

    # sidebar
    options = ['Homepage', 'About/Ajuda', 'Testes']
    page_option = st.sidebar.selectbox('Options', options)
    if page_option == 'Homepage':
        homepage()
    elif page_option == 'About/Ajuda':
        aboutAjuda()
    else:
        teste()        

def teste():
    #a
    True    

main()




