import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf_report(df, filename="outputs/monthly_report.pdf"):
    pdf = SimpleDocTemplate(filename)

    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data)
    style = TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ])

    table.setStyle(style)

    pdf.build([table])
    print("PDF Report Generated!")