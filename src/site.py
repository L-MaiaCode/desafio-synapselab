from pathlib import Path

import streamlit as st
from analise import *

st.title('Análise das Vendas de Vídeo Games (1980 - 2024)')

descricao1= st.container(border=True)
descricao1.text(
    'A base de dados usada oferece uma visão detalhada do mercado global de videogames de ' \
    '1980 até o início de 2024. Ela combina metadados (plataforma, gênero, editora) ' \
    'com desempenho financeiro (vendas globais).'
    )

descricao2= st.container(border=True)
descricao2.text(
    'Essa análise terá o intuito de responder algumas perguntas, como:' \
    '\nQuais os gêneros mais vendidos❔' \
    '\nQuais os gêneros mais publicados❔' \
    '\nQuais os anos de pico das vendas de vídeo games❔' \
    '\nQuais editoras e títulos dominaram o mercado❔' \
    '\nQual a relação da nota crítica com as vendas de um título❔'
)

st.markdown(
    "<h2 style='text-align: center;'>Visualização dos Dados</h2>",
    unsafe_allow_html=True
)

# Gráfico 1 
st.subheader('1. Quais os gêneros mais vendidos?')

fig = generos_mais_vendidos()

st.pyplot(fig)

txt1 = st.container(border=False)
txt1.text(
    'Observa-se que os gêneros com maior volume de vendas são: ' \
    '\t\n🏆 Esportes' \
    '\t\n🥈 Ação' \
    '\t\n🥉 Shooter (jogos de tiro)'
)

# Gráfico 2
st.subheader('2. Quais os top gêneros mais produzidos?')

fig2 = generos_mais_produzidos()

st.pyplot(fig2)

txt2 = st.container(border=False)
txt2.text(
    'Nota-se que os gêneros mais produzidos tendem a acompanhar os mais vendidos, ' \
    'evidenciando a influência das grandes empresas em direcionar a produção para ' \
    'títulos com maior potencial comercial.'
)

# Gráfico 3
st.subheader('3. Linha do tempo do volume de vendas')

fig3 = anos_com_mais_vendas()

st.pyplot(fig3)

txt3 = st.container(border=False)
txt3.text(
    'Observa-se um crescimento gradual até o início dos anos 2000, ' \
    'seguido por uma forte expansão que atinge o pico por volta de 2008–2009.' \
    ' A partir desse período, há uma tendência de queda nas vendas,' \
    ' possivelmente associada a mudanças no mercado, como a transição ' \
    'para o digital e novos modelos de consumo.'
)

# Gráfico 4
st.subheader('4. Top 10 editoras com mais vendas')

fig4 = editoras_com_mais_vendas()

st.pyplot(fig4)

txt4 = st.container(border=False)
txt4.text(
    'Destaca-se a liderança da Activision, seguida por Electronic Arts e EA Sports.' \
    ' O ranking evidencia a forte concentração de mercado em grandes empresas, ' \
    'responsáveis pela maior parte das vendas globais de videogames.'
)

# Gráfico 5
st.subheader('5. Jogos mais vendidos')

fig5 = jogos_mais_vendidos()

st.pyplot(fig5)

txt5 = st.container(border=False)
txt5.text(
    'Destaca-se a liderança expressiva de GTA V ' \
    'entre os títulos mais vendidos. ' \
    'Além disso, observa-se que a franquia Call of Duty ' \
    'desempenha um papel central no desempenho comercial da Activision, ' \
    'sendo uma das principais responsáveis pelo seu sucesso em vendas.'
)

# Gráfico 6 - Interativo
st.markdown('---')
st.subheader('6. Top 10 jogos mais vendidos por Console')

descricao3 = st.container(border=True)
descricao3.text(
    'Selecione um console no menu abaixo para descobrir quais' \
    'foram os 10 jogos de maior sucesso daquela platafroma.'
)

consoles_disponiveis = obter_lista_consoles()

console_selecionado = st.selectbox(
    'Escolha a plataforma',
    consoles_disponiveis,
    index=0
)

fig6 = jogos_mais_vendidos_por_console(console_selecionado)

st.pyplot(fig6)

# Gráfico 7 - Interativo
st.markdown('---')
st.subheader('7. Comparação da timeline de vendas entre Consoles')

descricao4 = st.container(border=True)
descricao4.text(
    'Selecione os consoles no menu abaixo para comparar.' \
)

consoles_escolhidos = st.multiselect(
    'Consoles 🕹️',
    consoles_disponiveis,
    default=['PS', 'PS2', 'PS3', 'PS4']
)

fig7 = timeline_vendas_por_console(consoles_escolhidos)

if fig7:
    st.pyplot(fig7)

# Gráfico 8

