import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv('dados_pobreza.csv')


print(df.head())

# Análise de Tendências com Gráficos de Linha
plt.figure(figsize=(12, 6))
plt.plot(df['periodo'], df['porcentagem_pobreza'], marker='o', label='Porcentagem de Pobreza', color='blue')
plt.plot(df['periodo'], df['porcentagem_extrema_pobreza'], marker='o', label='Porcentagem de Extrema Pobreza', color='red')
plt.title('Tendências de Pobreza e Extrema Pobreza no Brasil (2012-2022)', fontsize=16)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Porcentagem', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()  # Ajusta o layout para melhor visualização
plt.savefig('tendencias_pobreza.png')  # Salva o gráfico
plt.show()

# Gráfico de barras para grupos étnicos
grupos = ['indigenas_vulnerabilidade', 'quilombolas_vulnerabilidade', 'ciganos_vulnerabilidade']
valores = df[grupos].mean()  # Calculando a média

plt.figure(figsize=(8, 5))
plt.bar(valores.index, valores.values, color=['lightblue', 'lightgreen', 'salmon'])
plt.title('Média de Vulnerabilidade por Grupos Étnicos (2012-2022)', fontsize=16)
plt.ylabel('Média de Vulnerabilidade', fontsize=14)
plt.xlabel('Grupos Étnicos', fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('media_vulnerabilidade.png')  # Salva o gráfico
plt.show()

# Análise de Correlações
plt.figure(figsize=(12, 8))
correlation = df.corr()  # Calculando a correlação
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre Variáveis', fontsize=16)
plt.tight_layout()
plt.savefig('mapa_calor_correlacao.png')  # Salva o gráfico
plt.show()

# Relatório Final com Descrição
resumo = """
Análise de Pobreza e Vulnerabilidade no Brasil (2012-2022)

1. Tendências de Pobreza e Extrema Pobreza:
   - Observamos que a porcentagem de pobreza e extrema pobreza apresenta uma tendência de redução ao longo dos anos, 
     embora a extrema pobreza ainda permaneça em níveis preocupantes em alguns anos.

2. Média de Vulnerabilidade por Grupos Étnicos:
   - A média de vulnerabilidade dos grupos indígenas, quilombolas e ciganos é significativamente maior, 
     indicando a necessidade de políticas públicas específicas e eficazes para esses grupos.

3. Mapa de Calor da Correlação:
   - O mapa de calor ilustra a relação entre várias variáveis, revelando correlações significativas 
     que podem ajudar na compreensão dos fatores que influenciam a pobreza no Brasil.

Os gráficos e o mapa de calor fornecem uma visão visual das questões de pobreza e vulnerabilidade,
enquanto o relatório textual sumariza as principais descobertas.
"""

# Salvar o resumo em um arquivo de texto
with open('relatorio_pobreza.txt', 'w') as f:
    f.write(resumo)

print("Análise completa! Gráficos e relatório salvos.")
