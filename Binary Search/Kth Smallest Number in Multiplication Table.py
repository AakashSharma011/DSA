def findKthNumber(self, m, n, k):
        low=1
        high=m*n
        while low<=high:
            mid=low+(high-low)//2
            row=m
            count=0
            col=1
            while row>=1 and col<=n:
                if row*col <=mid:
                    count+=row
                    col+=1
                else:
                    row-=1
            if count <k:
                low=mid+1
            else:
                high=mid-1
        return low