# GeMS-GIS-SetID-
A series of scripts and models for QGIS for populating the _ID field

These models simplify adding the values for the _ID field. Currently a separate model
needs to be run for each feature class. If anyone knows how to iterate over a database 
using the graphical modeler, please reach out. 

The model/script will create a new field called _ID and adds the unique ID there.
The field calculator in the graphical modeler can only add a new field, not update one.
