#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

import json


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
    # 1-b. Import watchlist file.
    watchlist_list = import_watchlist_json(watchlist_file)
    # 1-c. Import countries file.
    countries_list = import_countries_json(countries_file)
    #traveler = import_travelers_json(input_file)

    # 2. Now we have each file stored in Lists.  Loop through each traveler in the travelers list
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
            def from_country_code(reader):
                from_country_code = [traveler['country']]

        def medical_advisory_country(reader):
            # read from_country_code
            #  from_data = traveler['from']  # assume From data is provided.
            from_country = {traveler['from']}  # put from_country data into a list.
            from_country_code = {traveler['country']}

        #4-b. Get 'via' country code, if exists.
        if "via" in traveler:
            #  via_data =  traveler['via']
            via_country = traveler['via']["country"]
            #via_country_code = via_country['country']
        else:
            via_country = ""

        if not is_countries_cleared(countries_list, traveler["from"]["country"], via_country):
            # This traveler should be sent to Quarantine as the 'from' country or 'via' country has
            print(traveler["from"]["country"], via_country)
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
                home_country = traveler['home']
                if home_country['country'] != "KAN":
                    # home country is not KAN. Get entry_reason and check if any visa is required.
                    entry_reason = traveler['entry_reason']
                    if 'visa' in traveler.keys():
                        visa = traveler['visa']
                        visa_date = visa['date']
                        # all dates are in YYYY-MM-DD format.

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

    # The below calls the json file to be read
    with open(input_file, "r") as file_reader:
        file_contents_input_file = file_reader.read()
        travelers_info = json.loads(file_contents_input_file)
        #travelers_list = [travelers_info]
        # print(travelers_list)
        #return travelers_list
        return travelers_info


def import_watchlist_json(watchlist_file):
    """
    Imports watchlist data from JSON file.
    :param watchlist_file:
    :return: List with watchlist info.
    """

    with open(watchlist_file, "r") as file_reader:
        file_contents_watchlist = file_reader.read()
        watchlist_info = json.loads(file_contents_watchlist)
        return watchlist_info


def watchlist_file(import_watchlist_json, watchlist_list):
    for line in import_watchlist_json(watchlist_file):
        line = line.strip()
        if line != "-":
            import_watchlist_json.len = str(line[:-1])
        if watchlist_file.len > str(line[:0]):
            # we want to print the line that is longer than a certain amount because it has content thus an alert len
            # function
            print(line)
            # Thus this would return a line that would have the name or passport number of the person on the watchlist


def import_countries_json(countries_file):
    """
    Imports countries data from json file to use it for validation.
    :param countries_file:
    :return: List with countries data.
    """

    with open(countries_file, "r") as file_reader:
        file_contents_countries = file_reader.read()
        countries_info = json.loads(file_contents_countries)
        #countries_list = [countries_info]
        #return countries_list
        return countries_info


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
    if "passport" not in traveler.keys() or "first_name" not in traveler.keys() or "last_name" not in traveler.keys() \
            or "entry_reason" not in traveler.keys() or "birth_date" not in traveler.keys() or "home" not in \
            traveler.keys()  or "from" not in traveler.keys():
        return False
    else:
        return True


def is_countries_cleared(countries_list, from_country, via_country):
    """
    Checks if 'from' or 'via' country has medical advisory.
    :param countries_list: list of countries.
    :param from_country:
    :param via_country:
    :return: Boolean True if medical advisory is cleared, False otherwise.
    """
    # Check from country.
    if countries_list[from_country]["medical_advisory"] != "":
        return False

    elif via_country != "":
        if countries_list[via_country]["medical_advisory"] != "":
            return False
        else:
            return True

    else:
        return True


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
    # check the last_name of people on watchlist

    for entry_in_watchlist in watchlist_list:
        if passport_number == entry_in_watchlist["passport"] or \
                (first_name == entry_in_watchlist["first_name"] and last_name == entry_in_watchlist["last_name"]):
            return False
    return True


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


def valid_passport_format(passport_number):
    # Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    """
    :param passport_number: alpha-numeric string

    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('^.{5}-.{5}-.{5}-.{5}-.{5}$')

    if passport_format.match(passport_number):
        return True
    else:
        return False


