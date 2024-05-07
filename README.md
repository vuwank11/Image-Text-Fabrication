# Text-Fabrication
This repository is about the Data Fabrication Technique to generate a variations in character numbers and symbols are necessary. For this, a blank image is used as the canvas, and the text fonts are loaded. Random characters are generated from these loaded fonts in the batch code format. By randomly arranging the batch code positions from horizontal and vertical and applying random rotation angles, this technique generates a high degree of randomization. As a result, a variety of data are used to make the both text detection and recognition model more generalized and robust.

Process of data fabrication:

1) Image Rotation
 1) To rotate the image "draw_rotated_text" function is used.   First we take the height and width of the input image, then calculates the maximum dimension of the image( either height or width) this is done to create a enough space to rotate the text without being cut off at the edges in transparency mask.

 2) Create a transparency mask in which all its pixels are set to transparent, which means their values are set to 0

 3) Creates a drawing object on the transparency mask using the ImageDraw.Draw() method. This object provides various methods for drawing shapes, lines, and text onto an image.

 4) Draws the text on the transparency mask at a specific position with white color (255). The text will appear as white against the transparent background because white color text will be clearly visible and easily separable from the background when blended onto the final image.

 5) If the angle is a multiple of 90 degrees, it directly rotates the transparency mask by that angle. This is a straightforward operation and can be done without much distortion. Otherwise, it enlarges the mask, rotates it, and then resizes it back to the original size to minimize distortion. 
    a) First, it enlarges the transparency mask by a factor of 8 in both dimensions. This enlargement provides more detail for the rotation operation and helps minimize distortion.
    b) Rotates the enlarged mask by the desired angle. This rotation operation is performed on the enlarged mask, which helps preserve the text's quality.
    c) After rotating, the code resizes the mask back to its original size using a high-quality resampling method (Image.LANCZOS). This resizing operation restores the mask to its original dimensions while retaining the benefits of the rotation and enlargement steps.

6) Calculates the bounding box for the rotated mask to match the size of the input image.

7) Now crops the rotated mask to match the size of the input image.

8) Creates a new image filled with the specified color and transparency.

9) Pastes this color-filled image onto the original input image using the cropped rotated mask as a transparency mask.

10) Finally, it returns the modified image with the text drawn at the specified angle.

