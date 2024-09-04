# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from customer.models import Cart
# from seller.models import Product,Category
# from django.contrib import messages
# from django.db.models import Q
# # Create your views here.
# products=Product.objects.none()
# # this make all   categories in category table will be remove  
# def home(request):
#    global products
#    global filtered_products
#    products= Product.objects.all()
#    filtered_products=products
#    data={}
#    products= Product.objects.all()
#    data["products"]=products
#    data["catogories"]=Category.objects.all()
#    if(request.user.is_authenticated):
#       user_id = request.user.id
#       print(user_id)
#       user=User.objects.get(id=user_id)
#       cart_count= Cart.objects.filter(customer_id=request.user.id).count()
#       data["cart_count"]=cart_count
#       print(cart_count)

#       if(user.is_staff==True):
#          return redirect("/seller")
#    return render(request,'customer/base.html',context=data)

# def user_register(request):
#    if(request.user.is_authenticated):
#       return redirect("/")
#    data={}
#    is_staff=False
#    if(request.method=="POST"):
#       uname = request.POST.get("username")
#       upass = request.POST.get("password")
#       ucpass = request.POST.get("cpassword")
#       utype = request.POST.get("type")
#       if(utype=="seller"):
#          is_staff=True
#       if(uname=="" or upass=="" or ucpass==""):
#          data["error_msg"] = "Fields cant be empty"
#       elif(upass!=ucpass):
#          data["error_msg"] = "Password does not matched"
#       elif(User.objects.filter(username=uname).exists()):
#          data["error_msg"] = uname+" is alredy exists"
#       else:
#          user=User.objects.create(username=uname,is_staff=is_staff)
#          user.set_password(upass)
#          user.save()
#          return redirect("/login")
#    return render(request,'customer/register.html',context=data)

# def user_login(request):
#    if(request.user.is_authenticated):
#       return redirect("/")
#    data={}
#    if(request.method=="POST"):
#       uname = request.POST.get("username")
#       upass = request.POST.get("password")
#       if(uname=="" or upass==""):
#          data["error_msg"] = "Fields cant be empty"
#       elif(not User.objects.filter(username=uname).exists()):
#          data["error_msg"] = uname+" is does not exists"
#       else:
#          authenticated_user=authenticate(username=uname,password=upass)
#          if (authenticated_user is None):
#             data["error_msg"] = "Incorrect password"
#          else:
#             login(request,authenticated_user)
#             if(authenticated_user.is_staff):
#                #to the seller dashboard
#                print("to the seller dashboard")
#                return redirect("/seller")
#             else:
#                print("to homepage  - customer")
#                #to homepage - customer
#                return redirect("/")
            
#    return render(request,'customer/login.html',context=data)

# def user_logout(request):
#    logout(request)
#    return redirect("/")

# def add_to_cart(request,product_id):
#   if(request.user.is_authenticated):
#      q1=Q(customer_id=request.user.id)
#      q2=Q(product_id=product_id)
#      cart_items= Cart.objects.filter(q1&q2)
#      if (cart_items.count()>=1):
       
#         messages.error(request,"product is alerdy in cart")
#         return redirect ('/')
#      else:
#       customer=User.objects.get(id=request.user.id)
#       product=Product.objects.get(id=product_id)
#       customer_cart=Cart.objects.create(quantity=1,customer_id=customer,product_id=product)
#       customer_cart.save()
#       messages.success(request,"product addded to cart")
   
#       return redirect ('/')
#   else:
#      return redirect('/login')
  




   
# def view_cart(request):
#    data={}
#    cart_items=Cart.objects.filter(customer_id=request.user.id)
#    # print(cart_items)
 
#    quantitiy=0
#    total_price=0
#    for item in cart_items:
#       quantitiy+=item.quantity
#       # print(quantitiy)
#       total_price+=(item.quantity*item.product_id.price)
#       # print(total_price)
      
#    data['total_price'] =total_price
#    data["quantity"]=quantitiy
#    data['cart_count']=cart_items.count()

#    data['cart_items']=cart_items
   
   
#    return render(request,'customer/cart.html',context=data)

# def delete_cart(request,cart_id):
#    cart_item=Cart.objects.get(id=cart_id)
   
#    cart_item.delete()
#    return redirect('/cart')
  
# def update_cart(request,flag,cart_id):
#    cart_items=Cart.objects.filter(id=cart_id)
#    actual_qunatity=cart_items[0].quantity
   
#    print("actual_qunatity", actual_qunatity)
  
#    if(flag=='inc'):
#       cart_items.update(quantity=actual_qunatity+1)
#    else:
#       if(actual_qunatity==1):
#          pass
#       else:
#          cart_items.update(quantity=actual_qunatity-1)
#    return redirect("/cart")

     





# def  filterBycategory(request,categoryId):
#    data={}
#    global products
#    global filtered_products
#    filtered_products=products.filter(category_id=categoryId)
#    data['products']=filtered_products
#    data["catogories"]=Category.objects.all()
   
#    return render(request,'customer/base.html',context=data)








