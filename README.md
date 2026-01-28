# Basic Web Path Enumerator (Bash Script)

##  Requirements

To run this script, you need:

* **Bash** shell (Linux, macOS, or WSL)
* **curl** installed
* A **wordlist file**
* Network access to the target web server

---

##  Introduction

This Bash script is a **basic web path enumerator**.
It is designed to discover existing directories or files on a web server by appending words from a wordlist to a base URL and analyzing the HTTP response codes.

The script performs simple web enumeration and can be useful for:

* Web reconnaissance
* Learning how directory enumeration works
* Identifying accessible paths on a web server

It is a lightweight and educational alternative to tools like `dirb`, `gobuster`, or `ffuf`.

---

##  How It Works

1. The script requires **exactly two arguments**:

   * A wordlist file
   * A base URL
2. If the required arguments are not provided, the script exits with an error message.
3. Each word from the wordlist is appended to the base URL.
4. A **HEAD request** is sent to the constructed URL using `curl`.
5. The HTTP response status code is extracted.
6. Only paths returning a status code **less than or equal to 399** are displayed, indicating that the resource exists or is accessible.

Client and server error responses (400+) are ignored.

---

##  Example Usage

### Command

```bash
bash script.sh words.txt https://example.com
```

### Sample Output

```text
admin : 200
login : 301
images : 403
```

This output indicates that the listed paths exist or respond successfully on the target server.

### Wordlists
The most widespread wordlists are found in the Seclist DB in Github.
Here are some of them 
  * Most common wordlists for hidden directories are:
    * https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
    * https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
    * https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt
  * Most common wordlists for hidden files are:
    * https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt

Here’s a clean, professional disclaimer section you can paste **after** the content:

---
##  To note

The provided description is for the .sh file. However, i advise you to try the .py file. It is more informative in its output.




# Basic Web Path Enumerator (Python Script)

## Requirements

To run this script, you need:

* **Python 3**
* The **requests** Python library
* A **wordlist file**
* Network access to the target web server

### Install dependencies

```bash
pip install requests
```

---

## Introduction

This Python script is a **basic web path enumerator**.
It is designed to discover existing directories or files on a web server by appending words from a wordlist to a base URL and analyzing HTTP response codes.

The script performs simple web enumeration and can be useful for:

* Web reconnaissance
* Learning how directory enumeration works
* Identifying accessible paths on a web server
* Understanding HTTP status codes and HEAD requests

It serves as a lightweight and educational alternative to tools like `dirb`, `gobuster`, or `ffuf`, with more readable output than a basic shell script.

---

## How It Works

1. The script requires **exactly two arguments**:

   * A wordlist file
   * A base URL
2. If the required arguments are not provided, the script prints an error message and exits.
3. The wordlist file is opened and read line by line.
4. Each word is appended to the base URL to form a full path.
5. A **HEAD request** is sent to the constructed URL using the `requests` library.
6. If the HTTP response status code is **less than 400**, the path is considered valid and displayed.
7. Each request is labeled with a numbered use case for easier tracking.

Client and server error responses (400+) are ignored.

---

## Example Usage

### Command

```bash
python3 script.py words.txt https://example.com
```

### Sample Output

```text
Usecase n 1
admin
Usecase n 2
login
Usecase n 3
images
```

This output indicates that the listed paths respond successfully or exist on the target server.

---

## Wordlists

The most widespread wordlists are found in the **SecLists** repository on GitHub.

### Common wordlists for hidden directories:

* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt)
* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt)
* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt)

### Common wordlists for hidden files:

* [https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt)

---

## To Note

The provided description above refers to the **Python (.py) implementation**.

Compared to the Bash version, the Python script is:

* More readable
* Easier to extend
* More informative in its output
* Better suited for learning and future enhancements

You are advised to use the **Python version** if you want clearer results and better control over request handling.

---

## Disclaimer

This script is provided **for educational and authorized security testing purposes only**.

You must **only** use this tool against web servers and applications that you **own** or have **explicit permission** to test. Unauthorized scanning, enumeration, or probing of systems you do not control may be illegal and could violate local, national, or international laws.

The author assumes **no responsibility or liability** for misuse of this script or for any damage caused by its use. By running this script, you acknowledge that you understand these risks and agree to use it responsibly and ethically.

If you are learning web security, always practice in controlled environments such as:

* Local test servers
* Lab environments
* Intentionally vulnerable applications (e.g., training platforms)

---

