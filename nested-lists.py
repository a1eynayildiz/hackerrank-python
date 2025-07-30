
# Ne isteniyor?
# - Öğrenci isimleri ve notları var
# - İKİNCİ en düşük nota sahip öğrencilerin isimlerini yazdır
# - Birden fazla öğrenci varsa alfabetik sırayla

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
    students.append([name, score])
    
    scores = [student[1] for student in students]
    unique_scores = sorted(set(scores))
    second_lowest = unique_scores[1]
    result = []
    for student in students:
        if student[1] == second_lowest:
            result.append(student[0])  
    
   
    result.sort()
    for name in result:
        print(name)
        
        
