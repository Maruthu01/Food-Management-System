from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Register,FoodStall,JuiceStall,IcecreamStall
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def Map(request, id):
    stall = get_object_or_404(FoodStall, id=id)
    if stall.Location and stall.Location != 'NIL':
        return redirect(stall.Location)
    else:
        messages.warning(request,'Location Not Available')
        return redirect('Show_stalls')
    
#Delete Icecream
def delete_icecream_stall(request,id):
    Creams = get_object_or_404(IcecreamStall, id=id, user = request.user)
    if request.method == 'POST':
        Creams.delete()
        messages.success(request,'Stall Deleted Successfully')
        return redirect('Icecream_stall')
    return redirect(request,'Icecream_stall.html')


#For Juice Detele
def delete_juice_stall(request,id):
    Juices = get_object_or_404(JuiceStall, id=id, user=request.user)
    if request.method == 'POST':
        Juices.delete()
        messages.success(request,'Stall Deleted Successfully')
        return redirect('Juice_stalls')
    return render(request,'delete_stall.html',{'Juices':Juices})

#For Food Stall
def delete_stall(request, id):
    stall = get_object_or_404(FoodStall, id=id, user=request.user)
    if request.method == 'POST': 
        stall.delete()
        messages.success(request, 'Stall deleted successfully!')
        return redirect('Home')  
    return render(request, 'delete_stall.html', {'stall': stall})



#For Update Icecream
def update_icecream_stall(request,id):
    Creams = get_object_or_404(IcecreamStall, id=id, user = request.user)
    if request.method == 'POST':
        Creams.Name = request.POST.get('stall_name',Creams.Name)
        Creams.Ice_type = request.POST.get('Ice_type',Creams.Ice_type)
        Creams.Contact_num = request.POST.get('contact_number', Creams.Contact_num)
        Creams.Address = request.POST.get('address', Creams.Address)
        Creams.opening_time = request.POST.get('opening_time', Creams.opening_time)
        Creams.closing_time = request.POST.get('closing_time', Creams.closing_time)
        Creams.Location = request.POST.get('Location',Creams.Location)
        
        if 'stall_image' in request.FILES:
            Creams.Stall_images = request.FILES['stall_image']
        Creams.save()
        messages.success(request,'Changes Updated Successfully')
        return redirect('Icecream_stall')
    return render(request,'update_icecream_stall.html',{'Creams':Creams})
        

#For Juice Stall
def update_juice_stall(request,id):
    Juices = get_object_or_404(JuiceStall, id=id, user=request.user)
    if request.method == 'POST':
        Juices.Name = request.POST.get('stall_name',Juices.Name)
        Juices.Juice_type = request.POST.get('Juice_type',Juices.Juice_type)
        Juices.Contact_num = request.POST.get('contact_number', Juices.Contact_num)
        Juices.Address = request.POST.get('address', Juices.Address)
        Juices.opening_time = request.POST.get('opening_time', Juices.opening_time)
        Juices.closing_time = request.POST.get('closing_time', Juices.closing_time)
        Juices.Location = request.POST.get('Location',Juices.Location)
        
        if 'stall_image' in request.FILES:
            Juices.Stall_images = request.FILES['stall_image']
        Juices.save()
        messages.success(request,'Changes Updated Successfully')
        return redirect('Juice_stalls')
    return render(request,'Update_juice.html',{'Juices':Juices})
        

#For FOOD Srall
def edit_stall(request, id):
    stall = get_object_or_404(FoodStall, id=id, user=request.user)  

    if request.method == 'POST':
        stall.Name = request.POST.get('stall_name', stall.Name)
        stall.Food_type = request.POST.get('food_type', stall.Food_type)
        stall.Contact_num = request.POST.get('contact_number', stall.Contact_num)
        stall.Address = request.POST.get('address', stall.Address)
        stall.ratings = request.POST.get('ratings', stall.ratings)
        stall.opening_time = request.POST.get('opening_time', stall.opening_time)
        stall.closing_time = request.POST.get('closing_time', stall.closing_time)
        stall.Location = request.POST.get('Location',stall.Location)
        
        if 'stall_image' in request.FILES:  
            stall.Stall_images = request.FILES['stall_image']
        stall.save()
        messages.success(request, 'Stall updated successfully!')
        return redirect('Home')  
    return render(request, 'edit_stall.html', {'stall': stall})  

def Icecream_stalls(request):
    Creams = IcecreamStall.objects.all()
    return render(request,'Icecream_stall.html',{'Creams':Creams})

def Juice_stalls(request):
    Juices = JuiceStall.objects.all()
    return render(request,'Juice_stalls.html',{'Juices':Juices})


