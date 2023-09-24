from django.shortcuts import render, redirect
from .models import *
from .forms import *

# from .models import Product
# from .forms import  FormaSok, FormaStudents
# Create your views here.
def index(req):
    return render(req,'index.html')

def add(request):
    # products = [
    #     [1, 'апельсин', 140, 1, 'тетрапак', True, 1],
    #     [2, 'apple', 150, 1, 'банка', True, 0.5],
    #     [3, 'multy', 155, 1, 'тетрапак', True, 2],
    #     [4, 'апельсин', 140, 2, 'пластик', False, 1.5],
    #     [5, 'apple', 150, 2, 'стекло', True, 0.5],
    #     [6, 'multy', 155, 2, 'стекло', True, 0.5],
    #     [7, 'апельсин', 140, 2, 'пластик', False, 1.5],
    #     [8, 'apple', 150, 2, 'тетрапак', True, 1],
    #     [9, 'multy', 155, 2, 'банка', True, 0.33]
    # ]
    #
    # for product in products:
    #     p = Product()
    #     p.id = product[0]
    #     p.name = product[1]
    #     p.price = product[2]
    #     p.firma_id = product[3]
    #     p.volume = product[6]
    #     p.packaging = product[4]
    #     p.recommended = bool(int(product[5]))
    #     p.save()
    #     return redirect('home')
    # if request.method == 'POST':
    #     product = Product()
    #     product.name = request.POST.get('name')
    #     product.price = request.POST.get('price')
    #     product.volume = request.POST.get('volume')
    #     product.packaging = request.POST.get('packaging')
    #     product.recommended = request.POST.get('recommended')
    #     product.save()
    #
    #     return redirect('home')
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    # p1=Product(name='orange', price=140)
    # p2 = Product(name='apple', price=150)
    # p3 = Product(name='multy', price=155)
    # c1=Company.objects.get(title='J7')
    # c2 = Company.objects.get(title='DOBRY')
    # c1.product_set.add(p1, bulk=False)
    # c1.product_set.add(p2, bulk=False)
    # c1.product_set.add(p3, bulk=False)
    # c2.product_set.add(p1, bulk=False)
    # c2.product_set.add(p2, bulk=False)
    # c2.product_set.add(p3, bulk=False)
    # print(c2.product_set.count)
    # print(c2.product_set.values_list())

    # s1 = Student.objects.create(name='Viktor',group='G001')
    # s2 = Student.objects.create(name='Boris', group='G001')
    # s3 = Student.objects.create(name='Maxim', group='G001')
    # s4 = Student.objects.create(name='Igor', group='G002')
    # s5 = Student.objects.create(name='Zahar', group='G002')
    # k1= Course.objects.create(title='Math')
    # k2 = Course.objects.create(title='Geo')
    # k1.student_set.add(s1,s2,s5)
    # k1.student_set.add(s2)
    # k1.student_set.add(s5)
    # k2.student_set.add(s1,s2,s3)
    # k2.student_set.add(s2)
    # k2.student_set.add(s3)
    # u1=User.objects.create(name='Alex')
    # ac1=Account.objects.create(login='asd', password='12345',user=u1)

    return redirect('home')

def table1(req):
    #заходим на страницу первый раз
    baza=Product.objects.all()
    anketa=FormaSok()
    bd=[]
    if req.POST:#нажали на кнопку submit
        # bd=[]
        anketa = FormaSok(req.POST)#форма с прошлым запросом
        a=req.POST['firma']#собираем данные
        b=req.POST['sok']
        print(a,b,'***************')
        #выбираем таблицу для вывода(перебор вариантов)
        if a and not b:
            baza = Product.objects.filter(firma_id=a)
        elif b and not a:
            c=Product.objects.get(id=b).name
            baza = Product.objects.filter(name=c)
        elif a and b:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(firma_id=a, name=c)
        else:
            baza = Product.objects.all()
    #заполняется таблица
    for i in baza:
        bd.append([i.name,i.price,i.volume,i.packaging,i.recommended,i.firma.title])
        # bd.append(i.price)
        # bd.append(i.firma.title)

    print(bd)
    title=['Название','Цена','Объем','Упаковка','Рекомендована','Фирма']#сторка с заголовком
    # if req.POST:
    #     bd=[]
    #     a=req.POST['firma']
    #     baza=Product.objects.filter(firma_id=a)
    #     for i in baza:
    #         bd.append([i.name,i.price,i.firma.title])
    data={'table':bd,'title':title,'forma':anketa}#данные для вывода
    return render(req,'totable.html',context=data)


def table2(req):
    #заходим на страницу
    baza = Student.objects.all()
    anketa = FormaStudents()
    bd=[]
    if req.POST:
        anketa = FormaStudents(req.POST)
        course_id = req.POST.get('course')  # собираем данные
        student_name = req.POST.get('name')

        if course_id and not student_name:
            baza = Student.objects.filter(course__id=course_id)  # Используйте course__id для фильтрации
        elif student_name and not course_id:
            c = Student.objects.get(id=student_name).name
            baza = Student.objects.filter(name=c)
        elif course_id and student_name:
            c = Student.objects.get(id=student_name).name
            baza = Student.objects.filter(course__id=course_id, name=c)  # Используйте course__id для фильтрации
        else:
            baza = Student.objects.all()

    for i in baza:
        temp=i.course.all()
        kursi=''
        for t in temp:
            kursi+=t.title + ' '

        bd.append([i.name, i.group, kursi])

    title = ['Имя', 'Группа', 'Курсы'] #  строка с загаловками
    data = {'table': bd, 'title': title, 'forma': anketa}  # данные для вывода
    return render(req, 'totable.html', context=data)


def table3(req):
    #заходим на страницу
    baza = User.objects.all()
    anketa = FormaUser()
    bd=[]

    if req.POST:
        anketa = FormaUser(req.POST)
        a = req.POST['user']  # собираем данные

        baza = User.objects.filter(id=a)

    for i in baza:
        bd.append([i.account.login, i.account.password])

    print(bd)
    title = ['Имя', 'Логин', 'Пароль'] #  строка с загаловками
    data = {'table': bd, 'title': title, 'forma': anketa}  # данные для вывода
    return render(req, 'totable.html', context=data)


