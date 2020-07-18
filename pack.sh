pip uninstall -y bamsnap
rm -rf build
rm -rf ./dist/*
python3 setup.py sdist bdist_wheel
pip install ./dist/bamsnap-0.2.5-py3-none-any.whl
