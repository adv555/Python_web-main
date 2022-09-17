from termcolor2 import colored
from tabulate import tabulate


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def pretty_title(text):
    return print(colored(text, color='blue'))


def error(text):
    return print(colored(text, color='red'))


def option(text):
    return print(colored(text, color='yellow'))


def message(text):
    return print(colored(text, color='green'))


def print_data(data):
    table_data = [
        ['First name', 'Last name', 'Email', 'Phone'],
        [data['first_name'], data['last_name'], data['email'], data['phone']]
    ]
    print(tabulate(table_data, headers='firstrow', tablefmt='grid'))
