from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.validators import ValidationError
from django.views import View
from django.urls import reverse_lazy
from .models import Booking, Product, Physiotherapist, Session, Price
from .forms import Registerform, Loginform, Bookingform
from django.views.generic import FormView, CreateView, UpdateView, DeleteView, ListView, RedirectView, DetailView
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta


User = get_user_model()


class Start(View):
    def get(self, request):
        return render(request, 'Physiotherapist_project/index.html')


class PriceList(View):
    def get(self, request):
        return render(request, 'Physiotherapist_project/price-list.html')


class BuyProduct(View):
    def get(self, request):
        return render(request, 'Physiotherapist_project/product.html')


class PageOne(View):
    def get(self,request):
        return render(request, 'Physiotherapist_project/service page 1.html')


class PageTwo(View):
    def get(self, request):
        return render(request, 'Physiotherapist_project/service page 2.html')


class PageThree(View):

    def get(self, request):
        return render(request, 'Physiotherapist_project/service page 3.html')


class LoadProduct(View):

    def get(self, request):
        physiotherapist_id = request.GET.get('physiotherapist')
        product = Product.objects.filter(physiotherapist=physiotherapist_id).order_by('name_of_product')
        return render(request, 'Physiotherapist_project/product.html', {'product': product})


class LoadSession(View):

    def get(self, request):
        product_id = request.GET.get('product')
        session = Session.objects.filter(product=product_id).order_by('name_of_session')
        return render(request, 'Physiotherapist_project/session.html', {'session': session})


class LoadPrice(View):
    def get(self, request):
        session_id = request.GET.get('session')
        price = Price.objects.filter(session=session_id).order_by('value')
        return render(request, 'Physiotherapist_project/price.html', {'price': price})


class Bookings(View):
    def get(self, request, pk_booking=None, pk_user=None):
        user = get_object_or_404(User, pk=pk_user)
        if pk_booking is None:
            booking = None
        else:
            booking = get_object_or_404(Booking, booking_id=pk_booking, user=user)
        return render(request, 'Physiotherapist_project/booking.html', {'booking': booking, 'user': user})

    def post(self, request, pk_booking=None, pk_user=None):
        user = get_object_or_404(User, pk=pk_user)
        if pk_booking is None:
            booking = None
        else:
            booking = get_object_or_404(Booking, booking_id=pk_booking, user=user)

        form = Bookingform(request.POST, instance=booking)
        if form.is_valid():
            if booking is None:
                save_booking = form.save(commit=False)
                save_booking.user = user
                save_booking.save()
            return render(request, 'Physiotherapist_project/index.html')
        else:
            return render(request, 'Physiotherapist_project/booking.html', {'booking': booking, 'user': user, 'form': form})




class DeleteBooking(DeleteView):
    model = Booking
    success_url = reverse_lazy('start')


class Login(FormView):
    template_name = 'Physiotherapist_project/login.html'
    success_url = reverse_lazy('start')
    form_class = Loginform

    def form_valid(self, form):
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']
        user = authenticate(password=password, username=username)
        login(self.request, user)
        return super().form_valid(form)


class Logout(RedirectView):
    url = reverse_lazy('start')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class Register(CreateView):
    model = User
    template_name = 'Physiotherapist_project/register.html'
    form_class = Registerform
    success_url = reverse_lazy('start')
    permission_required = 'auth.add_user'

    def form_valid(self, form):
        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['pass1'])
        self.object.save()
        login(self.request, self.object)
        print(self.object)
        return response


class UsersPanel(ListView):
    template_name = 'Physiotherapist_project/users-panel.html'
    model = Booking
    context_object_name = "users"
    ordering = "date"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class PhysiotherapistDetailsView(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        User.objects.get(username=current_user)
        booking = Booking.objects.all()
        users = Booking.objects.filter(user=request.user).order_by('date')
        return render(request, 'Physiotherapist_project/specialist_page.html',
                      context={"booking": booking, "users": users})


class PhysiotherapistUpdate(UpdateView):
    template_name = 'Physiotherapist_project/update_user.html'
    model = Booking
    fields = ['physiotherapist', 'product', 'price', 'date']
