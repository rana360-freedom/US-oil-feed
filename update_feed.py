import datetime
from xml.etree import ElementTree as ET
import sys

# Detect if it's a weekly run (we'll pass "weekly" from GitHub Actions)
is_weekly = "weekly" in sys.argv

# Load feed.xml
tree = ET.parse("feed.xml")
root = tree.getroot()
channel = root.find("channel")

now = datetime.datetime.utcnow()
pub_date = now.strftime("%a, %d %b %Y %H:%M:%S +0000")

if is_weekly:
    title = "Weekly Summary - " + now.strftime("%b %d, %Y")
    desc = "This is the weekly U.S. oil summary. Prices, inventories, OPEC+, and supply shocks wrapped up."
    guid = "weekly-" + now.strftime("%Y-%m-%d")
else:
    title = "Daily Update - " + now.strftime("%b %d, %Y")
    desc = "This is the daily U.S. oil update. Prices and inventories in focus, OPEC+ news, and supply trends."
    guid = "daily-" + now.strftime("%Y-%m-%d")

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

# Save
tree.write("feed.xml", encoding="utf-8", xml_declaration=True)
