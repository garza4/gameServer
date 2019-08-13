from pystrich.datamatrix import DataMatrixEncoder
encoder = DataMatrixEncoder('data matrix')
encoder.save("/.datamatrix_test.png")
print(encoder.get_ascii())
