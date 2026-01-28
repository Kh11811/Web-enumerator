# Usage Examples

This document provides detailed examples for using the Web-enumerator scripts.

## Table of Contents

- [Basic Usage](#basic-usage)
- [Using Different Wordlists](#using-different-wordlists)
- [Expected Output](#expected-output)
- [Common Use Cases](#common-use-cases)

---

## Basic Usage

### Bash Script

The Bash script uses `curl` to send HEAD requests to the target URL.

```bash
# Basic usage with sample wordlist
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com

# Using a custom wordlist
bash src/enumerator.sh /path/to/custom_wordlist.txt https://example.com

# Testing a specific subdirectory
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com/api
```

### Python Script

The Python script uses the `requests` library for more detailed HTTP handling.

```bash
# Basic usage with sample wordlist
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com

# Using a custom wordlist
python3 src/web_enumerator.py /path/to/custom_wordlist.txt https://example.com

# Testing a specific subdirectory
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com/api
```

---

## Using Different Wordlists

### Small Wordlist (Quick Testing)

Use the provided sample wordlist for quick tests:

```bash
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com
```

### Medium Wordlist (Comprehensive)

For more thorough enumeration, use wordlists from SecLists:

```bash
# Download a medium-sized wordlist
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt

# Run enumeration
bash src/enumerator.sh common.txt https://example.com
```

### Large Wordlist (Extensive)

For extensive enumeration (may take longer):

```bash
# Download a larger wordlist
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/directory-list-2.3-small.txt

# Run enumeration
python3 src/web_enumerator.py directory-list-2.3-small.txt https://example.com
```

---

## Expected Output

### Bash Script Output

The Bash script displays the path name and HTTP status code for successful responses:

```text
admin : 200
login : 301
images : 403
api : 200
```

**Explanation:**
- `200` - OK (resource found and accessible)
- `301` - Moved Permanently (redirect)
- `302` - Found (temporary redirect)
- `403` - Forbidden (resource exists but access denied)

### Python Script Output

The Python script displays use case numbers and successful paths:

```text
Usecase n 1
admin
Usecase n 2
login
Usecase n 5
Usecase n 9
images
```

**Note:** The Python script shows the iteration number for all checks and only displays the path name for successful responses (status code < 400).

---

## Common Use Cases

### 1. Testing a Local Development Server

```bash
# Test a local server
python3 src/web_enumerator.py examples/sample_wordlist.txt http://localhost:8080
```

### 2. Finding Hidden Admin Panels

Create a custom wordlist for admin panel discovery:

```bash
# Create admin-focused wordlist
cat > admin_wordlist.txt << EOF
admin
administrator
panel
dashboard
control
manage
backend
cpanel
wp-admin
phpmyadmin
EOF

# Run enumeration
bash src/enumerator.sh admin_wordlist.txt https://example.com
```

### 3. API Endpoint Discovery

```bash
# Create API-focused wordlist
cat > api_wordlist.txt << EOF
api
v1
v2
graphql
rest
swagger
docs
openapi
health
status
EOF

# Run enumeration
python3 src/web_enumerator.py api_wordlist.txt https://example.com
```

### 4. Testing with Different Base URLs

```bash
# Test main domain
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com

# Test subdomain
bash src/enumerator.sh examples/sample_wordlist.txt https://blog.example.com

# Test specific path
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com/app
```

### 5. Comparing Results Between Scripts

Run both scripts with the same inputs to compare output formats:

```bash
# Bash version
echo "=== Bash Script Results ==="
bash src/enumerator.sh examples/sample_wordlist.txt https://example.com

echo ""
echo "=== Python Script Results ==="
python3 src/web_enumerator.py examples/sample_wordlist.txt https://example.com
```

---

## Tips and Best Practices

1. **Always get permission** before scanning any website you don't own
2. **Start with small wordlists** to avoid overwhelming the target server
3. **Use HEAD requests** (both scripts do this by default) to minimize server load
4. **Review results carefully** - not all found paths may be relevant
5. **Combine with other tools** for comprehensive reconnaissance
6. **Test on controlled environments** like local servers or intentionally vulnerable apps

---

## Troubleshooting

### Script Not Finding Expected Paths

- Ensure the target URL is correct (include http:// or https://)
- Check network connectivity
- Verify the wordlist file exists and contains entries
- Some servers may block automated requests

### Permission Denied Errors

- Check file permissions: `chmod +x src/enumerator.sh`
- Ensure you have read access to the wordlist file
- For Python script, ensure requests library is installed: `pip install -r requirements.txt`

### No Output

- The server may not have any of the paths from your wordlist
- Try a different wordlist
- Verify the server is accessible: `curl -I https://example.com`

---

## Additional Resources

- [SecLists Wordlist Repository](https://github.com/danielmiessler/SecLists)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
