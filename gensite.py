from liquid import Environment
from liquid import CachingFileSystemLoader
from liquid import parse
from liquid import render

from os import listdir
from os.path import isfile, join

templates_dir = "templates"
env = Environment(loader=CachingFileSystemLoader(templates_dir, ext=".html"))

output_dir = "public"
files = [f for f in listdir(templates_dir) if isfile(f)]

for f in files:
    template = env.get_template(f)
    data = {"foo": 42, "bar": "hello"}

    with open("public/%s" % (f), "w") as file:
        file.write(template.render(**data))
