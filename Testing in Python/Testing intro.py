def future_gf():
    intro = raw_input('Hey! :')
    build_up = raw_input('Wanted to ask you a question : ')
    print('Ummm, I like you a lot')
    prop = raw_input('Do you like me as well ?')
    accept = False
    while not accept:
        if prop == 'yes':
            print('Inner self: jabadabaduuu')
            print('Outer self : That`s nice to hear, let`s date')
            accept = True
        else:
            prop = raw_input('wrong answer, please try again unitl you change your mind')
future_gf()