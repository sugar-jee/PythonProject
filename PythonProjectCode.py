
csvfilepath = 'Recorded_URLs.csv'
uccsvfilepath = 'Known_UC_URLs.csv'
results = [url_id, malicious_count, suspicious_count, undetected_count, harmless_count]

#def checks to see if the URL ID exists in a file
def check_URL(file_path, url_id):
    if os.path.isfile(file_path):
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if url_id in row:
                    print(f"URL ID FOUND")
                    return True
    return False

#def appends a URL to the recorded_urls file and creates one if not found + add headers
def append_URL(csvfilepath, results):
    file_exists = os.path.isfile(csvfilepath)
    with open(csvfilepath, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        if not file_exists:
            csv_writer.writerow(['URL ID', 'Malicious Count', 'Suspicious Count', 'Undetected Count', 'Harmless Count'])
        print(f"Appending URL")
        csv_writer.writerow(results)

#def that will process URL
def process_url_id(url_id, uccsvfilepath, csvfilepath):
    print(f"processing URL ID: ", url_id)
    if check_URL(uccsvfilepath, url_id):
        print(f"URL found in UC URLs File")
    elif check_URL(csvfilepath, url_id):
        print(f"URL found in Recorded URLs File")
    else:
        append_URL(csvfilepath, results)
        print(f"URL appended to CSV File")

#actually run the process
process_url_id(url_id, uccsvfilepath, csvfilepath)