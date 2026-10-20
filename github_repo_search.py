import requests
import json
from pathlib import Path 

def load_json():
	try:	
		with open("repo_data.json")as file:
			data=json.load(file)
		for i in data:
			print(i["repository name"])
			print(i["owner name/repo"])					
			print(i["discription"])
			print(i["program language"])
			print(i["no.of stars"])
			print(i["no.of forks"])
			print(i["repository url"])
			print(i["creation date"])
			print()
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")
	

def save_json(repo_data):
	try:
		file_path=Path("repo_data.json")
		new_repo=repo_data
		if file_path.exists():
				with open(file_path,"r")as file:
					old_repo=json.load(file)
		else:
			old_repo=[]
		exists_data={
		repo["repository name"] for repo in old_repo
		}
		for repo in new_repo:
				if repo["repository name"] not in exists_data:
					old_repo.append(repo)
					exists_data.add(repo["repository name"])
	
		with open("repo_data.json","w")as file:
			json.dump(old_repo,file,indent=4)
		print("\nsaved successfully \n")
	
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")


def search(Lname):
	try:
		url=f"https://api.github.com/search/repositories?q={Lname}&per_page=10"
		response=requests.get(url,timeout=10)
		data=response.json()
		item=data["items"]
		count=0
		for i in item:
			if i["language"]:
				if Lname.lower()==i["language"].lower():
					name=i["name"]
					owners=i["full_name"]
					potl=i["language"]
					star=i["stargazers_count"]
					forks=i["forks_count"]
					rurl=i["html_url"]
					die=i["description"]
					date=i["created_at"]
					print(count+1)
					print(f"repository name:{name}")
					print(f"owner name/repo:{owners}")
					print(f"discription:{die}")
					print(f"program language:{potl}")
					print(f"no.of stars:{star}")
					print(f"no.of forks:{forks}")
					print(f"repository url:{rurl}")
					print(f"creation date:{date}")
					count+=1
					print()
				if count==0:
					print("language not found")
					break 
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("Unexpected data received from the API.")
				

def largest():
	try:
		url="https://api.github.com/search/repositories?q=all&per_page=10"
		response=requests.get(url,timeout=10)
		data=response.json()
		item=data["items"]
		for i in item:
			largest_repo = max(data["items"], key=lambda x: x["stargazers_count"])
		print("Largest repo:", largest_repo["name"], "with", largest_repo["stargazers_count"], "stars")

	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("Unexpected data received from the API.")

def keyword(word):
	try:
		url=f"https://api.github.com/search/repositories?q={word}&per_page=10"
		response=requests.get(url,timeout=10)
		data=response.json()
		count=0
		item=data["items"]
		repo_data=[]
		for i in item:
			name=i["name"]
			owners=i["full_name"]
			potl=i["language"]
			star=i["stargazers_count"]
			forks=i["forks_count"]
			rurl=i["html_url"]
			die=i["description"]
			date=i["created_at"]
			print(count+1)
			print(f"repository name:{name}")
			print(f"owner name/repo:{owners}")
			print(f"discription:{die}")
			print(f"program language:{potl}")
			print(f"no.of stars:{star}")
			print(f"no.of forks:{forks}")
			print(f"repository url:{rurl}")
			print(f"creation date:{date}")
			count+=1
			print()
			repo_list={"repository name":name,
			"owner name/repo":owners,
			"discription":die,
			"program language":potl,
			"no.of stars":star,
			"no.of forks":forks,
			"repository url":rurl,
			"creation date":date}
			repo_data.append(repo_list)
		return repo_data
		
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	  print("Unexpected data received from the API.")
	
			
	

def all():
	try:
		url="https://api.github.com/search/repositories?q=all&per_page=10"
		response=requests.get(url,timeout=10)
		data=response.json()
		count=0
		item=data["items"]
		for i in item:
			name=i["name"]
			owners=i["full_name"]
			potl=i["language"]
			star=i["stargazers_count"]
			forks=i["forks_count"]
			rurl=i["html_url"]
			die=i["description"]
			date=i["created_at"]
			print(count+1)
			print(f"repository name:{name}")
			print(f"owner name/repo:{owners}")
			print(f"discription:{die}")
			print(f"program language:{potl}")
			print(f"no.of stars:{star}")
			print(f"no.of forks:{forks}")
			print(f"repository url:{rurl}")
			print(f"creation date:{date}")
			count+=1
			print()
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	  print("Unexpected data received from the API.")

def mane():
    while True:
        print("===GITHUB REPOSITORY MENU===")
        print("1. Search repositories")
        print("2. Display repository details")
        print("3. Find the most starred repository")
        print("4. Filter repositories by programming language")
        print("5. Save results to JSON")
        print("6. Load saved results")
        print("7. Exit")
        a=int(input("Enter your choice:"))
        if a==7:
            print("==GITHUB REPOSITORY MENU IS CLOSED==")
            break
        elif a==2:
        	all()
        elif a==1:
        	word=input("enter keyword:")
        	result=keyword(word)
        	if result is not None:
        		repo_data=result        	
        elif a==3:
        	largest()
        elif a==4:
        	search_lang=input("enter program language:")
        	search(search_lang)
        elif a==5:
        	save_json(repo_data)
        elif a==6:
        	load_json()	                
         
mane()           
         
      