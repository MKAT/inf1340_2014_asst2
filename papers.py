#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"


def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """
    # 1. Import JSON file contents into string list.

    # #1-a. Import travelers' info.
    travelers_list = import_travelers_json(input_file)
    #1-b. Import watchlist file.
    watchlist_list = import_watchlist_json(watchlist_file)
    #1-c. Import countries file.
    countries_list = import_countries_json(countries_file)

    #2. Now we have each file stored in Lists.  Loop through each traveler in the travelers list
    #   and validate application information, then store the result to output list.
    output_results = []
    for traveler in travelers_list:

        #3. Check if any required information is missing on this traveler.
        if not required_information_complete(traveler):
            # This traveler's required information is not complete, therefore Reject.
            output_results.append("Reject")
        else:  # continue next validation.

            #4. Check if 'from' or 'via' country has medical advisory. If yes, send to quarantine.
           """
            """
        with open("countries.json", "r") as countries_file:
            #4-a. Get 'from' country code.
            def from_country_code (reader):
                from_country_code = [traveler['country']]

        def medical_advisory_country(reader):
            # read from_country_code
            #  from_data = traveler['from']  # assume From data is provided.
            from_country = {traveler['from']}  # put from_country data into a list.
            from_country_code = {traveler['country']}

        #4-b. Get 'via' country code, if exists.
        if "via" in traveler:
            #  via_data =  traveler['via']
            via_country = {traveler['via']}
            via_country_code = via_country['country']
        else:
            via_country_code = ""

        if not is_countries_cleared(countries_list, from_country_code, via_country_code):
            # This traveler should be sent to Quarantine as the 'from' country or 'via' country has
            def medical_advisory(reader): #do I change to counties cleared?
                """
                :param reader: file open for reading)-> list
            Read zero or more quarantine countries from reader, return a list
                """
            result = []
            key, name = line.split()
            from_country_code = [name]
            via_country_code = [name]
            reading = True
            while reading:
                if medical_advisory:
                    result.append(medical_advisory)
                else:
                    reading = False
                    return

            #    medical advisory.
            output_results.append("Quarantine")

        else:  # continue next validation.
            # is_passport_valid = valid_passport_format(traveler['passport']) ---> NOT NECESSARY
            #5. Check if traveler is on watchlist. If yes, send to Secondary review.
            if not is_watchlist_cleared(watchlist_list, traveler['passport'], traveler['first_name'],
                                        traveler['last_name']):
                # This traveler's passport# or name is on watchlist. Send to Secondary review.
                output_results.append("Secondary")
            else:  # continue next validation.
                #6. Check if traveler's home country is KAN
                home_country = {traveler['home']}
                if home_country['country'] != "KAN":
                    # home country is not KAN. Get entry_reason and check if any visa is required.
                    entry_reason = traveler['entry_reason']
                    visa = {traveler['visa']}
                    visa_date = visa['date']  # all dates are in YYYY-MM-DD format.
                    #6-a. Check if traveler's home country require any visa.
                    if not is_visa_valid(countries_list, home_country['country'], entry_reason, visa_date):
                        # visa is invalid.  Reject the traveler.
                        output_results.append("Reject")
                    else:
                        output_results.append("Accept")
                else:
                    # this traveler's home country is KAN. Entry_reason is returning.
                    output_results.append("Accept")

    return output_results


def import_travelers_json(input_file):
    """
    imports travelers' data from JSON file.
    :param input_file:
    :return: List with travelers data.
    """
    import json
    # The below calls the json file to be read
    with open(input_file, "r") as file_reader:
        file_contents_input_file = file_reader.read()
        travelers_info = json.loads(file_contents_input_file)
        travelers_list = [travelers_info]
        # print(travelers_list)
        return travelers_list


def import_watchlist_json(watchlist_file):
    """
    Imports watchlist data from JSON file.
    :param watchlist_file:
    :return: List with watchlist info.
    """
    import json

    with open(watchlist_file, "r") as file_reader:
        file_contents_watchlist = file_reader.read()
        watchlist_info = json.loads(file_contents_watchlist)
        watchlist_list = [watchlist_info]
        # print(watchlist_list)
        return watchlist_list


def watchlist_file(import_watchlist_json, watchlist_list):

    for line in import_watchlist_json(watchlist_file):
        line = line.strip()
        if line != "-":
            import_watchlist_json.len = str(line[:-1])
        if watchlist_file.len > str(line[:0]):
            # we want to print the line that is longer than a certain amount because it has content thus an alert len function
            print(line)
        #Thus this would return a line that would have the name or passport number of the person on the watchlist

def import_countries_json(countries_file):
    """
    Imports countries data from json file to use it for validation.
    :param countries_file:
    :return: List with countries data.
    """
    import json

    with open(countries_file, "r") as file_reader:
        file_contents_countries = file_reader.read()
        countries_info = json.loads(file_contents_countries)
        countries_list = [countries_info]
        # print(countries_list)
        return countries_list


def required_information_complete(traveler):
    """
    Checks whether all the required information has been provided
    :param Personal and traveling information provided in strings
           All information is in one string
           First Name
           Last Name
           Passport number

    :return: Boolean True if info is complete, False otherwise.
    """
    import json
    #need a str statement to ensure info is str

    with open(traveler, "r") as file_reader:
        file_contents_input_file = file_reader.read()
        travelers_info = json.loads(file_contents_input_file)
        travelers_list = [travelers_info]
    for line in travelers_info:
        if travelers_info: str("")
        return False
    last_name = line.strip()
    first_name = line.strip()
    passport = line.strip()
    found = True
    if last_name in travelers_info:
       travelers_info[last_name] = travelers_info[last_name] > 1
    else:
        reading = False
        return

def is_countries_cleared(countries_list, from_country, via_country):
    """
    Checks if 'from' or 'via' country has medical advisory.
    :param countries_list: list of countries.
    :param from_country:
    :param via_country:
    :return: Boolean True if medical advisory is cleared, False otherwise.
    """
    # Check from country.
    data = countries_list.readline().rstrip()
    while data.startswith("medical_advisory"):
        data = countries_list.readline().rstrip()
    print(data)

    for data in countries_list:
        print(data.rstrip())

    with open(countries_list, "r") as file_reader:
            from_country = file_reader.read()
            via_country = file_reader.read()
            if from_country in countries_list:
                countries_list [from_country] = countries_list [from_country] > 1
    # Check via country
            if via_country in countries_list:
                countries_list [via_country] = countries_list [via_country] > 1
      # If via country is empty, no need to validate.
                if not via_country:
                    return True  # temporary for testing


def is_watchlist_cleared(watchlist_list, passport_number, first_name, last_name):
    """
    #Checks if traveler's passport, and if first or last name is on watchlist
    :param passport_number: passport number of the traveler.
           first_name: first name of the traveler.
           last_name: last name of the traveler.
    :return: Boolean True if traveler is not on the watchlist, False otherwise.
    """
    # check the passport number of passport watchlist
    # check the first_name of people on watchlist
    #check the last_name of people on watchlist
    if passport_number != "":
        # passport number is available so check with passport number.

        return True  # TEMPORARY FOR TESTING!
    elif first_name != "" and last_name != "":

        return True  #TEMPORARY FOR TESTING
    else:
        # Passport number nor names are given so we cannot validate. Return False.
        return False


def is_visa_valid(countries_list, home_country, entry_reason, visa_date):
    """
    Check if visa is valid if traveler's country and entry_reason require a visa.
    Note: This function is called only when home_country != KAN.
    :param countries_list:
    :param home_country:
    :param entry_reason:
    :param visa_date: traveler's visa date
    :return: Boolean True if either visa is not required or valid. False otherwise.
    """
    if entry_reason == "visit":
        # Check if traveler's country require a visitor's visa.

        return True  # TEMPORARY FOR TESTING
    elif entry_reason == "transit":
        # Check if traveler's country require a transit visa.

        return True  # TEMPORARY FOR TESTING
    else:
        return True


"""
def valid_passport_format(passport_number):
    #Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string

    :return: Boolean; True if the format is valid, False otherwise

    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False
