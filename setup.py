from distutils.core import setup, Extension

yescrypt_cryply_module = Extension('yescrypt_cryply',
        sources = ['yescrypt.c'],
        extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
        include_dirs=['.'])

setup (name = 'yescrypt_cryply',
       version = '1.0',
       description = 'Bindings for yescryptr16 proof of work used by yenten/cryply...etc.',
       ext_modules = [yescrypt_cryply_module])

