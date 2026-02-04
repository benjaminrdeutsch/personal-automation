log = ""
F12::
Hotkey, F12, Off
Input, keystrokes, V, {F12}
log := keystrokes
Hotkey, F12, On
FileAppend, %log%, %A_WorkingDir%\log.txt
Return