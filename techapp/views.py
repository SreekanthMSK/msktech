from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from .models import PublicPost
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView, BaseDetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from .forms import PublicPostForm, UserPostForm
from .models import PublicPost, UserPost
# https://myonlineoffers.com/
#################### index#######################################
def index(request):
    return render(request, 'user/index.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})


class AddPublicPost(SuccessMessageMixin, CreateView):
    form_class = PublicPostForm
    model = PublicPost
    template_name = "publicposts/createpublicpost.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('view_allpublicposts')


class ViewPublicPostDetail(DetailView):
    model = PublicPost
    context_object_name = 'publicpost'
    template_name = "publicposts/viewsinglepublicpost.html"


class ViewAllPublicPosts(ListView):
    model = PublicPost
    context_object_name = 'publicposts'
    template_name = "publicposts/viewallpublicpost.html"


class AddUserPost(SuccessMessageMixin, CreateView):
    form_class = UserPostForm
    model = UserPost
    template_name = "userposts/createuserpost.html"
    success_message = "Added Succesfully"

    def form_valid(self, form):
        form.instance.userid = self.request.user
        return super(AddUserPost, self).form_valid(form)

    def get_success_url(self):
        return reverse('view_userposts')


class ViewUserPosts(ListView):
    model = UserPost
    context_object_name = 'userposts'
    template_name = "userposts/viewuserposts.html"
    def get_queryset(self):
        return UserPost.objects.filter(userid=self.request.user)