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
