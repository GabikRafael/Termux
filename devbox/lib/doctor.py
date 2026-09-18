import shutil, subprocess
TOOLS=[('Python','python','python'),('pip','pip','python-pip'),('Java','java','openjdk-17'),('javac','javac','openjdk-17'),('Gradle','gradle','gradle'),('Maven','mvn','maven'),('C compiler','clang','clang'),('C++ compiler','clang++','clang'),('Rust','cargo','rust'),('Node.js','node','nodejs'),('npm','npm','nodejs'),('Godot','godot','godot'),('pygbag','pygbag','python-pygbag'),('adb','adb','android-tools'),('aapt','aapt','aapt'),('apksigner','apksigner','apksigner'),('zipalign','zipalign','zipalign')]
def report():
 for label, cmd, pkg in TOOLS:
  path=shutil.which(cmd)
  print(f"[{'✓' if path else '✗'}] {label}" + ("" if path else f"\n    Install: pkg install {pkg}"))
def missing_message(cmd): return f"{cmd} is missing. Run devbox doctor for the applicable Termux package."
