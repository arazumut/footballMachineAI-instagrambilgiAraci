import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

veri = pd.read_csv('understat_per_game.csv')

veri.dropna(inplace=True)

X = veri[['home_team_goal', 'away_team_goal']]
y = veri['toplam_olası_gol']  

# Produced By K. Umut Araz

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Ortalama Kare Hata (MSE):', mse)

takim1_skor = float(input("Ev sahibi takımın skorunu girin: "))
takim2_skor = float(input("Deplasman takımının skorunu girin: "))

tahmin = model.predict([[takim1_skor, takim2_skor]])
print('Tahmini Toplam Gol:', tahmin[0])
