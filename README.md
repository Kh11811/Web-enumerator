# Web Path Enumerator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

## Overview

This project contains **two simple web path enumeration scripts**:

* A **Bash script** using `curl`
* A **Python script** using the `requests` library

Both scripts are designed to discover existing directories or files on a web server by appending entries from a wordlist to a base URL and analyzing HTTP response codes.

These tools are intended for **educational purposes**, **web reconnaissance**, and **learning how directory enumeration works**. They are lightweight alternatives to tools such as `dirb`, `gobuster`, or `ffuf`.

---

## Features

* Uses **HEAD requests** (faster and less intrusive)
* Filters out client and server errors (HTTP 400+)
* Works with any custom wordlist
* Simple and readable output
* Available in **Bash** and **Python**

---

## Project Structure

```
Web-enumerator/
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── src/                    # Source code
│   ├── enumerator.sh       # Bash enumeration script
│   └── web_enumerator.py   # Python enumeration script
├── examples/               # Example files and usage
│   ├── sample_wordlist.txt # Sample wordlist for testing
│   └── usage_examples.md   # Detailed usage examples
├── docs/                   # Documentation
│   └── CONTRIBUTING.md     # Contributing guidelines
└── tests/                  # Test files
    └── test_enumerator.py  # Unit tests for Python script
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kh11811/Web-enumerator.git
cd Web-enumerator
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests
```

### 3. Verify Installation

```bash
# Test Bash script
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com

# Test Python script
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com
```

---

## Quick Start

### Bash Script

```bash
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com
```

**Sample Output:**
```text
admin : 200
login : 301
images : 403
```

### Python Script

```bash
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com
```

**Sample Output:**
```text
Usecase n 1
admin
Usecase n 2
login
Usecase n 3
images
```

---

## Script Versions

### Bash Script (`src/enumerator.sh`)

* Lightweight and dependency-minimal
* Uses `curl`
* Suitable for quick tests and shell environments

### Python Script (`src/web_enumerator.py`)

* More readable and extensible
* More informative output
* Better suited for learning and future improvements

> **Note:** While both scripts work similarly, the **Python version is recommended** for clarity and maintainability.

---

## Requirements

### Bash Script Requirements

* **Bash shell** (Linux, macOS, or WSL)
* **curl**
* A **wordlist file**
* Network access to the target web server

### Python Script Requirements

* **Python 3.7+**
* The **requests** library
* A **wordlist file**
* Network access to the target web server

---

## How It Works (Both Versions)

1. The script requires **exactly two arguments**:
   * A wordlist file
   * A base URL
2. If the arguments are missing, the script exits with an error.
3. Each word from the wordlist is appended to the base URL.
4. A **HEAD request** is sent to the constructed URL.
5. The HTTP response status code is checked.
6. Only responses with status codes **below 400** are displayed.

Client and server error responses (400+) are ignored.

---

## Usage Examples

For detailed usage examples, see [examples/usage_examples.md](examples/usage_examples.md).

### Basic Usage

```bash
# Bash Script
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com

# Python Script
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com
```

### Using Custom Wordlists

```bash
# Download a wordlist from SecLists
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt

# Run enumeration
bash src/enumerator.sh common.txt https://example.com
```

### Testing Specific Paths

```bash
# Test a subdirectory
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com/api
```

---

## Wordlists

The most commonly used wordlists can be found in the **SecLists** GitHub repository.

### Common Wordlists for Hidden Directories

* [directory-list-2.3-small.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-2.3-small.txt)
* [directory-list-2.3-medium.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-2.3-medium.txt)
* [common.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt)

---

## Testing

Run the test suite:

```bash
# Install pytest if not already installed
pip install pytest

# Run tests
python -m pytest tests/ -v
```

---

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](docs/CONTRIBUTING.md) for details on:

* Reporting bugs
* Suggesting features
* Code style guidelines
* Submitting pull requests
* Testing guidelines

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This project is provided **for educational and authorized security testing purposes only**.

You must **only** use these scripts against web servers and applications that you **own** or have **explicit permission** to test. Unauthorized scanning or enumeration of systems you do not control may be illegal and could violate local, national, or international laws.

The author assumes **no responsibility or liability** for misuse of these scripts or for any damage caused by their use. By running these scripts, you acknowledge that you understand these risks and agree to use them responsibly and ethically.

### Best Practices

For learning purposes, always practice in controlled environments such as:

* Local test servers
* Lab environments
* Intentionally vulnerable applications (e.g., OWASP WebGoat, DVWA, HackTheBox)

---

## Acknowledgments

* Inspired by tools like `dirb`, `gobuster`, and `ffuf`
* Wordlists from [SecLists](https://github.com/danielmiessler/SecLists) by Daniel Miessler

---

## Support

If you find this project helpful, please consider:

* ⭐ Starring the repository
* 🐛 Reporting bugs
* 💡 Suggesting new features
* 📖 Improving documentation

For questions or issues, please open an issue on GitHub.

