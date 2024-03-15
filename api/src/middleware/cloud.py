import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
load_dotenv()

def handleFileActions(img):
 try :
    print("testing ",img)
    img_file=cloudinary.uploader.upload(img['avatar'],folder="syndex_media_host")['secure_url']
    print("src",img_file)
    return img_file
 except Exception as e:
   return False 