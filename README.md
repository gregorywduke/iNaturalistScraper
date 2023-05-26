# iNaturalistScraper
Desktop application that downloads list of image urls contained in an "Export Observations" CSV file from iNaturalist. Written in Python, this scraper uses PySimpleGUI and comes packaged in an executable. 

To Use, Follow these Steps:
1. Visit the "Export Observations" page on iNaturalist.org, and select your desired parameters.
2. Before exporting your observations, make sure you unselect ALL options in (Section 3, Choose Columns) EXCEPT "image_url". That should be the only option enabled.
3. Export your observations and download the .csv provided.
4. Run iNaturalistScraper.exe
5. In the application, select the .csv file you downloaded. Select the folder you want your images to be deposited. 
6. Click "Proceed" and let the program download your images. Upwards of 500 images may take 5-10 minutes. More images will take longer, though the process is CPU-dependant. 

