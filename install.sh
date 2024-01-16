#!/bin/bash

echo "Please wait.."

mkdir -p /Jack-John-Joe/SuiteResources
+
cp easy-writer.py /Jack-John-Joe/SuiteResources
cp real-todo.py /Jack-John-Joe/SuiteResources

SourceFilePath="/Jack-John-Joe/SuiteResources/easy-writer.py"
ShortcutPath="~/Desktop/easy-writer.lnk"

echo "[Desktop Entry]
Type=Application
Name=Easy Writer
Exec=python3 $SourceFilePath
" > "$ShortcutPath"

SourceFilePath="/Jack-John-Joe/SuiteResources/real-todo.py"
ShortcutPath="~/Desktop/real-todo.lnk"

echo "[Desktop Entry]
Type=Application
Name=Real Todo
Exec=python3 $SourceFilePath
" > "$ShortcutPath"


echo "Done. Please report any issues to me!"
