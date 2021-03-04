#!/usr/bin/env python3

import configparser
import os

# Check if config file exists
if not os.path.isfile("config.ini"):
    raise Exception("config.ini not found.")

# Create a configpaser object
config = configparser.ConfigParser()

# Read the config file
config.read("config.ini")

# config_jonas_section refers to the [JonasSection] part of the config file.
config_jonas_section = config["JonasSection"]
# Typically, it would be named something like "main", but I chose
# "JonasSection" in this case to illustrate the fact that the name itself
# is arbitrary.

# Now we have a pointer to the JonasSection part of the config file.
# From there, we can get config values.
# use get() for strings, use getint() for integers.
example_int = config_jonas_section.getint("example_int", 5)  # 5 = default
example_string = config_jonas_section.get("example_string", "hoho")
#                                                            # hoho = default

# Let's try to get something from the config that doesn't exist:
doesnt_exist = config_jonas_section.get("foobar", "my default value")

print(f"example_int: {example_int}")
print(f"example_string: {example_string}")
print(f"doesnt_exist: {doesnt_exist}")
