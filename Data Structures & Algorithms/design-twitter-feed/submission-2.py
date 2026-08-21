class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # list of (time, tweetId)
        self.follows = defaultdict(set) # set of followeeId
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1   

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        uIds = self.follows[userId] | {userId}

        for uId in uIds:
            tweets = self.tweets[uId]
            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                heapq.heappush(heap, (time, tweetId, uId, index))

        ans = []

        while heap and len(ans) < 10:
            time, tweetId, uId, index = heapq.heappop(heap)
            ans.append(tweetId)

            if index > 0:
                index -= 1
                time, tweetId = self.tweets[uId][index]
                heapq.heappush(heap, (time, tweetId, uId, index))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
