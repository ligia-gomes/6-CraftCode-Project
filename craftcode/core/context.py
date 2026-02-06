from dataclasses import dataclass
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import os

from craftcode.config import settings


@dataclass(frozen=True)
class RunContext:
    base_input: str
    base_output: str
    report_date: str
    last_report_date: str
    report_year: str
    last_report_year: str
    report_month: str
    threshold_percent: float

    def input_file_path(self):
        return os.path.join(
            self.base_input,
            self.report_year,
            self.report_date,
            f"{settings.INPUT_FILE_PREFIX}{self.report_date}.csv",
        )

    def last_input_file_path(self):
        return os.path.join(
            self.base_input,
            self.last_report_year,
            self.last_report_date,
            f"{settings.INPUT_FILE_PREFIX}{self.last_report_date}.csv",
        )

    def output_dir(self):
        return os.path.join(self.base_output, self.report_year, self.report_date)

    def last_output_dir(self):
        return os.path.join(self.base_output, self.last_report_year, self.last_report_date)


def build_context(base_input, base_output, threshold_percent):
    today = date.today()
    report_date = (today - relativedelta(months=1)).strftime("%Y.%m")
    last_report_date = (today - relativedelta(months=2)).strftime("%Y.%m")
    report_year = datetime.now().strftime("%Y")
    last_report_year = (today - relativedelta(months=2)).strftime("%Y")
    report_month = (today - relativedelta(months=1)).strftime("%m")
    return RunContext(
        base_input=base_input,
        base_output=base_output,
        report_date=report_date,
        last_report_date=last_report_date,
        report_year=report_year,
        last_report_year=last_report_year,
        report_month=report_month,
        threshold_percent=threshold_percent,
    )
