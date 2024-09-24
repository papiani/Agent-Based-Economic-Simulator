## PERSON
'''
Attributes:
1. gender
2. age
3. life expectancy (randomise based on healthcare quality)
4. assets (seperate class ... liquidity scale also implemented)
5. Happiness (reward parameter)
6. education (affects earn-rate, based on skills in demand)
7. Parents (inheritence tracking/ happiness tank when death)

Methods:
'''
## BRAIN OF PERSON
# This holds randomized parameters on behavioural/intrinsic tendencies of each human.
# These are intrinsic values of a person, acting as a multiplier on top of market conditions/ general consumer sentiment.
'''
Weights:
1. risk tolerance -> job-hopping / investment vs saving
2. Consumption utility -> happiness gained from spending
3. work ethic -> affects gradient of dimishing returns from work
'''

import numpy as np
import pandas as pd
import csv
from scipy.stats import norm
class person:
    def __init__(self, gender, age, lifespan, assets, happiness) -> None:
        pass

def initialise_wealth_distribution():
    # read data_in.csv in controls to load in starting values
    df = pd.read_csv('controls/data_in.csv', skipinitialspace=True)
    gini_coeff = df.loc[0, 'gini_coeff']
    mean_net_worth = df.loc[0, 'mean_net_worth']
    mean_yearly_salary = df.loc[0, 'mean_yearly_salary']
    population = df.loc[0, 'initial_population']

    # get N-distribution standard deviation from gini coefficient
    quantile = norm.ppf((gini_coeff + 1) / 2)
    std_dev = np.sqrt(2) * quantile

    # get distribution and make objects for 
    salary_distribution = np.random.normal(loc=mean_yearly_salary, scale=std_dev, size=population)
    net_worth_distribution = np.random.normal(loc=mean_net_worth, scale=std_dev, size=population)
    return (salary_distribution,net_worth_distribution)
