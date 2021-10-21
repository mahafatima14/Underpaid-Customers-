log_file = open("um-server-01.txt")


#define the funtion
def sales_reports(log_file):
    """Print the Monday sales report from the file um-server-01.txt""" 
    
    #go through each line of code in log_file
    for line in log_file:
        #remove all extra whitespace at the end of each sentence
        line = line.rstrip() 
        day = line[0:3] #assign the variable day to the first three characters in the line
        #if day is "mon", we print those lines 
        if day == "Mon":
            print(line)

#call the function sales report and pass in the file "log files"
sales_reports(log_file)