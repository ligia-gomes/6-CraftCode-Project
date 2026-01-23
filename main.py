import os

from craftcode.core.console import red
from craftcode.core.prompts import choose_reports
from craftcode.core.runner import run_reports
from craftcode.reports.registry import REPORTS


def main():
    report_ids = list(REPORTS.keys())
    selected_reports = choose_reports(report_ids)
    if not selected_reports:
        print(red("No valid reports selected. Exiting."))
        return

    project_root = os.path.abspath(os.path.dirname(__file__))
    run_reports(selected_reports, project_root)


if __name__ == "__main__":
    main()
