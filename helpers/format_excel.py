

from openpyxl.styles import Alignment
from openpyxl import load_workbook

def format_trial():
    filepath = "data/trial.xlsx"

    wb =  load_workbook(filename=filepath)
    sheet = wb.active

    sheet.title = "trial"

    # Center text horizontally and vertically
    sheet['A'].alignment = Alignment(horizontal='center', vertical='center')

    # change column width
    sheet.column_dimensions['A'].width = 10
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C:D'].width = 10

    accounting_format = '[$$-409]#,##0.00;[BLACK]-[$$-409]#,##0.00'
    sheet['C3:D36'].number_format = accounting_format

    wb.save(filepath)


if __name__ == '__main__':
    format_trial()