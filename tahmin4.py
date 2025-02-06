from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Produced By K. Umut Araz

class ScorePrediction:
    
    def __init__(self):
        self.home_team = []
        self.away_team = []
        self.browser = webdriver.Firefox(service=webdriver.FirefoxService(r'C:\Users\arazu\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'))
        self.browser.get("https://istatistik.nesine.com/1573371/ozet")  # URL of the match statistics page
        time.sleep(5)
        self.table_1()
        self.table_2()
        self.browser.close()
        self.home_team_score = []
        self.away_team_score = []
        self.step_1()
        self.step_2()
        self.predict_home_team()
        self.predict_away_team()
        self.plot_home_away()    
    
    def get_tables(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.js-team-stats')

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

    def step_1(self):
        # Add code for step 1
        pass

    def step_2(self):
        # Add code for step 2
        pass

    def predict_home_team(self):
        # Add code to predict home team score
        pass

    def predict_away_team(self):
        # Add code to predict away team score
        pass

    def plot_home_away(self):
        plt.plot(self.home_team, self.home_team_score, label='Home Team')
        plt.plot(self.away_team, self.away_team_score, label='Away Team')
        plt.xlabel('Matches')
        plt.ylabel('Scores')
        plt.title('Home vs Away Team Scores')
        plt.legend()
        plt.show()