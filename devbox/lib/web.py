import shutil, subprocess, sys
from pathlib import Path
def web(root, serve=False, port=None, main=None):
 root=Path(root).resolve(); main=main or root/'main.py'; port=port or 8000
 if not main.exists(): raise RuntimeError('web requires a valid main.py')
 if not shutil.which('pygbag'): raise RuntimeError('pygbag is missing. Install it with: pip install pygbag')
 # pygbag writes build/web beside the supplied project; it must receive a directory.
 subprocess.run(['pygbag','--build',str(root)],cwd=root,check=True)
 if serve:
  output=root/'build'/'web'
  if not output.exists(): raise RuntimeError('pygbag did not produce build/web/')
  print(f'Server: http://127.0.0.1:{port}')
  subprocess.run([sys.executable,'-m','http.server',str(port),'--directory',str(output)],check=True)
