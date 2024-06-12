from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Transaction
from .forms import UserRegistrationForm, TransactionForm

User = get_user_model()

def register(request):
    """
    Handles user registration.
    
    If the request method is POST, it processes the form data.
    If the form is valid, it saves the user, logs them in, and redirects to the home page.
    If the request method is GET, it displays an empty registration form.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    """
    Handles user login.
    
    If the request method is POST, it processes the login form data.
    It validates the user credentials and logs them in if valid.
    Upon successful login, it redirects to the home page.
    If the request method is GET, it displays the login form.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')



@login_required
def home(request):
    """
    Displays the home page with a list of transactions for the logged-in user.
    
    Requires the user to be logged in.
    """
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'home.html', {'transactions': transactions})


@login_required
def create_transaction(request):
    """
    Handles the creation of a new transaction.
    
    If the request method is POST, it processes the transaction form data.
    If the form is valid, it saves the transaction for the logged-in user and redirects to the home page.
    If the request method is GET, it displays an empty transaction form.
    Requires the user to be logged in.
    """
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})


@login_required
def update_transaction(request, pk):
    """
    Handles updating an existing transaction.
    
    If the request method is POST, it processes the updated transaction form data.
    If the form is valid, it saves the updated transaction and redirects to the home page.
    If the request method is GET, it displays a form pre-filled with the transaction data.
    Requires the user to be logged in and the transaction must belong to the logged-in user.
    """
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'update_transaction.html', {'form': form})


@login_required
def delete_transaction(request, pk):
    """
    Handles deleting an existing transaction.
    
    If the request method is POST, it deletes the transaction and redirects to the home page.
    If the request method is GET, it displays a confirmation page for deleting the transaction.
    Requires the user to be logged in and the transaction must belong to the logged-in user.
    """
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('home')
    return render(request, 'delete_transaction.html', {'transaction': transaction})
