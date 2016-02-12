import urllib
import re

if __name__ == '__main__':
    mainurl = 'http://web.stanford.edu/class/cs224w/'
    htmlurl = mainurl + 'projects.html'
    utfHtml = urllib.urlopen(htmlurl).read()
    # unicodeHtml = html.decode("utf-8")
    # . can match \n
    matchPdfs = re.findall(r'<li><a href=.*?2015/(.*?)\'>(.*?)</a></li>', utfHtml, re.S)
    for pdf in matchPdfs:
        print('project name is:\n%s\n link is:\n%s' %(pdf[1], pdf[0]))
        f = open(pdf[0], 'wb')
        f.write(urllib.urlopen(mainurl + 'projects_2015/' + pdf[0]).read())
        f.close()
