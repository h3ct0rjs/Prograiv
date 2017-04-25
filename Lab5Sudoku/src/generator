import sys
import types

if sys.version_info[0] > 2:  # Python 3+
    create_bound_method = types.MethodType
else:
    def create_bound_method(func, obj):
        return types.MethodType(func, obj, obj.__class__)

class StrategyExample:
    def __init__(self, func=None):
        self.name = "Strategy Example 0"
        if func:
             self.execute = create_bound_method(func, self)

    def execute(self):
        print(self.name)

def executeReplacement1(self):
    print(self.name + " from execute 1")

def executeReplacement2(self):
    print(self.name + " from execute 2")

if __name__ == "__main__":
    strat0 = StrategyExample()
    strat1 = StrategyExample(executeReplacement1)
    strat1.name = "Strategy Example 1"
    strat2 = StrategyExample(executeReplacement2)
    strat2.name = "Strategy Example 2"

    strat0.execute()
    strat1.execute()
    strat2.execute()