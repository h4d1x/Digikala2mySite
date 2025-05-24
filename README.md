
```plaintext
                                 |\    /|
                              ___| \,,/_/
                           ---__/ \/    \
                          __--/     (D)  \
                          _ -/    (_      \
                         // /       \_ /  -\
   __-------_____--___--/           / \_ O o)
  /                                 /   \__/
 /                                 /
||          )                   \_/\
||         /              _      /  |
| |      /--______      ___\    /\  :
| /   __-  - _/   ------    |  |   \ \
 |   -  -   /                | |     \ )
 |  |   -  |                 | )     | |
  | |    | |                 | |    | |
  | |    < |                 | |   |_/
  < |    /__\                <  \
  /__\                       /___\
Boj4ckHoor3man 🐴 
```

This script takes product images (e.g., from Digikala), removes their backgrounds, and places them into a user-defined background and watermark template — making them ready for use on the user's own website or store.

🧠 Background Removal Model
Uses the isnet-general-use model from the rembg package for cleaner edge detection.

```

Step 1: Download the Model
To download the model, visit the following link:
https://huggingface.co/ClockZinc/IS-NET_pth/resolve/main/isnet-general-use.pth

Step 2: Save the Model File
Save the downloaded file to the following path:

C:\Users\BojackHors3man\.u2net\u2net.onnx

Troubleshooting
If the .u2net folder does not exist:
You can manually create it by going to C:\Users\BojackHors3man\ and creating a new folder named .u2net.

```


🧾 Sample Output Structure
Input:

Any product image (JPG, PNG, WEBP, etc.)

Output:

A .png file with transparent watermark and custom background.

Example file: product_01.png

📁 How to Use
Run the script — it opens file dialogs to:

Select the input folder (with products images)
Choose an output folder
Pick a background image
Choose a watermark image

The script will:

Enhance contrast
Remove the background
Composite the image over your Selected background
Add watermark 

Save the final .png images in the Selected output folder


📌 Customization
Margin from edges:

```
margin = 50  # pixels

```

Watermark position: Currently fixed at (0, 0) (top-left).

Contrast enhancement:

```
enhancer.enhance(2.0)  # Increase for higher contrast

```

Ensure your background and watermark are .png files with transparency.

Images are resized proportionally to fit inside the background with margins.




Boj4ckHoor3man 🐴
chasing clarity.
They Never Have Dark mode for this Xd
