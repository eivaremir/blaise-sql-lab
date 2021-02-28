pyinstaller -F server.py --distpath "./" 
mkdir ".\dist\win-unpacked\templates\"
copy /y /v ".\templates\*" ".\dist\win-unpacked\templates\"

mkdir ".\dist\win-unpacked\styles\"
copy /y /v ".\static\styles\*" ".\dist\win-unpacked\styles\"  

mkdir ".\dist\win-unpacked\js\"
copy /y /v ".\static\js\*" ".\dist\win-unpacked\js\"  

copy /y /v ".\server.exe" ".\dist\win-unpacked\"

pause