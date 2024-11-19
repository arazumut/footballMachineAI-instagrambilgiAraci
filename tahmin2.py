from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Produced By K. Umut Araz

class  SkorTahmin():
    def __init__(self):
        self.ev_Sahibi = []
        self.deplasman = []
        
        self.tarayici = webdriver.Firefox(service=webdriver.FirefoxService(r'C:\Users\arazu\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'))
        self.tarayici.get("https://istatistik.nesine.com/1573371/ozet") # => Analiz edilecek maçın istatisitikler sayfasının linkini giriniz 
        time.sleep(5)
        self.tablo_1()
        self.tablo_2()
        self.tarayici.close()
        self.ev_sahibi_Skor = []
        self.deplasman_skor = []
        self.adim1_()
        self.adim_2()
        self.ev_Shabi_tahimi()
        
        self.deplasman_tahmin()
        self.grafik_evsahibi_deplasman()

    def tablolar_(self):
        return self.tarayici.find_element(By.CLASS_NAME,'e67a6cb121a2998f0608 ')



if __name__ == "__main__":
    tahmin = SkorTahmin()
