from bs4 import BeautifulSoup as bs
import webbrowser as web

import requests
from pprint import pprint
import json








data=requests.get("https://collegedunia.com/bangalore-colleges").text

soup=bs(data,'html.parser')


main_div=soup.find('div',class_="row listing-block-cont js-scrolling-container")

all_div=main_div.find_all('div',class_='listing-block')


# pprint(all_div)

link_list= []
clg_info=[]  #this is for making a list of collage information

# sr_no = 0


for div in all_div:
	top_block_class = div.find('div',class_='top-block')
	college_name_adress_class = div.find('div',class_='clg-name-address')
	college_link=college_name_adress_class.find('a')['href']
	link_list.append(college_link)

# print(link_list)


clg_name=[]
clg_url=[]
clg_type=[]
clg_esd=[]
clg_ratings=[]
img_url=[]
location=[]


for i in link_list:
	b=(requests.get(i)).text

	# main div for next page 

	soup2=bs(b,'html.parser')
	main_div2=(soup2.find('div',class_="college_top_wrapper"))



	# div for image 
	img_div=(main_div2.find('img',class_="img-resposnsive bg-college"))['src']
	# pprint(img_div)
	# break

	img_url.append(img_div)

# 	# college information

	clg_info_div=main_div2.find('div',class_="container-fluid wrapper-top").find('div',class_="college_data")

# 	# college name

	clg_name_div=clg_info_div.find('h1',class_="college_name").text
	# print (clg_name_div)
	# break

	clg_name.append(clg_name_div)


# 	# extra information of college

	more_info_div=(clg_info_div.find('div',class_="extra_info"))
	# pprint(more_info_div)
	# break

	info_=[]

	for inl in more_info_div:
		p=(inl.text).strip()
		
		if len(info_)<=3:
			info_.append(p)
		else:
			break
	# 	print (info_)
	# break
	location.append((info_[0]))
	clg_type.append(info_[1])

	clg_esd.append((info_[2]))


	# print(location)
	# print(clg_type)
	# print(clg_esd)

	# break

	
	for  no in range(len(clg_name)):
		main_dict={}

		main_dict['college_name']=clg_name[no]
		main_dict['college_type']=clg_type[no]
		main_dict['clg_esd']=clg_esd[no]
		# main_dict['clg_url']=clg_url[no]
		main_dict['img_url']=img_url[no]
		main_dict['location']=location[no]
		clg_info.append(main_dict)

with open ('bangolre_clg.json','w')as l:
	json.dump(clg_info,l)

	print ("done")




