# Basic Web Path Enumerator

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

## Script Versions

### Bash Script (`.sh`)

* Lightweight and dependency-minimal
* Uses `curl`
* Suitable for quick tests and shell environments

### Python Script (`.py`)

* More readable and extensible
* More informative output
* Better suited for learning and future improvements

> **Note:** While both scripts work similarly, the **Python version is recommended** for clarity and maintainability.

---

## Requirements

### Bash Script Requirements

To run the Bash script, you need:

* **Bash shell** (Linux, macOS, or WSL)
* **curl**
* A **wordlist file**
* Network access to the target web server

---

### Python Script Requirements

To run the Python script, you need:

* **Python 3**
* The **requests** library
* A **wordlist file**
* Network access to the target web server

#### Install dependencies

```bash
pip install requests
```

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

### Bash Script

#### Command

```bash
bash script.sh words.txt https://example.com
```

#### Sample Output

```text
admin : 200
login : 301
images : 403
```

---

### Python Script

#### Command

```bash
python3 script.py words.txt https://example.com
```

#### Sample Output

```text
Usecase n 1
admin
Usecase n 2
login
Usecase n 3
images
```

This output indicates that the listed paths exist or respond successfully on the target server.

---

## Wordlists

The most commonly used wordlists can be found in the **SecLists** GitHub repository.

### Common Wordlists for Hidden Directories

* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt)
* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt)
* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt)

### Common Wordlists for Hidden Files

* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt)

---

## To Note

The Bash and Python scripts perform the same core task, but the **Python implementation**:

* Is easier to read
* Is easier to extend
* Produces clearer output
* Is better suited for learning and customization

You are encouraged to experiment with both versions.

---

## Disclaimer

This project is provided **for educational and authorized security testing purposes only**.

You must **only** use these scripts against web servers and applications that you **own** or have **explicit permission** to test. Unauthorized scanning or enumeration of systems you do not control may be illegal and could violate local, national, or international laws.

The author assumes **no responsibility or liability** for misuse of these scripts or for any damage caused by their use. By running these scripts, you acknowledge that you understand these risks and agree to use them responsibly and ethically.

For learning purposes, always practice in controlled environments such as:

* Local test servers
* Lab environments
* Intentionally vulnerable applications (e.g., training platforms)

