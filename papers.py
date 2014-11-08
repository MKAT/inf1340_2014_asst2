
#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
#Test comment

import json
#The below calls the json files to be read
with open("example_entries.json", "r") as file_reader:
    file_contents_example_entries = file_reader.read()
    json_contents = json.loads(file_contents_example_entries)
    print(file_contents_example_entries)

with open("watchlist.json", "r") as file_reader:
    file_contents_watchlist = file_reader.read()
    json_contents = json.loads (file_contents_watchlist)
    print(file_contents_watchlist)

with open("countries.json", "r") as file_reader:
    file_contents_countries = file_reader.read()
    json_contents = json.loads (file_contents_countries)
    print(file_contents_countries)
# Does the above go within the below  def decide(input....) where the parameters are listed?


def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """

    #For each traveler in the file, loop through each traveler and validate application information
    for traveler in json_contents:

        #Validate passport number
        is_passport_valid = valid_passport_format(traveler['passport'])

        #If passport number if valid, check watchlist for countries with medical advisory
        does_country_have_medical_advisory = check_countries(travler['from']['via'])

                # the check_countries function needs to be defines to raise the argument

        #If country not on medical advisory list, check if all required information has been provided
        is_information_complete = check_required_information(traveler)

                # the check_required_information function needs to be defines to raise the argument

        # If all required information has been provided, check for valid birthday format
        if is_passport_valid==True:
            is_birthday_vaid = valid_date_format(traveler['birth_date'])

        #If birthday format is valid, check to see if traveler's home country is KAN
            #If home country is KAN and reason for entry is re-entry, accept

        #MT addition part
#The only options for entry reason are returning, visit, or transit
    for traveler in json_contents:
        entry_reason = (traveler["returning", "visit", "transit"])

        returning_home =["returning"]
        entry_reason = check_returning_home(traveler["returning"])
            return ['Accept']
    print("returning home to KAN")

#If home country is not KAN, check to see reason for entry

        elif:
        entry_reason =check_entry_reason is(traveler("visit"))
         return ['secondary']
#after this step It then goes to be secondarily processed for other visa parameters
        elif:
        entry_reason =check_entry_reason is(traveler("transit"))
         return ['secondary']

#after this step It then goes to be secondarily processed for other visa parameters

"""
entry_reason is "returning" == True:
for entry_reason in ('example_entries.json'):
 return(entry_reason("returning"))"""

            #If reason for entry is visit and the traveler's country requires a visa, visitor visa required
            #entry_reason is

            #If reason for entry is transit and the traveler's country requires a visa, transit visa required

        #If visa is required, check that visa date format is valid and did not expire

        #If visa is valid, check if traveler's name is on watchlist

            #If name is on watchlist secondary

        #If traveler's name is not on watchlist, accept

    else:
        return ["Reject"]
print("push to futher questioning and checks")

def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string

    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False


#Checks if traveler's passport, and if first or last name is on watchlist
def check_watchlist(on_watchlist):
    #check the first_name of people on watchlist
    #check the last_name of people on watchlist
    #check the passport number of passport watchlist
first_name = ""
last_name = ""
#confused about the passport part of the json file
    if first_name is not "":
    if last_name is not "":
    return: [Reject]


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def required_information_complete():
    """
    Checks whether all the required information has been provided
    :param Personal and traveling information provided in strings
           First Name
           Last Name

    :return:
    """