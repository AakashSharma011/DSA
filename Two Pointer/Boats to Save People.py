people = [1,2]
limit = 3

def numRescueBoats(self, people, limit):
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats
print(numRescueBoats(0,people, limit))