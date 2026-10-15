Opening_Balance = 50000  
Deposit_Salary = 35000
withdrawal_Amount = 12000
rent =15000
rec_refund = 2500
Cradit_Card = 8500
purchase_laptop = 48000
rec_bonus = 10000
Donate = 500

total_deposits = Deposit_Salary + rec_refund + rec_bonus
total_withdrawals = rent + Cradit_Card + purchase_laptop + Donate +withdrawal_Amount
total_balance = Opening_Balance + total_deposits - total_withdrawals
Interst = total_balance * 0.03 # 3% interest on the closing balance
Closing_Balance = total_balance + Interst


print(f"Opening Balance: {Opening_Balance}")
print(f"Total Deposit: {total_deposits}")
print(f"Total Withdrawals: {total_withdrawals}")
print(f"Closing Balance: {Closing_Balance}")

