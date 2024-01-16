@echo off
python -m pip install requests pyqt5
echo "Please wait.."
New-Item -Path "C:\" -Name "Jack-John-Joe" -ItemType Directory
New-Item -Path "C:\Jack-John-Joe" -Name "SuiteResources" -ItemType Directory
Move-Item -Path $pwd/easy-writer.py -Destination C:/Jack-John-Joe/SuiteResources
Move-Item -Path $pwd/real-todo.py -Destination C:/Jack-John-Joe/SuiteResources
$SourceFilePath = "C:\Jack-John-Joe/SuiteResources/easy-writer.py"
$ShortcutPath = "C:\Users\$env:USERNAME\Desktop\easy-writer.lnk"
$WScriptObj = New-Object -ComObject ("WScript.Shell")
$shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
$shortcut.TargetPath = $SourceFilePath
$shortcut.Save()
# asdfghjkl
$SourceFilePath = "C:\Jack-John-Joe/SuiteResources/real-todo.py"
$ShortcutPath = "C:\Users\$env:USERNAME\Desktop\real-todo.lnk"
$WScriptObj = New-Object -ComObject ("WScript.Shell")
$shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
$shortcut.TargetPath = $SourceFilePath
$shortcut.Save()
echo "Done. Please report any issues to me!"