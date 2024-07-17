apt update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt-get install -f -y
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver
apt install python3 -y
apt install pip3 -y
pip3 install selenium
wget https://raw.githubusercontent.com/monhodsompul/luckminechrm/main/asu.py
python3 asu.py
