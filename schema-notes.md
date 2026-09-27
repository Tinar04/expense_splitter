# Expense Splitter — Schema & Design Notes

## Models

### Group
- id
- g_name
- members → ManyToManyField(User)

### Expense
- id
- group → ForeignKey(Group)
- e_name
- total_amount
- paid_by → ForeignKey(User)
- split_type → choices: equal / custom
- created_at

### Split
- id
- expense → ForeignKey(Expense)
- owed_by → ForeignKey(User)
- shared_amount

### Settlement
- id
- group → ForeignKey(Group)
- paid_by → ForeignKey(User, related_name='settlements_paid')
- paid_to → ForeignKey(User, related_name='settlements_received')
- amount_paid
- comment
- settled_at

## Relationships

- Group ↔ User: Many-to-Many (group membership)
- Group → Expense: One-to-Many
- Expense → User (paid_by): Many-to-One
- Expense → Split: One-to-Many
- Split → User (owed_by): Many-to-One
- Group → Settlement: One-to-Many
- Settlement → User (paid_by): Many-to-One
- Settlement → User (paid_to): Many-to-One

## Business Logic — Net Balance Calculation

For each person X in a group:
```
total_paid = sum of Expense.total_amount where Expense.paid_by = X
total_owed = sum of Split.shared_amount where Split.owed_by = X
net_balance = total_paid - total_owed
```

All net balances in a group must sum to zero (money isn't created/destroyed, only moved).

## Business Logic — Debt Simplification

Goal: minimize number of transactions needed to settle all balances to zero.

Approach (greedy):
1. Calculate net balance for every group member
2. Repeatedly match the person with the highest positive balance (owed the most) with the person with the highest negative balance (owes the most)
3. Settle the smaller of the two amounts between them
4. Repeat until everyone's balance is zero

## Split Type Logic

- **Equal**: total_amount ÷ number of members, auto-generates Split rows
- **Custom**: user manually enters each person's share; sum of all shares must equal total_amount, else reject with remaining amount shown

## Access Control

- Membership-based, not role-based
- Only Group members can view/add Expenses, Splits, Settlements for that group
- Enforced via `get_queryset()` filtering + `permission_classes` in DRF
- Invite/join flow via unique `invite_code` on Group (UUID) — only endpoint accessible without prior membership
