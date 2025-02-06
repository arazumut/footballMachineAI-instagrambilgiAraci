import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Produced By K. Umut Araz

class ScorePrediction:
    def __init__(self):
        self.home_team = []
        self.away_team = []
        self.browser = webdriver.Firefox(service=webdriver.FirefoxService(r'C:\Users\arazu\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'))  # Replace with your GeckoDriver path
        self.browser.get("https://istatistik.nesine.com/p1/1568476")
        time.sleep(5)

        self.data = self.extract_data()  # Combine data extraction into a single method

        self.model = LinearRegression()
        self.model.fit(np.array(self.data['home_team']).reshape(-1, 1), np.array(self.data['away_team']).reshape(-1, 1))

        self.browser.quit()

        self.home_team_score = self.model.predict(np.array(self.data['home_team']).reshape(-1, 1))
        self.away_team_score = self.model.predict(np.array(self.data['away_team']).reshape(-1, 1))

        self.plot_home_away()

    def extract_data(self):
        self.table_1()
        self.table_2()
        return {'home_team': self.home_team, 'away_team': self.away_team}

    def table_1(self):
        try:
            first_team = self.get_tables()
            first_team = first_team.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTableFirst"]')
            # Add more code to process the first team data
        except Exception as e:
            print(f"Error in table_1: {e}")

    def table_2(self):
        try:
            second_team = self.get_tables()
            second_team = second_team.find_element(By.CSS_SELECTOR, '[data-test-id="LastMatchesTableSecond"]')
            # Add more code to process the second team data
        except Exception as e:
            print(f"Error in table_2: {e}")

    def get_tables(self):
        # Add code to get the tables from the webpage
        pass

    def plot_home_away(self):
        plt.plot(self.home_team, self.home_team_score, label='Home Team')
        plt.plot(self.away_team, self.away_team_score, label='Away Team')
        plt.xlabel('Matches')
        plt.ylabel('Scores')
        plt.title('Home vs Away Team Scores')
        plt.legend()
        plt.show()