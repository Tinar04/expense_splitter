def get_net_balance(payments:list , shares: list)->dict:
    net_balance = {}

    for payment in payments:
        user = payment['user']
        amount_paid = payment['amount_paid']

        net_balance[user] = net_balance.get(user,0)+amount_paid

    for share in shares:
        user = share['owed_by']
        shared_amount = share['shared_amount']
        net_balance[user] = net_balance.get(user,0) - shared_amount



    return net_balance

def get_settle(settlements:list,net_balance:dict)->dict:
    for d in settlements:

        amount = d['amount_paid']
        payer = d['paid_by'] 
        receiver = d['paid_to']

        net_balance[payer] = net_balance.get(payer,0)+amount
        net_balance[receiver] = net_balance.get(receiver,0)-amount


               
    return net_balance

def get_receivers_and_payers(final_net_balance:dict):
    receivers = []
    payers = []

    for key,value in final_net_balance.items():
        if value>0:
            pair = [key,value]
            receivers.append(pair)
        elif value<0:
            pair = [key,value]
            payers.append(pair)

    # big_receiver = max(receivers)
    # big_payer = min(payers)
    # print(big_receiver[1] ,"And", big_payer[1])
    return receivers,payers

# receivers - [('riya', 2100), ('kabir', 1800), ('meher', 1200)] , and payers = [('dev', -2100), ('arjun', -3000)]
def matching_function(receivers, payers):
    receivers = [[name, amt] for name, amt in receivers]
    payers = [[name, abs(amt)] for name, amt in payers]
    transactions = []

    while receivers and payers:
        big_r = max(receivers, key=lambda x: x[1])
        big_p = max(payers, key=lambda x: x[1])

        amount = min(big_r[1], big_p[1])
        transactions.append((big_p[0], big_r[0], amount))

        big_r[1] -= amount
        big_p[1] -= amount

        if big_r[1] == 0:
            receivers.remove(big_r)
        if big_p[1] == 0:
            payers.remove(big_p)

    return transactions
        
        
        
       








    


payments = [
    {"expense_id": 1, "user": "riya", "amount_paid": 7500},
    {"expense_id":2,"user":"kabir","amount_paid":6000},
    {"expense_id":2,"user":"meher","amount_paid":4000},
    {"expense_id":3,"user":"dev","amount_paid":3000},
    {"expense_id":4,"user":"arjun","amount_paid":2000},
    {"expense_id":5,"user":"meher","amount_paid":1500},


    
]
shares = [
    {"expense_id": 1, "owed_by": "riya", "shared_amount": 1500},
    {"expense_id": 1, "owed_by": "kabir", "shared_amount": 1500},
    {"expense_id": 1, "owed_by": "meher", "shared_amount": 1500},
    {"expense_id": 1, "owed_by": "dev", "shared_amount": 1500},
    {"expense_id": 1, "owed_by": "arjun", "shared_amount": 1500},
    {"expense_id":2,"owed_by":"kabir","shared_amount":2000},
    {"expense_id":2,"owed_by":"meher","shared_amount":2000},
    {"expense_id":2,"owed_by":"riya","shared_amount":2000},
    {"expense_id":2,"owed_by":"arjun","shared_amount":2000},
    {"expense_id":2,"owed_by":"dev","shared_amount":2000},
    {"expense_id":3,"owed_by":"dev","shared_amount":1000},
    {"expense_id":3,"owed_by":"arjun","shared_amount":1000},
    {"expense_id":3,"owed_by":"riya","shared_amount":1000},
    {"expense_id":4,"owed_by":"riya","shared_amount":400},
    {"expense_id":4,"owed_by":"kabir","shared_amount":400},
    {"expense_id":4,"owed_by":"meher","shared_amount":400},
    {"expense_id":4,"owed_by":"dev","shared_amount":400},
    {"expense_id":4,"owed_by":"arjun","shared_amount":400},
    {"expense_id":5,"owed_by":"riya","shared_amount":500},
    {"expense_id":5,"owed_by":"kabir","shared_amount":300},
    {"expense_id":5,"owed_by":"meher","shared_amount":400},
    {"expense_id":5,"owed_by":"dev","shared_amount":200},
    {"expense_id":5,"owed_by":"arjun","shared_amount":100},

        
    

    
]

net_balance = get_net_balance(payments,shares)
print("balance before settlement ",net_balance )



receivers,payers = get_receivers_and_payers(net_balance)
print(f"receivers - {receivers} , and payers = {payers}")


ans = matching_function(receivers,payers)
print(ans)