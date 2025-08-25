from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from .models import Report
from .forms import ReportForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'reports/home.html')

def report_form(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    
    form = ReportForm(initial={'date_of_incident': timezone.now().date()})
    return render(request, 'reports/report_form.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'reports/admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'reports/admin_login.html')


@login_required
def delete_report(request, report_id):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        Report.objects.filter(id=report_id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def admin_logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('home')
from django.core.paginator import Paginator

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    
    report_list = Report.objects.all().order_by('-timestamp')
    paginator = Paginator(report_list, 10)  # Show 10 reports per page
    
    page_number = request.GET.get('page')
    reports = paginator.get_page(page_number)
    
    harassment_count = Report.objects.filter(category='Harassment').count()
    discrimination_count = Report.objects.filter(category='Discrimination').count()
    safety_count = Report.objects.filter(category='Safety Concern').count()
    
    context = {
        'reports': reports,
        'harassment_count': harassment_count,
        'discrimination_count': discrimination_count,
        'safety_count': safety_count,
    }
    return render(request, 'reports/admin_dashboard.html', context)

@login_required
def report_detail(request, report_id):
    if not request.user.is_staff:
        raise PermissionDenied
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})