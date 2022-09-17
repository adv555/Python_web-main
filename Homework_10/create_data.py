import json

from bson import ObjectId
from mongoengine import DoesNotExist
from tabulate import tabulate

from models import Contact
from faker import Faker

from styles import error, message
from lru_cash import client, LruCache

fake = Faker()


def generate_fake_contacts():
    print('Generating fake contacts...')
    for _ in range(10):
        fake_contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=[fake.phone_number() for _ in range(2)]
        )
        fake_contact.save()


@LruCache
def show_contact(contact_id):
    try:
        contact = Contact.objects.get(id=ObjectId(contact_id))
        contact_cash_value = {
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'email': contact.email,
            'phone': contact.phone
        }
        return contact_cash_value
    except DoesNotExist:
        print('Contact does not exist!')


def show_contact_old(contact_id):
    if client.exists(contact_id):
        value_json = client.get(contact_id).decode('utf-8')
        value = json.loads(value_json)
        table_data = [
            ['First name', 'Last name', 'Email', 'Phone'],
            [value['first_name'], value['last_name'], value['email'], value['phone']]
        ]
        print(tabulate(table_data, headers='firstrow', tablefmt='grid'))

    else:
        contact = Contact.objects.get(id=ObjectId(contact_id))
        value = {
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'phone': contact.phone,
            'email': contact.email
        }
        value_json = json.dumps(value)
        client.set(contact_id, value_json)
        table_data = [
            ['First name', 'Last name', 'Email', 'Phone'],
            [contact.first_name, contact.last_name, contact.email, contact.phone]
        ]
        print(tabulate(table_data, headers='firstrow', tablefmt='grid'))


def get_contact_by_id(contact_id):
    try:
        contact = Contact.objects.get(id=ObjectId(contact_id))
        print("Contact_data", contact.first_name, contact.last_name, contact.phone, contact.email)
        table_data = [
            ['First name', 'Last name', 'Email', 'Phone'],
            [contact.first_name, contact.last_name, contact.email, contact.phone]
        ]
        print(tabulate(table_data, headers='firstrow', tablefmt='grid'))

    except DoesNotExist:
        print('Contact does not exist!')


def add_contact(first_name, last_name, phone, email):
    new_contact = Contact(first_name=first_name, last_name=last_name, phone=[phone], email=email)
    new_contact.save()


def add_phone(contact_id, phone):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact.phone.append(phone)
    contact.save()
    message('Phone added successfully!')


def add_email(contact_id, email):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact_email = contact.email
    if contact_email == email:
        error('This email already exists!')
    else:
        contact.email = email
        contact.save()
        message('Email added successfully!')


def delete_contact(contact_id):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact.delete()
    message('Contact deleted successfully!')
