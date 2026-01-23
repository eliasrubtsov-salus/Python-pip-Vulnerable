# Vulnerable Python Application for Testing

⚠️ **WARNING**: This application contains intentional security vulnerabilities for testing purposes only. DO NOT use in production or expose to the internet!

## Purpose

This application is designed to test vulnerability detection and remediation tools. It includes multiple known CVEs across different dependency categories.

## Known Vulnerabilities

### High Severity

1. **PyYAML 5.3.1** - CVE-2020-14343
   - Arbitrary code execution via unsafe YAML deserialization
   - Exploited in `/parse_yaml` endpoint

2. **Pillow 8.0.0** - Multiple CVEs
   - Buffer overflow vulnerabilities
   - Image processing vulnerabilities

3. **Cryptography 3.3.0** - CVE-2023-23931
   - Cipher.update_into memory corruption

4. **Flask 2.0.1** - CVE-2023-30861
   - Cookie parsing vulnerability

### Medium Severity

5. **Requests 2.25.0** - CVE-2023-32681
   - Proxy-Authorization header information leak

6. **Jinja2 2.11.0** - CVE-2020-28493
   - Regular Expression Denial of Service (ReDoS)

7. **Django 3.1.0** - Multiple CVEs
   - Various security issues in older versions

8. **urllib3 1.26.0** - CVE-2023-43804
   - Cookie request header leak

9. **SQLParse 0.4.0** - CVE-2021-32839
   - Regular Expression Denial of Service

10. **Notebook 6.1.5** - CVE-2021-32797
    - Cross-Site Scripting (XSS) vulnerabilities

### Low Severity

11. **Certifi 2020.12.5**
    - Outdated root certificates

12. **Setuptools 50.0.0** - CVE-2022-40897
    - Regular Expression Denial of Service

13. **IPython 7.16.0** - CVE-2022-21699
    - Execution with unnecessary privileges

## Application Vulnerabilities

Beyond vulnerable dependencies, the application code itself contains security issues:

- **SSTI (Server-Side Template Injection)**: Root endpoint uses user input directly in template
- **YAML Deserialization**: Uses unsafe `yaml.load()` allowing code execution
- **Debug Mode**: Flask runs with debug=True
- **Bind to 0.0.0.0**: Exposed to all network interfaces

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install vulnerable dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The application will run on http://localhost:5000

## Testing Vulnerability Detection

Use tools like:
- `pip-audit` - For Python dependency scanning
- `safety check` - For known security vulnerabilities
- `bandit` - For code security issues
- `snyk test` - Comprehensive vulnerability scanning
- Your custom vulnerability elimination agent

Example commands:
```bash
pip install pip-audit
pip-audit -r requirements.txt

pip install safety
safety check -r requirements.txt

pip install bandit
bandit -r .
```

## Expected Scan Results

A vulnerability scanner should detect:
- 13+ vulnerable packages
- Multiple high-severity CVEs
- Code-level security issues (if using static analysis)

## Remediation

To fix vulnerabilities, update to latest stable versions:

```
flask>=3.0.0
requests>=2.31.0
pillow>=10.0.0
cryptography>=41.0.0
pyyaml>=6.0.1
jinja2>=3.1.2
django>=4.2.0
urllib3>=2.0.0
certifi>=2023.7.22
setuptools>=65.5.1
sqlparse>=0.4.4
notebook>=7.0.0
ipython>=8.10.0
```

## License

MIT License - For testing purposes only

## Disclaimer

This application is for educational and testing purposes only. The vulnerabilities are intentional and should never be deployed to production environments.
