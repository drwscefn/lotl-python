#!/usr/bin/python3

import subprocess
import datetime
import os
import argparse

def run_bash_command(command):
    subprocess.run(command, shell=True)

def combine_subdomains_files(today_date, yesterday_date):
    with open(f"subdomains/{yesterday_date}_subdomains.txt", "r") as yesterday_file:
        yesterday_subdomains = yesterday_file.readlines()
    
    with open(f"subdomains/{today_date}_subfinder.txt", "r") as subfinder_file:
        today_subfinder_subdomains = subfinder_file.readlines()
    
    with open(f"subdomains/{today_date}_amass.txt", "r") as amass_file:
        today_amass_subdomains = amass_file.readlines()
    
    all_subdomains = set(yesterday_subdomains + today_subfinder_subdomains + today_amass_subdomains)
    
    with open(f"subdomains/{today_date}_subdomains.txt", "w") as combined_file:
        combined_file.writelines(sorted(all_subdomains))

def main():

    parser = argparse.ArgumentParser(description="Subdomain enumeration script")
    parser.add_argument("-d", "--domain", required=True, help="Domain to perform subdomain enumeration on")
    args = parser.parse_args()

    domain = args.domain

    today_date = datetime.datetime.now().strftime("%Y%m%d")
    yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")
    
    subfinder_command = f"subfinder -all -d {domain} -o subdomains/{today_date}_subfinder.txt"
    amass_command = f"amass enum -passive -d {domain} -o subdomains/{today_date}_amass.txt"
    
    run_bash_command(subfinder_command)
    run_bash_command(amass_command)
    
    combine_subdomains_files(today_date, yesterday_date)
    
if __name__ == "__main__":
    main()
