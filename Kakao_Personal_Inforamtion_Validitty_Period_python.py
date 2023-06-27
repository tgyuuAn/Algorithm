def solution(today, terms, privacies):
    answer = []
    dic = dict()

    today_year, today_month, today_date = map(int,today.split("."))
    
    for term in terms:
        term_type, month = term.split()
        dic[term_type] = int(month)
    
    for idx,privacy in enumerate(privacies):

        date, term_type = privacy.split()
        year, month, date = map(int,date.split("."))
        month += dic[term_type]
    
        date -= 1
        
        if date<=0:
            date += 28
            month -= 1
        
        if month > 12:
            year_gap, month_gap = divmod(month,12)
            year += year_gap
            month = month_gap
        
        if month<=0:
            month += 12
            year -= 1
            
        if today_year < year:
            continue
        
        elif today_year > year:
            answer.append(idx+1)
            continue
            
        elif today_year == year:
            if today_month < month:
                continue
                
            elif today_month > month:
                answer.append(idx+1)
                continue
            
            elif today_month == month:
                if today_date <= date:
                    continue
                
                elif today_date > date:
                    answer.append(idx+1)
                    continue
    
    return answer