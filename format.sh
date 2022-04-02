#!/usr/bin/env bash

# Format code with yapf.
yapf -i -r -p -vv AzureVisionTools/

# Format docstrings with docformatter.
docformatter -i -r AzureVisionTools/
