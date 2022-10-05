class Solution:
    def minCostOld(colors, neededTime) -> int:
        time = 0
        n = len(colors)
        m=0
        while m < n-1:
            print("wsk",m)
            skok = 0
            for i in range(m,n-1):
                if colors[m] == colors[i+1]:
                    if neededTime[m] < neededTime[i+1]:
                        time = time + neededTime[m]
                        print("usuwam wskaznik",m)
                        break
                    else:
                        time = time + neededTime[i+1]
                        print("usuwam nastepny duplikat",i+1)
                        i = i+1
                        skok = skok+1
                else:
                    break
            m = m +1 +skok


        print(time)
        return time

    def minCost(colors, neededTime) -> int:
        time = 0
    
        start = 0
        end = 0
        while(start < len(neededTime) and end < len(neededTime)):
            sumtime = 0
            maxtime = 0
            while(end < len(neededTime) and start < len(neededTime) and colors[start] == colors[end]):
                maxtime = max(maxtime, neededTime[end])
                sumtime = sumtime +  neededTime[end]
                end = end+1
            time = time + sumtime - maxtime    
            start = end
        print(time)
        return time

if __name__ == '__main__':
    test = Solution
    test.minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1])
    test.minCost("abc", [1,2,3])
    test.minCost("aabaa",[1,2,3,4,1])
    

