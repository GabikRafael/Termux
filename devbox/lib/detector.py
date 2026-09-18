from pathlib import Path
def detect(root):
 p=Path(root); has=lambda n:(p/n).exists(); text=lambda n:(p/n).read_text(errors='ignore') if has(n) else ''
 if has('fabric.mod.json'): return {'type':'Fabric Minecraft','reason':'fabric.mod.json'}
 if has('mods.toml'): return {'type':'Forge Minecraft','reason':'mods.toml'}
 if has('project.godot'): return {'type':'Godot','reason':'project.godot'}
 if has('Cargo.toml'): return {'type':'Rust','reason':'Cargo.toml'}
 if has('pom.xml'): return {'type':'Maven Java','reason':'pom.xml'}
 if has('build.gradle') or has('build.gradle.kts') or has('gradlew'):
  return {'type':'Android Gradle' if has('AndroidManifest.xml') or (p/'app'/'src'/'main'/'AndroidManifest.xml').exists() else 'Gradle','reason':'Gradle files'}
 if has('package.json'): return {'type':'Node.js','reason':'package.json'}
 if has('CMakeLists.txt') or list(p.glob('**/*.cpp')) or list(p.glob('**/*.cc')): return {'type':'C++','reason':'C++ sources'}
 if list(p.glob('**/*.c')): return {'type':'C','reason':'C sources'}
 if list(p.glob('**/*.kt')): return {'type':'Kotlin','reason':'Kotlin sources'}
 if list(p.glob('**/*.java')): return {'type':'Java','reason':'Java sources'}
 py=has('pyproject.toml') or has('requirements.txt') or has('setup.py') or has('main.py')
 if py:
  blobs=' '.join(text(x) for x in ('pyproject.toml','requirements.txt','setup.py','main.py')).lower()
  return {'type':'Pygbag' if 'pygbag' in blobs else 'Pygame' if 'pygame' in blobs else 'Python','reason':'Python files'}
 return {'type':'Unknown','reason':'no supported project files'}
