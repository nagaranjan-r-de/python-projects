class Solution(object):  
    def duplicates(self,num):
        corrected_list = []
        
        if len(num) < 1:
            print("list is empty")
                
        for i in range (len(num)):
            if num[i] not in corrected_list:
                corrected_list.append(num[i])
                
        return self.divide(corrected_list)

    def divide(self,divide_list):
        
        if len(divide_list) <= 1:
            return divide_list
        
        mid = len(divide_list) // 2
        
        left = divide_list[:mid]
        right = divide_list[mid:]
        
        left = self.divide(divide_list[:mid])
        right = self.divide(divide_list[mid:])
        
        return self.merge(left, right)

    def merge(self,left,right):#[7, 4, 5, 9, 2, 0, 3, 1]
        
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j +=1
                
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
        
        
    
number = [7,4,5,9,2,7,5,9,0,4,3,2,1,3]

sol = Solution()
print(sol.duplicates(number))
