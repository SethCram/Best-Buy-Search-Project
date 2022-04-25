from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse, reverse_lazy

from django.views import generic

from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages

from django.db.models import Q #for query objs

from .models import VendorProduct, User, Customer, Vendor#, Question, Choice
#from django.contrib.auth.models import User

from .forms import CustomerSignUpForm, VendorSignUpForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import customer_required, vendor_required

# Create your views here.

#cart related views

@login_required
@customer_required
def add_to_cart(request, pk):
    
    #get product requested
    vendorproduct = get_object_or_404(VendorProduct, PID = pk)
    #get customer who initiated 
    customer = Customer.objects.get(user = request.user)
    #save product to customer's products
    customer.products.add(vendorproduct)
    customer.save()

    #succeed message + redir to cart
    messages.success(request, "Cart updated!")
    
    #send to checkout
    #return redirect('BestBuySearch:checkout')

    #redirect user to url user left
    #return HttpResponseRedirect(request.path_info)

    #return user to prev url (works better for me)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@customer_required
def rm_from_cart(request, pk):
    
    #get product requested
    vendorproduct = get_object_or_404(VendorProduct, PID = pk)
    #get customer who initiated 
    customer = Customer.objects.get(user = request.user)
    #save product to customer's products
    customer.products.remove(vendorproduct)
    customer.save()

    #succeed message + redir to cart
    messages.success(request, "Cart updated!")
    #send to checkout
    return redirect('BestBuySearch:checkout')

@method_decorator([login_required, customer_required], name = 'dispatch')
class Cart( generic.ListView ):
    template_name = "BestBuySearch/checkout.html" #have to specify app_name/template_name bc templates r namespaced using app_name
    context_object_name = 'checkoutproducts_list'

    def get_queryset(self):
        """
        Return all products in customer's cart.
        """
        #find customer w/ user id
        customer = Customer.objects.get(pk = self.request.user.id)
        #retrieve that customer's products added to their cart
        checkoutproducts_list = customer.products.all() #need to call all(), or else not list of iteratable objs
        return checkoutproducts_list


#signup views
    
"""First ed: 
class CustomerSignUpView( generic.CreateView ):
    form_class = UserCreationForm #assign form
    
    #w/ form completed, ret to login page:
    success_url = reverse_lazy("login") #used to be BestBuySearch:index
    template_name = "registration/customer_signup.html"
"""
    
class CustomerSignUpView( generic.CreateView ):
    """Use model user and custom form_class."""
    model = User
    
    #custom form class
    form_class = CustomerSignUpForm
    
    template_name = "registration/customer_signup.html"

    def get_context_data(self, **kwargs):
        """Assign user type."""
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        """Save custom form and pass it to the user to save."""
        user = form.save()
        login(self.request, user)
        return redirect('login')
    
"""First ed:
class VendorSignUpView( generic.CreateView ):
    form_class = UserCreationForm #assign form
    
    #w/ form completed, ret to index page:
    success_url = reverse_lazy("login")
    template_name = "registration/vendor_signup.html"
"""

class VendorSignUpView( generic.CreateView ):
    model = User
    
    #custom form class
    form_class = VendorSignUpForm
    
    template_name = "registration/vendor_signup.html"
    
    def get_context_data(self, **kwargs):
        """Assign user type."""
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        """Save custom form and pass it to the user to save."""
        user = form.save()
        login(self.request, user)
        return redirect('login')

#item views

@method_decorator([login_required], name = 'dispatch') #why dispatch?
class ProductView(generic.ListView):
    """Generic product view displayed on home page."""
    template_name = 'BestBuySearch/products.html'
    #usable from html:
    context_object_name = 'vendorproduct_list'
    
     
    def get_queryset(self):
        """Return four most recently updated products."""
        return VendorProduct.objects.order_by('-update_date')[:4]

@method_decorator([login_required], name = 'dispatch') 
class ProductDetailsView(generic.DetailView): #should be DetailView not ListView
    """A specific product's detail view."""
    #need to specify model for DetailView
    model = VendorProduct
    template_name = 'BestBuySearch/product_details.html'
    #usable from html:
    #can't have in details view?: context_object_name = 'recommendedproduct_list'
     

class ExactResultsView(generic.ListView):
    """Exact search results view."""
    model = VendorProduct
    template_name = "BestBuySearch/exact_results.html" #have to specify app_name/template_name bc templates r namespaced using app_name
    context_object_name = 'exactmatch_list'
    
    def get_queryset(self):
        """
        Return VendorProduct filtered by search.
        Empty query returns four most recently updated products.
        """
        
        #get user input from template
        query = self.request.GET.get("q") #get "q" rslt from template
        
        #if no query:
        if( query == None ):
            #order by most recently updated items:
            exactmatch_list = VendorProduct.objects.order_by('-update_date')[:4]
            return exactmatch_list
        else:
        
            exactmatch_list = VendorProduct.objects.filter(
                #filter by name and category being contained
                Q(name__iexact = query) | Q(category__iexact = query)
            )
            return exactmatch_list
        
        
