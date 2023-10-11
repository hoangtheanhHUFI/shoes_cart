import jinja2
import os

def environment(**options):
    env = jinja2.Environment(**options)
    # Add any custom Jinja2 configurations here
    return env
