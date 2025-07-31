import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados
df = pd.read_csv('acidentes.csv')

# Mostrar as primeiras linhas
print("Dados iniciais:")
print(df.head())

# Contar os tipos de acidente
contagem = df['tipo_acidente'].value_counts()
print("\nAcidentes por tipo:")
print(contagem)

# Plotar gráfico
contagem.plot(kind='bar', title='Acidentes por Tipo')
plt.xlabel('Tipo de Acidente')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()