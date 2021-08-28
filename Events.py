import threading as tr

try:
    event = tr.Event()

    choose = int(
        input('''Kerakli fremework tartib raqamini tanlang    
        1) Django
        2) Flask
        3) CherryPy

        :'''))

    def frameworks():
        event.wait()
        if choose == 0:
            print("iltimos so'rov buyicha faqat mavjud bo'lgan tartib raqam kiriting❗")
        if choose == 1:
            print("Django, bepul va ochiq manbali Python asosi, ishlab chiquvchilarga murakkab kod va ilovalarni tezda ishlab chiqish imkonini beradi. Django ramkasi sifatli veb -ilovalarni ishlab chiqishda yordam beradi. Bu eng yaxshi python ramkalaridan biri bo'lib, API va veb -ilovalarni tez ishlab chiqish uchun ishlatiladi")
        if choose == 2:
            print("Flask - bu Sinatra Ruby ramkasidan ilhomlangan BSD litsenziyasi ostida foydalanish mumkin bo'lgan Python ramkasi. Idish Werkzeug WSGI asboblar qutisi va Jinja2 shabloniga tayanadi. Asosiy maqsad - kuchli veb -ilovalar bazasini yaratishga yordam berish.")    
        if choose == 3:
            print("CherryPy, deyarli o'n yoshda, juda tez va barqaror ekanligini isbotladi. Bu ochiq manbali Python veb-ishlab chiqish tizimi bo'lib, u o'zining ko'p tarmoqli serverini o'rnatadi. Python -ni qo'llab -quvvatlaydigan har qanday ishchi tizimda ishlashi mumkin.")


    starting = tr.Thread(target = frameworks)
    starting.start()


    if 1 <= choose <= 3:
        event.set()
    elif choose != 1 | 2 | 3:
        choose = 0
        event.set()    

except ValueError:
    print("iltimos so'rov bo'yicha faqat tartib raqamlardan foydalaning❗")
