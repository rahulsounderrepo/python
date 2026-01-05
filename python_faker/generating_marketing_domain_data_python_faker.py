from faker import Faker # This Imports the Faker library which helps us to generate fake data
import random # It provides multiple methods which helps us to generate random numbers and select random elements
import xml.etree.ElementTree as ET # This Library is used for Building and Manipulating XML Structures
from xml.dom import minidom # This library Beautify/Prettify the XML Output, Making it more readable

# Initialize Faker
fake = Faker() # It creates a faker object (fake) which helps us to generate Random data (Names, Phrases, etc)

def generate_campaign_data(num_campaigns): # This function helps to generate campaign data, Also has a input parameter (num_campaigns) where we define how many campaign we need to generate
    campaigns = [] # It initialize an empty list to store all campaign data
    for i in range(1, num_campaigns + 1): # This will help us to loop the number of times mentioned in the parameter (num_campaigns) to create multiple campaign entries
        campaign = {
            "id": f"{i:03}", # Creates a zero-padded campaign ID
            "name": fake.catch_phrase(), # It generates a random marketing phrase for the campaign name
            "start_date": fake.date_between(start_date="-30d", end_date="today").strftime("%Y-%m-%d"), # date_between - Picks up a date between a specified range
            "end_date": fake.date_between(start_date="today", end_date="+30d").strftime("%Y-%m-%d"), # strftime formats the date as YYYY-MM-DD
            "metrics": {
                "clicks": random.randint(1000, 5000), # randint will generare a random Integer value
                "impressions": random.randint(20000, 100000),
                "ctr": round(random.uniform(1.0, 10.0), 2) # It will give you the random floating point number between 1.0 to 10.0 and also rounds of the value with two decimal points
            },
            "channels": [
                {"name": fake.random_element(elements=["Email", "TV", "Social Media", "SMS", "Billboard","Whatsapp"]), "budget": random.randint(1000, 20000)} # It randomly selects the channel name
                for _ in range(random.randint(2, 5))  # Randomly choose 2-5 channels
            ]
        }
        campaigns.append(campaign)
    return campaigns

#generate_campaign_data(100)

# Function to create XML from data
def create_xml(campaigns): # This function will help you to convert the campaign list data into XML Data
    root = ET.Element("campaigns") # It Creates the Root XML Element named <campaigns>
    
    for campaign in campaigns: # It iterates through the list of campaigns to add their data to XML elements
        campaign_elem = ET.SubElement(root, "campaign") # This Creates a Child XML Element <campaign> under <campaigns>
        ET.SubElement(campaign_elem, "id").text = campaign["id"] # Sets the text of each sub-element with the corresponding value from the list of campaign dictionary
        ET.SubElement(campaign_elem, "name").text = campaign["name"]
        ET.SubElement(campaign_elem, "start_date").text = campaign["start_date"]
        ET.SubElement(campaign_elem, "end_date").text = campaign["end_date"]
        
        metrics_elem = ET.SubElement(campaign_elem, "metrics") # This Creates a Child XML Element <metrics> under <campaign>
        ET.SubElement(metrics_elem, "clicks").text = str(campaign["metrics"]["clicks"]) # We are creating sub-elements and setting values for clicks, Impressions and ctr
        ET.SubElement(metrics_elem, "impressions").text = str(campaign["metrics"]["impressions"])
        ET.SubElement(metrics_elem, "ctr").text = str(campaign["metrics"]["ctr"])
        
        channels_elem = ET.SubElement(campaign_elem, "channels") # This Creates a Child XML Element <channels> under <campaign>
        for channel in campaign["channels"]:
            channel_elem = ET.SubElement(channels_elem, "channel") # This Creates a Child XML Element <channel> under <channels>
            ET.SubElement(channel_elem, "name").text = channel["name"] # We are creating sub-elements and setting values for name and budget
            ET.SubElement(channel_elem, "budget").text = str(channel["budget"])
    
    # Prettify the XML
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ") # It converts the XML Root to a String, It prettify using the minidom
    return xml_str

# Generate sample data and save as XML

# Adjust this to generate more or fewer campaigns
num_campaigns = 9999 

campaign_data = generate_campaign_data(num_campaigns)
xml_output = create_xml(campaign_data)
output_file_path = '/content/sample_data/XML_Output_Data/9999_big_data_xml_marketing_campaign.xml'

with open(output_file_path,"w") as f:
    f.write(xml_output)
	

# Reading the Big Data - XML File using Python and PySpark

import xml.etree.ElementTree as ET
import pandas as pd

file_path = '/content/sample_data/XML_Output_Data/9999_big_data_xml_marketing_campaign.xml'

def parse_nested_xml(file_path_param):
    tree = ET.parse(file_path_param)
    root = tree.getroot()

    list_with_entire_data = []

    for campaign in root.findall('campaign'):
        id = campaign.find('id').text
        name = campaign.find('name').text
        start_date = campaign.find('start_date').text
        end_date = campaign.find('end_date').text

        #print(id,name,start_date,end_date,clicks)

        # We are Parsing the Metrics as a Dictionary
        metrics = {"clicks": campaign.find('metrics/clicks').text,\
                   "impressions": campaign.find('metrics/impressions').text,\
                   "ctr": campaign.find('metrics/ctr').text,}
        #print(metrics)


        channels = []
        for channel in campaign.findall('channels/channel'):
            channels.append({"name": channel.find('name').text,\
                             "budget": channel.find('budget').text,})

        #print(channels)

        list_with_entire_data.append({"id":id,"name":name,"start_date":start_date,\
                              "end_date":end_date,"metrics":metrics,"channels":channels})
    
    return list_with_entire_data

big_data_xml_result_mc = parse_nested_xml(file_path)
print(type(big_data_xml_result_mc))
print(big_data_xml_result_mc)