# Imports
import numpy as np
import pandas as pd

#Function Definitions
def duration(row):
    return (row['Book Returned'] - row['Book checkout']).days

def main():

#files

    systembook = pd.read_csv('Data/03_Library Systembook.csv')
    customers = pd.read_csv('Data/03_Library SystemCustomers.csv')

#cleansing customers

    customers_cleaned = customers
    customers_cleaned = customers_cleaned.dropna()
    customers_cleaned["Customer ID"] = customers_cleaned["Customer ID"].astype(int)
    customers_cleaned = customers_cleaned.drop_duplicates()
    customers_cleaned.to_csv("Data/03_Library SystemCustomers_cleaned.csv", index=False)

#cleansing rentals

    systembook_cleaned = systembook
    systembook_cleaned = systembook_cleaned.replace(r'^\s*$',np.nan, regex=True)
    systembook_cleaned = systembook_cleaned.dropna()
    systembook_cleaned["Id"] = systembook_cleaned["Id"].astype(int)
    systembook_cleaned["Customer ID"] = systembook_cleaned["Customer ID"].astype(int)
    systembook_cleaned["Book checkout"]= systembook_cleaned["Book checkout"].str.replace('"','', regex=False)
    systembook_cleaned["Book Returned"]= systembook_cleaned["Book Returned"].str.replace('"','', regex=False)
    systembook_cleaned["Book checkout"] = pd.to_datetime(systembook_cleaned["Book checkout"], format="%d/%m/%Y", errors="coerce")
    systembook_cleaned["Book Returned"] = pd.to_datetime(systembook_cleaned["Book Returned"], format="%d/%m/%Y", errors="coerce")
    systembook_cleaned['Duration_Days'] = systembook_cleaned.apply(duration, axis=1)
    systembook_cleaned.to_csv("Data/03_Library Systembook_cleaned.csv", index=False)

#valid rentals
    systembook_valid = systembook_cleaned[systembook_cleaned['Duration_Days']>=0]
    systembook_notvalid = systembook_cleaned[systembook_cleaned['Duration_Days']<0]
    systembook_valid.to_csv("Data/03_Library Systembook_valid.csv", index=False)
    systembook_notvalid.to_csv("Data/03_Library Systembok_notvalid.csv", index=False)

    

if __name__ == "__main__":
    main()