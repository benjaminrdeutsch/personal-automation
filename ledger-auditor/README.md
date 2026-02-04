# Ledger Auditor

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-darkslategray?logo=linux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success)

> "*Dedicated to my two wonderful roommates; we may all suck at keeping track of rent, but I still love you guys.*"

A Python-based command-line interface (CLI) tool designed to audit shared housing finances. It parses raw transaction logs to calculate tenant balances, detect payment discrepancies, and generate historical debt reports.

## Features

* 💸 **Automated Auditing** - Instantly parses CSV ledgers to identify which roommates underpaid and by exactly how much.
* 🖥️ **Interactive CLI** - Features a clean terminal interface with auto-clearing and banner display for a professional user experience.
* 🧩 **Modular Architecture** - Built using an MVC-inspired structure with separated `models` for scalable data handling.
* 📊 **CSV Parsing** - Ingests standard rent ledger exports without manual formatting.
* 🛡️ **Error Handling** - Robust validation to ensure data integrity when processing financial records.

## Usage

1. **Prerequisite:** Ensure you have Python 3.9+ installed.
2. Place your formatted `.xlsx` ledger in the root folder of the project.
3. Run the file in your terminal of choice:
```bash
cd ledger-auditor
python3 ledger_auditor.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

