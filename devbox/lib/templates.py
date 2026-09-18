from pathlib import Path
def create(path, kind):
 path=Path(path).resolve()
 if path.exists(): raise RuntimeError(f'{path} already exists; refusing to overwrite')
 if '/' in path.name or path.name in ('','.','..'): raise RuntimeError('invalid project name')
 path.mkdir(); (path/'src').mkdir(); (path/'build').mkdir(); (path/'dist').mkdir()
 (path/'devbox.toml').write_text(f'[project]\nname = "{path.name}"\ntype = "{kind}"\n\n[build]\n\n[run]\n')
 (path/'README.md').write_text(f'# {path.name}\n\nCreated with DevBox.\n')
 files={'python':('main.py','print("Hello from DevBox")\n'),'pygame':('main.py','import pygame\npygame.init()\nprint("Pygame ready")\n'),'cpp':('src/main.cpp','#include <iostream>\nint main(){ std::cout << "Hello\\n"; }\n'),'java':('src/Main.java','class Main { public static void main(String[] a) { System.out.println("Hello"); } }\n'),'godot':('project.godot','[application]\nconfig/name="DevBox Game"\n'),'web':('index.html','<!doctype html><title>DevBox</title><h1>Hello DevBox</h1>\n')}
 f,data=files[kind]; (path/f).write_text(data); print(f'Created {path} ({kind} template).')
