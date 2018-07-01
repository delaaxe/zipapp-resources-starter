rm -rf build
rm -rf dist
mkdir build
cp -R myapp build
pip install --target build -r requirements.txt
python -m zipapp --output myapp.pyz --main 'myapp:main' build
rm -rf build
mkdir dist
mv myapp.pyz dist

