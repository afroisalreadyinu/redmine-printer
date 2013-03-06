import sys, os
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

OUT_FILENAME = 'stories.pdf'

def generate_pdf(story, existing_canvas=None):
    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']

    c = existing_canvas or canvas.Canvas(OUT_FILENAME, pagesize=A5)
    #c.setFont("Helvetica", 28)
    # draw some lines
    #a5 is 210 mm * 148 mm
    c.rect(1*cm, 1*cm, 12.8*cm, 19*cm, fill=0)

    c.rotate(90)
    style.fontSize = 24
    style.leading = 24
    story_points = "%s points" % story['Story points'] if story['Story points'] else 'Not estimated'
    title = Paragraph("%s [%s]" % (story['Subject'],story_points), style)

    title.wrap(17*cm, 4*cm)
    title.drawOn(c, 2*cm, -3.5*cm)

    # c.drawString(2*cm, -3*cm, "%s [%d points]" % (story['Subject'],
    #                                               int(float(story['Story points']))))

    style.fontSize = 14
    style.leading = 16
    description = Paragraph(story['Description'], style)
    description.wrap(14*cm, 15*cm)
    description.drawOn(c, 2*cm, -8*cm)
    c.showPage()
    return c

def process_stories(filepath):
    with open(filepath, 'r') as infile:
        reader = csv.DictReader(infile)
        canvas = None
        for row in reader:
            canvas = generate_pdf(row, canvas)
        canvas.save()
    print "Stories saved to %s" % OUT_FILENAME

def print_stories():
    if len(sys.argv) != 2:
        print "Usage: print-stories stories.csv"
    else:
        filename = sys.argv[1]
        process_stories(os.path.abspath(filename))
