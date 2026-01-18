import qrcode

url = input("Enter the url=")

img = qrcode.make(url)
img.save('qrcode_geenrate.png')
print("Done")
