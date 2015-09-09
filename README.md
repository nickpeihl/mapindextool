
#Map Index Tool for ArcGIS Desktop Version 10+

The Map Index Tool creates a geographic index of all ArcMap documents (MXDs) in a folder supplied by the user. For each MXD, the tool finds the largest dataframe on the Layout view and sends the extent of that dataframe to a shapefile in the folder (map_index.shp). Tested on ArcGIS Desktop version 10. Not tested and likely not working on ArcGIS Desktop versions 9.3.1 and below.

##WARNING

This tool will destroy and overwrite any shapefile named map_index within the supplied folder. Please use with caution.

##Features

- Create shapefile of the extent of each ArcMap document (MXD) in a supplied folder
- Includes several properties of each MXD such as:
  - Title
  - Author
  - Path to file
  - Last date the map was saved
  - Last date the Map Index Tool was run 

NOTE: If the MXD being indexed was last opened and saved using ArcMap 9.3.1 or lower, the Last Save Date will not be available and will be blank in the table. The Title and Author fields come from the fields in Map Document Properties from the File menu in ArcMap.

## License
Copyright 2015 Nick Peihl

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

