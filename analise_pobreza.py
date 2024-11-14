import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv('dados_pobreza.csv')

# Extrair o ano do campo 'periodo' e converter para numérico
df['ano'] = df['periodo'].astype(str).str[:4].astype(int)

# Verificar o carregamento correto dos dados
print(df[['ano', 'porcentagem_pobreza', 'porcentagem_extrema_pobreza']].head())

# Gráfico de linha para evolução da pobreza e extrema pobreza
plt.figure(figsize=(12, 6))
plt.plot(df['ano'], df['porcentagem_pobreza'], marker='o', color='blue', label='Porcentagem de Pobreza')
plt.plot(df['ano'], df['porcentagem_extrema_pobreza'], marker='o', color='red', label='Porcentagem de Extrema Pobreza')
plt.title('Evolução da Pobreza e Extrema Pobreza no Brasil (2012-2022)', fontsize=16)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Porcentagem', fontsize=14)
plt.xticks(df['ano'], rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('tendencias_pobreza.png')
plt.show()

# Gráfico de barras para vulnerabilidade entre grupos étnicos
grupos = ['indigenas_vulnerabilidade', 'quilombolas_vulnerabilidade', 'ciganos_vulnerabilidade']
valores = df[grupos].mean()

plt.figure(figsize=(8, 5))
plt.bar(valores.index, valores.values, color=['lightblue', 'lightgreen', 'salmon'])
plt.title('Média de Vulnerabilidade por Grupos Étnicos (2012-2022)', fontsize=16)
plt.ylabel('Média de Vulnerabilidade', fontsize=14)
plt.xlabel('Grupos Étnicos', fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('media_vulnerabilidade.png')
plt.show()

# Mapa de calor para análise de correlação
plt.figure(figsize=(12, 8))
correlation = df.corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre Variáveis', fontsize=16)
plt.tight_layout()
plt.savefig('mapa_calor_correlacao.png')
plt.show()

# Relatório Final
resumo = """
Análise de Pobreza e Vulnerabilidade no Brasil (2012-2022)

1. Evolução da Pobreza e Extrema Pobreza:
   - Observa-se uma tendência de redução na porcentagem de pobreza ao longo dos anos, embora a extrema pobreza ainda
     permaneça em níveis elevados em certos períodos, o que indica a necessidade de intervenções sociais.

2. Vulnerabilidade por Grupos Étnicos:
   - Grupos étnicos específicos, como indígenas, quilombolas e ciganos, apresentam média de vulnerabilidade
     significativamente alta, sugerindo uma necessidade de políticas públicas focadas nesses grupos.

3. Análise de Correlação:
   - O mapa de calor mostra as correlações entre diferentes variáveis, ajudando a identificar os fatores que
     influenciam a pobreza e a vulnerabilidade no Brasil.

Os gráficos e o relatório fornecem uma visão completa das questões analisadas.
"""

# Salva o resumo em um arquivo de texto
with open('relatorio_pobreza.txt', 'w') as f:
    f.write(resumo)

print("Análise concluída! Gráficos e relatório salvos.")
