from craftcode.reports.base import ReportSpec
from craftcode.reports import report_1, report_2, report_3, report_4, report_x


REPORTS = {
    '1': ReportSpec(
        report_id='1',
        name='1_name_of_report_file',
        file_prefix='1_name_of_report_file ',
        builder=report_1.build_report,
    ),
    '2': ReportSpec(
        report_id='2',
        name='2_name_of_report_file',
        file_prefix='2_name_of_report_file ',
        builder=report_2.build_report,
    ),
    '3': ReportSpec(
        report_id='3',
        name='3_name_of_report_file',
        file_prefix='3_name_of_report_file ',
        builder=report_3.build_report,
    ),
    '4': ReportSpec(
        report_id='4',
        name='4_name_of_report_file',
        file_prefix='4_name_of_report_file ',
        builder=report_4.build_report,
    ),
    'x': ReportSpec(
        report_id='x',
        name='401_name_of_report_file',
        file_prefix='401_name_of_report_file ',
        builder=report_x.build_report,
    ),
}
