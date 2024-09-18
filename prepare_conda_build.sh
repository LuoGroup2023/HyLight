
mkdir -p hylight/HyLight 
cp -r script tools hylight/HyLight
cp README.md setup.py hylight
touch hylight/HyLight/__init__.py
touch hylight/HyLight/script/__init__.py
# add current path as package searching path, may be not need, no test
sed -i '9a\pwd=os.path.split(os.path.realpath(__file__))[0]' hylight/HyLight/script/HyLight.py
sed -i '10a\sys.path.append(pwd)' hylight/HyLight/script/HyLight.py

tar -czvf hylight.tar.gz hylight
