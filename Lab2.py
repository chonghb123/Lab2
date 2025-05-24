def display_main_menu():
    print("display_main_menu")
def calc_average(temp):
    total=sum(temp)
    ave = total/len(temp)
    return ave

def get_user_input():
    number = input("How many inputs do you want to enter?")
    temp = []
    for i in range(int(number)):
        temp.append(float(input("Input: ")))
    return temp
def find_min_max(temp):
    mintemp = min(temp)
    maxtemp = max(temp)
    min_max = []
    min_max.append(mintemp)
    min_max.append(maxtemp)
    return min_max

def sort_temperature(temp):
    
    return sorted(temp)

def calc_median_temperature(sorted):
  
    number = float(len(sorted))
    if number % 2 ==0:

        return sorted[int(number/2)-1], sorted[int(number/2)]
    else: 
        return sorted[int(number/2)]

def main():
    x = get_user_input()
    calc_average(x)
    find_min_max(x)
    y = sort_temperature(x)
    print(calc_median_temperature(y))


if __name__ == "__main__":
    main()
    
          