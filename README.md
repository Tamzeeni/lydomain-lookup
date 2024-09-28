# developed by @Tamzeeni
# lydomain-lookup

Here’s a `README.md` file for your domain availability checker project:

---

# Domain Availability Checker

This Python script generates 3-letter `.ly` domain names, checks their availability using the `whois` lookup, and exports the registered domains with their expiration dates into a `.txt` file.

## Features

- Generates all possible combinations of 3-letter `.ly` domains.
- Performs WHOIS lookup to check if the domain is registered.
- Exports domains that are registered (have an expiration date) into a text file.
- Includes rate-limiting to avoid overwhelming the WHOIS servers.

## Prerequisites

Before running the script, ensure that you have the following installed:

1. **Python 3.x**: Make sure Python is installed. You can download it from [here](https://www.python.org/downloads/).

2. **Required Python Libraries**:
   - `whois`: This is the library used to perform WHOIS lookups.

### Install the `whois` Library:

You can install it via `pip`:

```bash
pip install python-whois
```

## How to Use

1. **Clone or Download** the repository to your local machine.

2. **Run the Script**:

   ```bash
   python domain_checker.py
   ```

   The script will:
   - Generate all possible 3-letter `.ly` domain names.
   - Check if each domain is registered or available.
   - Print the status of each domain in the console.
   - Export the registered domains with their expiration dates into a text file.

3. **View the Results**:

   After the script finishes running, you can find the list of registered domains along with their expiration dates in the `taken_domains_with_expiration_date.txt` file located in the same directory.

## File Structure

```
.
├── domain_checker.py         # The main script that performs domain generation and availability checking.
├── taken_domains_with_expiration_date.txt  # Output file with registered domains and expiration dates.
└── README.md                 # This file, describing the project.
```

## Code Explanation

- **`generate_domains()`**: Generates all possible 3-letter domain combinations using lowercase English letters (e.g., `aaa.ly`, `aab.ly`).
  
- **`check_availability(domain)`**: Performs a WHOIS lookup for a given domain. If the domain has an expiration date (i.e., it's registered), the function returns the domain and its expiration date.

- **`main()`**: Orchestrates the domain generation and checking process, stores available and registered domains, and exports the registered domains to a text file.

## Example Output

In the console:

```
Checking aaa.ly...
aaa.ly is taken. Expiration date: 2025-03-21
Checking aab.ly...
aab.ly is available!
...
```

In the output file `taken_domains_with_expiration_date.txt`:

```
aaa.ly: Expiration Date: 2025-03-21
abc.ly: Expiration Date: 2024-09-12
...
```

## Notes

- The script uses a sleep timer (`time.sleep(2)`) to avoid overwhelming the WHOIS server. You can adjust the sleep time if needed, but be careful not to send too many requests in a short period.
  
- The `.ly` TLD (Libya) may have specific rate limits or restrictions on WHOIS lookups. If you encounter issues with blocked requests, consider using a domain availability API instead.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

developed by @Tamzeeni