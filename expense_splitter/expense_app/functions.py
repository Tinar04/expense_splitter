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
ans = get_net_balance(payments,shares)
print(ans)