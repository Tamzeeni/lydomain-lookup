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
        if w.expiration_date:
            return domain, w.expiration_date  # Return domain and expiration date
        else:
            return None, None  # Domain is available
    except Exception as e:
        # Print the specific exception message
        print(f"Error checking {domain}: {e}")
        # Consider domain available if there's an exception (whois lookup failed)
        return None, None

# Main function to generate and check domain availability
def main():
    available_domains = []
    taken_domains = []  # To store domains with expiration dates
    
    domains = generate_domains()

    for domain in domains:
        print(f"Checking {domain}...")
        available, expiration_date = check_availability(domain)
        if available:
            print(f"{domain} is taken. Expiration date: {expiration_date}")
            taken_domains.append(f"{domain}: Expiration Date: {expiration_date}")
        else:
            print(f"{domain} is available!")
            available_domains.append(domain)
        
        # Sleep for a bit to avoid overwhelming the WHOIS server
        time.sleep(2)  # Increase sleep time to avoid getting blocked

    # Output the available domains
    print("\nAvailable .ly domains:")
    for domain in available_domains:
        print(domain)

    # Export the taken domains with expiration dates to a text file
    with open("taken_domains_with_expiration_date.txt", "w") as file:
        for domain in taken_domains:
            file.write(domain + "\n")
    
    print("\nExported taken domains with expiration dates to 'taken_domains_with_expiration_date.txt'")

if __name__ == '__main__':
    main()
