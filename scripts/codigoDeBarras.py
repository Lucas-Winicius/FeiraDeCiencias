from barcode import Code128
from barcode.writer import ImageWriter # para salvar em png

numero = "teste12345"

codigo_barra = Code128(numero, writer=ImageWriter()) # writer para salvar em png
codigo_barra.save("codigo_barra")