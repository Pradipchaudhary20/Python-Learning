def categorize_transactions(transactions):
    gains = []
    losses = []

    for transaction in transactions:
        if transaction > 0:
            gains.append(transaction)
        else:
            losses.append(transaction)
    
    return gains, losses
categorize_transactions(100)