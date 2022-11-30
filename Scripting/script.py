from PIL import Image , ImageFilter
#open the .jpeg into an image object with PIL
img = Image.open('Scripting\\pokedex\\pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

filter_img = img.convert('L')
filter_img.save('grey.png', 'png')
croocked = filtered_img.rotate(90)
croocked.save('gary.png', 'png')

print(img.format)
print(img.size)
print(img.mode)

