from stakeholders.household import *

working_population = []
(salary,networth) = initialise_wealth_distribution()
for x in len(salary):
    worker = person(salary,networth)