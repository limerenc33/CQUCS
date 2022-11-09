class Account:
  def __init__(self,id='N/A',balance='N/A',annualinterestrate='N/A'):
    self.__id=id
    self.__balance=balance
    self.__annualinterestrate=annualinterestrate
  def getmonthlyinterestrate(self):
    monthlyinterestrate=(self._Account__annualinterestrate/100)/12
    print(monthlyinterestrate)
  def getmonthlyinterest(self):
    monthlyinterestrate=(self._Account__annualinterestrate/100)/12
    monthlyinterest=self._Account__balance*monthlyinterestrate
    print(monthlyinterest)
  def withdraw(self,a):
    self._Account__balance=self._Account__balance-a
    print(self._Account__balance) 
  def deposit(self,b):
    self._Account__balance=self._Account__balance+b 
    print(self._Account__balance) 
t1=Account('1122',20000,4.5)
t1.withdraw(2500)
t1.deposit(3000)
t1.getmonthlyinterest()
t1.getmonthlyinterestrate()
print(t1._Account__id,t1._Account__balance)



  



