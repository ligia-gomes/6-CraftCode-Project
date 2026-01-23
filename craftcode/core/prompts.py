def confirm_continue(message):
    response = input(f"{message} (Y/N) ").strip().lower()
    return response == "y"


def parse_report_selection(selection, report_ids):
    if not selection:
        return []
    normalized = selection.replace(" ", "").lower()
    if normalized == "all":
        return list(report_ids)

    selected = set()
    for token in normalized.split(","):
        if "-" in token:
            start, end = token.split("-", 1)
            if start.isdigit() and end.isdigit():
                for report_id in report_ids:
                    if report_id.isdigit() and int(start) <= int(report_id) <= int(end):
                        selected.add(report_id)
            continue
        if token in report_ids:
            selected.add(token)
    return [report_id for report_id in report_ids if report_id in selected]


def choose_reports(report_ids):
    print("Available reports:", ", ".join(report_ids))
    print("Do you want to:")
    print("1 - Run all reports")
    print("2 - Run a specific report")
    print("3 - Run a sequence or batch of reports")
    menu_choice = input("Choose an option (1/2/3): ").strip()

    if menu_choice == "1":
        return list(report_ids)
    if menu_choice == "2":
        selection = input("Which Report you want to run? ").strip()
        return parse_report_selection(selection, report_ids)
    if menu_choice == "3":
        selection = input("Which sequence or batch you want to run? (e.g. 1,2 or 1-3): ").strip()
        return parse_report_selection(selection, report_ids)
    return []
