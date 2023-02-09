class Solution:
    def reformatDate(self, date: str) -> str:
        lst=date.split(" ")
        months={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        finalDate=[]
        for i in range(len(lst)):
            if i==0:
                day=""
                if len(lst[i])>3:
                    day=lst[i][:2]
                else:
                    day="0"+lst[i][:1]
                finalDate.append(day)
            elif i==1:
                finalDate.append(months[lst[i]])
            else:
                finalDate.append(lst[i])
        finalDate.reverse()
        return "-".join(finalDate)