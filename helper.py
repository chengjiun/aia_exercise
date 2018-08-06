import xml.etree.ElementTree as ET
import pandas as pd


def read_files2df(files):
    df = pd.DataFrame()
    for f in files:
        record = read_xmlfile2dict(f)
        sr = pd.Series(record, name=f)
        df = df.append(sr)
    return df
    
def read_xmlfile2dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # print(xml_file, flush=True)
    record={
        'image_size_width': int(root.find('size').find('width').text),
        'image_size_height': int(root.find('size').find('height').text),
        'image_size_depth': int(root.find('size').find('depth').text),
        'op_defect_name': root.find('object').find('name').text,
        'subfolder': root.find('folder').text,
        'real_subfolder': xml_file.split('/')[-2],
        'pose': root.find('object').find('pose').text,
        'xmin': root.find('object').find('bndbox').find('xmin').text,
        'xmax': root.find('object').find('bndbox').find('xmax').text,
        'ymin': root.find('object').find('bndbox').find('ymin').text,
        'ymax': root.find('object').find('bndbox').find('xmax').text,
        'path': str(xml_file).split('/')[5],
        'label': str(xml_file).split('/')[7],
    }
    return record