#Sample of strategypattern
class StrategyGenerator:
    def __init__(self, func=None):
        if func:
             self.execute = func

    def execute(self):
        print("Easy One Challenge")

def executeMedium():
    print("Medium")
    return 'Yo retornando desde medium'

def executeHardcore():
    print("HardCore Sudoku Challenge")

def executeInsane():
    print("Insane Sudoku")

if __name__ == "__main__":
    choice=input("?")
    if choice=='1':
        strat0 = StrategyGenerator()
    elif choice=='2':
        strat0 = StrategyGenerator(executeMedium)
    elif choice =='3' :
        strat0 = StrategyGenerator(executeHardcore)
    elif choice=='4':
        strat0 = StrategyGenerator(executeInsane)
    else:
        strat0 = StrategyGenerator()

    x=strat0.execute()
    print(x)