class SimilarResultsView(generic.ListView):
    """
    Similar search results view. 
    """
    model = VendorProduct
    template_name = "BestBuySearch/similar_results.html" #have to specify app_name/template_name bc templates r namespaced using app_name
    context_object_name = 'similarmatch_list'
    
    def get_queryset(self):
        """
        Return VendorProduct filtered by substring search.
        Empty query returns four most recently updated products.
        """
        
        #get user input from template
        query = self.request.GET.get("q") 
        
        #if no query:
        if( query == None ):
            #order by most recently updated items:
            similarmatch_list = VendorProduct.objects.order_by('-update_date')[:4]
            return similarmatch_list
        else:
        
            similarmatch_list = VendorProduct.objects.filter(
                #filter by name or category being similar
                Q(name__icontains = query) | Q(category__icontains = query)
            )
            return similarmatch_list

class RequirementResultsView(generic.ListView):
    """
    Requirements search results view. Incomplete.
    """
    model = VendorProduct
    template_name = "BestBuySearch/requirement_results.html" 
    context_object_name = 'requirementmatch_list'
    
    def get_queryset(self):
        """
        Return VendorProduct filtered by substring search.
        Empty query returns four most recently updated products.
        """
        
        #get user input from template
        query = self.request.GET.get("q") 
        
        #if no query:
        if( query == None ):
            #order by most recently updated items:
            requirementmatch_list = VendorProduct.objects.order_by('-update_date')[:4]
            return requirementmatch_list
        else:
        
            requirementmatch_list = VendorProduct.objects.filter(
                #filter by name or category being similar
                Q(name__icontains = query) | Q(category__icontains = query)
            )
            return requirementmatch_list


@method_decorator([login_required], name = 'dispatch') #why dispatch?
class AllProductsView( generic.ListView ):
    #unneeded?: model = VendorProduct
    template_name = "BestBuySearch/all_products.html" #have to specify app_name/template_name bc templates r namespaced using app_name
    context_object_name = 'allproducts_list'

    def get_queryset(self):
        """
        If vendor, return products created by this vendor.
        If customer return all products.
        """
        if(self.request.user.is_vendor):
            allproducts_list = VendorProduct.objects.filter(created_by = self.request.user.id)
            return allproducts_list
        elif(self.request.user.is_customer):
            allproducts_list = VendorProduct.objects.all()
            return allproducts_list
   
#form views    
   
@method_decorator([login_required, vendor_required], name = 'dispatch') #why dispatch?
class ProductCreateView( LoginRequiredMixin, generic.edit.CreateView ):
    model = VendorProduct
    fields = ['name', 'cost', 'category', 'payment_type', 'quantity', 'small_display_image', 'big_display_image']
    template_name = 'BestBuySearch/VendorProduct_add.html'
    
    def form_valid(self, form):
        """Overrides form_valid to add product."""
        #fill for vendor:
        form.instance.pub_date = timezone.now()
        form.instance.update_date = timezone.now()
        form.instance.created_by = self.request.user
        
        return super().form_valid(form)
  
@method_decorator([login_required, vendor_required], name = 'dispatch') #why dispatch?
class ProductUpdateView( generic.edit.UpdateView ):
    model = VendorProduct
    fields = ['name', 'cost', 'category', 'payment_type', 'quantity', 'small_display_image', 'big_display_image']
    template_name = 'BestBuySearch/VendorProduct_edit.html'
    success_url = reverse_lazy('BestBuySearch:all_products')
    
    def form_valid(self, form):
        """Overrides form_valid to edit product."""
        #fill for vendor:
        form.instance.update_date = timezone.now()
        
        return super().form_valid(form)

@method_decorator([login_required, vendor_required], name = 'dispatch') #why dispatch?
class ProductDeleteView( generic.edit.DeleteView ):
    model = VendorProduct
    template_name = 'BestBuySearch/vendorproduct_delete.html'
    success_url = reverse_lazy('BestBuySearch:all_products') #use reverse_lazy bc bc urls not loaded w/ file imported
    
    
#polls views

    
"""#Fifth rendition: (generic view)
class IndexView(generic.ListView):
    template_name = 'BestBuySearch/index.html'
    context_object_name = 'latest_question_list'
    
    #Second ed: (publish questions w/ pub date passed)
    def get_queryset(self):
        return Question.objects.filter(
                pub_date__lte = timezone.now()
                ).order_by('-pub_date')[:5]

#Fourth rendition: (generic views)
class DetailView(generic.DetailView):
    model = Question
    template_name = 'BestBuySearch/detail.html'
    
    def get_queryset(self):
        
        return Question.objects.filter(pub_date__lte = timezone.now())

#Second Rendition: (generic views)
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'BestBuySearch/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  #rets id of sel'd choice using POST
    except (KeyError, Choice.DoesNotExist):
        #redisplay question voting form
        return render(request, 'BestBuySearch/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #incr vote amt and save in DB
        selected_choice.votes += 1
        selected_choice.save()
        
        #Always ret an HtttpResponseRedirect after successful POST data
        # Prevents data from being posted twice if user hits Back btn
        return HttpResponseRedirect(reverse('BestBuySearch:results', args=(question.id,)))
"""