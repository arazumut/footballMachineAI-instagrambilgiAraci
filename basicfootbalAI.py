import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


veri = pd.read_csv("understat_per_game.csv")





print(veri.head())


X = veri.drop("gol_sayisi", axis=1)
y = veri["gol_sayisi"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)



mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
