from fpdf import FPDF
from datetime import datetime

def create_pdf(expenses):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.cell(200, 10, txt="TAX EXPENSE REPORT", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Generated on {datetime.now().strftime('%d/%m/%Y')}", ln=1, align="C")
    
    # Table Header
    pdf.cell(40, 10, "Amount", border=1)
    pdf.cell(50, 10, "Category", border=1)
    pdf.cell(100, 10, "Description", border=1)
    pdf.ln()
    
    # Table Rows
    for exp in expenses:
        pdf.cell(40, 10, str(exp.amount), border=1)
        pdf.cell(50, 10, exp.category, border=1)
        pdf.cell(100, 10, exp.description, border=1)
        pdf.ln()
    
    pdf_path = "tax_report.pdf"
    pdf.output(pdf_path)
    return pdf_path