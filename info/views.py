from django.shortcuts import render, get_object_or_404
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