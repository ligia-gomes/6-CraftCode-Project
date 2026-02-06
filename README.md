# CraftCode-Project
Local automation for monthly reports using Python, with validations and comparisons between the current month and the previous month.

**Note**  
This project was **co-developed** with a colleague as part of a real-world analytics automation initiative.  
It is intentionally shared here as a **sanitized and abstracted version**, preserving structure and logic without exposing sensitive data or business rules.
Comparisons ask for manual confirmation when variation exceeds 2,5%.

## Overview
- Reads local input files.
- Processes and creates the monthly reports.
- Compares against the previous report and asks for manual confirmation if the difference exceeds the threshold.
- Saves files in the standard year/month folder structure.

## Architecture (current)
```
/
  main.py
  craftcode/
    config/
      env.py
      settings.py
    core/
      console.py
      context.py
      prompts.py
      runner.py
    io/
      inputs.py
      outputs.py
    comparisons/
      validators.py
    reports/
      base.py
      registry.py
      report_1.py
      report_2.py
      report_3.py
      report_4.py
      report_x.py
```

Key responsibilities:
- `main.py`: CLI entrypoint.
- `craftcode/core/runner.py`: orchestrates the end-to-end flow.
- `craftcode/config/`: .env loading and global settings.
- `craftcode/io/`: input parsing and output saving.
- `craftcode/comparisons/`: validation and comparison rules.
- `craftcode/reports/`: individual report builders and registry.

## Reports folder structure)
```
/
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
### Why local execution?
- The pipeline processes **sensitive HR-related data**
- Cloud execution is intentionally avoided due to confidentiality and access constraints
- All examples and configurations assume a local runtime environment

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
0 - Exit
```
