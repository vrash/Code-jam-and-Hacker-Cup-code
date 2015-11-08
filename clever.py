from __future__ import division
import requests
import json
''' Vrashabh -- Clever API test
'''
'''
Take a look at our sandbox API and see if you can figure out the average number of students per section: https://clever.com/developers/docs/. *
Open Ended -- Assumed per section across all districts
'''
def average_number_of_students_per_section():

	'''
	1. Declare API and Authorization mechanism
	'''
	req = 'https://api.clever.com/v1.1/districts'
	sec_req = 'https://api.clever.com/{0}/sections'
	authorize = {'Authorization':'Bearer DEMO_TOKEN'}

	'''
	2. Initialize total number of students and number of sections to 0
	'''
	totalNumberOfStudents = 0
	numberOfSections = 0

	'''
	3. Get all districts first. Then get the section API URL's from each district(Pure REST), make the call, calculate number of students and sections
	 per district and finally aggregate across all districts
	'''
	#Get all districts
	req_districts = requests.get(req, headers=authorize)
	req_districts.raise_for_status()
	urisPerDistrict = urisPerDistrict = [district['uri'] for district in json.loads(req_districts.text)['data']]
	#For URI in district, get sections, count total number of students per section and keep track of number of sections
	for uri in urisPerDistrict:
		req_sections = requests.get(sec_req.format(uri), headers=authorize)
		req_sections.raise_for_status()
		section_list = json.loads(req_sections.text)['data']
		students = sum([len(section['data']['students']) for section in section_list])
		totalNumberOfStudents = totalNumberOfStudents + students
		numberOfSections = numberOfSections + len(section_list)
	#Return average students per section across all districts
	return totalNumberOfStudents/numberOfSections


def main():
	#Clever
	clever_number = average_number_of_students_per_section()
	print(clever_number)

if __name__ == '__main__':
    main()
