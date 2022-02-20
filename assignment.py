import datetime     #importing Datetime module to print the pay-stub

"""defining the anual salary function to calculate all the amounts of an associate
    This function takes company name, Employee name, Position and Salary as arguments"""

def anual_salary(comp_name, emp_name,pos,salary):
    print('Company name: '+comp_name)

    #conversion of date time to the desired output
    date_stub=datetime.date.today()
    print('Date of pay-stub:', date_stub)

    #printing the employee basic details
    print('Employee: '+emp_name)
    print('Position: '+ pos)
    print('Salary: '+ str(salary))
    

    #if condition block to calcualte the bonus
    if(salary<=25000):
        bonus=salary*0.105
    elif(salary>25000 and salary<=50000):
        bonus=salary*0.115
    elif(int(salary)>55000):
        bonus=salary*0.125
    else:
        bonus=0
        
    print('Bonus: '+str(bonus))

    #formula to calculate gross anual income 
    gross_anual_inc=int(salary)+bonus
    print('Gross Anual Income: '+ str(gross_anual_inc))

    #formula to calculate tax and benefits
    tax=gross_anual_inc*0.155
    benefits=gross_anual_inc*0.065
    deductables=tax+benefits

    """printing the deductables in required output formats.
        Here we are type casting all the salary related information in order for the
        string concatenation to work properly"""

    print('Deductables: '+ str(deductables))
    print('Deductables (Taxes): '+str(tax))
    print('Deductables (Benefits): '+str(benefits))
    net_anual_inc=gross_anual_inc-deductables
    print('Net Anual Income: '+str(net_anual_inc))

#calling the function to calculate the required data
anual_salary('abc','Siva','Software Developer',30000)