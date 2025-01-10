from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Produced By K. Umut Araz

class SkorTahmin:
    def __init__(self):
        self.ev_Sahibi = []
        self.deplasman = []
        self.ev_sahibi_Skor = []
        self.deplasman_skor = []

        try:
            self.tarayici = webdriver.Firefox(service=webdriver.firefox.service.Service(r'C:\Users\arazu\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'))
            self.tarayici.get("https://istatistik.nesine.com/1573371/ozet")  # URL of the match statistics page
            time.sleep(5)
            self.tablo_1()
            self.tablo_2()
        except Exception as e:
            print(f"Error initializing WebDriver: {e}")
        finally:
            self.tarayici.quit()

        self.adim1_()
        self.adim_2()
        self.ev_sahibi_tahmini()
        self.deplasman_tahmin()
        self.grafik_evsahibi_deplasman()

    def tablo_1(self):
        try:
            birinci_takim = self.tablolar_()
            birinci_takim = birinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTableFirst"]')
            birinci_takim_adi = birinci_takim.find_element(By.TAG_NAME, "a").get_attribute("text")
            self.ev_Sahibi.append(birinci_takim_adi)
            skorlar = birinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTable"]').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
            for i in skorlar:
                kontrol = i.find_element(By.CSS_SELECTOR, '[data-test-id="TableBodyMatch"]')
                ev_sahibi = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="HomeTeam"]').text
                deplasman = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="AwayTeam"]').text
                skor = kontrol.find_element(By.CSS_SELECTOR, '[data-testid="nsn-button"]').find_element(By.TAG_NAME, "span").text
                if skor:
                    self.ev_Sahibi.append(f"{ev_sahibi}/{skor}/{deplasman}")
        except Exception as e:
            print(f"Error extracting table 1: {e}")

    def tablo_2(self):
        try:
            ikinci_takim = self.tablolar_()
            ikinci_takim = ikinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTableSecond"]')
            ikinci_takim_adi = ikinci_takim.find_element(By.TAG_NAME, "a").get_attribute("text")
            self.deplasman.append(ikinci_takim_adi)
            skorlar = ikinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTable"]').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
            for i in skorlar:
                kontrol = i.find_element(By.CSS_SELECTOR, '[data-test-id="TableBodyMatch"]')
                ev_sahibi = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="HomeTeam"]').text
                deplasman = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="AwayTeam"]').text
                skor = kontrol.find_element(By.CSS_SELECTOR, '[data-testid="nsn-button"]').find_element(By.TAG_NAME, "span").text
                if skor:
                    self.deplasman.append(f"{ev_sahibi}/{skor}/{deplasman}")
        except Exception as e:
            print(f"Error extracting table 2: {e}")

    def adim1_(self):
        for i in self.ev_Sahibi[1:]:
            try:
                ayir = str(i).split("/")
                indexi = ayir.index(self.ev_Sahibi[0])
                if indexi == 0:
                    t = ayir[1].split("-")[0].strip()
                    self.ev_sahibi_Skor.append(int(t))
                elif indexi == 2:
                    t = ayir[1].split("-")[1].strip()
                    self.ev_sahibi_Skor.append(int(t))
            except ValueError:
                continue

    def adim_2(self):
        for i in self.deplasman[1:]:
            try:
                ayir = str(i).split("/")
                indexi = ayir.index(self.deplasman[0])
                if indexi == 0:
                    t = ayir[1].split("-")[0].strip()
                    self.deplasman_skor.append(int(t))
                elif indexi == 2:
                    t = ayir[1].split("-")[1].strip()
                    self.deplasman_skor.append(int(t))
            except ValueError:
                continue

    def ev_sahibi_tahmini(self):
        veri_kumesi = np.array(self.ev_sahibi_Skor[::-1]).reshape(-1, 1)
        x = np.arange(len(veri_kumesi)).reshape(-1, 1)
        model = LinearRegression()
        model.fit(x, veri_kumesi)
        gelecekteki_mac_sayisi = len(veri_kumesi) + 1
        tahmin_edilen_gol = model.predict([[gelecekteki_mac_sayisi]])[0][0]
        print(f"Gelecekteki gol tahmini ev sahibi: {tahmin_edilen_gol}")

    def deplasman_tahmin(self):
        veri_kumesi = np.array(self.deplasman_skor[::-1]).reshape(-1, 1)
        x = np.arange(len(veri_kumesi)).reshape(-1, 1)
        model = LinearRegression()
        model.fit(x, veri_kumesi)
        gelecekteki_mac_sayisi = len(veri_kumesi) + 1
        tahmin_edilen_gol = model.predict([[gelecekteki_mac_sayisi]])[0][0]
        print(f"Gelecekteki gol tahmini deplasman: {tahmin_edilen_gol}")

    def grafik_evsahibi_deplasman(self):
        plt.subplot(1, 2, 1)
        plt.title("Ev Sahibi Goller", loc='left')
        plt.plot(self.ev_sahibi_Skor[::-1], color="red")
        plt.subplot(1, 2, 2)
        plt.title("Deplasman Goller", loc='left')
        plt.plot(self.deplasman_skor[::-1], color="green")
        plt.show()

    def tablolar_(self):
        return self.tarayici.find_element(By.CLASS_NAME, 'e67a6cb121a2998f0608')

if __name__ == "__main__":
    tahmin = SkorTahmin()
