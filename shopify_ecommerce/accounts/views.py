from django.shortcuts import redirect, render
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Kullanıcıyı kaydediyoruz
            login(request, user)  # Yeni kullanıcıyı otomatik olarak giriş yaptırıyoruz
            return redirect('product_list')  # Başarılı kayıt sonrası ürün listesine yönlendiriyoruz
    else:
        form = SignUpForm()  # GET isteğinde boş formu oluşturuyoruz
    return render(request, 'accounts/signup.html', {'form': form})