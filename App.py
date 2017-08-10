import DownloadHandler
from Image import Image

# parser = argparse.ArgumentParser(description="Download files from a sequentially repeating URL")
# parser.add_argument("-b", "--begin", help="Start of URL", required=True)
# parser.add_argument("-e", "--end", help="End of URL", required=True)
# parser.add_argument("-f", "--first", help="Start value for sequence", default=0, type=int)
# parser.add_argument("-l", "--last", help="End value for sequence", required=True, type=int)
# parser.add_argument("-p", "--pad", help="Number of padding 0's", default=1, type=int)
# parser.add_argument("-r", "--pre", help="String to prefix filename with", default="", type=str)
# parser.add_argument("-x", "--ext", help="Extension, including dot (.)", default=".jpg", type=str)
# args = vars(parser.parse_args())
#
# print(args)


prefix = "http://sssscomic.com/comicpages/"
end = ".jpg"

_images = []

for i in range(764, 769):
    _images.append(Image(prefix, i, end))

download_h = DownloadHandler.DownloadHandler()

download_h.downloadAll(_images, "Stay Still - Stay Silent - ", 3, ".jpg")
