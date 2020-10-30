from imagedown import ImageDown 

imagedown = ImageDown('system of a down', 10)
imagedown.get_urls()
print(imagedown.download('./ig/'))