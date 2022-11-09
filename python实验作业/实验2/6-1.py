aslist=[['01','yi'],['02','er'],['03','san'],['04','si'],['05','wu'],
['06','liu'],['07','qi'],['08','ba'],['09','jiu'],['10','shi'],
['11','shiyi'],['12','shier'],['13','shisan'],['14','shisi'],['15','shiwu'],
['16','shiliu'],['17','shiqi'],['18','shiba'],['19','shijiu'],['20','ershi'],]
import math
searchlist=[aslist[i][0] for i in range(0,20)]
data=int(input('请输入学号:'))
def bisearch(data,searchlist):
    left=0
    right=len(aslist)-1
    while left<=right:
        mid=left+math.ceil((right-left)/2)
        if data==int(searchlist[mid]):
            return aslist[mid]
        elif data<int(searchlist[mid]):
            right=mid-1
        else:
            left=mid+1
    return '没有找到' 
print(bisearch(data,searchlist))