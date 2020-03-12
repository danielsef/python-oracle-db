

#!/usr/bin/env python3

from jinja2 import Template

if __name__ == '__main__':

    name = input("Enter your name: ")

    tm = Template("Hello {{ name }}")
    msg = tm.render(name=name)

    print(msg)
















