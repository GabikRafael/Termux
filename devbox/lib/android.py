import shutil, subprocess
from builder import apk
from doctor import report, missing_message
def android(root, action, args):
 if action=='doctor': return report()
 if action=='build': return apk(root)
 if action=='adb':
  if not shutil.which('adb'): raise RuntimeError(missing_message('adb'))
  return subprocess.run(['adb',*args],check=True)
 if action=='install':
  if not args: raise RuntimeError('Usage: devbox android install APK')
  if not shutil.which('adb'): raise RuntimeError(missing_message('adb'))
  return subprocess.run(['adb','install','-r',args[0]],check=True)
 if action=='sign':
  if not shutil.which('apksigner'): raise RuntimeError(missing_message('apksigner'))
  if not args: raise RuntimeError('Usage: devbox android sign APKSIGNER_ARGUMENTS')
  return subprocess.run(['apksigner','sign',*args],check=True)
