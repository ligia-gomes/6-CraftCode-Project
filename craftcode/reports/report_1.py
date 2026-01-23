def build_report(noml, context):
    establist = ['ValA', 'ValB', 'ValC', 'ValD', 'ValE', 'ValF']
    bandlist = ['ValG', 'ValH', 'ValI']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report.merge(cost_center_map, on='Col2', how='left')
    # PSEUDO-CODE: df_report['KPI_1'] = df_report['AWF_Heads'] * factor
    # PSEUDO-CODE: df_report = df_report[df_report['AWF_FTE'] > 0]

    return df_report
