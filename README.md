A minimalistic python package to read image data and image metadata from Olympus .oir image files.
The image data is output as multidimensional numpy array.
The metadata is output as Dictionary.

Installation:

-pip install oirFileReader

Quickstart usage:

from oirFileReader import oirFileReader

ofr = oirFileReader.OirFileReader("YourFile.oir")

imageContent = ofr.getImagePixels()  #outputs as multitimensional numpy array with dimensions [channels, z, x, y]
fullMetaDataList = ofr.getImageMetadataList() #outputs image metadata as list of dictionaries
