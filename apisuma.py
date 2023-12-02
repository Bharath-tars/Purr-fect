import requests
# from message import details

def request_text(name,email,text):
	NAME = name
	EMAIL = email
	TEXT = text
	url = "https://text-analysis12.p.rapidapi.com/summarize-text/api/v1.1"

	payload = {
		"language": "english",
		"summary_percent": 10,
		"text": f"{TEXT}"
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "7772dc233amsh57a1b27f7c8206dp1da486jsn7987d3f048ee",
		"X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)
	data = response.json()
	message = data["msg"]
	summary = data["summary"]
	sentences = data["sentences"]
	full_data = ""
	cnt=1
	for i in sentences:
		full_data+= f"{cnt}. {i}\n"
		cnt+=1
	# details(NAME,EMAIL,message, summary, full_data)
	return message, summary, full_data
# app_version
# time_taken
# msg
# ok
# sentence_count
# summary
# sentences


