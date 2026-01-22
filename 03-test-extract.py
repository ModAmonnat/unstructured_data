#The following script has been polished by Clude

test_transactions = extract_transactions(sample_data, "Test")                                             
test_df = pd.DataFrame(test_transactions)

print("SUMMARY")
print(f"Total Transactions: {len(test_df)}")
print(f"Total DEBIT:        {len(test_df[test_df['Transaction Type']=='DEBIT'])}")
print(f"Total CREDIT:       {len(test_df[test_df['Transaction Type']=='CREDIT'])}")

print("=" * 70)
test_df.head(10)
