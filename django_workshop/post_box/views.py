from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from post_box.models import Adress, Person, PhoneNumber, Email

@method_decorator(csrf_exempt, name="dispatch")
class New(View):
    
    def get(self,request):
        response = HttpResponse()
          
        response.write("""
            <form method="POST">
            First name: <input type="text" name="fname"><br>
            Surname: <input type="text" name="sname"><br>
            Description: <input type="text" name="descr"><br>
            City: <input type="text" name="city"><br>
            Street: <input type="text" name="street"><br>
            House number: <input type="text" name="h_number">
            Flat number:<input type="text" name="f_number"><br>
            Phone number: <input type="text" name="ph_number">
            Type: <input type="text" name="ph_type"><br>
            E-mail: <input type="text" name="email">
            Type: <input type="text" name="em_type"><br>
            <input type="submit" value="Submit">
            </form> """)
        
        return response
    
    def post(self, request):
        response = HttpResponse()
        
        fname = request.POST.get("fname")
        sname = request.POST.get("sname")
        desc = request.POST.get("descr")        #To wszystko mozna napisac ladniej
        city = request.POST.get("city")         #ponizej
        street = request.POST.get("street")
        h_num = request.POST.get("h_number")
        f_num = request.POST.get("f_number")
        ph_num = request.POST.get("ph_number")
        ph_type = request.POST.get("ph_type")
        email = request.POST.get("email")
        em_type = request.POST.get("em_type")
        
        a = Adress.objects.create(city=city, street=street, house_number=h_num, flat_number=f_num) 
        p = Person.objects.create(name=fname, surname=sname, description=desc, adress=a)
        PhoneNumber.objects.create(number=ph_num, type=ph_type, person=p)
        Email.objects.create(email=email, type=em_type, person=p)
        
        #chce podpiac adres pod persona
        
        response.write("Wyslales forma")
        
        return response
    
class Modify(View):
    
    def get(self, request, id):
        response = HttpResponse()
        
        person = Person.objects.get(pk=id)
        response.write("{} {}".format(person.name, person.surname))
        
        return response
    