import easyocr
print(easyocr)
reader=easyocr.Reader(["en"],gpu=False)
print(reader)
result=reader.readtext("day10/gpay.png",detail=0)
print(result)