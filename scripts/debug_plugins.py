import sys
if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points

print("Python executable:", sys.executable)
print("Installed MkDocs Plugins:")
eps = entry_points(group='mkdocs.plugins')
for ep in eps:
    print(f"  - Name: {ep.name}, Value: {ep.value}")

print("\nInstalled MkDocs Themes:")
eps = entry_points(group='mkdocs.themes')
for ep in eps:
    print(f"  - Name: {ep.name}, Value: {ep.value}")
