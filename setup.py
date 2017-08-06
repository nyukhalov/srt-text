from setuptools import setup

setup(
    name='srt-text',
    version='1.0.1',
    url='https://github.com/nyukhalov/srt-text',
    author='Roman Niukhalov',
    license='MIT',
    packages=['srttext'],
    entry_points={
        'console_scripts': [
            'srttext=srttext.app:main'
        ]
    }
)
