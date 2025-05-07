
def calculate_bmi(height, weight):
    print("Height=",height)
    print("Weight= ",weight)
    bmi = weight/(height*height) 
    print("bmi " ,bmi)

    return bmi

def classify_bmi(bmi):
    if(bmi < 18.5):
         return -1
    elif(bmi >= 18.5 and bmi <=25 ):
        return 0
    else:
        return 1
    

def app(): 
    output=calculate_bmi(1.78,105)
    print(classify_bmi(output))
    return

if __name__ == "_main_":
    app()

app()