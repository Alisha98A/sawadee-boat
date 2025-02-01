from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .models import Menu



# -------------------------------------
# Home & About Views
# -------------------------------------
def home(request):
    """Render the home page."""
    return render(request, 'info/home.html')

def about(request):
    """Render the about page."""
    return render(request, 'info/about.html')

# -------------------------------------
# Staff Restriction
# -------------------------------------
def staff_required(user):
    """Restrict access to staff members only."""
    return user.is_authenticated and user.is_staff

# -------------------------------------
# Display Set Sail View template
# -------------------------------------
def set_sail_view(request):
    return render(request, "info/setsail.html")

# -------------------------------------
# Menu 
# -------------------------------------
def menu_view(request, menu_id=None):
    """Fetch the active menu or a specific menu if requested."""
    if menu_id:
        menu = get_object_or_404(Menu, id=menu_id)  
    else:
        menu = Menu.objects.filter(is_active=True).first()  

    # If no active menu is set, fall back to the first available menu
    if not menu:
        menu = Menu.objects.first()

    return render(request, "info/menu.html", {"menu": menu, "menu_list": Menu.objects.all()})

# -------------------------------------
# Staff Menu Management
# -------------------------------------
@login_required
@user_passes_test(staff_required, login_url="no_access")
def staff_menu_view(request):
    """Allow staff to manage menus, with pagination (5 per page)."""
    menus = Menu.objects.all()
    paginator = Paginator(menus, 5)
    page_number = request.GET.get("page")
    page_menus = paginator.get_page(page_number)

    return render(request, "info/staff_menu.html", {"menus": page_menus})