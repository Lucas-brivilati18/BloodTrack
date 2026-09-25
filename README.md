BloodTrack 🩸

Sistema de análise e previsão de estoque de bolsas de sangue O- desenvolvido em Python.

📌 Sobre o projeto

O BloodTrack utiliza dados históricos para estimar o consumo de bolsas de sangue O- e identificar possíveis situações de risco de falta de estoque.

O sistema utiliza técnicas de Machine Learning para realizar:

Previsão do consumo de bolsas de sangue;
Classificação do risco de falta de bolsas O-;
Análise de cenários de emergência;
Geração de uma decisão automática de acordo com o nível de risco;
Visualização do histórico de consumo.

🛠️ Tecnologias utilizadas
Python
Pandas
Matplotlib
Scikit-learn

🤖 Modelos utilizados

O projeto utiliza dois modelos de Machine Learning:

Regressão Linear

Utilizada para estimar a quantidade de bolsas O- que poderá ser consumida a partir da quantidade de traumas em emergência e cirurgias eletivas.

Regressão Logística

Utilizada para classificar o risco de falta de bolsas O- em categorias como:

Normal
Alerta
Crítico

📊 Funcionamento

O programa carrega os dados históricos através de um arquivo CSV e utiliza essas informações para treinar os modelos.

Em seguida, é analisado um cenário de 48 horas, considerando:

Estoque disponível;
Número de traumas em emergência;
Número de cirurgias eletivas.

Com essas informações, o sistema realiza a previsão de consumo e classifica o nível de risco.

⚙️ Decisão automática

Após identificar o nível de risco, o sistema verifica algumas condições para determinar uma possível ação.

Entre as ações previstas estão:

Suspender cirurgias eletivas e acionar doadores com urgência;
Manter o calendário e avisar os doadores preventivamente;
Manter o fluxo normal;
Encaminhar o caso para aprovação da chefia.

As regras de decisão estão implementadas diretamente no código.

📈 Gráfico

Ao final da execução, o programa apresenta um gráfico com o histórico de consumo das bolsas O-.
