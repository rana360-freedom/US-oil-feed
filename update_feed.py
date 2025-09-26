import datetime
from xml.etree import ElementTree as ET

# Load feed.xml
tree = ET.parse("feed.xml")
root = tree.getroot()
channel = root.find("channel")

# Example new summary (replace with ChatGPT output)
title = "Daily Update - " + datetime.datetime.now().strftime("%b %d, %Y")
desc = "Oil prices under pressure as OPEC+ output hike looms. U.S. inventories steady."
pub_date = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0100")
guid = "daily-" + datetime.datetime.now().strftime("%Y-%m-%d")

# Create new item
item = ET.Element("item")
ET.SubElement(item, "title").text = title
ET.SubElement(item, "description").text = desc
ET.SubElement(item, "pubDate").text = pub_date
ET.SubElement(item, "guid").text = guid

# Insert item at top
channel.insert(4, item)

# Update lastBuildDate
channel.find("lastBuildDate").text = pub_date

# Save feed.xml
tree.write("feed.xml", encoding="utf-8", xml_declaration=True)
