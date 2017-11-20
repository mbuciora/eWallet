from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from eWallet_app.models import ChangeDetail, User, Group
from django.views import generic
from django.views.generic import View
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from eWallet_app.forms import UserForm, LoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect

class AccountBalance(View):
    def get(self, request):
        amounts = ChangeDetail.objects.values_list('amount', flat=True)
        balance = sum(amounts)
        context = {'balance': balance}
        return render(request, 'balance.html', context)


class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return ChangeDetail.objects.all()

class GroupsView(generic.ListView):
    template_name = 'groups.html'

    def get_queryset(self):
        return Group.objects.all()

class DetailView(generic.DetailView):
    model = ChangeDetail
    template_name = 'detail.html'

class GroupView(generic.DetailView):
    model = Group
    template_name = 'group-detail.html'


class CreateChange(CreateView):
    model = ChangeDetail
    fields = ['title', 'amount', 'revenue', 'description']

    def add_change(request):
        if request.method == 'POST':
            form = CreateChange(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                amount = form.cleaned_data['amount']
                revenue = form.cleaned_data['revenue']
                description = form.cleaned_data['description']
                change = ChangeDetail.objects.create(
                    title=title,
                    amount=amount,
                    revenue=revenue,
                    description=description,)

class AddGroup(CreateView):
    model = Group
    fields = ['name', 'expenses_amount', 'members_count', 'expenses_per_person']

    def add_change(request):
        if request.method == 'POST':
            form = AddGroup(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                expenses_amount = form.cleaned_data['expenses_amount']
                members_count = form.cleaned_data['members_count']
                expenses_per_person = form.cleaned_data['expenses_per_person']
                group = Group.objects.create(
                    name=name,
                    expenses_amount=expenses_amount,
                    members_count=members_count,
                    expenses_per_person=expenses_per_person,)

class AddUser(CreateView):
    model = User
    fields = ['username']




class UpdateChange(UpdateView):
    model = ChangeDetail
    fields = ['title', 'amount', 'revenue', 'description']

class DeleteChange(DeleteView):
    model = ChangeDetail
    success_url = reverse_lazy('index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login')
        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                 auth.login(request, user)
                 return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')