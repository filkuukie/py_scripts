# tdu2-microphone-fix
A small fix for Test Drive Unlimited 2 to disable access to microphone. 

The game checks once your microphone and run it on game's launch. It can be annoying or suspicious for some people, especially when they pirated the game (which you can't buy anymore).

So, what these batch files do is running a game's launcher (UpLauncher) and searching for TestDrive2.exe (game itself) process in your task manager. When the game is running the script modifies a Windows registry responsible for enabling/disabling microphone in system settings. First, it disables a microphone, then after 15 seconds it enables again and closes UpLauncher. Time would be shorter, but sometimes the game launches longer as usual and script won't work.

To use it, just put these files in game's directory and run CMD1.bat, thats'it.

In fact, you can simply modify CMD2 batch file by changing EXE filename to use it for any Win32-based application. Quite useful since Windows doesn't offer any option to disable microphone for individual non-UWP app.
