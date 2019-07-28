from setuptools import setup

setup(
    name='middles_editor',
    version='1.0',
    packages=['middles_editor'],
    url='https://gitlab.com/beaudrychase/middles-editor',
    license='',
    author='beaudry chase',
    author_email='beauchase213@gmail.com',
    description='A tool created to go over the results of middles-tool',
    entry_points={
        'console_scripts': [
            'middles_editor =middles_editor.middles_editor_app:main'
        ]
    },
    install_requires=['Pyqt5']

)
