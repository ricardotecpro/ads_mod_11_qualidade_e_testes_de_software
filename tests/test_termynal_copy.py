from playwright.sync_api import Page, expect
import pytest

def test_termynal_copy_button(page: Page, base_url: str):
    """
    Test that the Termynal copy button is injected and visible.
    """
    # Grant clipboard permissions
    page.context.grant_permissions(['clipboard-write', 'clipboard-read'])

    # Navigate to Lesson 04 which contains console blocks (Termynal)
    page.goto(f"{base_url}/aulas/aula-04/")

    # Wait for Termynal to be visible
    # Note: custom_termynal.js looks for .termy, but the mkdocs-termynal plugin
    # renders a custom structure. We need to match what's actually rendered.
    # Usually it's a div with data-termynal attribute or class.
    # Let's try a broader selector if .termy isn't found
    termynal = page.locator(".termy, [data-termynal]").first
    expect(termynal).to_be_visible()

    # Check for copy button
    copy_button = termynal.locator(".termynal-copy-button")
    expect(copy_button).to_be_attached()
    
    # Check that it's visible (might need hover, but let's check attachment first)
    # The CSS makes it opacity 0.5 initially, so it should be visible-ish
    # But let's check strict visibility
    expect(copy_button).to_be_visible()

    # Click the button
    copy_button.click()

    # Check for feedback "Copied!" (managed by CSS class .copied showing the span)
    expect(copy_button).to_have_class(r"termynal-copy-button copied")
    
    feedback = copy_button.locator(".termynal-copy-feedback")
    expect(feedback).to_be_visible()
