import shutil, subprocess
from pathlib import Path
from detector import detect
from config import load_config
from doctor import missing_message
def call(args, cwd):
 try:
  subprocess.run(args, cwd=cwd, check=True)
 except FileNotFoundError:
  raise RuntimeError(f"Required command '{args[0]}' is not installed. Run devbox doctor and install the listed Termux package.")
 except subprocess.CalledProcessError as e:
  raise RuntimeError(f"Build command failed with exit status {e.returncode}.")
def configured(root, section):
 c=load_config(root).get(section,{}) .get('command')
 if c: subprocess.run(c, cwd=root, shell=True, check=True); return True
 return False
def build(root, package=False):
 if configured(root,'build'): return
 d=detect(root)['type']; root=Path(root)
 if d in ('Gradle','Android Gradle'): call(['./gradlew','build'] if (root/'gradlew').exists() else ['gradle','build'],root)
 elif d=='Maven Java': call(['mvn','package'],root)
 elif d=='Rust': call(['cargo','build','--release'],root)
 elif d=='C++': call(['cmake','-S','.','-B','build'],root); call(['cmake','--build','build'],root)
 elif d=='C': raise RuntimeError('No C build recipe found; add [build] command to devbox.toml.')
 elif d=='Node.js': call(['npm','run','build'],root)
 elif d in ('Python','Pygame','Pygbag'): raise RuntimeError('Python projects have no universal native build. Use devbox web for a configured pygbag web build.')
 else: raise RuntimeError(f'No safe build strategy for {d}; add [build] command to devbox.toml.')
def run(root):
 if configured(root,'run'): return
 d=detect(root)['type']; root=Path(root)
 if d in ('Python','Pygame','Pygbag') and (root/'main.py').exists(): call(['python','main.py'],root)
 elif d=='Godot': call(['godot','--path','.','--editor'],root)
 elif d=='Node.js': call(['npm','start'],root)
 else: raise RuntimeError(f'No run recipe for {d}; add [run] command to devbox.toml.')
def apk(root):
 root=Path(root); d=detect(root)['type']
 if d!='Android Gradle': raise RuntimeError('APK generation needs an Android Gradle project with an existing Android packaging setup; DevBox will not fake an APK.')
 build(root); out=root/'dist'; out.mkdir(exist_ok=True); found=list(root.glob('**/build/outputs/apk/**/*.apk'))
 if not found: raise RuntimeError('Gradle completed but produced no APK.')
 for f in found: shutil.copy2(f,out/f.name)
 print(f'Copied {len(found)} APK file(s) to dist/.')
def clean(root):
 root=Path(root).resolve();
 for name in ('build','dist'):
  target=(root/name).resolve()
  if target.parent != root: raise RuntimeError('unsafe clean path')
  if target.exists(): shutil.rmtree(target); print(f'Removed {target.name}/')
