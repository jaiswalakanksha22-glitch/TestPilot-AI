from openpyxl import Workbook


def export_to_excel(test_cases, filename="exports/TestCases.xlsx"):

    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    ws.append(["ID", "Test Case"])

    lines = test_cases.split("\n")

    count = 1

    for line in lines:

        if line.strip():

            ws.append([count, line])

            count += 1

    wb.save(filename)

    return filename