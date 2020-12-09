from django.shortcuts import render,redirect
from student.models import Grade, Student

def index(request):
    Grade.objects.create(g_name="大数据一班")
    Grade.objects.create(g_name="大数据二班")
    Grade.objects.create(g_name="大数据三班")
    g1 = Grade.objects.filter(g_name="大数据一班").first()
    Student.objects.create(s_name="aa", age="19", sex="男", address="宇宙", phone="123", s_id=g1)
    Student.objects.create(s_name="bb", age="18", sex="女", address="地球", phone="321", s_id=g1)
    Student.objects.create(s_name="cc", age="20", sex="男", address="陕西", phone="135", s_id=g1)
    g2 = Grade.objects.filter(g_name="大数据二班").first()
    Student.objects.create(s_name="cc", age="20", sex="男", address="西安", phone="135", s_id=g2)
    Student.objects.create(s_name="cc", age="20", sex="男", address="咸阳", phone="135", s_id=g2)
    Student.objects.create(s_name="cc", age="20", sex="男", address="渭南", phone="135", s_id=g2)
    g3 = Grade.objects.filter(g_name="大数据三班").first()
    Student.objects.create(s_name="cc", age="20", sex="男", address="四川", phone="135", s_id=g3)
    Student.objects.create(s_name="cc", age="20", sex="男", address="延安", phone="135", s_id=g3)
    Student.objects.create(s_name="cc", age="20", sex="男", address="山西", phone="135", s_id=g3)
    return render(request, "index.html")

def show(request):
    if request.method == "GET":
        g_all = Grade.objects.all()
        s_all = Student.objects.all()
        return render(request,"show.html",{"g_all":g_all,"s_all":s_all})
    else:
        g_name = request.POST.get("g_name")
        s_name = request.POST.get("s_name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        g1 = Grade.objects.filter(g_name=g_name).first()
        if g1:
            Student.objects.create(s_name=s_name,age=age,sex=sex,address=address,phone=phone,s_id=g1)
        else:
            new_g = Grade(g_name=g_name)
            new_g.save()
            Student.objects.create(s_name=s_name,age=age,sex=sex,address=address,phone=phone,s_id=new_g)
        return redirect("show")

def delete(request,id):
    s = Student.objects.filter(id = id).first()
    if s:
        s.delete()
    return redirect("show")

def update(request,id):
    s= Student.objects.filter(id = id).first()
    if request.method=="GET":
        return render(request,"update.html",{"s":s})
    else:
        g_name = request.POST.get("g_name")
        s_name = request.POST.get("s_name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        if s_name:
            s.s_name = s_name
        if age:
            s.age = age
        if sex:
            s.sex = sex
        if address:
            s.address = address
        if phone:
            s.phone = phone
        gg = Grade.objects.filter(g_name=g_name).first()
        if gg:
            s.s_id = gg
        else:
            new_g = Grade(g_name=g_name)
            new_g.save()
            s.s_id = new_g

        s.save()
        return redirect("show")
