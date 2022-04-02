#!/bin/bash
rm -rf ./docs
mkdir -p docs/html
pdoc3 --force --html -o docs/html AzureVisionTools


