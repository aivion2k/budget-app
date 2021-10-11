import math

class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.exp = 0
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount,'description': description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if amount>self.balance:
            return False
        else:
            self.ledger.append({'amount': -amount,'description': description})
            self.balance -=amount
            self.exp += amount
            return True

    def get_balance(self):
        balance = self.balance       
        return balance

    def transfer(self,amount,category):
        if amount>self.balance:
            return False
        else:
            self.balance -=amount
            self.exp += amount
            self.ledger.append({'amount': -amount,'description': 'Transfer to '+category.name})
            category.balance += amount
            category.ledger.append({'amount': amount,'description': 'Transfer from '+self.name})
            return True
    
    def check_funds(self,amount):
          if amount>self.balance:
            return False
          elif self.balance>=amount:
            return True

    def __str__(self):        
        print_string = self.name.center(30, '*')+'\n'
        for i in range(len(self.ledger)):
            print_string+=self.ledger[i]['description'][:23].ljust(23) + '{0:.2f}'.format(self.ledger[i]['amount']).rjust(7) + '\n'
        print_string += 'Total: '+'{0:.2f}'.format(self.balance)
        return print_string

def create_spend_chart(categories):
    total_exp = 0
    perc =[]
    names = []
    for i in range(len(categories)):
        total_exp += categories[i].exp
        names.append(categories[i].name)
    

    for category in categories:
        perc.append((math.floor(((category.exp/total_exp)*100)/10)*10))
    
    spend_chart = ""
    spend_chart += 'Percentage spent by category\n'
    
    for i in range(11):
        lp = 100-(i*10)
        if 1<len(str(lp))<3:
            spend_chart += ' '+ str(lp) + '|'
        elif lp == 0:
            spend_chart += '  '+ str(lp) + '|'
        else:
            spend_chart += str(lp) + '|'
        for j in range(len(categories)):
            if lp <= perc[j]:
                spend_chart += ' o '
        spend_chart += ' \n'
    
    spend_chart += '    ' +'-'*3*len(categories) + '-' + '\n'

    max_len = max(names, key=len)
    
    max_len = len(max_len)

    for i in range(max_len):
        spend_chart+= '    '
        for j in range(len(names)):
            try: 
                spend_chart += ' '+names[j][i] + ' '
            except:
                spend_chart += '   '
        spend_chart += '\n'
    spend_chart = spend_chart[:-1]
            
    return spend_chart
