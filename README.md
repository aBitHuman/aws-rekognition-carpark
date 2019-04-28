
Utilising AWS rekognition to recognise carparks from aerial photography.  Including scripts to create labelled datasets from polygon feature classes and WMS aerial web services.

Our aim is to use existing spatial data from other open data providers to train ML models.
These ML models can then be applied to other aerial photography from other locations to identify the same features.

## The Source Data
We will use open data from the City of Melbourne, Australia and Victorian open data aerial image services.
For Aerial Imagery for the Melbourne region we will use this WMS web service, to create the labeled datasets.
https://base.maps.vic.gov.au/wms?request=getcapabilities

To identify car parks in Melbourne, we will be using the melbourne carpark web service, but will need to format into GeoJSON centroids.
https://data.melbourne.vic.gov.au/Transport-Movement/On-street-Parking-Bays/crvt-b4kt 