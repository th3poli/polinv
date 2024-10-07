from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='polinv',
    version='1.0.0',
    description='Simple Python with collected in one place many modules with extra configurations and useful tools.',
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    author='th3poli',
    author_email='',
    keywords=['polinv', 'helpful', 'tool'],
    packages=['polinv'],
    url='https://github.com/th3poli/polinv',
    install_requires=['requests', 'pyautogui', 'undetected-chromedriver', 'cloudscraper'] # 'beautifulsoup4'
)

# python setup.py sdist bdist_wheel
# pip install ./dist/polinv-1.0.0.tar.gz --no-cache-dir
# python -m twine upload .\dist\*