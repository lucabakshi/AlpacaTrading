
from DataQueryandClean import cleaned_trades
import pandas

refdata1 = pandas.read_csv("DataValidationReference.csv")
refdata1dict = refdata1.to_dict()

def validate_symbol(x):
    for trade in x:
        if trade['symbol'] in refdata1['Instrument'].values:
            pass
        else:
            print(f"Invalid trade found: {trade['symbol']}!")
            return False
    return True

validate_all = validate_symbol(cleaned_trades)

print(f'Symbol Data is valid: {validate_all}')