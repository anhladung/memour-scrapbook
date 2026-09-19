import os
import shutil

src = r"C:\Users\TTC\.gemini\antigravity\brain\112fcc6e-6c30-411f-b2af-bf6b159f6a07\.user_uploaded\media_1787803945461.png"
dest_dir = os.path.join(r"C:\Users\TTC\Documents\scrapbook-genz\static\assets")
os.makedirs(dest_dir, exist_ok=True)

dest_logo = os.path.join(dest_dir, "logo.png")
shutil.copy2(src, dest_logo)
print(f"Copied {src} to {dest_logo} ({os.path.getsize(dest_logo)} bytes)")
