from reportlab.pdfgen import canvas

def generate_report(traits, filename):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Palm Reading Report")
    c.setFont("Helvetica", 12)
    y = 720
    for trait in traits:
        c.drawString(100, y, f"• {trait}")
        y -= 20
    c.save()
