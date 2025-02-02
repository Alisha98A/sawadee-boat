# Testing Documentation for the Project

* [Introduction](#introduction)
* [Test Setup](#test-setup)
* [Automatic Tests](#automatic-tests)
  * [Phone Number Validation](#phone-number-validation)
  * [Birth Date Validation](#birth-date-validation)
  * [Address Validation](#address-validation)
  * [Missing or Invalid Data](#missing-or-invalid-data)
  * [MenuForm Tests](#menuform-tests)
  * [MenuItemForm Tests](#menuitemform-tests)
  * [ItemForm Tests](#itemform-tests)
* [Manual Tests](#manual-tests)
* [Running the Tests](#running-the-tests)
* [Test Results](#test-results)
* [Conclusion](#conclusion)

---

## Introduction

This document outlines the testing strategy for the **Sawadee Dining Boat** project. The objective is to ensure that all forms and user inputs, such as phone numbers, birth dates, addresses, and menu-related forms, behave as expected.

## Test Setup

Before running the tests, ensure that the following requirements are met:
* Python 3.x
* Django 4.x
* Virtual environment set up (e.g., using `venv`)
* All dependencies installed via `pip install -r requirements.txt`

## Automatic Tests

The project includes a comprehensive set of **automatic tests** that validate the behavior of the form (`ProfileForm`, `MenuForm`, `MenuItemForm`, and `ItemForm`). These tests run automatically using Django’s test framework and ensure that form validation works correctly for various scenarios.

<details>
  <summary>Phone Number Validation</summary>


The `phone_number` field in the form is validated by a custom validator to ensure that it:
* Contains only digits.
* Has a length between 9 and 15 digits.

**Test Cases:**
* **Valid Phone Number**: Ensures the form accepts a valid phone number (`1234567890`).
* **Invalid Phone Number Length**: Tests that a phone number shorter than 9 digits or longer than 15 digits is rejected.
* **Non-Digit Phone Number**: Ensures the form rejects a phone number containing non-digit characters (e.g., `12a34567b890`).

```python
def test_valid_phone_number(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '1234567890',
        'birth_date': '2000-01-01',
        'address': '123 Main St',
    }
    form = ProfileForm(data=form_data)
    self.assertTrue(form.is_valid())
```

Invalid Phone Number Length: Tests that a phone number shorter than 9 digits or longer than 15 digits is rejected.

```python
def test_invalid_phone_number_length(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '123',  # Invalid phone number (too short)
        'birth_date': '2000-01-01',
        'address': '123 Main St',
    }
    form = ProfileForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['phone_number'], ['Phone number must be between 9 and 15 digits.'])
```

Non-Digit Phone Number: Ensures the form rejects a phone number containing non-digit characters (e.g., 12a34567b890).
 
```python
def test_invalid_phone_number_non_digit(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '12a34567b890',  # Invalid phone number (contains non-digits)
        'birth_date': '2000-01-01',
        'address': '123 Main St',
    }
    form = ProfileForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['phone_number'], ['Phone number must only contain digits.'])
```
  </details>
---
<details>
  <summary>Birth Date Validation</summary>

The birth_date field is validated to ensure that:
* The birth date is not in the future.
* The user is at least 18 years old.

* Test Cases:
	•	Future Birth Date: Ensures that a future birth date is rejected.

```python
def test_birth_date_in_future(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '1234567890',
        'birth_date': str(date.today().year + 1) + '-01-01',
        'address': '123 Main St',
    }
    form = ProfileForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['birth_date'], ['Birth date cannot be in the future.'])
```

Underage Birth Date: Ensures that users under 18 are rejected.

```python
def test_underage_birth_date(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '1234567890',
        'birth_date': str(date.today().year - 17) + '-01-01',  # Underage
        'address': '123 Main St',
    }
    form = ProfileForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['birth_date'], ['You must be at least 18 years old.'])
```
  </details>
---
<details>
  <summary>Address Validation</summary>

The address field is validated to ensure that:
* The address does not contain invalid characters (e.g., $, %, &, @).

* Test Cases:
	•	Valid Address: Ensures that a valid address is accepted.

```python
def test_valid_address(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '1234567890',
        'birth_date': '2000-01-01',
        'address': '123 Main St',  # Valid address
    }
    form = ProfileForm(data=form_data)
    self.assertTrue(form.is_valid())
```

Invalid Address Characters: Ensures that an address containing invalid characters is rejected.

```python
def test_invalid_address_characters(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '1234567890',
        'birth_date': '2000-01-01',
        'address': '123 Main $t',  # Invalid address (contains $)
    }
    form = ProfileForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['address'], ['Address contains invalid characters.'])
```
  </details>
---
<details>
  <summary>Missing or Invalid Data</summary>

Test cases for required fields ensure that:
* Missing fields (like first_name) raise validation errors.

Missing First Name: Ensures that the form raises a validation error when the first_name field is empty.

```python
def test_form_invalid_data(self):
    form_data = {
        'first_name': '',  # Missing first name
        'last_name': 'Doe',
        'phone_number': '1234567890',
        'birth_date': '2000-01-01',
        'address': '123 Main St',
    }
    form = ProfileForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['first_name'], ['This field is required.'])
```
  </details>
---
<details>
  <summary>MenuForm Tests</summary>

The MenuForm validates the creation of a menu with name, description, and active status.

Test Cases:
* Valid MenuForm: Ensures the form is valid when given correct data.
 
```python
 def test_menu_form_is_valid(self):
    form = MenuForm({'name': 'Lunch Menu', 'description': 'A delicious lunch menu', 'is_active': True})
    self.assertTrue(form.is_valid(), msg="MenuForm should be valid")
```
Invalid MenuForm: Ensures the form is invalid when the name is missing.

```python
def test_menu_form_is_invalid(self):
    form = MenuForm({'name': '', 'description': 'No name provided', 'is_active': True})
    self.assertFalse(form.is_valid(), msg="MenuForm should be invalid due to missing name")
```
  </details>
---
<details>
  <summary>MenuItemForm Tests</summary>

The MenuItemForm validates the creation of a menu item associated with a menu.

Test Cases:
* Valid MenuItemForm: Ensures the form is valid when given correct data.

```python
  def test_menu_item_form_is_valid(self):
    form = MenuItemForm({'menu': self.menu.id, 'category': 'Drinks'})
    self.assertTrue(form.is_valid(), msg="MenuItemForm should be valid")
```

Invalid MenuItemForm: Ensures the form is invalid when the menu is missing.

```python
def test_menu_item_form_is_invalid(self):
    form = MenuItemForm({'menu': '', 'category': 'Desserts'})
    self.assertFalse(form.is_valid(), msg="MenuItemForm should be invalid due to missing menu")
```
  </details>
---
<details>
  <summary>ItemForm Tests</summary>

The ItemForm validates the creation of an item associated with a menu item, including handling file uploads.

Test Cases:
* Valid ItemForm: Ensures the form is valid when the item has a valid image file.

```python
def test_item_form_is_valid(self):
    image_file = self.create_test_image()
    form = ItemForm(data={
        'menu_item': self.menu_item.id,
        'name': 'Spaghetti',
        'description': 'Delicious spaghetti with tomato sauce',
        'price': 15.99,
    }, files={'image': image_file})
```

Invalid ItemForm due to Large File: Ensures the form is invalid when the uploaded image file is too large.

```python
def test_item_form_is_invalid_due_to_large_file(self):
    large_image = SimpleUploadedFile("large.jpg", b"x" * (2 * 1024 * 1024 +
    self.assertTrue(form.is_valid(), msg=f"ItemForm should be valid but failed with errors: {form.errors}")
```
  </details>
---
