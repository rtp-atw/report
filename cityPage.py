import csv
import json

with open("data-1537331912509.csv") as f:

    datas = []
    review = [{
        "img":"",
        "rating" :5,
        "feedback":"",
        "customer_name":""
    }]
    city =[]
    current_year_month = '20174'

    for line in f:
        splitted = line.split(",")
        data = {}
        seo = []
        if len(splitted) == 5 :
            seo.append(splitted[1])
            seo.append(splitted[2])
            data["id"] = splitted[3].lower()
            for x in data:
                data["id"] = data["id"].replace(' ',"-")
            data["name"] = splitted[4]
        else:
            seo.append(splitted[1])
            data["id"] = splitted[2].lower()
            for x in data:
                data["id"] = data["id"].replace(' ',"-")
            data["name"] = splitted[3]

        data["city_id"] = ""
        data["main_text"] = "Content"
        json.dumps(data)
        data["seo"] = seo
        data["review"] = review
        city.append(data)
        print(data)

    with open("output.csv", "wt") as f:
        writer = csv.writer(f)
        writer(city)

