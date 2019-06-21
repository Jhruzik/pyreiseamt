# -*- coding: utf-8 -*-

def main():
    
    # Import Modules
    import scraper
    import argparse
    import json
    
    # Parse User Input
    parser = argparse.ArgumentParser(description = "Gather country specific information from German Foreign Office")
    parser.add_argument("command", help = "Command to execute [list or extract]")
    parser.add_argument("-c", "--countries", help = "Countries to extract [seperate by ;]")
    parser.add_argument("-o", "--output", help = "Where to save extracted information as JSON")
    args = parser.parse_args()
    
    if args.command not in ["list", "extract"]:
        raise ValueError("command should be either 'list' or 'extract'")
    if args.command == "extract" and args.countries is None:
        raise ValueError("specify the countries to extract (seperate by ';')")
    if args.command == "extract" and not args.output.endswith(".json"):
        raise ValueError("output must end with .json")
        
    # Get latest Country Information
    print("Gathering latest data\r", end = "")
    countries = scraper.list_countries()
    
    # React to list command
    if args.command == "list":
        country_names = [x for x in countries]
        country_names.sort()
        format_list = list()
        i = 0
        total = len(country_names)-1
        while i <= total:
            if total - i >= 4:
                concat_string = " | ".join(country_names[i:i+4])
            else:
                concat_string = " | ".join(country_names[i:total+1])
            format_list.append(concat_string)
            i += 4
        print("Available Countries: \n")
        print("\n".join(format_list))
        
    # React to extract command
    if args.command == "extract":
        countries_to_do = args.countries.split(";")
        result_extract = list()
        for country in countries_to_do:
            result_tmp = scraper.extract_country(countries[country])
            result_extract.append(result_tmp)
        with open(args.output, mode = "w", encoding = "utf-8") as o:
            json.dump(result_extract, o, ensure_ascii = False, indent = 1)
        print("Output written to: {}".format(args.output))
        
# Run Main function
if __name__ == "__main__":
    main()