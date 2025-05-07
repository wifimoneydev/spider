import pandas as pd  # lib for excel
import os  # to read file names

# This function converts Excel to JSON and JSONL
def convert_excel_to_json(input_file, output_dir):
    # Load the Excel file into a table
    data = pd.read_excel(input_file)

    # Get just the file name (no .xlsx)
    file_base = os.path.splitext(os.path.basename(input_file))[0]

    # Create new file names for the outputs
    json_output = os.path.join(output_dir, file_base + ".json")
    jsonl_output = os.path.join(output_dir, file_base + ".jsonl")

    # Save everything to one JSON file 
    data.to_json(json_output, orient="records", indent=4)

    # Save one line per row in a JSONL file
    with open(jsonl_output, "w", encoding="utf-8") as file:
        for row in data.to_dict(orient="records"):
            file.write(str(row).replace("'", '"') + "\n")  # Make sure it's JSON style

    print("✅Done! Saved as:")
    print("-", json_output)
    print("-", jsonl_output)

# Run the function with your input file path and output directory
# replace doc id with yours 
input_file = "https://docs.google.com/spreadsheets/d/<1Uz_XzfKg4cxFVLq_uXM1j7cQijjMqExI7pzufmEzAwU>/export?format=xlsx"
#replace output dir with your path
output_dir = "/Users/desktop/output"
convert_excel_to_json(input_file, output_dir)