from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for
from src.repository.contacts import create_contact, get_user_contacts
from werkzeug.exceptions import abort

contact = Blueprint('contacts', __name__, url_prefix='/contacts')


class InvalidRequestException(Exception):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg


@contact.route('/', methods=['GET', 'POST'], strict_slashes=False)
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        new_contact = create_contact(name, surname, email, phone, user_id=5)
        flash(f'Contact {new_contact.full_name} created successfully.', 'success')
        user_contacts = get_user_contacts(user_id=5)
        return render_template('contacts/contacts.html', contacts=user_contacts)

    user_contacts = get_user_contacts(user_id=5)

    if not user_contacts:
        flash('You have no contacts. Create one!', 'warning')
        return redirect(url_for('contacts.create_contact'))

    return render_template('contacts/contacts.html', contacts=user_contacts)


@contact.route('/<contact_id>/delete', methods=['GET', 'POST'], strict_slashes=False)
def delete_contact(contact_id):
    try:

        delete_contact(contact_id)
        flash(f'Contact {contact_id} deleted successfully.', 'success')
    except InvalidRequestException as e:
        abort(404, e.msg)
