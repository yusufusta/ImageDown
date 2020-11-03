from imagedown import ImageDown 

imagedown = ImageDown().Yandex('altın gün', 10)
imagedown.get_urls()
print(imagedown.download('./ig/'))