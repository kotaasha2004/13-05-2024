def Calculate(d,n):
    fuel_needed=d/10
    fuel_cost=fuel_needed*70
    revenue=n*80
    profit=revenue-fuel_cost
    if(profit>0):
        print(profit)
    else:
        print("-1")
distance=int(input())
no_of_passengers=int(input())
Calculate(distance,no_of_passengers)
