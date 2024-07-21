# 4475_Project1: Photo Mosaic

**Developed by Noah Flanagan, Annarose Hilhorst, Dylan Paige, and Maxine Spencer**


Run with
python transformers.py image_path output_path size_H size_W -pixel_scale scale

* image_path is a string giving the relative path to the image file to take as input

* output_path is a string giving the relative path where the program will write the output image

* size_H is an int giving the height of sections of the final mosaic

* size_W is an int giving the width of sections of the final mosaic

* scale is an int giving the resolution scale for the final mosaic. For example, a 600x400 image processed with a scale of 2 will output as 1200x800. This can help preserve detail but can also make the filesize of the output rather large


This example command gives the following result: 

python transformers.py HTML_CS4475_P1/mosaic-wall.jpg HTML_CS4475_P1/output_final_mosaic.jpg 15 10 -scale 5

Input Image            |  Output Image
:-------------------------:|:-------------------------:
<img src="HTML_CS4475_P1/mosaic-wall.jpg" width="500"> |  <img src="HTML_CS4475_P1/output_final_mosaic.jpg" width="500">

