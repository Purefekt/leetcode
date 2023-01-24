"""
Use a hashmap for the followers. The key will be followerId and value will be a hashset of all followeeIds
Use an hashmap for tweets.
postTweet -> Append the (time, tweetId) to the value of the key userId. Then decrement the time. This is to use a maxheap later
follow -> add the followeeId to the set of followerId
unfollow -> if followerId exits in follower hashmap and if followeeId exists in the followerId hashset, use set.remove() to remove
getNewsFeed -> get the set of valid users, which is the user itself and the set of followees. Then use the hashmap tweets to get a list of valid tweets by combining all lists. Heapify this to turn it into a maxheap. the smallest time (largest negative time) will be the most recent tweet. Pop from the heap till heap exists or we reach 10 tweets.

O(n) time where n is the number of total tweets in the system. This is for getNewFeed. In the worst case it is same as using stack but in average case the heapify function will use less than that time since it will run on a smaller subset of tweets. The other methods run in O(1) time
O(n) space to store n tweets. O(n) to store the followers hashmap as well
"""

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = [(self.time, tweetId)]
        else:
            self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # valid users
        valid_users = set([userId])
        if userId in self.followers:
            valid_users = valid_users.union(self.followers[userId])
        
        # get all the tweets from the valid_users
        valid_tweets = []
        for valid_user in valid_users:
            if valid_user in self.tweets:
                valid_tweets.extend(self.tweets[valid_user])
        
        # use a maxheap to get the 10 most freq tweets
        heapq.heapify(valid_tweets)
        res = []
        while len(res)<10 and valid_tweets:
            _, tweetId = heapq.heappop(valid_tweets)
            res.append(tweetId)
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set([followeeId])
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)

        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)