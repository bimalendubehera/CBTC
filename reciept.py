from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
  
DATA = [
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ],
    [
        "24/01/2024",
        "Full Stack Development with JAVA - Live",
        "2 Year",
        "9,999.00/-",
    ],
    [ "28/01/2024", "Cyber Security", "6 months", "9,999.00/-"],
    [ "05/02/2024", "Data Structure and Algorithm","3 month","20,000.00/-"],
    [ "Sub Total", "", "", "39,998.00/-"],
    [ "Discount", "", "", "-5,000.00/-"],
    [ "Total", "", "", "34,998.00/-"],
]
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )
  
styles = getSampleStyleSheet()
  
title_style = styles[ "Heading1" ]

title_style.alignment = 1
  
title = Paragraph( "BILL RECEIPT" , title_style )
  
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.blueviolet ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),  
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6), 
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]
)

table = Table( DATA , style = style )
pdf.build([ title , table ])
