
from setuptools import setup
from setuptools.extension import Extension

from pathlib import Path
import shutil

from Cython.Build import cythonize
from Cython.Distutils import build_ext

class encBuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent
        target_dir = build_dir if not self.inplace else root_dir

        self.copy_file(Path('app') / '__init__.py', root_dir, target_dir)
        self.copy_file(Path('app') / '__main__.py', root_dir, target_dir)
        self.copy_file(Path('app/modules') / '__init__.py', root_dir, target_dir)
        self.copy_file(Path('app/modules') / '__main__.py', root_dir, target_dir)
        self.copy_file(Path('app/modules/db') / '__init__.py', root_dir, target_dir)
        self.copy_file(Path('app/modules/db') / '__main__.py', root_dir, target_dir)




    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return

        shutil.copyfile(str(source_dir / path), str(destination_dir / path))


setup(
    name="smart_tagger_enc",
    ext_modules=cythonize(
        [
           Extension("app.*", ["app/*.py"]),
           Extension("app.modules.*", ["app/modules/*.py"]),
           Extension("app.modules.db*", ["app/modules/db/*.py"]),
        ],
        build_dir="build",
        compiler_directives=dict(
        always_allow_keywords=True
        )),
    cmdclass=dict(
        build_ext=encBuildExt
    ),
    packages=[]
)