import praw
import requests


class RedditInterface:
    """
    Interfaces with PRAW to grab data from the Reddit API.
    """

    def __init__(self):
        self.reddit = praw.Reddit(
            client_id="D3kUCpTjpSa8Ww",
            client_secret="D7EgRxsECLr84hMAzZNWaS5HOSKC5g",
            password="De03090309",
            user_agent="Grabs images.",
            username="inunsmart",
        )

    def grab_images(self, subreddit, images):
        """
        Grabs images from a subreddit.

        subreddit: The subreddit to grab images from.
        images: The number of images to grab.

        Returns: A list of images.
        """
        imageData = []

        # Get hot images from the subreddit, use images * 20 to get more images than specified,
        # since not every post is an image, (max allowed by API is 1000).
        for post in self.reddit.subreddit(subreddit).hot(
                limit=max(images * 20, 1000)):
            if post.url.endswith(".jpg") or post.url.endswith(".png"):
                # make a get request to get image bytes
                data = requests.get(post.url).content

                imageData.append(data)

                print(
                    f"Grabbed image from {post.url} ({len(imageData)}/{images})"
                )

                # if we have enough images, break
                if len(imageData) == images:
                    break

        return imageData