"""

"""

        #MT addition part
#The only options for entry reason are returning, visit, or transit

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

"""
Prof notes:
passport_format = re.compile('^\w{5}-\w{5}-\w{5}-\w{5}-\w{5}$')
The first line in valid_visa_format should be:
passport_format = re.compile('^\w{5}-\w{5}$')
"""

"""
#Attempted traveler function
   with open(traveler, "r") as file_reader:
        file_contents_input_file = file_reader.read()
        travelers_info = json.loads(file_contents_input_file)
        travelers_list = {travelers_info}
       #need a str statement o ensure info is str
        result = []
        travelers_info = [name]
        while reading:
            if required_information_complete:
                result.append(travelers_info)
                while reading:
                    line = file_reader.readline()
                    if "passport":
                        result.__contains__("passport")
                        if len("passport") > 8:
                            return True
                    if "last_name":
                        result.__contains__("last_name")
                        if len("last_name") > 9:
                            return True
                    if "first_name":
                        result.__contains__("first_name")
                        if len("first_name") > 10:
                            return True

                else:
                    reading = False
                    return result
                    """

"""
            countries_file.readline()
            data = countries_file.readline().rstrip()
            while data.startswith("medical_advisory"):
                data = countries_file.readline().rstrip()
            print(data)
            for data in countries_file:
            """

""" if __name__ =='__main__':
    medical_advisory = open("countries.json"."r")
    """
