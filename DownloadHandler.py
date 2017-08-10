import requests
import pp
import time


class DownloadHandler:

    def downloadAll(self, images, prefix, padding, extension):
        jobServer = pp.Server()
        jobs = []

        totalTime = 0
        downloadTime = 0
        writeTime = 0

        for image in images:
            jobs.append(jobServer.submit(self.download, (image, prefix, padding, extension), (), ("requests", "time")))

        for job in jobs:
            downloadTime += job()[0]
            writeTime += job()[1]
            totalTime += job()[2]

        print("Total time: "+str(totalTime)+"s.")
        print("Time spent downloading: "+str(downloadTime)+"s.")
        print("Time spent writing: "+str(writeTime)+"s.")

    def download(self, image, prefix, padding, extension):
        totalTime = time.time()
        downloadTime = 0
        writeTime = 0
        try:
            startTime = time.time()
            response = requests.get(image.url(), stream=True)
            if response.status_code == 200:
                image.content = response
                downloadTime += time.time()-startTime

                file = None
                try:
                    startTime = time.time()
                    filename = prefix + str(image.index).zfill(padding)+extension
                    file = open(filename, "wb")

                    print("Writing contents to "+filename)

                    for chunk in image.content.iter_content(1024):
                        if not chunk:
                            break

                        file.write(chunk)
                except IOError as e:
                    print ("I/O error({0}): {1}".format(e.errno, e.strerror))

                finally:
                    file.close()
                    writeTime += time.time()-startTime
            elif response.status_code == 404:
                print("ERROR 404: "+image.url())

        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            print("ERROR: Request Timed Out")

        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print("ERROR: "+image.url()+" Too many redirects.")

        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            print("BIG ERROR.")

        return (downloadTime, writeTime, time.time()-totalTime)