from fpdf import FPDF

def txt_para_pdf(caminho_txt, caminho_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(caminho_txt, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            pdf.cell(0, 8, txt=linha.strip(), ln=True)

    pdf.output(caminho_pdf)