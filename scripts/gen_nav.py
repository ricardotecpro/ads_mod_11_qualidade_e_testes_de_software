
def gen_section(name, folder, prefix, count):
    print(f"  - {name}:")
    print(f"      - 'Índice': {folder}/index.md")
    for i in range(1, count + 1):
        num = f"{i:02d}"
        print(f"      - '{prefix} {num}': {folder}/{prefix.lower()}-{num}.md")

print("  - Exercícios:")
print("      - 'Índice': exercicios/index.md")
for i in range(1, 17):
    print(f"      - 'Exercicio {i:02d}': exercicios/exercicio-{i:02d}.md")

print("  - Projetos:")
print("      - 'Índice': projetos/index.md")
for i in range(1, 17):
    print(f"      - 'Projeto {i:02d}': projetos/projeto-{i:02d}.md")

print("  - Quizzes:")
print("      - 'Índice': quizzes/index.md")
for i in range(1, 17):
    print(f"      - 'Quiz {i:02d}': quizzes/quiz-{i:02d}.md")

print("  - Slides:")
print("      - 'Índice': slides/index.md")
for i in range(1, 17):
    print(f"      - 'Slide {i:02d}': slides/slide-{i:02d}.md")
