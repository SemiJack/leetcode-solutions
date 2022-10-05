class Solution:
    # 01.01.1971 - friday
    def dayOfTheWeek(day: int, month: int, year: int): 
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        y = 1971

        years = year - y
        leapYears = 0
        while y < year:
            if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)):
                leapYears = leapYears + 1
            y=y+1
        days = (leapYears * 366) + ((years - leapYears) * 365)
        
        m = 0
        days = days + sum(months[:(month-1)]) + day - 1
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))and (month > 2):
            days = days + 1
       
if __name__ == '__main__':
    test = Solution 
    
    test.dayOfTheWeek(31,8,2019)
    test.dayOfTheWeek(18,7,1999)
    test.dayOfTheWeek(15,8,1993)
    test.dayOfTheWeek(29,2,2016)
    