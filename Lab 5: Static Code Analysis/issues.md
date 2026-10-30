# Lab 5 – Static Code Analysis
## Issue Identification and Documentation

The original `address_book.py` program was analyzed using three static code analysis tools: Pylint, Bandit and Flake8. The tools identified coding convention violations, security vulnerabilities and formatting issues.

The following table documents the issues identified in the initial analysis, arranged with high and medium severity security findings first.

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
| --------- | -------- | ----------- | --------------- | ---------------- |
| Weak MD5 Hash Algorithm | Bandit – High (B324) | 19 | The program uses MD5 to generate contact identifiers. MD5 is considered a weak hashing algorithm and is vulnerable to collision attacks. | Replaced `hashlib.md5()` with `hashlib.sha256()` while retaining the six-character identifier format. |
| Unsafe Pickle Deserialization | Bandit – Medium (B301) | 67 | The use of `pickle.load()` can execute arbitrary code when deserializing an untrusted or maliciously crafted file. | Replaced pickle-based backup and restoration with JSON serialization and deserialization using `json.dump()` and `json.load()`. |
| Missing Module Docstring | Pylint – Convention (C0114) | 1 | The Python source file does not contain a module-level docstring explaining its purpose. | Added a module docstring describing the address book application. |
| Missing Function Docstrings | Pylint – Convention (C0116) | 10, 18, 22, 30, 39, 47, 53, 60, 65, 70 | Functions do not have docstrings explaining their purpose and functionality. | Added descriptive docstrings to all functions, including `main()`. |
| Invalid Function and Argument Names | Pylint – Convention (C0103) | 10, 13, 18, 22, 30, 31, 39, 47, 53, 54, 60, 61, 65, 66 | Function names and arguments use camelCase instead of the recommended snake_case naming convention. | Renamed functions and arguments using snake_case, such as `addContact` to `add_contact` and `fullName` to `full_name`. |
| Broad Exception Handling | Pylint – Warning (W0718) | 34 | The program catches the general `Exception` class, which may hide unexpected errors and make debugging difficult. | Replaced `except Exception` with the specific `except KeyError` exception handler. |
| Inefficient Loop Iteration | Pylint – Refactor (C0200) | 49 | The program uses `range(len(names))` to iterate over a list, which is less readable and less Pythonic. | Replaced the loop with `enumerate(names, start=1)`. |
| Missing File Encoding | Pylint – Warning (W1514) | 54 | The CSV file is opened without explicitly specifying a character encoding, which may cause inconsistent behavior across environments. | Added `encoding="utf-8"` to the `open()` function. |
| Pickle Module Import | Bandit – Low (B403) | 3 | Importing the pickle module introduces potential security risks when handling serialized data from untrusted sources. | Removed the pickle import and replaced it with the JSON module. |
| Hardcoded Password | Bandit – Low (B105) | 6 | The source code contains a hardcoded password string in the `SYNC_PASSWORD` constant. | Removed the unused hardcoded password constant. |
| Missing Whitespace Around Operator | Flake8 – E225 | 23 | The assignment statement `found=[]` does not contain the required whitespace around the assignment operator. | Changed it to `found = []`. |
| Excessive Blank Lines | Flake8 – E303 | 47 | The source code contains three blank lines between functions, exceeding the recommended limit. | Removed unnecessary blank lines to follow Python formatting conventions. |
| Missing Whitespace After Comma | Flake8 – E231 | 84 | A comma is not followed by the required whitespace in the function call. | Added a space after the comma. |
| Line Too Long | Flake8 – E501 | 85 | A line contains 86 characters, exceeding the configured maximum of 79 characters. | Split the statement across multiple lines to improve readability and comply with the line-length limit. |

## Static Analysis Results

The following results were obtained by comparing the initial and final static analysis reports.

| **Tool** | **Before Fixes** | **After Fixes** |
| -------- | ---------------- | --------------- |
| Pylint | 5.47/10 | 10.00/10 |
| Bandit | 4 security findings | 0 security findings |
| Flake8 | 4 formatting violations | 0 formatting violations |

## Conclusion

The static code analysis process helped identify and resolve issues related to code quality, security and formatting in the original address book application.

- Pylint score improved from 5.47/10 to 10.00/10.
- All four Bandit security findings were resolved.
- All four Flake8 formatting violations were resolved.
- The original address book functionality was preserved, and the program was tested after the modifications.

The final source code was successfully verified using all three static analysis tools.
