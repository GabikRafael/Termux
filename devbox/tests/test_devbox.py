import contextlib, io, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]/'lib'))
from detector import detect
from config import load_config
from templates import create
from doctor import report
from builder import clean

class DevBoxTests(unittest.TestCase):
 def project(self, file, content=''):
  d=tempfile.TemporaryDirectory(); p=Path(d.name); (p/file).write_text(content); self.addCleanup(d.cleanup); return p
 def test_python_and_pygame_detection(self):
  self.assertEqual(detect(self.project('main.py'))['type'],'Python')
  self.assertEqual(detect(self.project('requirements.txt','pygame'))['type'],'Pygame')
 def test_java_cpp_and_godot_detection(self):
  self.assertEqual(detect(self.project('src.java'))['type'],'Java')
  self.assertEqual(detect(self.project('CMakeLists.txt'))['type'],'C++')
  self.assertEqual(detect(self.project('project.godot'))['type'],'Godot')
 def test_web_build_detection(self): self.assertEqual(detect(self.project('requirements.txt','pygbag'))['type'],'Pygbag')
 def test_config_parsing(self):
  p=self.project('devbox.toml','[project]\nname="x"\n'); self.assertEqual(load_config(p)['project']['name'],'x')
 def test_python_creation_and_path_safety(self):
  d=Path(tempfile.mkdtemp()); self.addCleanup(lambda: __import__('shutil').rmtree(d))
  create(d/'demo','python'); self.assertTrue((d/'demo'/'main.py').exists())
  with self.assertRaises(RuntimeError): create(d/'demo','python')
 def test_clean_is_project_local(self):
  d=Path(tempfile.mkdtemp()); self.addCleanup(lambda: __import__('shutil').rmtree(d,ignore_errors=True)); (d/'build').mkdir(); clean(d); self.assertFalse((d/'build').exists())
 def test_doctor_output(self):
  output=io.StringIO()
  with contextlib.redirect_stdout(output): report()
  self.assertIn('Python',output.getvalue())
if __name__=='__main__': unittest.main()
