import pytest
from pathlib import Path
import os

def test_site_exists():
    assert Path("site").exists()

def test_site_slides_exists():
    assert Path("site/slides").exists()
    assert Path("site/slides/index.html").exists()

def test_debug_cwd():
    print(f"DEBUG CWD: {os.getcwd()}")
    print(f"DEBUG site content: {os.listdir('site')}")
    if Path("site/slides").exists():
        print(f"DEBUG slides content: {os.listdir('site/slides')}")
