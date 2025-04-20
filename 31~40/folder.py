from pathlib import Path
path=Path.cwd()
print(path)
Python=path/'Python'
print(Python)


入門_g=path.iterdir()
for x in 入門_g:
    print(x.name, x.is_file(),x.is_dir())

files=[x.name for x in (Path.cwd() / path).iterdir()]
print(files)

g=path.glob('**/*')
for x in g:
    print(x.name)