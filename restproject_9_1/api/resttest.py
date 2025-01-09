import requests

BASE_URL="http://localhost:8000/"
END_POINT="createstudent/"

rollno=int(input("Enter Rollno "))
name=input("Enter Name ")
course=input("Enter Course ")
fee=float(input("Enter Fee "))
stud_data={'rollno':rollno,
          'name':name,
          'course':course,
          'fee':fee}

response=requests.post(BASE_URL+END_POINT,data=stud_data)
statuscode=response.status_code
if statuscode==200:
    print(response.json())
else:
    print(response.json())
    
