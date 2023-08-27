import os
import PIL.Image

def resize_imgs(org_folder, resized_folder, name):
    i = 1
    for file in os.listdir(org_folder):
        img = PIL.Image.open(os.path.join(org_folder, file))
        img = img.resize((300,300))
        if img.mode == "RGBA":
            img = img.convert("RGB")
        img.save(os.path.join(resized_folder, name+str(i)+".jpg"))
        i += 1
        
if __name__ == "__main__":
    resize_imgs("ai_imgs", "ai_resized", "ai_imgs_")
    resize_imgs("real_imgs", "real_resized", "real_imgs_")
