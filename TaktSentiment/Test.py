import json

def getItemsRAI():
    comments = []
    with open("Hk3-RAI") as json_data:
        d = json.load(json_data)
        json_data.close()
        for i in d:
            for key in d:
                for item in d[key]:
                    print (item)
                    comments.append(item)
    return comments

if __name__ == "__main__":
    getItemsRAI()
