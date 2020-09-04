import requests

headers = {'Content-Type':'text/xml'}



#c_no = "1138656537"
#c_no = "5112200104"
c_no = "1111111111"

xml = "<map id='ATTABZAA001R08'><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>" + c_no + "</txprDscmNo><dongCode>05</dongCode><psbSearch>Y</psbSearch><map id='userReqInfoVO'/></map>"


r = requests.post('https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId=', data=xml, headers=headers)
#
# # 상태 코드
print(r.status_code)
print(r.text)
