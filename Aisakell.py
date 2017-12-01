from wordcloud import WordCloud
pilv=WordCloud().generate(open("Aisakell", "r").read())
pilt=pilv.to_image()
pilt.save('pilt1.png')