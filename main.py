
def action():
    income=float(input("Enter Income"))
    Expen=float(input("Enter Daily Expenditure"))
    Status=int(input(''' 
                    1.Single
                    2.Married
                     '''))
    Texpen=Expen*30
    
    if Status==1:
        addition=(income*45)/100
        final=Texpen+addition
        result=income-final
    else :
        addition=(income*20)/100
        final=Texpen+addition
        result=income-final
    if final>income:
        print("Overspending by $"+ str(result))
    else:
        print("Saving $"+ str(result))
        
action()
