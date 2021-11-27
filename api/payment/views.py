from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import get_user_model 
from django.views.decorators.csrf import csrf_exempt 
import braintree
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="3kc84dyqrb5rkqwg",
        public_key="2y9kc9t6q462jd7d",
        private_key="66674c6a0b4f4816754d9273cef438be"
    )
)
def validate_user_session(id,token):
    UserModel=get_user_model() 
    try:
        user=UserModel.objects.get(pk=id) 
        if user.session_token==token:
            return True 
        else:
            return False
    except UserModel.DoesNotExist:
        return False
@csrf_exempt 
def generate_token(request,id,token):
    if not validate_user_session(id,token):
        return({'error':'invalid user'}) 
    else:
        return JsonResponse({'clientToken':gateway.client_token.generate(),'success':True}) 
@csrf_exempt 

def process_payment(request,id,token):
     if not validate_user_session(id,token):
        return({'error':'invalid user| please login'}) 
     nonce_from_the_client=request.POST['paymentMethodNonce'] 
     amount_from_client=request.POST['amount'] 

     result= geteway.transaction.sale({
         "amount":amount_from_client,
         "payment_method_nonce": nonce_from_the_client,
         "options":{
             "submit_for_settlement":True
         }
     })
     if result.is_success:
         return JsonResponse({"success": result.is_success,"trasanction":{'id':result.result.transaction.id,'amount':result.transaction.amount}})
     else:
         return JsonResponse({'error':True,'success':False})