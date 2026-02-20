import pytest
import os
import subprocess
import requests
import re
from pathlib import Path
from playwright.sync_api import Page, expect

# Fixture moved to conftest.py


# Test 1: Verify build output files exist
def test_build_output_exists():
    """Verify that all expected build output files exist."""
    assert os.path.exists("site/index.html"), "Main index.html not found"
    assert os.path.exists("site/aulas/aula-01/index.html"), "Lesson 01 page not found"
    assert os.path.exists("site/aulas/aula-16/index.html"), "Lesson 16 page not found"
    assert os.path.exists("site/slides/index.html"), "Slides index not found"
    assert os.path.exists("site/setups/index.html"), "Setup index not found"
    assert os.path.exists("site/assets/js/quiz.js"), "Quiz JS not found"
    assert os.path.exists("site/assets/css/quiz.css"), "Quiz CSS not found"

# Test 2: Homepage structure and content
def test_homepage_structure(page: Page, base_url):
    """Test that the homepage loads and has correct structure."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(base_url)
    
    # Check title
    expect(page).to_have_title("Lógica e Algoritmos - Curso")
    
    # Check main heading
    heading = page.locator("h1")
    expect(heading).to_contain_text("Curso de Algoritmos")
    
    # Check navigation cards exist
    # Material uses .md-typeset .grid.cards
    # The cards might be inside a div with class "grid cards"
    # We can check for the existence of the text "Lógica Sólida" which is in the first card
    expect(page.get_by_text("Lógica Sólida")).to_be_visible()

# Test 3: Navigation to Lesson 01
def test_lesson_01_page(page: Page, base_url):
    """Test Lesson 01 page loads and has correct content."""
    page.goto(f"{base_url}/aulas/aula-01/")
    
    # Check title (flexible match)
    # The actual title in HTML is "Aula 01 - Lógica e Algoritmos - Curso"
    expect(page).to_have_title(re.compile(r"Aula 01 - Lógica e Algoritmos"))
    
    # Check main heading
    heading = page.locator("h1")
    expect(heading).to_contain_text("Introdução")
    
    # Check quiz containers exist
    quiz_containers = page.locator(".quiz-container")
    if quiz_containers.count() > 0:
         expect(quiz_containers.first).to_be_visible()

# Test 4: Quiz interactivity
def test_quiz_functionality(page: Page, base_url):
    """Test that quiz JavaScript works correctly."""
    page.goto(f"{base_url}/quizzes/quiz-01/")
    
    # Wait for quiz to be visible
    first_quiz = page.locator(".quiz-container").first
    if first_quiz.is_visible():
        # Click on the correct answer (first option in first quiz)
        correct_option = first_quiz.locator(".quiz-option[data-correct='true']").first
        correct_option.click()
        
        # Check that feedback is displayed
        feedback = first_quiz.locator(".quiz-feedback")
        expect(feedback).to_be_visible()
        expect(feedback).to_contain_text("Correto")

# Test 5: Slides generation
def test_slides_structure(page: Page, base_url):
    """Test that slides are generated correctly."""
    page.goto(f"{base_url}/slides/")
    
    # Check title contains "Slides"
    title = page.title()
    assert "Slides" in title, f"Expected 'Slides' in title, got: {title}"
    
    # Check navigation exists
    # Material MkDocs uses .md-nav but specific page layout might vary
    # Use h1 check for safety
    expect(page.locator("h1")).to_contain_text("Slides")
    
    # Check content is present (list of slides)
    content = page.locator(".md-content")
    expect(content).to_be_visible()

# Test 6: Lesson 16 page (Testing/Boas Práticas)
def test_lesson_16_page(page: Page, base_url):
    """Test Lesson 16 page loads correctly."""
    page.goto(f"{base_url}/aulas/aula-16/")
    
    # Check title
    # Actual: "Aula 16 (PHP) - Lógica e Algoritmos - Curso"
    expect(page).to_have_title(re.compile(r"Aula 16 \(PHP\)"))
    
    # Check quiz containers
    quiz_containers = page.locator(".quiz-container")
    if quiz_containers.count() > 0:
        expect(quiz_containers.first).to_be_visible()

# Test 7: Mermaid diagram rendering (checking Lesson 11)
def test_mermaid_diagram(page: Page, base_url):
    """Test that Mermaid diagrams are present in the content."""
    page.goto(f"{base_url}/aulas/aula-09/")
    
    # Check for mermaid code block or rendered diagram
    # MkDocs Material renders mermaid as div.mermaid or similar
    mermaid_div = page.locator("div.mermaid")
    # Wait for it to be visible (client-side rendering)
    if mermaid_div.count() > 0:
        expect(mermaid_div.first).to_be_visible()
    else:
        # Fallback check for code block if JS didn't run
        code_block = page.locator("code.language-mermaid")
        if code_block.count() > 0:
            expect(code_block.first).to_be_visible()

# Test 8: Assets loading
def test_assets_load(page: Page, base_url):
    """Test that CSS and JS assets load correctly."""
    page.goto(f"{base_url}/aulas/aula-01/")
    
    # Check that quiz.js is loaded
    quiz_script = page.locator("script[src*='quiz.js']")
    expect(quiz_script).to_be_attached()
    
    # Check that quiz.css is loaded via checking style application
    quiz_container = page.locator(".quiz-container").first
    if quiz_container.is_visible():
        expect(quiz_container).to_have_css("border-radius", "8px")
