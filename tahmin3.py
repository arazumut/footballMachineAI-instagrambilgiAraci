import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Produced By K. Umut Araz

class SkorTahmin:
    def __init__(self):
        self.ev_Sahibi = []
        self.deplasman = []
        self.tarayici = webdriver.Firefox(service=webdriver.FirefoxService(r'C:\Users\arazu\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'))  # Replace with your GeckoDriver path
        self.tarayici.get("https://istatistik.nesine.com/p1/1568476")
        time.sleep(5)

        self.data = self.extract_data()  # Combine data extraction into a single method

        self.model = LinearRegression()
        self.model.fit(np.array(self.data['ev_Sahibi']).reshape(-1, 1), np.array(self.data['deplasman']).reshape(-1, 1))

        self.tarayici.quit()

        self.ev_sahibi_Skor = self.model.predict(np.array(self.data['ev_Sahibi']).reshape(-1, 1))
        self.deplasman_skor = self.model.predict(np.array(self.data['deplasman']).reshape(-1, 1))

        self.grafik_evsahibi_deplasman()

    def extract_data(self):
        self.tablo_1()
        self.tablo_2()
        return {'ev_Sahibi': self.ev_Sahibi, 'deplasman': self.deplasman}

    def tablo_1(self):
        # Implement the logic for extracting the first table
        pass

    def tablo_2(self):
        # Implement the logic for extracting the second table
        pass

    def grafik_evsahibi_deplasman(self):
        plt.subplot(1, 2, 1)
        plt.title("Ev Sahibi Goller", loc='left')
        plt.plot(self.ev_sahibi_Skor, color="red")
        plt.subplot(1, 2, 2)
        plt.title("Deplasman Goller", loc='left')
        plt.plot(self.deplasman_skor, color="green")
        plt.show()

if __name__ == "__main__":
    tahmin = SkorTahmin()
