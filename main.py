import sys

print("\nLet's create our monthlies!")
from functions import report_date, report_month, START_GREEN, START_RED, END_COLORS
print('\nThe report date is', START_GREEN + report_date() + END_COLORS)
print('The report month is', START_GREEN + report_month() + END_COLORS)

from functions import call_path_input, call_path_last_input, START_GREEN, START_RED, END_COLORS
from comparisons_functions import column_structure_comparison, read_function
print('\n', START_GREEN + "âœ“ " + END_COLORS + 'The nominative list was processed and headcounts created!')
#import_preprocess_movlist('mov.xlsx')
#print('Movements list is ready to use.')

last_input_file = call_path_last_input()
current_input_file = call_path_input()

#comparison in input files
print('\nStarting comparison between current and last nominative list...')
input_comparison = column_structure_comparison(read_function(last_input_file), read_function(current_input_file)) 


def comp_aux():
    if input_comparison == "Cancelled":
        sys.exit(0) 
comp_aux()  

from report.comparisons_report import compare_file_report

REPORTS = {
    "1": ("name_of_report_file", compare_file_report),
}

def parse_report_selection(selection):
    if not selection:
        return list(REPORTS.keys())
    normalized = selection.replace(" ", "").lower()
    if normalized == "all":
        return list(REPORTS.keys())

    selected = set()
    for token in normalized.split(","):
        if "-" in token:
            start, end = token.split("-", 1)
            if start.isdigit() and end.isdigit():
                for report_id in REPORTS:
                    if report_id.isdigit() and int(start) <= int(report_id) <= int(end):
                        selected.add(report_id)
            continue
        if token in REPORTS:
            selected.add(token)
    return sorted(selected)

# start saving reports...
print('\nComparing and saving the files...')
print('Available reports:', ", ".join(REPORTS.keys()))
selection = input("Choose reports (all, 1, 1,2, 1-3): ").strip()
selected_reports = parse_report_selection(selection)

if not selected_reports:
    print(START_RED + "No valid reports selected. Exiting." + END_COLORS)
    sys.exit(0)

for report_id in selected_reports:
    report_name, report_fn = REPORTS[report_id]
    print('\nRunning report', report_id, '-', report_name)
    report_fn()
