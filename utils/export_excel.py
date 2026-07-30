import re
import pandas as pd


def export_to_excel(result):

    pattern = r"(\|.+\|\n\|[-:| ]+\|\n(?:\|.*\|\n?)*)"

    tables = re.findall(pattern, result)

    filename = "exports/TestCases.xlsx"

    if not tables:
        with open(filename.replace(".xlsx", ".txt"), "w") as f:
            f.write(result)
        return filename.replace(".xlsx", ".txt")

    writer = pd.ExcelWriter(filename)

    sheet = 1

    for table in tables:

        lines = table.split("\n")

        headers = [
            h.strip()
            for h in lines[0].strip("|").split("|")
        ]

        rows = []

        for row in lines[2:]:

            if row.strip():

                rows.append(
                    [c.strip() for c in row.strip("|").split("|")]
                )

        df = pd.DataFrame(rows, columns=headers)

        df.to_excel(
            writer,
            sheet_name=f"Table{sheet}",
            index=False
        )

        sheet += 1

    writer.close()

    return filename