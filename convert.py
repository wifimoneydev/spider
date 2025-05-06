import pandas as pd  # lib for excel
import os  # to read file names

# This function converts Excel to JSON and JSONL
def convert_excel_to_json(file_name):
    # Load the Excel file into a table
    data = pd.read_excel(file_name)

    # Get just the file name (no .xlsx)
    file_base = os.path.splitext(file_name)[0]

    # Create new file names for the outputs
    json_output = file_base + ".json"
    jsonl_output = file_base + ".jsonl"

    # Save everything to one JSON file 
    data.to_json(json_output, orient="records", indent=4)

    # Save one line per row in a JSONL file
    with open(jsonl_output, "w", encoding="utf-8") as file:
        for row in data.to_dict(orient="records"):
            file.write(str(row).replace("'", '"') + "\n")  # Make sure it's JSON style

    print("✅Done! Saved as:")
    print("-", json_output)
    print("-", jsonl_output)


#  Run the function with your file name
convert_excel_to_json("data2.xlsx")
