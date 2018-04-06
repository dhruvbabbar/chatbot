
def print_date():
    
        from datetime import date
        import holidays
        mydict={}
        
        for name,date in sorted(holidays.US(state='CA', years=2017).items()):   
                date_string = name.strftime('%Y-%m-%d')
                mydict[date_string]=date
        return mydict
print_date()