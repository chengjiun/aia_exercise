import xml.etree.ElementTree as ET
import pandas as pd

# convert XML to dataframe (assumes only one layer of nesting)
def xml2df(xml_data):
    root = ET.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    df = pd.DataFrame(all_records)

    # how to make datetimes from unix epoch ints
    df['CreatedTimestamp'] = pd.to_datetime(df['CreatedDate'], unit='s')
    df['ModifiedTimestamp'] = pd.to_datetime(df['ModifiedDate'], unit='s')

    return df