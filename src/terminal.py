########################################################################################
# File       : terminal.py
# Author     : Devin Arena
# Description: A simple terminal interface for displaying pictures as ASCII art.
# Since      : 6/19/2022
########################################################################################

from reddit_interface import RedditInterface
from image_handler import ImageHandler
import os
import sys
import random


def main(args):
    """
    Main function.
    """
    if len(args) != 2:
        print("Reddit ASCII image grabber v1.0")
        print("Created by Devin Arena, MIT License\n")
        print("Usage: python terminal.py <subreddit> [<number of images>]\n")
        return
    if not args[1].isdigit():
        print("Invalid number of images.")
        return

    subreddit = args[0]
    images = int(args[1])

    # Create an instance of the Reddit interface.
    reddit = RedditInterface()
    # Create an instance of the image handler.
    handler = ImageHandler()

    # Grab images from the subreddit.
    print(f"Grabbing image from r/{subreddit}...")
    images = reddit.grab_images(subreddit, images)

    # Convert each image to ASCII art.
    print("Converting images to ASCII art...")
    if images:
        os.system("clear")
        for image in images:
            print(handler.convert_image_to_ascii(image))
            print("\n\n\n")


if __name__ == "__main__":
    main(sys.argv[1:])