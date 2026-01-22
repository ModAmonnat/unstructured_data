#The following script has been polished by Clude

def extract_transactions(data, source_file="File1"):
    transactions = []
    lines = data.strip().split('\n')
    current_date = None
    boundary = None
    
    # Find boundary from header
    for line in lines:
        if 'EFF DATE' in line and 'DEBIT' in line and 'CREDIT' in line:
            last_debit = line.rfind('DEBIT')
            first_credit = line.find('CREDIT')
            boundary = (last_debit + first_credit) // 2
            break
    
    # Use default if header not found
    if boundary is None:
        boundary = 60 #I manually count to position from the file
    
    # Extract transactions
    for line in lines:
        # Only process lines starting with 111-1
        if not line.strip().startswith('111-1'):
            continue

        # Get date if present
        date_match = re.search(r'(\d{1,2}/\d{1,2}/\d{2})', line)
        if date_match:
            current_date = date_match.group(1)
        
        if not current_date:
            continue
        
        # Find all amount+code pairs
        for match in re.finditer(r'(-?\d{1,3}(?:,\d{3})*\.\d{2})\s*([A-Z]{2,3})', line):
            amount = float(match.group(1).replace(',', ''))
            code = match.group(2)
            
            # Determine if transaction type is DEBIT or CREDIT
            if match.start() < boundary:
                trans_type = 'DEBIT'
            else:
                trans_type = 'CREDIT'
                amount = -amount
            
            transactions.append({
                'Date': current_date,
                'Transaction Code': code,
                'Transaction Type': trans_type,
                'Amount': f"{amount:.2f}",
            })
    
    return transactions
