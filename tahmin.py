from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Produced By K. Umut Araz

class SkorTahmin:
    def __init__(self, ev_sahibi_takim="Girona", deplasman_takim="Alaves"):
        self.ev_sahibi_takim = ev_sahibi_takim
        self.deplasman_takim = deplasman_takim
        self.ev_Sahibi = []
        self.deplasman = []
        
        # Initialize WebDriver with error handling
        try:
            self.tarayici = webdriver.Firefox()
            self.tarayici.get("https://istatistik.nesine.com/1409407/son-maclari")  # URL of the match statistics page
            time.sleep(5)
            self.tablo_1()
            self.tablo_2()
        except Exception as e:
            print(f"Error initializing WebDriver or fetching data: {e}")
        finally:
            self.tarayici.close()
        
        self.ev_sahibi_Skor = []
        self.deplasman_skor = []
        self.adim1_()
        self.adim_2()
        self.ev_Shabi_tahimi()
        self.deplasman_tahmin()
        self.grafik_evsahibi_deplasman()
    
    def tablolar_(self):
        return self.tarayici.find_element(By.CLASS_NAME, 'e67a6cb121a2998f0608')

    def tablo_1(self):
        try:
            birinci_takim = self.tablolar_()
            birinci_takim = birinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTableFirst"]')
            birinci_takim_Adi = birinci_takim.find_element(By.TAG_NAME, "a").get_attribute("text")
            self.ev_Sahibi.append(birinci_takim_Adi)
            skorlar = birinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTable"]').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
            for i in skorlar:
                kontrol = i.find_element(By.CSS_SELECTOR, '[data-test-id="TableBodyMatch"]')
                ev_Sahibi = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="HomeTeam"]').text
                deplasman = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="AwayTeam"]').text
                skor = kontrol.find_element(By.CSS_SELECTOR, '[data-testid="nsn-button"]').find_element(By.TAG_NAME, "span").text
                if skor:
                    self.ev_Sahibi.append(f"{ev_Sahibi}/{skor}/{deplasman}")
        except Exception as e:
            print(f"Error extracting table 1: {e}")

    def tablo_2(self):
        try:
            ikinci_takim = self.tablolar_()
            ikinci_takim = ikinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTableSecond"]')
            ikinci_takim_Adi = ikinci_takim.find_element(By.TAG_NAME, "a").get_attribute("text")
            self.deplasman.append(ikinci_takim_Adi)
            skorlar = ikinci_takim.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTable"]').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
            for i in skorlar:
                kontrol = i.find_element(By.CSS_SELECTOR, '[data-test-id="TableBodyMatch"]')
                ev_Sahibi = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="HomeTeam"]').text
                deplasman = kontrol.find_element(By.CSS_SELECTOR, '[data-test-id="AwayTeam"]').text
                skor = kontrol.find_element(By.CSS_SELECTOR, '[data-testid="nsn-button"]').find_element(By.TAG_NAME, "span").text
                if skor:
                    self.deplasman.append(f"{ev_Sahibi}/{skor}/{deplasman}")
        except Exception as e:
            print(f"Error extracting table 2: {e}")

    def adim1_(self):
        for i in self.ev_Sahibi[1:]:
            try:
                ayır = str(i).split("/")
                indexi = ayır.index(self.ev_sahibi_takim)
                if indexi == 0:
                    t = ayır[1].split("-")[0].strip()
                    self.ev_sahibi_Skor.append(t)
                elif indexi == 2:
                    t = ayır[1].split("-")[1].strip()
                    self.ev_sahibi_Skor.append(t)
            except ValueError:
                continue

    def adim_2(self):
        for i in self.deplasman[1:]:
            try:
                ayır = str(i).split("/")
                indexi = ayır.index(self.deplasman_takim)
                if indexi == 0:
                    t = ayır[1].split("-")[0].strip()
                    try:
                        self.deplasman_skor.append(int(t))
                    except ValueError:
                        pass
                elif indexi == 2:
                    t = ayır[1].split("-")[1].strip()
                    try:
                        self.deplasman_skor.append(int(t))
                    except ValueError:
                        pass
            except ValueError:
                continue

    def ev_Shabi_tahimi(self):
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

if __name__ == "__main__":
    tahmin = SkorTahmin()
