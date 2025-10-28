""""
document juniors url for different filters
make a hashmap for each type of filter
define what you want to output, maybe link to external website
basic url = https://www.juniors.ro/jobs
vechime anunt: + /data:ultimele-24h,-3-zile,-7-zile,ultima-luna
pozitie : + /tip-job:  
    Job == 100
    Internship == 200
    Intern == 300
    Trainee == 400
    Pre-Employment == 500
    Bootcamp == 600
    Academy == 650
remote: + /remote:1
experienta: + /experienta:
    fara == 100
    0-1 == 200
    >1 == 300

search filter : +?q=... at the end
"""
import sys
import bs4
import requests

if __name__== "__main__":
    url="https://www.juniors.ro/jobs"
    print("Enter values separated by ','")
    search=input("Search filter : ")
    vechime_anunt=input("Vechime anunt in zile (1 / 3 / 7 / 30) : ")
    pozitie=input("Pozitie (Job / Internship / Intern / Trainee / Pre-Employment / Bootcamp / Academy) : ")
    remote=input("Remote (1 / 0) : ")
    experienta=input("Experienta (fara / 0-1 / >1) : ")

    # vechime
    match vechime_anunt:
        case "1": url = url + "/data:ultimele-24h"
        case "3": url = url + "/data:ultimele-3-zile"
        case "7": url = url + "/data:ultimele-7-zile"
        case "30": url = url + "/data:ultima-luna"

    #remote
    if remote=="1":
        url = url + "/remote:1"

    #pozitie
    values=pozitie.split(",") if pozitie.strip()!="" else []
    if values : url = url + "/tip-job:"
    for x in values:
        match x:
            case "Job": url=url+"100"
            case "Internship": url = url + "200"
            case "Intern": url = url + "300"
            case "Trainee": url = url + "400"
            case "Pre-Employment": url = url + "500"
            case "Bootcamp": url = url + "600"
            case "Academy": url = url + "650"
        url = url + ","
    url=url.rstrip(",")
    
    #experienta
    match experienta:
        case "fara": url = url + "/experienta:100"
        case "0-1": url = url + "/experienta:200"
        case ">1": url = url + "/experienta:300"
    #search filter
    if search.strip()!="":
        url = url + "?q=" + search.replace(" ","+")

    web_response = requests.get(url)
    soup = bs4.BeautifulSoup(web_response.content,'html.parser')
    jobs = soup.select("li.job",None,7)
    for i,job in enumerate(jobs):
        company = job.find("ul",class_="job_requirements").find("strong").next_sibling.strip()
        job_title = job.find("div",class_="job_header_title").find("h3").text.strip()
        locatie_data = job.find("div",class_="job_header_title").find("strong").text.strip()
        location=locatie_data.split("|")[0].strip()
        post_date=locatie_data.split("|")[1].strip()
        techs = [a.get_text(strip=True) for a in job.select("ul.job_tags li a")]
        technologies =", ".join(techs)
        print(f"{i+1}.")
        print(f"Job title = {job_title}")
        print(f"Company name = {company}")
        print(f"Location = {location}")
        print(f"Technologies = {technologies}")
        print(f"Post date = {post_date}")
        print()


       