# def sortByPrice(request,flag):
#    # data={}
#    # global filtered_products 
#    # # we want sorting done only fliterd_product when we click categories>electronics then fliterd _product show 
#    # if(flag=="high-to-low"):
#    #    sorted_products=filtered_products.order_by("-price")
#    #    data[products]=sorted_products
#    #    data["catogories"]=Category.objects.all()
#    #    return render(request,'customer/base.html',context=data)
#    # else:
#    #    sorted_products=filtered_products.order_by("-price")
#    #    data[products]=sorted_products
#    #    data["catogories"]=Category.objects.all()
#    #    return render(request,'customer/base.html',context=data)
#    data={}
#    global filtered_products
#    if(flag=="high-to-low"):
#       sorted_products=filtered_products.order_by("-price") 
#       data['products'] = sorted_products 
#       data['categories']=Category.objects.all()
#       return render(request, 'customer/base.html', context=data)
#    else:
#       sorted_products=filtered_products.order_by("price") 
#       data['products'] = sorted_products 
#       data['categories']=Category.objects.all()
#       return render (request, 'customer/base.html', context=data)
    

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from customer.models import Cart, Profile
from seller.models import Product,Category
from django.contrib import messages
from django.db.models import Q
# Create your views here.

products=Product.objects.none()
def home(request):
   data={}
   global products
   global filtered_products
   products= Product.objects.all()
   filtered_products = products
   data["products"]=products
   if(request.user.is_authenticated):
      user_id = request.user.id
      print(user_id)
      user=User.objects.get(id=user_id)

      if(user.is_staff==True):
         return redirect("/seller")
      
      cart_count= Cart.objects.filter(customer_id=request.user.id).count()
      data["cart_count"]=cart_count
      print(cart_count)

   data['categories']=Category.objects.all()
      

   return render(request,'customer/base.html',context=data)

def user_register(request):
   if(request.user.is_authenticated):
      return redirect("/")
   data={}
   is_staff=False
   if(request.method=="POST"):
      uname = request.POST.get("username")
      upass = request.POST.get("password")
      ucpass = request.POST.get("cpassword")
      utype = request.POST.get("type")
      if(utype=="seller"):
         is_staff=True
      if(uname=="" or upass=="" or ucpass==""):
         data["error_msg"] = "Fields cant be empty"
      elif(upass!=ucpass):
         data["error_msg"] = "Password does not matched"
      elif(User.objects.filter(username=uname).exists()):
         data["error_msg"] = uname+" is alredy exists"
      else:
         user=User.objects.create(username=uname,is_staff=is_staff)
         user.set_password(upass)
         user.save()
         return redirect("/login")
   return render(request,'customer/register.html',context=data)

def user_login(request):
   if(request.user.is_authenticated):
      return redirect("/")
   data={}
   if(request.method=="POST"):
      uname = request.POST.get("username")
      upass = request.POST.get("password")
      if(uname=="" or upass==""):
         data["error_msg"] = "Fields cant be empty"
      elif(not User.objects.filter(username=uname).exists()):
         data["error_msg"] = uname+" is does not exists"
      else:
         authenticated_user=authenticate(username=uname,password=upass)
         if (authenticated_user is None):
            data["error_msg"] = "Incorrect password"
         else:
            login(request,authenticated_user)
            if(authenticated_user.is_staff):
               #to the seller dashboard
               print("to the seller dashboard")
               return redirect("/seller")
            else:
               print("to homepage  - customer")
               #to homepage - customer
               return redirect("/")
            
   return render(request,'customer/login.html',context=data)

def user_logout(request):
   logout(request)
   return redirect("/")

def add_to_cart(request,product_id):
  if(request.user.is_authenticated):
     q1=Q(customer_id=request.user.id)
     q2=Q(product_id=product_id)
     cart_items= Cart.objects.filter(q1&q2)
     if (cart_items.count()>=1):
       
        messages.error(request,"product is alerdy in cart")
        return redirect ('/')
     else:
      customer=User.objects.get(id=request.user.id)
      product=Product.objects.get(id=product_id)
      customer_cart=Cart.objects.create(quantity=1,customer_id=customer,product_id=product)
      customer_cart.save()
      messages.success(request,"product addded to cart")
   
      return redirect ('/')
  else:
     return redirect('/login')
   
def view_cart(request):
   data={}
   cart_items=Cart.objects.filter(customer_id=request.user.id)
   # print(cart_items)
 
   quantitiy=0
   total_price=0
   for item in cart_items:
      quantitiy+=item.quantity
      # print(quantitiy)
      total_price+=(item.quantity*item.product_id.price)
      # print(total_price)
      
   data['total_price'] =total_price
   data["quantity"]=quantitiy
   data['cart_count']=cart_items.count()
   data['categories']=Category.objects.all() 
   data['cart_items']=cart_items
   
   
   return render(request,'customer/cart.html',context=data)

def delete_cart(request,cart_id):
   cart_item=Cart.objects.get(id=cart_id)
   
   cart_item.delete()
   return redirect('/cart')
  
