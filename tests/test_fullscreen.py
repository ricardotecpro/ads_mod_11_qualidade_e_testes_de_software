import pytest
from playwright.sync_api import Page, expect

def test_shortcuts_hidden_in_fullscreen(page: Page):
    """
    Test that the .reveal-shortcuts element is hidden when the presentation
    enters fullscreen mode.
    
    Note: Fullscreen API in headless mode can be tricky. 
    We rely on checking if the CSS pseudo-class matches or if specific styling is applied.
    However, forcing pseudo-classes in Playwright is hard. 
    Instead, we check if the element has the class or if we can simulate the state.
    
    Actually, triggering 'F' in Reveal.js triggers the API. 
    Browsers usually require user gesture. page.keyboard.press helps.
    """
    # Load a slide
    page.on("console", lambda msg: print(f"BROWSER LOG: {msg.text}"))
    page.goto("/slides/slide-01.html")

    
    # 1. Verify shortcuts are initially visible
    shortcuts = page.locator(".reveal-shortcuts")
    print(f"\nCreated locator. Count: {shortcuts.count()}")
    
    # Debug info
    if shortcuts.count() > 0:
        box = shortcuts.bounding_box()
        print(f"Bounding box: {box}")
        viz = shortcuts.is_visible()
        print(f"Is visible: {viz}")
        if not viz:
            # Check style
            display = shortcuts.evaluate("el => getComputedStyle(el).display")
            print(f"Computed display: {display}")
            opacity = shortcuts.evaluate("el => getComputedStyle(el).opacity")
            print(f"Computed opacity: {opacity}")

    expect(shortcuts).to_be_visible()
    print("Step 1: Initially visible - PASSED")
    
    # 2. Simulate Fullscreen Event
    page.evaluate("""
        Object.defineProperty(document, 'fullscreenElement', {
          get: () => document.documentElement,
          configurable: true
        });
        document.dispatchEvent(new Event('fullscreenchange'));
    """)
    
    # 3. Verify shortcuts are hidden
    # Wait for JS to run
    page.wait_for_timeout(500)
    
    # Debug info
    viz = shortcuts.is_visible()
    print(f"Step 3 Is visible: {viz}")
    if viz:
        display = shortcuts.evaluate("el => el.style.display")
        print(f"Step 3 Inline display: {display}")

    expect(shortcuts).not_to_be_visible()
    print("Step 3: Hidden - PASSED")

    # 4. Simulate exit
    page.evaluate("""
        Object.defineProperty(document, 'fullscreenElement', {
          get: () => null,
          configurable: true
        });
        document.dispatchEvent(new Event('fullscreenchange'));
    """)
    
    # Wait for JS to run
    page.wait_for_timeout(500)

    # 5. Verify visible again
    expect(shortcuts).to_be_visible()
    print("Step 5: Visible again - PASSED")


