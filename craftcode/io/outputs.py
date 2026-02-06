import os


def ensure_output_dir(path):
    os.makedirs(path, exist_ok=True)


def save_report(df, output_dir, file_prefix, report_date, sheet_name):
    ensure_output_dir(output_dir)
    file_path = os.path.join(output_dir, f"{file_prefix}{report_date}.xlsx")
    df.to_excel(file_path, index=False, sheet_name=sheet_name)
    return file_path
