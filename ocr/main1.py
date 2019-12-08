from tesserocr import PyTessBaseAPI

with PyTessBaseAPI(path='./tessdata_best-master', lang='tur+eng') as api:
    print(api.GetAvailableLanguages())
    api.SetImageFile('IMG_5430.jpg')
    print(api.GetUTF8Text())
    
