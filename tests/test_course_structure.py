import pytest
import os
from pathlib import Path

# Expected course structure
EXPECTED_LESSONS = [f"aulas/aula-{i:02d}.md" for i in range(1, 17)]
EXPECTED_SLIDES = [f"slide-{i:02d}.md" for i in range(1, 17)]
EXPECTED_QUIZZES = [f"quiz-{i:02d}.md" for i in range(1, 17)]
EXPECTED_EXERCISES = [f"exercicio-{i:02d}.md" for i in range(1, 17)]
EXPECTED_PROJECTS = [f"projeto-{i:02d}.md" for i in range(1, 17)]
EXPECTED_SETUPS = [f"setup-{i:02d}.md" for i in range(1, 10)]
EXPECTED_INDEXES = [
    "aulas/index.md",
    "exercicios/index.md",
    "projetos/index.md",
    "quizzes/index.md",
    "slides/index.md",
    "setups/index.md"
]

def test_content_structure_exists():
    """Verify that the basic directory structure exists."""
    assert os.path.exists("docs"), "Docs directory missing"
    assert os.path.exists("docs/slides"), "Slides directory missing"
    assert os.path.exists("docs/quizzes"), "Quizzes directory missing"
    assert os.path.exists("docs/exercicios"), "Exercises directory missing"
    assert os.path.exists("docs/projetos"), "Projects directory missing"

def test_lessons_exist():
    """Verify that all 15 lessons exist in docs/."""
    missing_lessons = []
    for lesson in EXPECTED_LESSONS:
        if not os.path.exists(f"docs/{lesson}"):
            missing_lessons.append(lesson)
    
    assert not missing_lessons, f"Missing lessons: {missing_lessons}"

def test_slides_exist():
    """Verify that all 15 slides exist in docs/slides/."""
    missing_slides = []
    for slide in EXPECTED_SLIDES:
        if not os.path.exists(f"docs/slides/{slide}"):
            missing_slides.append(slide)
    
    assert not missing_slides, f"Missing slides: {missing_slides}"

def test_quizzes_exist():
    """Verify that all 15 quizzes exist in docs/quizzes/."""
    missing_quizzes = []
    for quiz in EXPECTED_QUIZZES:
        if not os.path.exists(f"docs/quizzes/{quiz}"):
            missing_quizzes.append(quiz)
    
    assert not missing_quizzes, f"Missing quizzes: {missing_quizzes}"

def test_exercises_exist():
    """Verify that all 15 exercises exist in docs/exercicios/."""
    missing_exercises = []
    for exercise in EXPECTED_EXERCISES:
        if not os.path.exists(f"docs/exercicios/{exercise}"):
            missing_exercises.append(exercise)
    
    assert not missing_exercises, f"Missing exercises: {missing_exercises}"

def test_projects_exist():
    """Verify that all 15 projects exist in docs/projetos/."""
    missing_projects = []
    for project in EXPECTED_PROJECTS:
        if not os.path.exists(f"docs/projetos/{project}"):
            missing_projects.append(project)
    
    assert not missing_projects, f"Missing projects: {missing_projects}"

def test_setups_exist():
    """Verify that all 9 setups exist in docs/setups/."""
    missing_setups = []
    for setup in EXPECTED_SETUPS:
        if not os.path.exists(f"docs/setups/{setup}"):
            missing_setups.append(setup)
    
    assert not missing_setups, f"Missing setups: {missing_setups}"

def test_indexes_exist():
    """Verify that all subdirectory index files exist."""
    missing_indexes = []
    for index in EXPECTED_INDEXES:
        if not os.path.exists(f"docs/{index}"):
            missing_indexes.append(index)
    
    assert not missing_indexes, f"Missing indexes: {missing_indexes}"
