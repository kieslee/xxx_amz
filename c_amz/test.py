
import sys
import acache
import json

'''
key_list = acache.get_keys()

for k in key_list:
    print acache.get_value(k)
    '''

print sys.argv
f = open(sys.argv[1])
con = f.read()

item_list = json.loads(con)

for item in item_list:
    class_name = item['class_name']
    url = item['url']

    if class_name.startswith('Gift Cards'):
        continue

    if class_name.startswith('Kindle Store'):
        continue

    if class_name.startswith('MP3 Downloads'):
        continue

    if class_name.startswith('Magazines'):
        continue

    if class_name.startswith('Movies & TV'):
        continue

    if class_name.startswith('Music'):
        continue

    if class_name.startswith('Software'):
        continue

    if class_name.startswith('Video Games'):
        continue

    acache.set_value(class_name, url)
