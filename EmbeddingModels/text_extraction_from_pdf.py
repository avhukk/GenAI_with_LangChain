import os 
import fitz

doc = fitz.open(os.path.join("/home/sysad/Documents/Study/GenAI_with_LangChain/main.pdf"))

with open("output.txt", "w", encoding= "utf-8") as f:
    for page_num in range(len(doc)): 
        page = doc.load_page(page_num)
        text = page.get_text()

        #The page heading 
        f.write(f"--- Page {page_num +1} --- \n")

        # Write page text 
        f.write(text)

        # Add some separation between pages
        f.write("\n\n")
doc.close()
print("Text extracted successfully")