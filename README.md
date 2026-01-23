# CraftCode-Project
Local automation for monthly reports using Python, with validations and comparisons between the current month and the previous month.

## Overview
- Reads local input files.
- Processes and creates the monthly reports.
- Compares against the previous report and asks for manual confirmation if the difference exceeds the threshold.
- Saves files in the standard year/month folder structure.

## Folder structure
```
/
  comparisons_functions.py
  functions.py
  main.py
  report_1/
  report_2/
  report_3/
  report_4/
  report_x/
```

Each `report_*` folder contains:
- `comparison_report_*.py`: compares structure and row counts with the previous report.
- `file_report_*.py`: builds the report dataframe (with commented pseudocode).
- `save_report_*.py`: saves the final output file.

## .env (local)
Create a `.env` in the project root (use `.env.example` as a base):
```
input=C:/Users/your_user/Documents/Input/
output=C:/Users/your_user/Documents/Output/
```

The system creates the year/month structure inside these paths.

## How to run
```
python main.py
```

Main menu:
```
Do you want to:
1 - Run all reports
2 - Run a specific report
3 - Run a sequence or batch of reports
```

## Notes
- The project uses pseudocode in `file_report_*` to preserve confidentiality.
- Comparisons ask for confirmation when variation exceeds 5%.
