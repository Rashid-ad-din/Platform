from django.contrib.auth import login, logout, authenticate, get_user_model, update_session_auth_hash
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, UpdateView

from accounts.forms import AccountForm
# from accounts.forms import AccountForm, LoginForm
from accounts.models import Account


class AccountCreateView(CreateView):
    template_name = 'account_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        user = request.user

        if form.is_valid():
            account = form.save(commit=False)
            account.type = kwargs['type']
            account.username = account.email
            account.save()
            login(request, account)
            if account.type == 'psychologist':
                return redirect('psychologist_cabinet',
                                pk=account.pk)
            if account.type == 'client':
                return redirect('client_cabinet',
                                pk=account.pk)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


def logout_view(request):
    logout(request)
    return redirect('index')
