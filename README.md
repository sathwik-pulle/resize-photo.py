Make sure the output folder exists

If the folder where we’ll save the new images doesn’t exist, create it.

Go through every file in the input folder

Look at each file inside the input folder.

If it’s not a file (like a subfolder), skip it.

Open the image

Use with Image.open(...) so that when we’re done, the file closes automatically.

Resize it

Shrink the image so it fits inside the given width and height, without stretching it.

Handle transparency if saving as JPEG

JPEGs don’t support transparent areas.

If the image has transparency, change it to a normal RGB image so it can be saved.

Save it with a new name and format

Change the file extension to match the format (like .jpeg, .png).

Save the resized image in the output folder.

Show progress

Print a message each time an image is saved.

If there’s a problem

If the image can’t be opened or saved, show an error but keep going with the rest.