def update_cart(request,flag,cart_id):
   cart_items=Cart.objects.filter(id=cart_id)
   actual_qunatity=cart_items[0].quantity
   
   print("actual_qunatity", actual_qunatity)
  
   if(flag=='inc'):
      cart_items.update(quantity=actual_qunatity+1)
   else:
      if(actual_qunatity==1):
         pass
      else:
         cart_items.update(quantity=actual_qunatity-1)
   return redirect("/cart")

def filterByCategory(request,categoryId):
   data={}
   global products
   global filtered_products
   filtered_products = products.filter(category_id=categoryId)
   data['products'] = filtered_products
   data['categories'] = Category.objects.all()
   
   cart_count= Cart.objects.filter(customer_id=request.user.id).count()
   data["cart_count"]=cart_count
   return render(request,'customer/base.html',context=data)


def sortByPrice (request, flag):
   data={}
   global filtered_products
   if(flag=="high-to-low"):
      sorted_products=filtered_products.order_by("-price") 
      data['products'] = sorted_products 
      data['categories']=Category.objects.all()
      return render(request, 'customer/base.html', context=data)
   else:
      sorted_products=filtered_products.order_by("price") 
      data['products'] = sorted_products 
      data['categories']=Category.objects.all()
      return render (request, 'customer/base.html', context=data)
 
def searchByName(request):
    data = {}
    # This is an empty dictionary. We'll use it to collect data to send to the HTML page.

    global filtered_products
    # This tells the function that it will use the global list called filtered_products.

    if request.method == "POST":
        product_name = request.POST.get("product_name")
        # Get the product name that the user typed in the form.

       
        searched_products = filtered_products.filter(name__icontains=product_name)
        # Search for products in filtered_products where the name contains the product_name.

        data['products'] = searched_products
        # Add the found products to the data dictionary under the key 'products'.

        data['categories'] = Category.objects.all()
        # Add all categories from the database to the data dictionary under the key 'categories'.
        cart_count= Cart.objects.filter(customer_id=request.user.id).count()
        data["cart_count"]=cart_count
        return render(request, 'customer/base.html', context=data)
        # Render the 'customer/base.html' page with the data dictionary.
     
    return redirect("/")
        # Redirect the user back to the home page.




def filterByPriceRange(request):
   data={}
   global filtered_products
   if(request.method=="POST"):
      min=request.POST.get("min")
      max=request.POST.get("max")
      q1=Q(price__gte=min)
      # Q(price__gte=min) note price is column name in sql table gte=greate than equal lte=less than equal
      q2=Q(price__gte=max)
      filter_by_price_range= filtered_products.filter(q1&q2)
      print(filter_by_price_range)
      data["products"]=filter_by_price_range
      data['categories']=Category.objects.all()
      return render(request,'customer/base.html',context=data)
   return redirect("/")
   

def updateProfile(request):
    data = {}
    user = User.objects.filter(id=request.user.id)

    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")

        # Updating firstname, lastname and email into User model (i.e., auth_user)
        user.update(first_name=firstname, last_name=lastname, email=email)

        if Profile.objects.filter(user_id=request.user.id).exists():
            existing_profile = Profile.objects.filter(user_id=request.user.id)
            existing_profile.update(contact=contact, street=street, city=city, state=state, pincode=pincode)
        else:
            user_object = User.objects.get(id=request.user.id)
            new_profile = Profile.objects.create(
                contact=contact, street=street, city=city, state=state, pincode=pincode, user_id=user_object)
            new_profile.save()

        return redirect("/profile")

    cart_count = Cart.objects.filter(customer_id=request.user.id).count()
    data['cart_count'] = cart_count

    userx = User.objects.get(id=request.user.id)
    profilex = Profile.objects.filter(user_id=userx)

    if not userx.first_name and profilex.count() == 0:
        print("data does not exist")
    else:
        data['user'] = userx
        data['address'] = profilex[0]
        return render(request, 'customer/profile.html', context=data)

    return render(request, 'customer/profile.html', context=data)




def order_summary(request):
    data={}
    cart_items=Cart.objects.filter(customer_id=request.user.id)
   # print(cart_items)
    quantitiy=0
    total_price=0
    for item in cart_items:
       quantitiy+=item.quantity
      # print(quantitiy)
       total_price+=(item.quantity*item.product_id.price)
      # print(total_price)
       data['total_price'] =total_price
       data["quantity"]=quantitiy
       data['cart_count']=cart_items.count()
       data['categories']=Category.objects.all() 
       data['cart_items']=cart_items
       address=Profile.objects.filter(user_id=request.user.id)
       data["address"]=address[0] 



      
    import razorpay  

    client = razorpay.Client(auth=("rzp_test_93atKPgF1eLJ4M", "ZighzyBxP2GddO81jA8fXqCy"))  
    payment_data = {  
                       "amount": total_price,  
                        "currency": "INR",  
                        "receipt": "order_rcptid_11"  
                               }
    payment = client.order.create(data=payment_data)
    return render(request, 'customer/order_summary.html', context=data)