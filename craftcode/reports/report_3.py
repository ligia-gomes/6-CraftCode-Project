def build_report(noml, context):
    establist = ['ValO', 'ValP', 'ValQ']
    bandlist = ['ValR']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report[df_report['Temps_Heads'] > 0]
    # PSEUDO-CODE: df_report = df_report.assign(Month=context.report_date)
    # PSEUDO-CODE: df_report = df_report.sort_values(['Col4', 'Col2'])

    return df_report
