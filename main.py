import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("bloodtrack_dados_historicos.csv")

cols1 = ["traumas_emergencia", "cirurgias_eletivas"]
X = df[cols1]
y = df["bolsas_o_neg_consumidas"]

reg = LinearRegression()
reg.fit(X, y)

# classificador
cols2 = ["traumas_emergencia", "cirurgias_eletivas", "bolsas_o_neg_consumidas"]
X2 = df[cols2]

le = LabelEncoder()
y2 = le.fit_transform(df["risco_falta_o_neg"])

clf = LogisticRegression(max_iter=1000)
clf.fit(X2, y2)

# teste 48h
estoque = 6
traumas = 14
cirurgias = 8

# predicoes
x_novo = pd.DataFrame([[traumas, cirurgias]], columns=cols1)
gasto = float(reg.predict(x_novo)[0])

x_risco = pd.DataFrame([[traumas, cirurgias, gasto]], columns=cols2)
idx = clf.predict(x_risco)[0]
risco_pred = le.inverse_transform([idx])[0]

# debug 
print("--- Relatório O- ---")
print(f"Estoque disponível: {estoque} bolsas")
print(f"Previsão para 48h: {gasto:.1f} bolsas")
print(f"Status atual: {risco_pred}")

print("\nVerificação de cenário:")
print(f"- Risco crítico? {'Sim' if risco_pred == 'Critico' else 'Não'}")
print(f"- Eletivas > 5? {'Sim' if cirurgias > 5 else 'Não'} ({cirurgias})")
print(f"- Estoque insuficiente? {'Sim' if gasto > estoque else 'Não'}")

print("\nDecisão automática:")
if risco_pred == "Critico" and cirurgias > 5:
    r = "R1"
    print("-> Ação: Suspender as cirurgias eletivas e acionar doadores com urgência.")
elif risco_pred == "Alerta" and cirurgias <= 5:
    r = "R2"
    print("-> Ação: Manter o calendário e avisar os doadores preventivamente.")
elif risco_pred == "Normal":
    r = "R3"
    print("-> Ação: Fluxo normal mantido.")
else:
    r = "Nenhuma"
    print("-> Nenhuma regra automática atendida. Repassar para aprovação da chefia.")

print(f"Regra acionada: {r}\n")

# grafico 
plt.plot(df["dia"], df["bolsas_o_neg_consumidas"], marker="x", color="red")
plt.title("Histórico O-")
plt.show()