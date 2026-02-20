import pytest
import os

def test_assets_exist():
    """Verify that critical assets exist in the correct locations."""
    assets = [
        "docs/assets/js/mathjax.js",
        "docs/assets/js/custom_termynal.js",
        "docs/assets/js/quiz.js",
        "docs/assets/js/mermaid-init.js"
    ]
    
    missing_assets = []
    for asset in assets:
        if not os.path.exists(asset):
            missing_assets.append(asset)
            
    assert not missing_assets, f"Missing assets: {missing_assets}"
