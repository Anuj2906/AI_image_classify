import os
import PIL.Image

def rename_imgs(org_folder, renamed_folder, name):
    i = 1
    for file in os.listdir(org_folder):
        img = PIL.Image.open(os.path.join(org_folder, file))
        # img = img.resize((300,300))
        # if img.mode == "RGBA":
        #     img = img.convert("RGB")
        img.save(os.path.join(renamed_folder, name+str(i)+".jpg"))
        i += 1
        
        
if __name__ == "__main__":
    rename_imgs("real_small", "Real", "real_train")
    rename_imgs("ai_small", "AI generated", "ai_train")