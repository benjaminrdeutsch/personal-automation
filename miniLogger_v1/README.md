# miniLogger_v1

![AutoHotkey](https://img.shields.io/badge/AutoHotkey-v2.0-334455?logo=autohotkey&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-blue?logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Stable-success)

A simple lightweight keylogger that captures local keystrokes. I wrote it while studying cybersecurity to understand what certain attack vectors look like from the other side.

## Features

* 🪶 **Ultra-Lightweight** - Complete standalone executable weighing in at just ~880KB.
* 🚀 **Zero Dependencies** - The portable `.exe` runs instantly without needing anything else installed.
* 🔒 **100% Local Storage** - All data is saved locally to disk; strictly no network connectivity or cloud uploading.
* ⚡ **Silent Operation** - Runs efficiently in the background with negligible CPU and RAM footprint.
* 📄 **Human-Readable Logs** - Outputs clear, timestamped text files ready for parsing or manual review.

## Usage
1. Run the program like you would any typical Windows executable.
2. Press `F12` to start listening, and when you're done, press `F12` once more to end the listening session.
3. When a listening session ends, a `log.txt` file is created in the same directory that miniLogger ran in.
4. To terminate the program, you must either close it through the **System Tray**, or **Task Manager**, as the application will not appear in the taskbar.

> **Disclaimer:** I wrote this tool as a proof-of-concept designed strictly for local environment testing and personal usage analysis. It was written purely for educational purposes and any usage should reflect this philosophy.

## Technical Details
* This utility is written in the **AutoHotkey** scripting language, and compiled to a standalone `.exe` using the official [Ahk2Exe](https://github.com/AutoHotkey/Ahk2Exe) compiler.
* It's currently compiled to run natively on a Windows machine with x86 architecture, but can be run through any available AHK 2.0 compatible compiler.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
