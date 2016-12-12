import os
import random
import string
import sys
from time import time

from flask import flash, redirect, url_for

sys.path.append(os.path.dirname(__file__) + '/..')
from latex import create_jpg_file, create_pdf_file, create_tex_file


def random_filename():
    return ''.join(random.sample(string.ascii_lowercase, 6))


def get_time():
    return '?{}'.format(time())


def remove_items(data):
    items = 'num', 'is_z', 'solve'
    [data.pop(i) for i in items]


def pop_ff(data):
    return data.pop('ff_type')


def is_valid(data):
    values = data.values()

    def is_item_valid(item):
        return item is None or item in range(16)

    return all(is_item_valid(i) for i in values)


def is_empty(data):
    return all(i is None for i in data.values())


def decide(data, ff_type, ip):
    if is_empty(data):
        print('empty table')
        flash('Tabela jest pusta!', category='warning')
        return redirect(url_for('index'))

    if not is_valid(data):
        print('bad move')
        flash('Podano złe przejście!', category='warning')
        return redirect(url_for('index'))

    create_files(data, ff_type, ip)


def parse_key(key):
    return key.split('_')[1:]


def parse_form(data):
    parsed = []
    for key, value in data.items():
        if not value:
            continue
        parsed_key = parse_key(key) + [value]
        parsed.append(tuple(int(i) for i in parsed_key))

    if len(parsed[0]) == 3 and not any(i[0] for i in parsed):
        return [i[1:] for i in parsed]
    return parsed


def error(filetype):
    flash('Nastąpił problem z tworzeniem pliku {}'.format(filetype), category='error')


def create_files(data, ff_type, file):
    tex_file = file + '.tex'
    moves = parse_form(data)

    if create_tex_file(moves, ff_type, tex_file):
        print('Probably you run server from wrong directory')
        return error('TEX')
    if create_pdf_file(tex_file):
        return error('PDF')
    if create_jpg_file(file):
        return error('JPG')
