from pathlib import Path
from django.conf import settings
import requests
import json
import re
from django.utils.html import mark_safe
from django.urls import reverse

def remove_empty_photo_folders():
    path = Path.cwd().joinpath('media/listing_imgs/')
    elements = list(path.rglob('*'))[::-1]
    for element in elements:
        if element.is_dir() and not list(element.glob('*')):
            element.rmdir()

def rename_photos_on_delete(listing_path, photo_objs):
    photo_paths = [photo for photo in listing_path.glob('*.jpeg')]
    if photo_paths:
        photo_paths = sorted(photo_paths, key=lambda x: x.stem.split('_')[1])
        for i, path in enumerate(photo_paths):
            try:
                new_path = path.with_name(f"photo_{i + 1}.jpeg")
                path.replace(new_path)
                photo_objs[i].photo = str(new_path)
                print(photo_objs[i].photo, new_path)
                photo_objs[i].save()
            except Exception as e:
                print(e)
                continue

def move_photos(prev_url, dest_url, photo_objs):
    # print(f"Prev path {prev_url}")
    # print(f"New path {dest_url}")
    for obj in photo_objs:
        photo_name = Path(obj.photo.name).name
        obj.photo = str(dest_url.joinpath(photo_name))
        obj.save()
        new_path = Path('media', dest_url)
        new_path.mkdir(parents=True, exist_ok=True)
        Path('media', prev_url, photo_name).rename(new_path.joinpath(photo_name))

def get_address_coordinates(obj, fields):
    url = settings.GEOCODER_API_URL.replace('\n', '').strip()
    fields = {field: re.sub(r'[^\sA-Za-z0-9]', '', str(getattr(obj, field))) for field in fields}
    for benchmark in ['Current', 'Census2010']:
        fields['benchmark'] = benchmark
        url = url.format(**fields)
        print(url)
        try:
            response = requests.get(url).json()
            match = response['result']['addressMatches'][0]
            return match['coordinates']
        except Exception as e:
            pass
    return None

def get_html_link(obj, id_field, text):
    href = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=(id_field,))
    return mark_safe(
        f"<a target='_blank' href='{href}'>{text}</a>"
    )
