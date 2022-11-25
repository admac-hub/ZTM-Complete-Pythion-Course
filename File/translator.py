from transalte Import Translator 

translator = Translator(to_lang='ja')

try: 
    with open('File\\test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('File\\text-ja.txt', mnode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('check your file path')