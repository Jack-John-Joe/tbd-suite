echo "If you didn't run this as an Administrator, please run it as one!"
# Download the Python installer
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe" -OutFile "c:/temp/python-3.12.1-amd64.exe"

# Run the installer with the desired options
Start-Process c:/temp/python-3.12.1-amd64.exe '/quiet InstallAllUsers=0 PrependPath=1 Include_test=0' -wait

# Verify the installation
python --version

# Delete the installer file
Remove-Item c:/temp/python-3.12.1-amd64.exe
