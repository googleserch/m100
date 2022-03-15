from multiprocessing import Condition
from unicodedata import category
from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.http import HttpResponse
from divya.settings import RAZARPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from product.models import amount, post
from product.models import categories
from product.models import order
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.contrib import messages
from datetime import datetime ,timedelta
from django.utils import timezone
from datetime import date
from django.core.paginator import Paginator



def expired(request):
     
    tr=True
    troo=order.objects.filter(user=request.user,payment_status=tr)   
    for ad in troo:
       
        atr=datetime.now()
        at=str(atr)
        a=ad.date
        print("this is current date",at)
        ExpectedDate = str(a)
        
        print("this is expire date",ExpectedDate)

        if at > ExpectedDate:
           
            print("deactivate")
            tr=True
            sp=order.objects.get(payment_status=tr)
            sp1=sp
            sp1.user=request.user
            sp1.delete()
            

            cat12=User.objects.get(username= request.user)
            pro=False
            sp=order(order_id=ad.order_id,amount=ad.amount,payment_status=pro,user=cat12,date=ad.date)
            sp1=sp
            sp1.user=request.user
            sp1.save()

        else:
            print("activate")

def profilehandle(request):
    if not request.user.is_authenticated:
        return redirect("login/")
    condition12=order.objects.filter(user=request.user)
    tr=True    
    troo=order.objects.filter(user=request.user,payment_status=tr)   
    # print(a)
    expired(request)
  

    data={
        'or':troo,
        'tor':condition12,
    }    
    return render(request,'profile.html',data)








def handlelogin(request):
   
    return render(request,'login.html')





def homepage(request):
    if not request.user.is_authenticated:
        return redirect("login/")

    expired(request)

    
    # sp=order(order_id=razorpay_order_id,amount=500,payment_status=pro,user=cat12,date=expiry)
    # sp1=sp
    # sp1.user=request.user
    # sp1.save()    

    category=categories.objects.all()
    data={
        
        'category':category,
        
    }

   
   
   
    return render(request, 'home.html',data)


def posts(request,url):
    if not request.user.is_authenticated:
        return redirect("login")

    expired(request)
    cat=categories.objects.get(url=url)
    post1=post.objects.filter(category=cat)
   
    condition=order.objects.filter(user=request.user)
   
    p = Paginator(post1, 100)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
  
    data={
        'or':condition,
        'cat':cat,
        'post':page_obj
       
    }

    
    return render(request,'posts.html',data)    





def handlelogout(request):
    if request.user.is_authenticated:
        logout(request) 
        return redirect("login")
    else:   
        return redirect("login") 


razorpay_client  = razorpay.Client(auth=(RAZARPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def payment(request):
    if not request.user.is_authenticated:
        return redirect("login/")

    am=amount.objects.all()

    currency = 'INR'
    
    
    for i in am:
        a=i.s_amount
        
    # Create a Razorpay Order
    amounts = a*100
    razorpay_order = razorpay_client.order.create(dict(amount=amounts,
                                                       currency=currency,
                                                       payment_capture='0'))
    
    
   
        
    currency="inr"        
    payment_order_id=razorpay_order['id']
    callback_url = '/paymenthandler/'
    context={}
        
    context['a'] =a
    context['razorpay_amount'] =amounts
    context['razorpay_merchant_key']=RAZARPAY_API_KEY
    context['razorpay_order_id']=payment_order_id
    context['callback_url']=callback_url
    context['currency']=currency
    
    return render(request,'payment.html',context) 
   
      

@csrf_exempt
def paymenthandler(request):
    if not request.user.is_authenticated:
        return redirect("login")
  # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            cat12=User.objects.get(username= request.user)
            pro=True
            expiry=datetime.now() + timedelta(30)
            sp=order(order_id=razorpay_order_id,amount=500,payment_status=pro,user=cat12,date=expiry)
            sp1=sp
            sp1.user=request.user
            sp1.save()

            
            
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)

            
    
            if result is None:
                amount = a  # Rs. 200
                try:
 
                    # capture the payemt
                    a=razorpay_client.payment.capture(payment_id, amount)
                    print(a)
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            # return HttpResponseBadRequest()
            return HttpResponse(request,"paymentfail")
    else:
       # if other than POST request is made.
        # return HttpResponseBadRequest()
        return HttpResponse(request,"paymentfail")

    
   

def paymentsuccess(request):
    # return HttpResponse(request,"paymentsuccess")
    return render(request,'paymentsuccess.html')

def paymentfail(request):
    return HttpResponse(request,"paymentfail")

