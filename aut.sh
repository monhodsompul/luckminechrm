wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt-get install -f -y
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip
apt install unzip -y
unzip chromedriver-linux64.zip
cd chromedriver-linux64
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver
apt install python3 -y
apt install pip3 -y
pip3 install selenium
wget https://raw.githubusercontent.com/monhodsompul/luckminechrm/main/asu.py

clear
python3 asu.py
