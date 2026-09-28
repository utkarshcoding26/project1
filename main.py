totalfinalterm_marks=70            #final exams
UT_marks=20                         #unit test
CT=10                               #class test
Totalterms=3
totalsections=5
print("total students in a batch :",12)
print("passing criteria out of 70 is 30")
print("compulsorily pass in maths and computer ")
print("compulsorily pass in all subjects in third term")
print("no passing criteria in unit test and class test")
print("no passing criteria in first and second term except maths and computer")
print("compulsorily passing marks in third term")
print("section a contains 2 students")
print("section b contains 2 students")
print("section c contains 3 students")
print("section d contains 2 students")
print("section e contains 3 students")
section_a_names=['utkarsh agarwal','akash b']               
section_b_names=['anmol garg','shivam a']
section_c_names=['udhav g','mahesh s','sanchit t']
section_d_names=['shivam d','shivam gupta']
section_e_names=['vedant k','akash gupta','aarav goyal']     
totaldays_each_term=80
seventypercent_80=56
print("candidate must fulfill attendance criteria")
def UTmarks_CTmarks_finalmarks1_attendance():                 # function for evaluating marks,status,attendance
    attend=int(input("no of days attended"))
    if(attend>=56):
            if(attend<=80 and attend>=70):
                    print(j,":criteria fullfilled and 'A' grade for attendance")
            elif(attend<=70 and attend >=60):
                    print(j,":criteria fullfilled and 'B' grade for attendance")
            elif(attend<=60 and attend>=56):
                    print(j,":criteria fullfilled and 'c' grade for attendance")
                    
            ut1=float(input("enter maths ut marks"))
            ut2=float(input("enter computer ut marks"))
            ut3=float(input("enter english ut marks"))
            ut4=float(input("enter science ut marks"))
            ut5=float(input("enter EVS ut marks"))
            ct1=float(input(" enter maths ct marks"))
            ct2=float(input(" enter computer ct marks"))
            ct3=float(input(" enter english ct marks"))
            ct4=float(input(" enter science ct marks"))
            ct5=float(input(" enter EVS ct marks"))
            m1=float(input("enter maths final marks"))
            m2=float(input("enter computer final marks"))
            m3=float(input("enter english final marks"))
            m4=float(input("enter science final marks"))
            m5=float(input("enter EVS final marks"))
            global c1                 # for count of number of students passed
            global c2                 # for count of number of students failed
            global status1
            if(m1+ut1+ct1>=45 and m2+ut2+ct2>=45 and m1>=30 and m2>=30):
             
             print(j,":passed in the term")
             status1="passed" 
             c1+=1
             
            else:
             c2+=1
             status1="failed"
             print(j,":failed in the term")
            percentage_term=(m1+m2+m3+m4+m5+ut1+ut2+ut3+ut4+ut5+ct1+ct2+ct3+ct4+ct5)/500*100        #for calculating percentage
            print(j,end=":")
            print(percentage_term,end="")
            print("%") 
    else:
            print(j,"disqualified for exams and failed in the term")
            c2+=1
        
