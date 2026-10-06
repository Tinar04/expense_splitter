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
            pair = (key,value)
            receivers.append(pair)
        elif value<0:
            pair = (key,value)
            payers.append(pair)

    return receivers,payers
       


payments = [
    {"expense_id": 1, "user": "tina", "amount_paid": 6000},
    {"expense_id": 1, "user": "kumkum", "amount_paid": 6000},
]
shares = [
    {"expense_id": 1, "owed_by": "tanvi", "shared_amount": 3000},
    {"expense_id": 1, "owed_by": "tina", "shared_amount": 3000},
    {"expense_id": 1, "owed_by": "muskan", "shared_amount": 3000},
    {"expense_id": 1, "owed_by": "kumkum", "shared_amount": 3000},
]
net_balance = get_net_balance(payments,shares)
print("balance before settlement ",net_balance )


settlements = [
    {"paid_by": "tanvi", "paid_to": "tina", "amount_paid": 30},
    {"paid_by":"kumkum","paid_to":"muskan","amount_paid":5000},
    {"paid_by":"muskan","paid_to":"kumkum","amount_paid":5000},

]
new_balance= get_settle(settlements,net_balance)
print("balance after settlement", new_balance)


receivers,payers = get_receivers_and_payers(new_balance)
print(f"receivers - {receivers} , and payers = {payers}")