import itertools
import whois
import time

# Function to generate 3-letter domain names
def generate_domains():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    domains = [''.join(domain) + '.ly' for domain in itertools.product(chars, repeat=3)]
    return domains

# Function to check domain availability using WHOIS lookup
def check_availability(domain):
    try:
        w = whois.whois(domain)
        # Debugging: print WHOIS data to see what is returned
        print(f"WHOIS data for {domain}: {w}")
        
        # Check if the domain has an expiration or creation date, meaning it's taken
        if w.expiration_date or w.creation_date:
            return None  # Domain is taken
        else:
            return domain  # Domain is available
    except Exception as e:
        # Print the specific exception message
        print(f"Error checking {domain}: {e}")
        # Consider domain available if there's an exception (whois lookup failed)
        return domain

# Main function to generate and check domain availability
def main():
    available_domains = []
    domains = generate_domains()

    for domain in domains:
        print(f"Checking {domain}...")
        available = check_availability(domain)
        if available:
            print(f"{domain} is available!")
            available_domains.append(domain)
        else:
            print(f"{domain} is taken.")
        
        # Sleep for a bit to avoid overwhelming the WHOIS server
        time.sleep(2)  # Increase sleep time to avoid getting blocked

    # Output the available domains
    print("\nAvailable .ly domains:")
    for domain in available_domains:
        print(domain)

if __name__ == '__main__':
    main()
