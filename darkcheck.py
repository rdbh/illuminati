# get information from text
import requests
import config

# constants
BANNER = \
    "-------------------------\n" + \
    "- Dark Web Address Menu -\n" + \
    "-------------------------\n"

# Check dark web addresses and get HTTP status
def check(addresses):
    # create results dictionary
    results = {}

    # set up a proxy session through TOR
    session = requests.session()
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'

    # Let user know the timeout
    print(f"Timeout is {config.HTTP_TIMEOUT} seconds")

    # iterate addresses into dictionary
    for address in addresses:
        # add "http://" to the beginning of each website
        newurl = "http://" + address
        status = ""
        try:
            print(f"Checking: {address}")
            response = session.get(newurl,timeout=config.HTTP_TIMEOUT)
            status = response.status_code
            print(f"\tResponse took {response.elapsed} seconds\n")
        except:
            # status of 0 is no connection
            status = 0
            print("No response")
        results[address] = status
        

    # return the results as a dictionary
    return results

def darkcheck():
    # get file name
    website_file="web sites.txt"

    # Open the file
    # Try except block
    try:
        first_file = open(website_file, "r")
        print("source file opened\n")
    except:
        print("file not opened")
    # read the contents of the file
    contents = first_file.read()
    first_file.close()
    addresses = contents.splitlines()

    # print the contents
    results = check(addresses)

    # print website statue
    for key in results:
        print(f"Website: {key}, Return Code: {results[key]}")

def main():
    darkcheck()

if __name__ == "__main__":
    main()


    
    
