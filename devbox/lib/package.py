import shutil, subprocess
FEATURES={'python':['python'],'pygame':['python','python-pygame'],'java':['openjdk-17'],'web':['python'], 'android':['android-tools']}
def install_feature(feature):
 if not feature: print('Features: '+', '.join(FEATURES)); return
 if feature not in FEATURES: raise RuntimeError(f'{feature} is not a DevBox feature. Known features: '+', '.join(FEATURES))
 pkgs=FEATURES[feature]
 print('Will install real Termux packages: '+' '.join(pkgs))
 if not shutil.which('pkg'): raise RuntimeError('pkg is unavailable; run this command inside Termux.')
 # pkg prompts before package changes; no root or remote scripts are used.
 subprocess.run(['pkg','install',*pkgs],check=True)
 if feature=='web': print('For pygbag, run: pip install pygbag (PyPI package, reviewed by you before installation).')
