import requests
from bs4 import BeautifulSoup
import re

# List of URLs of the webpages you want to extract HTML data from
urls = ["https://professional-education-gl.mit.edu/mit-applied-data-science-course?&utm_source=Google&utm_medium=search&utm_campaign=ADSB_Int_Search_main_Phrase_EU&adgroup_id=135301101548&campaign_id=14490790962&Keyword=courses%20data%20science&placement=&gclid=Cj0KCQjw1OmoBhDXARIsAAAYGSHpc4_0jKNaT52EKbCiJs6FF6FteTIiRIfcdlQ05Squ7aRKz7rbAEgaAlk-EALw_wcB", "https://www.coursera.org/specializations/data-science?utm_medium=sem&utm_source=gg&utm_campaign=B2C_EMEA_data-science_uw_FTCOF_specializations_country-GB-country-UK&campaignid=20494103659&adgroupid=151403407126&device=c&keyword=scaler%20data%20science%20course&matchtype=b&network=g&devicemodel=&adposition=&creativeid=671145339090&hide_mobile_promo&gclid=Cj0KCQjw1OmoBhDXARIsAAAYGSFidF9eI2F-weXod98bfkNnoCX6fPa6rXzke2nJehzq1g07yugPGm8aAgbgEALw_wcB", "https://info.lewagon.com/en/data-science-course-gsa-uk?utm_adgroup=&utm_term=syllabus%20data%20science&utm_campaign=UK_%7C_United_Kingdom_%7C_EN_%7C_S_%7C_Data_Science&utm_source=google&utm_medium=cpc&hsa_acc=9887519486&hsa_cam=17795863124&hsa_grp=146284066232&hsa_ad=646724945746&hsa_src=g&hsa_tgt=aud-1887943845289:kwd-1233964679490&hsa_kw=syllabus%20data%20science&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad=1&gclid=Cj0KCQjw1OmoBhDXARIsAAAYGSHe6bJTaMQ9JyJ04b-CVphWVPd-68SFS0CzvyD_dcYiEmiED6cww9caAm-tEALw_wcB"]

# Create an empty string to store the extracted text
text_data = ""

# Iterate over each URL
for url in urls:
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Remove HTML tags and schema tags
    text = soup.get_text()
    text = re.sub(r"\[.*?\]", "", text)  # Remove schema tags
    
    # Remove leading and trailing whitespaces
    text = text.strip()
    
    # Append the extracted text to the main text_data string
    text_data += text + "\n\n"

# Save the cleaned text data as a .txt file
with open("Text.txt", "w", encoding="utf-8") as file:
    file.write(text_data)

print("HTML data extracted and saved as webpages_text.txt.")