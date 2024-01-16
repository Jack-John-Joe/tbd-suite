#!/bin/bash

# Install essential build tools
sudo apt-get update
sudo apt-get install -y build-essential

# Download the Python installer
wget -O /tmp/python-3.12.1.tar.xz https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tar.xz

# Extract the archive
tar -xf /tmp/python-3.12.1.tar.xz -C /tmp/

# Navigate to the extracted directory
cd /tmp/Python-3.12.1/

# Configure and install Python
./configure
make
sudo make install

# Verify the installation
python3 --version

# Clean up temporary files
rm -rf /tmp/python-3.12.1.tar.xz /tmp/Python-3.12.1/
