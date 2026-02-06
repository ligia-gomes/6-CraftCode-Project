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


def choose_reports(report_ids, report_labels=None):
    report_labels = report_labels or {}
    print("Available reports:")
    for report_id in report_ids:
        label = report_labels.get(report_id, "")
        if label:
            print(f"{report_id} - {label}")
        else:
            print(report_id)

    while True:
        print("\nDo you want to:")
        print("1 - Run all reports")
        print("2 - Run a specific report")
        print("3 - Run a sequence or batch of reports")
        print("0 - Exit")
        menu_choice = input("Choose an option (1/2/3/0): ").strip().lower()

        if menu_choice in {"0", "q", "quit", "exit"}:
            return []
        if menu_choice == "1":
            return list(report_ids)
        if menu_choice == "2":
            selection = input("Which report do you want to run? (e.g. 1 or x): ").strip()
            selected = parse_report_selection(selection, report_ids)
            if selected:
                return selected
        if menu_choice == "3":
            selection = input(
                "Which sequence or batch do you want to run? (e.g. 1,2 or 1-3): "
            ).strip()
            selected = parse_report_selection(selection, report_ids)
            if selected:
                return selected
        print("No valid reports selected. Try again.")
