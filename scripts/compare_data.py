from fuzzywuzzy import fuzz

def compare_data(extracted_name, extracted_address, reference_name, reference_address):
    name_score = fuzz.ratio(extracted_name, reference_name)
    address_score = fuzz.ratio(extracted_address, reference_address)
    print(f"Name Match: {name_score}%, Address Match: {address_score}%")
    return name_score, address_score

if __name__ == "__main__":
    compare_data("John Doe", "123 Street", "Jon Doe", "123 St")
