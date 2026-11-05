
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =====================================
# 1. CARREGAR A BASE DE DADOS
# =====================================

caminho = Path(__file__).resolve().parent.parent / "dados" / "base_ficticia_clinica_estetica.csv"

dados = pd.read_csv(caminho, encoding="utf-8-sig")

print("BASE DE DADOS")
print(dados.head())

print("\nDIMENSÕES DA BASE:")
print(dados.shape)

# =====================================
# 2. PROCEDIMENTOS DA CLÍNICA
# =====================================

print("\nPROCEDIMENTOS DA CLÍNICA:")
print(dados["procedimento"].unique())

# =====================================
# 3. FATURAMENTO POR PROCEDIMENTO
# =====================================

faturamento = dados.groupby("procedimento")["valor_cobrado_brl"].sum()
faturamento = faturamento.sort_values(ascending=False)

print("\nFATURAMENTO POR PROCEDIMENTO:")
print(faturamento)

# =====================================
# 4. LUCRO ESTIMADO
# =====================================

dados["lucro"] = dados["valor_cobrado_brl"] - dados["custo_variavel_estimado_brl"]

lucro_procedimento = dados.groupby("procedimento")["lucro"].sum()
lucro_procedimento = lucro_procedimento.sort_values(ascending=False)

print("\nLUCRO POR PROCEDIMENTO:")
print(lucro_procedimento)

# =====================================
# 5. PACIENTES POR CANAL DE AQUISIÇÃO
# =====================================

pacientes_canal = dados.groupby("canal_aquisicao")["paciente_id"].nunique()
pacientes_canal = pacientes_canal.sort_values(ascending=False)

print("\nPACIENTES POR CANAL DE AQUISIÇÃO:")
print(pacientes_canal)

# =====================================
# 6. ANÁLISE DE MARKETING
# =====================================

melhor_canal = pacientes_canal.idxmax()
maior_quantidade = pacientes_canal.max()

print("\nANÁLISE DE MARKETING:")
print(f"O canal com maior quantidade de pacientes foi {melhor_canal}, com {maior_quantidade} pacientes.")

# =====================================
# 7. GRÁFICO DE PACIENTES POR CANAL
# =====================================

plt.figure(figsize=(8, 5))

pacientes_canal.plot(kind="bar")

plt.title("Quantidade de pacientes por canal de aquisição")
plt.xlabel("Canal de aquisição")
plt.ylabel("Quantidade de pacientes")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar gráfico automaticamente
pasta_documentacao = Path(__file__).resolve().parent.parent / "documentacao"
pasta_documentacao.mkdir(exist_ok=True)

plt.savefig(pasta_documentacao / "grafico_pacientes_por_canal.png")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =====================================
# 1. CARREGAR A BASE DE DADOS
# =====================================

caminho = Path(__file__).resolve().parent.parent / "dados" / "base_ficticia_clinica_estetica.csv"

dados = pd.read_csv(caminho, encoding="utf-8-sig")

print("BASE DE DADOS")
print(dados.head())

print("\nDIMENSÕES DA BASE:")
print(dados.shape)

# =====================================
# 2. PROCEDIMENTOS DA CLÍNICA
# =====================================

print("\nPROCEDIMENTOS DA CLÍNICA:")
print(dados["procedimento"].unique())

# =====================================
# 3. FATURAMENTO POR PROCEDIMENTO
# =====================================

faturamento = dados.groupby("procedimento")["valor_cobrado_brl"].sum()
faturamento = faturamento.sort_values(ascending=False)

print("\nFATURAMENTO POR PROCEDIMENTO:")
print(faturamento)

# =====================================
# 4. LUCRO ESTIMADO
# =====================================

dados["lucro"] = dados["valor_cobrado_brl"] - dados["custo_variavel_estimado_brl"]

lucro_procedimento = dados.groupby("procedimento")["lucro"].sum()
lucro_procedimento = lucro_procedimento.sort_values(ascending=False)

print("\nLUCRO POR PROCEDIMENTO:")
print(lucro_procedimento)

# =====================================
# 5. PACIENTES POR CANAL DE AQUISIÇÃO
# =====================================

pacientes_canal = dados.groupby("canal_aquisicao")["paciente_id"].nunique()
pacientes_canal = pacientes_canal.sort_values(ascending=False)

print("\nPACIENTES POR CANAL DE AQUISIÇÃO:")
print(pacientes_canal)

# =====================================
# 6. ANÁLISE DE MARKETING
# =====================================

melhor_canal = pacientes_canal.idxmax()
maior_quantidade = pacientes_canal.max()

print("\nANÁLISE DE MARKETING:")
print(f"O canal com maior quantidade de pacientes foi {melhor_canal}, com {maior_quantidade} pacientes.")

# =====================================
# 7. GRÁFICO DE PACIENTES POR CANAL
# =====================================

plt.figure(figsize=(8, 5))

pacientes_canal.plot(kind="bar")

plt.title("Quantidade de pacientes por canal de aquisição")
plt.xlabel("Canal de aquisição")
plt.ylabel("Quantidade de pacientes")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar gráfico automaticamente
pasta_documentacao = Path(__file__).resolve().parent.parent / "documentacao"
pasta_documentacao.mkdir(exist_ok=True)

plt.savefig(pasta_documentacao / "grafico_pacientes_por_canal.png")

plt.show()
