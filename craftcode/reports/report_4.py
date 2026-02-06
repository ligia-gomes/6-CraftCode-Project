def build_report(noml, context):
    establist = ['ValS', 'ValT']
    bandlist = ['ValU', 'ValV', 'ValW']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report[df_report['Col7'].isin(['Val6', 'Val7'])]
    # PSEUDO-CODE: df_report = df_report.merge(band_mapping, on='Col4', how='left')
    # PSEUDO-CODE: df_report = df_report.drop_duplicates(subset=['Col2'])

    return df_report
