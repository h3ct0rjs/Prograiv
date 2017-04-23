#test app using observable pattern , 
#resource:http://www.giantflyingsaucer.com/blog/?p=5117
from util import Observer, Observable 

class AmericanMarket(Observer):
    def update(self,*args,**kwargs):
        print("American Market received: {0}\n {1}".format(args,kwargs))

class EuropeanMarket(Observer):
    def update(self,*args,**kwargs):
        print("European Market received: {0}\n {1}".format(args,kwargs))

if __name__ == '__main__':
    objectoobservado=Observable()
    usaobserver=AmericanMarket()
    objectoobservado.add_observer(usaobserver)
    euobserver=AmericanMarket()
    objectoobservado.add_observer(euobserver)
    objectoobservado.notify_observers('Hallo',some='hey kwars')
    print("So easy to notify multiple objects that observ one observable")
