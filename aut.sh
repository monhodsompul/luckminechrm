wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

dpkg -i google-chrome-stable_current_amd64.deb

apt-get install -f -y

wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip

unzip chromedriver-linux64.zip

sudo mv chromedriver /usr/bin/chromedriver

sudo chown root:root /usr/bin/chromedriver

sudo chmod +x /usr/bin/chromedriver

pip3 install selenium

python3 asu.py
