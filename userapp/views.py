from django.shortcuts import render,redirect
from adminapp.models import Category,Product,UserInfo,PaymentMaster
from django.contrib import messages
from userapp.models import MyCart,OrderMaster
from datetime import datetime
# Create your views here.
def homepage(request):
    cat=Category.objects.all
    flower=Product.objects.all()
    return render(request,'home.html',{"cat":cat,"flower":flower})

def login(request):
    if(request.method == "GET"):
        return render(request,"login.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(uname=uname,password=password)
            messages.success(request,'Login Successful')
            messages.success(request,'Plz proceed to buy items')
        except:
            messages.success(request, 'Invalid Login')
            return redirect(login)
        else:
            request.session["uname"]=uname
            return redirect(homepage)

def showflower(request,id):    
    #get method returns single object
    id = Category.objects.get(id=id) 
    #filter method returns multiple objects   
    flower = Product.objects.filter(cat = id)
    cat = Category.objects.all()    
    return render(request,"home.html",{'flower':flower,'cat':cat})

def viewdetails(request,id):
    flower1=Product.objects.get(id=id)
    return render(request,'viewdetails.html',{'flower1':flower1})

def signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = UserInfo(uname,password,email)
        user.save()
        return redirect(login)

def signout(request):
    request.session.clear()
    return redirect(homepage)

def addToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            floid = request.POST["floid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            flower = Product.objects.get(id=floid)
            user = UserInfo.objects.get(uname = user)
            #check for duplicate entry
            try:
                cart = MyCart.objects.get(flower=flower,user=user)
            except:
                cart = MyCart()
                cart.user = user
                cart.flower= flower
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)
        else:
            return redirect(login)

def ShowAllCartItems(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    if(request.method == "GET"):       
        cartitems = MyCart.objects.filter(user=user)
        total = 0
        for item in cartitems:
            total+= item.qty*item.flower.price
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"items":cartitems})
    else:
        id = request.POST["floid"]
        flower= Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,flower=flower)            
        qty = request.POST["qty"]
        item.qty = qty
        item.save() #Update
        return redirect(ShowAllCartItems)

def removeItem(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    id = request.POST["floid"]
    flower = Product.objects.get(id=id)
    item = MyCart.objects.get(user=user,flower=flower)   
    item.delete()
    return redirect(ShowAllCartItems)


def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = PaymentMaster.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            #Its a match
            owner = PaymentMaster.objects.get(cardno='111',cvv='111',expiry='12/2025')
            owner.balance += request.session["total"]
            buyer.balance -=request.session["total"]
            owner.save()
            buyer.save()
            #Delete all items from cart
            uname = request.session["uname"]
            user = UserInfo.objects.get(uname = uname)
            
            order = OrderMaster()
            order.user = user
            order.amount = request.session["total"]
            #order.dateOfOrder = datetime.now
            #Fetch all cart items for that user
            details = ""
            items = MyCart.objects.filter(user=user)
            for item in items:
                details += (item.cake.pname)+","
                item.delete()            
            order.details = details
            order.save()
            return redirect(homepage)
def search(request):
    cat=Category.objects.all
    flower=Product.objects.all()
    return render(request,'home.html',{"cat":cat,"flower":flower})
