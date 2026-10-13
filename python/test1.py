##-------------------------------------
##
##
##
##
##-------------------------------------
import csv
from datetime import datetime
from pathlib import Path

# --------------------------------------------------
# Start timestamp
# --------------------------------------------------
start_time = datetime.now()

print("=" * 60)
print(f"Script started: {start_time:%Y-%m-%d %H:%M:%S}")
print("=" * 60)

# CSV file location
file_path = Path(r"C:\appl\scripts\python\test1\sample1.csv")

try:

    # Check that the file exists
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Open and read the CSV file
    with file_path.open(mode="r", newline="", encoding="utf-8-sig") as file:

        reader = csv.reader(file)

        # Load the CSV rows
        rows = list(reader)

        if not rows:
            print("The CSV file is empty.")

        else:
            # Determine appropriate width for each column
            column_widths = [
                max(len(str(value)) for value in column)
                for column in zip(*rows)
            ]

            print(f"\nFile: {file_path.name}")
            print(f"Data rows: {len(rows) - 1}")
            print(f"Columns: {len(rows[0])}")
            print()

            # Display the data as a table
            for row_number, row in enumerate(rows):

                formatted_row = " | ".join(
                    f"{value:<{width}}"
                    for value, width in zip(row, column_widths)
                )

                print(formatted_row)

                # Separator after header
                if row_number == 0:
                    print("-+-".join("-" * width for width in column_widths))

except FileNotFoundError as error:
    print(f"\nERROR: {error}")

except Exception as error:
    print(f"\nERROR: {error}")

finally:

    # --------------------------------------------------
    # End timestamp
    # --------------------------------------------------
    end_time = datetime.now()

    print()
    print("=" * 60)
    print(f"Script ended:   {end_time:%Y-%m-%d %H:%M:%S}")
    print(f"Elapsed time:   {end_time - start_time}")
    print("=" * 60)
