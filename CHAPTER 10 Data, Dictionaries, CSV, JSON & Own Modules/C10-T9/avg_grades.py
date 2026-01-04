import csv

def avg_grades(path):
    file = open(path)
    reader = csv.reader(file)
    
    subjects = {}
    first_row = True
    
    for row in reader:
        if first_row:
            first_row = False
            continue
        subject = row[2]
        grade = float(row[3])
        
        if subject not in subjects:
            subjects[subject] = {'sum': 0, 'count': 0}
        
        subjects[subject]['sum'] += grade
        subjects[subject]['count'] += 1
    
    file.close()
    
    result = {}
    for subject, data in subjects.items():
        avg = data['sum'] / data['count']
        result[subject] = round(avg, 2)
    
    return result
#print(avg_grades("sample.csv"))
