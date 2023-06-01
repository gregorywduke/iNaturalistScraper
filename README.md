# iNaturalistScraper
Desktop application that downloads images from a list of image urls contained in an "Export Observations" CSV file from iNaturalist. Written in Python, this scraper uses PySimpleGUI and comes packaged in an executable. If you need to compile a dataset of nature images, this is the tool to use. 

To Use, Follow these Steps:
1. Visit the "Export Observations" page on iNaturalist.org, and select your desired parameters.
2. Before exporting your observations, make sure you unselect ALL options in (Section 3, Choose Columns) EXCEPT "image_url". That should be the only option enabled.
3. Export your observations and download the .csv provided.
4. Check the .csv you downloaded. Make sure there is no text besides the urls present. If there is a first line that is NOT a URL, delete it. 
5. Download iNaturalistScraper v1.0.0 from the "Releases" section, and run the .exe. 
6. In the application, select the .csv file you downloaded. Select the folder you want your images to be deposited. 
7. Click "Proceed" and let the program download your images. Upwards of 500 images may take 5-10 minutes. More images will take longer, though the process is CPU-dependant. 

Notes: (PLEASE READ)
- Ensure you delete the first line, if it is not a URL. 
- Ensure you ONLY select the "image_url" option in Export Observations, and no other option. 
