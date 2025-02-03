from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Menu, MenuItem, Item
from .forms import MenuForm, MenuItemForm, ItemForm


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
@staff_member_required
def staff_menu_view(request):
    """Allow staff to manage menus, with pagination (5 per page)."""
    menus = Menu.objects.all().order_by("-created_on")
    paginator = Paginator(menus, 5)
    page_number = request.GET.get("page")
    page_menus = paginator.get_page(page_number)

    return render(request, "info/staff_menu.html", {"menus": page_menus})

@login_required
@staff_member_required
def add_menu(request):
    """Allow staff to add a new menu."""
    form = MenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Menu added successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Add Menu"})

@login_required
@staff_member_required
def edit_menu(request, menu_id):
    """Allow staff to edit an existing menu."""
    menu = get_object_or_404(Menu, id=menu_id)
    form = MenuForm(request.POST or None, instance=menu)
    
    if form.is_valid():
        form.save()
        messages.success(request, "Menu updated successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Edit Menu"})

# -------------------------------------
# MenuItem (Category) Management
# -------------------------------------
@login_required
@staff_member_required
def add_menu_item(request):
    """Allow staff to add a menu category."""
    form = MenuItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Menu category added successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Add Menu Item"})

@login_required
@staff_member_required
def edit_menu_item(request, menu_item_id):
    """Allow staff to edit a menu category."""
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    form = MenuItemForm(request.POST or None, instance=menu_item)

    if form.is_valid():
        form.save()
        messages.success(request, "Menu category updated successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Edit Menu Item"})

# -------------------------------------
# Item (Dish) Management
# -------------------------------------
@login_required
@staff_member_required
def add_item(request):
    """Allow staff to add a menu item."""
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Menu item added successfully!")
        return redirect("staff_menu")

    return render(request, "info/item_form.html", {"form": form, "title": "Add Item"})

@login_required
@staff_member_required
def edit_item(request, item_id):
    """Allow staff to edit a menu item."""
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        messages.success(request, "Menu item updated successfully!")
        return redirect("staff_menu")

    return render(request, "info/item_form.html", {"form": form, "title": "Edit Item"})

# -------------------------------------
# Generic Delete View (Replaces All Individual Delete Views)
# -------------------------------------
@login_required
@staff_member_required
def delete_object(request, obj_id, model, redirect_url):
    """Generic view to delete an object (menu, menu item, or item)."""
    obj = get_object_or_404(model, id=obj_id)
    
    # Determine the correct name field
    obj_name = getattr(obj, "name", getattr(obj, "category", "Unnamed Object"))

    if request.method == "POST":
        obj.delete()
        messages.success(request, f"'{obj_name}' deleted successfully!")
        return redirect(redirect_url)

    return render(request, "info/confirm_delete.html", {"object": obj, "redirect_url": redirect_url})

# -------------------------------------
# Set Menu Active
# -------------------------------------

@login_required
@staff_member_required
def set_active_menu(request, menu_id):
    """Set the selected menu as the active menu, ensuring only one menu is active at a time."""
    menu = get_object_or_404(Menu, id=menu_id)
    
    # Deactivate all menus first
    Menu.objects.update(is_active=False)
    
    # Set the selected menu to active
    menu.is_active = True
    menu.save()

    messages.success(request, f"'{menu.name}' is now the active menu!")
    return redirect("staff_menu")

# -------------------------------------
# No Access Page
# -------------------------------------
def no_access(request):
    """Render the 'No Access' page."""
    return render(request, "info/no_access.html")


# -------------------------------------
# Error handlers
# -------------------------------------
def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

def custom_403_view(request, exception):
    return render(request, "403.html", status=403)

def custom_500_view(request):
    return render(request, "500.html", status=500)

def custom_400_view(request, exception):
    return render(request, "400.html", status=400)