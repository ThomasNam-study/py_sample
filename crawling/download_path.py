import urllib.request as req

img_url = 'https://lh3.googleusercontent.com/proxy/z2_CX8ouxmxNQeng1cFcKWOdsqetcDvt-lgts_Spx29Z9enqajrgC7EQIOMK2Ebb_zZCC2ndAuqBQO_dh8xSI6FP_AkrHaemS3F588gYNQZc3xqR7slwmPLu2OqdsgbS3b1E49IUlCD2KRHN6FVTeNmztdkzbQXE4NZPX55hFuk'
html_url = 'http://www.google.com'

save_path_1 = 'test1.jpg'
save_path_2 = 'test1.html'

try:
    file1, header1 = req.urlretrieve(img_url, save_path_1)
    file2, header2 = req.urlretrieve(html_url, save_path_2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    print(header1)
    print(header2)