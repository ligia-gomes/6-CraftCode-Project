import os

import pandas as pd

from craftcode.comparisons import validators
from craftcode.config import env, settings
from craftcode.core import prompts
from craftcode.core.console import green, red
from craftcode.core.context import build_context
from craftcode.io import inputs, outputs
from craftcode.reports.registry import REPORTS


def run_reports(report_ids, project_root):
    base_input, base_output = env.load_paths(project_root)
    context = build_context(base_input, base_output, settings.THRESHOLD_PERCENT)

    print("\nLet's create our monthlies!")
    print("\nThe report date is", green(context.report_date))
    print("The report month is", green(context.report_month))

    last_input_file = context.last_input_file_path()
    current_input_file = context.input_file_path()

    if not os.path.isfile(last_input_file):
        print(red(f"Last input file not found: {last_input_file}"))
        return
    if not os.path.isfile(current_input_file):
        print(red(f"Current input file not found: {current_input_file}"))
        return

    print("\nStarting comparison between current and last nominative list...")
    if not validators.column_structure_comparison(
        inputs.read_raw_input(last_input_file),
        inputs.read_raw_input(current_input_file),
        prompts.confirm_continue,
    ):
        return

    noml = inputs.load_nom_list(current_input_file)
    print("\n" + green("OK ") + "The nominative list was processed and headcounts created!")

    for report_id in report_ids:
        spec = REPORTS.get(report_id)
        if not spec:
            print(red(f"Unknown report id: {report_id}"))
            continue
        print(f"\nRunning report {report_id} - {spec.name}")
        _run_report(spec, noml, context)


def _run_report(spec, noml, context):
    df_report = spec.builder(noml, context)
    old_report_path = os.path.join(
        context.last_output_dir(),
        f"{spec.file_prefix}{context.last_report_date}.xlsx",
    )

    if not os.path.isfile(old_report_path):
        message = f"Previous report not found at {old_report_path}. Continue without comparison?"
        if not prompts.confirm_continue(message):
            print(red("Operation Cancelled!"))
            return
        _save_report(spec, df_report, context)
        return

    try:
        old_df = pd.read_excel(old_report_path)
    except Exception as exc:
        message = f"Failed to read previous report ({exc}). Continue without comparison?"
        if not prompts.confirm_continue(message):
            print(red("Operation Cancelled!"))
            return
        _save_report(spec, df_report, context)
        return

    if not validators.column_structure_comparison(old_df, df_report, prompts.confirm_continue):
        return
    if not validators.compare_shape(old_df, df_report, context.threshold_percent, prompts.confirm_continue):
        return

    _save_report(spec, df_report, context)


def _save_report(spec, df_report, context):
    try:
        file_path = outputs.save_report(
            df_report,
            context.output_dir(),
            spec.file_prefix,
            context.report_date,
            settings.OUTPUT_SHEET_NAME,
        )
        print('Report "' + green(os.path.basename(file_path)) + '" was created and saved successfully!')
    except Exception:
        print(red(f"Report {spec.file_prefix}{context.report_date}.xlsx not saved successfully - check error!"))