def Show_stalls(request):
    stalls = FoodStall.objects.all()
    return render(request,'Show_stalls.html',{'stalls':stalls})



#For Icecream stalll
def Add_icecream(request):
    if not request.user.is_authenticated:
        messages.warning(request,'You need to login to add stalls')
        return redirect ('Login')
    
    if request.method == 'POST':
        Name = request.POST.get('stall_name')
        Ice_type = request.POST.get('Ice_type')
        Contact_num = request.POST.get('contact_number')
        Address = request.POST.get('address')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        Stall_images = request.FILES.get('stall_image')
        Location = request.POST.get('Location')
        if len(Contact_num) == 10:
            IcecreamStall.objects.create(
                Name=Name,
                Ice_type = Ice_type,
                Contact_num = Contact_num,
                Address = Address,
                opening_time = opening_time,
                closing_time = closing_time,
                Stall_images = Stall_images,
                Location=Location,
                user = request.user                
            )
            messages.success(request,'Stall Added Successfully')
            return redirect('Add_icecream')
        else:
            messages.warning(request,'Enter Valid Num')
            return render(request,'Icecream_stall.html')
    return render(request,'Add_icecream.html')


def Add_juice(request):
    if not request.user.is_authenticated:
        messages.warning(request,'You need to log in to add Juice stalls.')
        return redirect('Login')
        
    if request.method == 'POST':
        Name = request.POST.get('stall_name')
        Juice_type = request.POST.get('Juice_type')
        Contact_num = request.POST.get('contact_number')
        Address = request.POST.get('address')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        Stall_images = request.FILES.get('stall_image')
        Location = request.POST.get('Location')
        if len(Contact_num) == 10:
            JuiceStall.objects.create(
                Name=Name,
                Juice_type = Juice_type,
                Contact_num = Contact_num,
                Address = Address,
                opening_time = opening_time,
                closing_time = closing_time,
                Stall_images = Stall_images,
                Location=Location,
                user = request.user
            )
            messages.success(request,'Juice Stall added Successfully')
            return redirect('Juice_stalls')
        else:
            messages.warning(request,'Enter valid number')
            return render(request,'Add_juice.html')
    return render(request,'Add_juice.html')
    


def Add_stall(request): 
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to log in to add stalls.')
        return redirect('Login') 

    if request.method == 'POST':
        Name = request.POST.get('stall_name')
        Food_type = request.POST.get('food_type')
        Contact_num = request.POST.get('contact_number')
        Address = request.POST.get('address')
        ratings = request.POST.get('ratings')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        Stall_images = request.FILES.get('stall_image')
        Location = request.POST.get('Location')   
        if len(Contact_num) == 10:
            FoodStall.objects.create(
                Name=Name,
                Food_type=Food_type,
                Contact_num=Contact_num,
                Address=Address,
                ratings=ratings,
                opening_time=opening_time,
                closing_time=closing_time,
                Stall_images=Stall_images,
                Location = Location,
                user=request.user,
            )
            messages.success(request, 'Stall added successfully!')
            return redirect('Home')
        else:
            messages.warning(request,'Please enter valid Contact Number')
            return render(request,'Add_stall.html')

    return render(request, 'Add_stall.html')    
        
        
def Logout_page(request):
    logout(request)
    messages.success(request,'You are Logged Out!!!')
    return redirect('Home')

def Login_page(request):
    if request.method == 'POST':
        User_name = request.POST['username']
        Password = request.POST['password']
        user = authenticate(request, username=User_name, password=Password)
        if user is not None:
            login(request, user)
            return redirect('Home') 
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('Login')
    return render(request, 'login.html')



def Registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_id = request.POST['email_id']
        mob_num = request.POST['mob_num']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']
        terms_check = request.POST.get('terms_check')
        
        
        
        
        if not email_id.endswith('@gmail.com'):
            messages.warning(request, 'Please enter a valid Gmail address')
            return render(request, 'Register_page.html')
        if password == conf_pass:
            if len(mob_num) == 10:
                if terms_check:
                    user = User.objects.create_user(username=username, email=email_id, password=password)
                    user.save()
                    Register.objects.create(User_name=username, Email_id=email_id, Ph_no=mob_num, Password=password)
                    messages.success(request, 'You are registered successfully')
                    return redirect('Login')
                else:
                    messages.warning(request, 'You must agree to the terms and conditions')
                    return redirect('Register')
            else:
                messages.warning(request, 'Please enter a valid mobile number')
                return redirect('Register')
        else:
            messages.warning(request, 'Password and Confirmed Password should be the same...')
            return redirect('Register')

    return render(request, 'Register_page.html')



def Home_page(request):
    return render (request,'Home.html')
