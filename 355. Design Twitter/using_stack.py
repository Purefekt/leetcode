"""
Use a hashmap for the followers. The key will be followerId and value will be a hashset of all followeeIds
Use an stack for tweets.
postTweet -> simply append the userId, tweetId to the stack
follow -> add the followeeId to the set of followerId
unfollow -> if followerId exits in follower hashmap and if followeeId exists in the followerId hashset, use set.remove() to remove
getNewsFeed -> get the set of valid users, which is the user itself and the set of followees. Run a loop till either get have 10 tweets or we have gone through all tweets. Start from the end of the array (top of stack) and check the userId, if it exists in the valid users set, append it to the tweets.

O(n) time where n is the number of total tweets in the system. This is for getNewFeed. The other methods run in O(1) time
O(n) space to store n tweets. O(n) to store the followers hashmap as well
"""

class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId)) 

    def getNewsFeed(self, userId: int) -> List[int]:
        # valid users
        valid_users = set([userId])
        if userId in self.followers:
            valid_users = valid_users.union(self.followers[userId])
        
        all_tweets = self.tweets.copy()
        this_tweets = []
        while len(this_tweets) < 10 and all_tweets:
            userId, tweetId = all_tweets.pop()
            if userId in valid_users:
                this_tweets.append(tweetId)
        return this_tweets     

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