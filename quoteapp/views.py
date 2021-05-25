from quoteapp.models import CoverageInfo, Customer, Quotation, Vehicle
from django.views.generic.base import TemplateView
from .forms import CusotmerForm, LoginForm, VehicleForm, CoverageSelectedForm
from django.shortcuts import redirect, render
from django.db.models import Sum

#seperating business logic into different functions from actual views
def calculate_quote(price, coverage_ids):
    """ Calcuate quote for given price and coverages """
    quote = float(price) * 0.02
    coverage_ids = [int(cov) for cov in coverage_ids]
    # Getting the sum of coverage values
    quote += float(CoverageInfo.objects.filter(id__in=coverage_ids)
                   .aggregate(Sum('value'))['value__sum'])
    # returning the quote value
    return quote


def save(form):
    """ Method to save form and return id"""
    form_saved = form.save()
    return form_saved.id


def create_quote(customer, vehicle, coverage, quote, email_flag):
    """ Method to create quote """
    # getting required instances
    customer = Customer.objects.get(id=customer)
    vehicle = Vehicle.objects.get(id=vehicle)
    coverage = list(CoverageInfo.objects.filter(id__in=coverage))
    # creating a quote object
    quote_obj = Quotation.objects.create(customer=customer,
                                         vehicle=vehicle,
                                         quote_price=quote,
                                         email_preference=email_flag)
    # saving many to many relationship for coverage in quote
    quote_obj.coverage.set(coverage)
    # return the quote id
    return quote_obj.id

# Views start from here
class HomePageView(TemplateView):
    """ Template view for HomePage """
    template_name = "home.html"


class CreateQuoteView(TemplateView):
    """ Template View for CreateQuote """
    template_name = "form.html"

    def get(self, request):
        """ GET actions for create quote vie"""
        context = {}
        # getting the empty forms and sending as response
        form = [CusotmerForm, VehicleForm, CoverageSelectedForm]
        # assigning the labels
        labels = ["Customer", "Vehicle", "Coverage"]
        context['forms'] = zip(form, labels)
        # rendering the template with required context
        return render(request, self.template_name, context)

    def post(self, request):
        """ POST actions for create quote view """
        # getting the request.POST values
        form_values = request.POST
        print('form-values', form_values)
        context = {}
        # assigning to individual forms
        form = [CusotmerForm(form_values), VehicleForm(form_values),
                CoverageSelectedForm(form_values)]
        # getting the labels
        labels = ["Customer", "Vehicle", "Coverage"]
        context['forms'] = zip(form, labels)
        # checking for form validations
        if CusotmerForm(form_values).is_valid() and \
                VehicleForm(form_values).is_valid() and \
                CoverageSelectedForm(form_values).is_valid():
            # checking for quote and summary flags
            if 'quote' or 'summary' in form_values:
                # calculating the quote value
                context['quote_value'] = calculate_quote(
                    form_values.get('price'),
                    form_values.getlist('the_coverages'))
                print('hree', context['quote_value'])
                if 'summary' in form_values:
                    # saving the forms
                    customer_id = save(CusotmerForm(form_values))
                    vehicle_id = save(VehicleForm(form_values))
                    email_flag = True if form_values.get('email_flag') == 'true' else False 
                    # saving a quote and get the quote id
                    get_quote_id = create_quote(customer_id,
                                                vehicle_id,
                                                form_values.getlist('the_coverages'),
                                                context['quote_value'],
                                                email_flag)
                    # redirect to quote summary page
                    return redirect(f'/quote/quoteSummary/{get_quote_id}/')
        print('hree', CoverageSelectedForm(form_values).is_valid(), 
            CusotmerForm(form_values).is_valid(),
                VehicleForm(form_values).is_valid())
        return render(request, self.template_name, context)


class QuoteSummaryView(TemplateView):
    """ Template View for QuoteSummary """
    template_name = "summary.html"

    def get(self, request, quote_id):
        """ GET request action for Quote Summary Page"""
        context = {'quote': Quotation.objects.get(id=quote_id)}
        # assigning the context variables
        context['coverages'] = list(context['quote'].coverage.all())
        # return the quote summary details
        return render(request, self.template_name, context)


class CustomerView(TemplateView):
    """ Template View for Customer Login and View Quote"""
    template_name = 'customer-quotes.html'

    def get(self, request):
        """ GET actions for customer"""
        context = {}
        # using request session for validation of customer
        if request.session.get('customer_id'):
            # getting the customer id from session if logged in
            get_quote = Quotation.objects.filter(customer=
                                                 request.session.get('customer_id'))
            context['quote'] = list(get_quote)
        else:
            # else returning the login form
            context['form'] = LoginForm
        return render(request, self.template_name, context)

    def post(self, request):
        """POST actions for customer template view"""
        context = {}
        # checking for request post
        if request.method == "POST":
            if request.POST.get('type') == 'login':
                # if customer clicks on login
                customer = Customer.objects.filter(email=request.POST.get('email'))
                if customer:
                    # if customer exists, assign customer id to request session
                    # which acts as a login for customer
                    request.session['customer_id'] = customer[0].id
                    # assigning session expiry to 2 mins and can be varied
                    request.session.set_expiry(60)
                    # returning the quote summary details
                    get_quote = Quotation.objects.filter(customer=customer[0].id)
                    context['quote'] = list(get_quote)
            elif request.POST.get('type') == 'logout':
                # if user clicks on logout button all the session will be removed
                request.session.flush()
                # user will be redirected to home page
                return redirect('/quote/')
        return render(request, self.template_name, context)
