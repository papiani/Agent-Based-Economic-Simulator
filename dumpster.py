class LaborerWorker:
    def __init__(self, id, wage):
        self.id = id
        self.wage = wage
        self.employed = False

    def work(self):
        if self.employed:
            print(f"Laborer {self.id} is working and earning {self.wage}.")
        else:
            print(f"Laborer {self.id} is unemployed.")

class Firm:
    def __init__(self, id, budget):
        self.id = id
        self.budget = budget
        self.employees = []

    def hire(self, worker):
        if self.budget >= worker.wage:
            self.employees.append(worker)
            worker.employed = True
            self.budget -= worker.wage
            print(f"Firm {self.id} hired Laborer {worker.id}.")
        else:
            print(f"Firm {self.id} cannot afford to hire Laborer {worker.id}.")

    def operate(self):
        for worker in self.employees:
            worker.work()
def main():
    # Create laborers
    laborers = [LaborerWorker(i, wage=100) for i in range(500000)]

    # Create firms
    firms = [Firm(i, budget=300) for i in range(200)]

    # Firms hire laborers
    for firm in firms:
        for laborer in laborers:
            firm.hire(laborer)

    # Firms operate
    for firm in firms:
        firm.operate()

if __name__ == "__main__":
    main()
