# ledger_auditor.py
# B. Deutsch (1/30/26)

# Library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files
import openpyxl

# Load the workbook
wb = openpyxl.load_workbook('sample_ledger.xlsx')
# Get the active sheet (or specify a sheet name: wb['SheetName'])
sheet = wb.active
# List of all transactions; must be populated at start of main
t_list = []

def getCell(cell: str):
    return sheet[cell].value

class Transaction:
    def __init__(self, rowNumber):
        self.date = getCell(f'A{rowNumber}')[1:]
        self.note = getCell(f'B{rowNumber}').lower()
        source = getCell(f'C{rowNumber}').lower()
        self.source = source if source != 'you' else 'benjamin deutsch'
        amount = getCell(f'D{rowNumber}')[1:].replace(",","")
        self.amount = float(amount[:amount.find('(')]) if (amount.find('(') != -1) else float(amount) # scrap the "fee" portion; it's irrelevent
        self.balance = float(getCell(f'E{rowNumber}')[1:].replace(",",""))
    def __str__(self):
        return f'{self.date}\n{self.note}\n{self.source}\n{self.amount}\n{self.balance}'

def fillTransactionList(minRow, maxRow):
    t_list = []
    for rowNumber in range(minRow, maxRow, 1):
        t_list.append(Transaction(rowNumber))
    return t_list

def getTotalCommunalCost():
    total = 0.0
    for t in t_list:
        if (t.source == 'property' and 'parking' not in t.note):
            total += t.amount
    return total

def getParkingCost():
    total = 0.0
    for t in t_list:
        if ('parking' in t.note):
            total += t.amount
    return total

def getTotalPayment(surname: str):
    surname = surname.lower()
    total = 0.0
    for t in t_list:
        if (surname in t.source):
            total += t.amount
    return total

def getRenterInfo(surname: str, isParking = False):
    renter = dict()
    renter['surname'] = surname.lower()
    renter['paid'] = getTotalPayment(surname)
    renter['charged'] = round(getTotalCommunalCost()/3, 2)
    renter['charged'] += getParkingCost() if isParking else 0
    renter['owes'] = round(renter['charged'] - renter['paid'], 2)
    return renter

def renterInfoToStr(renter):
    owe_str = 'Over by: ' if renter['owes'] < 0 else 'Under by:'
    return f'''-- {renter['surname']} --
Paid:     ${renter['paid']}
Charged:  ${renter['charged']}
{owe_str} ${abs(renter['owes'])}
'''

if __name__ == '__main__':
    t_list = fillTransactionList(9, 37)

    renters = list()
    renters.append(getRenterInfo('Doe'))
    renters.append(getRenterInfo('Tinkle', isParking=True))
    renters.append(getRenterInfo('Butz'))

    for renter in renters:
        print(renterInfoToStr(renter))