c1=0
c2=0
for j in section_a_names:                 #  loop to work for every student 
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section a :",c1)
print("number of students failed in section a:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_b_names:                 #  loop to work for every student 
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section b :",c1)
print("number of students failed in section b:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_c_names:                #  loop to work for every student 
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section c:",c1)
print("number of students failed in section c:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0 
for j in section_d_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section d :",c1)
print("number of students failed in section d:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_e_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section e :",c1)
print("number of students failed in section e:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
print("second term started")
c1=0
c2=0
for j in section_a_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section a :",c1)
print("number of students failed in section a:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_b_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section b :",c1)
print("number of students failed in section b:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_c_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section c:",c1)
print("number of students failed in section c:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_d_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section d :",c1)
print("number of students failed in section d:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_e_names:
          UTmarks_CTmarks_finalmarks1_attendance()
print("number of students passed in section e :",c1)
print("number of students failed in section e:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
print("third term started")
def UTmarks_CTmarks_finalmarks3_attendance():             #function for third term marks,status,attendance
    attend=int(input("no of days attended"))
    if(attend>=56):
                if(attend<=80 and attend>=70):
                        print(j,":criteria fullfilled and 'A' grade for attendance")
                elif(attend<=70 and attend >=60):
                        print(j,":criteria fullfilled and 'B' grade for attendance")
                elif(attend<=60 and attend>=56):
                        print(j,":criteria fullfilled and 'c' grade for attendance")

                ut1=float(input("enter maths ut marks"))
                ut2=float(input("enter computer ut marks"))
                ut3=float(input("enter english ut marks"))
                ut4=float(input("enter science ut marks"))
                ut5=float(input("enter EVS ut marks"))
                ct1=float(input(" enter maths ct marks"))
                ct2=float(input(" enter computer ct marks"))
                ct3=float(input(" enter english ct marks"))
                ct4=float(input(" enter science ct marks"))
                ct5=float(input(" enter EVS ct marks"))
                m1=float(input("enter maths final marks"))
                m2=float(input("enter computer final marks"))
                m3=float(input("enter english final marks"))
                m4=float(input("enter science final marks"))
                m5=float(input("enter EVS final marks"))
                global c1
                global c2
                global status3
                if(m1+ut1+ct1>=45 and m2+ut2+ct2>=45 and m1>=30 and m2>=30 and m3+ut3+ct3>=45 and m4+ut4+ct4>=45 and m3>=30 and m4>=30 and m5+ut5+ct5>=45 and m5>=30):
                 print(j,":passed in third term") 
                 status3="passed"
                 c1+=1
                else:
                        print(j,":failed in third term and has to repeat a year")
                        status3="failed"
                        c2+=1
                percentage_term3=(m1+m2+m3+m4+m5+ut1+ut2+ut3+ut4+ut5+ct1+ct2+ct3+ct4+ct5)/500*100
                print(j,end=":")
                print(percentage_term3,end="")
                print("%")
    else:
            print(j,"disqualified and has to repeat a year")
            c2+=1
c1=0
c2=0
for j in section_a_names:
          UTmarks_CTmarks_finalmarks3_attendance()
print("number of students passed in section a :",c1)
print("number of students failed in section a and has to repeat the year:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_b_names:
          UTmarks_CTmarks_finalmarks3_attendance()
print("number of students passed in section b :",c1)
print("number of students failed in section b and has to repeat a year:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_c_names:
          UTmarks_CTmarks_finalmarks3_attendance()
print("number of students passed in section c:",c1)
print("number of students failed in section c and has to repeat a year:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
c1=0
c2=0
for j in section_d_names:
          UTmarks_CTmarks_finalmarks3_attendance()
print("number of students passed in section d :",c1)
print("number of students failed in section d and has to repeat a year:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure")
c1=0
c2=0
for j in section_e_names:
          UTmarks_CTmarks_finalmarks3_attendance()
print("number of students passed in section e :",c1)
print("number of students failed in section e and has to repeat a year:",c2)
if(c1>c2):
        print("academic excellence class")
elif(c1<=c2):
        print("academic failure class")
print("grades entering and remarks evaluation for discipline,punctuality and responsibility")
def grades():                        #function for evaluating grades and remarks
        print("discipline remarks")
        graded=input("enter grade of discipline")
        if(graded=='A'):
                print(g,"discipline",end=":")
                print("excellent")
        elif(graded=='B'):
                print(g,"discipline",end=":")
                print("good")
        elif(graded=='C'):
                print(g,"discipline",end=":")
                print("bad")
        elif(graded=='F'):
                print(g,"discipline",end=":")
                print("fail")
        print("punctuality remarks")
        gradep=input("enter grade of punctuality")
        if(gradep=='A'):
                        print(g,"punctuality",end=":")
                        print("excellent")
        elif(gradep=='B'):
                        print(g,"punctuality",end=":")
                        print("good")
        elif(gradep=='C'):
                        print(g,"punctuality",end=":")
                        print("bad")
        elif(gradep=='F'):
                        print(g,"punctuality",end=":")
                        print("fail")
        print("responsibility remarks")
        grader=input("enter grade of responsibility")
        if(grader=='A'):
                         print(g,"responsibility",end=":")
                         print("excellent")
        elif(grader=='B'):
                         print(g,"responsibility",end=":")
                         print("good")
        elif(grader=='C'):
                         print(g,"responsibility",end=":")
                         print("bad")
        elif(grader=='F'):
                         print(g,"responsibility",end=":")
                         print("fail")
for g in section_a_names:
         grades()
for g in section_b_names:
        grades()
for g in section_c_names:
        grades()
for g in section_d_names:
        grades()
for g in section_e_names:
        grades()
        
         



                
        



 






        




          

        


        




    


    









    
    

    
    
    
    
    

