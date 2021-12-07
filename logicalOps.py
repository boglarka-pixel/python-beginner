has_high_income = True
has_good_credit = False
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligibel for loan AND")

if has_high_income or has_good_credit:
    print("Eligibel for loan OR")

if has_high_income and not has_criminal_record:
    print("Eligibel for loan AND NOT")
