from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')

	else:
		form = UserRegistrationForm()
	return render(request, 'user/register.html', {'form' : form})





























# def login_view(request):
# 	# print(request)
# 	print(request.method)
# 	if request.method == 'POST':
# 		print('ok')
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			print('ok2')
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				print('okkk')
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("blog-home")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="user/login.html", context={"form":form})



# @login_required
# def profile(request):
# 	if request.method == 'POST':
# 		u_form = UserUpdateForm(request.POST, instance=request.user)
# 		c_form = ChickenUpdateForm(request.POST, instance=request.user.profile)
# 		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()
# 			messages.success(request, f'Your Accounthas been updated!')
# 			return redirect('profile')
# 	else:
# 		u_form = UserUpdateForm(instance=request.user)
# 		p_form = ProfileUpdateForm(instance=request.user.profile)
# 		c_form = ChickenUpdateForm(instance=request.user.profile)		

# 	context = {
# 		'u_form': u_form,
# 		'p_form': p_form,
# 		'c_form': c_form
# 	}
# 	return render(request, 'user/profile.html', context)

# # Create your views here.
