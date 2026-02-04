from fpdf import FPDF

def txt_para_pdf(caminho_txt, caminho_pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    #TÍTULO
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, txt="Conversão de TXT para PDF", ln=True, align="C")
    pdf.ln(5)
    
    #CORPO DO TEXTO
    pdf.set_font("Arial", size=12)

    with open(caminho_txt, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            pdf.multi_cell(0, 8, linha)
    pdf.output(caminho_pdf)