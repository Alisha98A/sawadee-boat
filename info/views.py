from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
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
@user_passes_test(staff_required, login_url="no_access")
def staff_menu_view(request):
    """Allow staff to manage menus, with pagination (5 per page)."""
    menus = Menu.objects.all()
    paginator = Paginator(menus, 5)
    page_number = request.GET.get("page")
    page_menus = paginator.get_page(page_number)

    return render(request, "info/staff_menu.html", {"menus": page_menus})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def add_menu(request):
    """Allow staff to add a new menu."""
    form = MenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Menu added successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Add Menu"})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def edit_menu(request, menu_id):
    """Allow staff to edit an existing menu."""
    menu = get_object_or_404(Menu, id=menu_id)
    form = MenuForm(request.POST or None, instance=menu)
    
    if form.is_valid():
        form.save()
        messages.success(request, "Menu updated successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Edit Menu"})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def delete_menu(request, menu_id):
    """Allow staff to delete a menu."""
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == "POST":
        menu.delete()
        messages.success(request, "Menu deleted successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_confirm_delete.html", {"menu": menu})

# -------------------------------------
# MenuItem (Category) Management
# -------------------------------------
@login_required
@user_passes_test(staff_required, login_url="no_access")
def add_menu_item(request):
    """Allow staff to add a menu category."""
    form = MenuItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Menu category added successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Add Menu Item"})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def edit_menu_item(request, menu_item_id):
    """Allow staff to edit a menu category."""
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    form = MenuItemForm(request.POST or None, instance=menu_item)

    if form.is_valid():
        form.save()
        messages.success(request, "Menu category updated successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_form.html", {"form": form, "title": "Edit Menu Item"})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def delete_menu_item(request, menu_item_id):
    """Allow staff to delete a menu category."""
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    if request.method == "POST":
        menu_item.delete()
        messages.success(request, "Menu category deleted successfully!")
        return redirect("staff_menu")

    return render(request, "info/menu_confirm_delete.html", {"menu_item": menu_item})

# -------------------------------------
# Item (Dish) Management
# -------------------------------------
@login_required
@user_passes_test(staff_required, login_url="no_access")
def add_item(request):
    """Allow staff to add a menu item."""
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Menu item added successfully!")
        return redirect("staff_menu")

    return render(request, "info/item_form.html", {"form": form, "title": "Add Item"})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def edit_item(request, item_id):
    """Allow staff to edit a menu item."""
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        messages.success(request, "Menu item updated successfully!")
        return redirect("staff_menu")

    return render(request, "info/item_form.html", {"form": form, "title": "Edit Item"})

@login_required
@user_passes_test(staff_required, login_url="no_access")
def delete_item(request, item_id):
    """Allow staff to delete a menu item."""
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item.delete()
        messages.success(request, "Menu item deleted successfully!")
        return redirect("staff_menu")

    return render(request, "info/item_confirm_delete.html", {"item": item})

# -------------------------------------
# Set Menu Active
# -------------------------------------

@login_required
@user_passes_test(staff_required, login_url="no_access")
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
