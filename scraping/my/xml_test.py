import xml.etree.ElementTree as elemTree

# xmlStr = """
# <map id='' >
#     <map id='resultMsg' >
#         <detailMsg></detailMsg>
#         <msg></msg>
#         <code></code>
#         <result>S</result>
#     </map>
#     <trtEndCd>Y</trtEndCd>
#     <smpcBmanEnglTrtCntn>The business registration number is registered</smpcBmanEnglTrtCntn>
#     <nrgtTxprYn>N</nrgtTxprYn>
#     <smpcBmanTrtCntn>등록되어 있는 사업자등록번호 입니다. </smpcBmanTrtCntn>
#     <trtCntn>부가가치세 일반과세자 입니다.</trtCntn>
# </map>"""

# xmlStr = """
# <map id='' >
#     <map id='resultMsg' >
#         <detailMsg></detailMsg>
#         <msg></msg><code></code>
#         <result>S</result>
#     </map>
#
#     <trtEndCd>Y</trtEndCd>
#     <smpcBmanEnglTrtCntn>The business registration number is not registered(date of closure: 2017-12-31)</smpcBmanEnglTrtCntn>
#     <nrgtTxprYn>N</nrgtTxprYn>
#     <smpcBmanTrtCntn>등록되어 있지 않은 사업자등록번호 입니다. (폐업일자: 2017-12-31)</smpcBmanTrtCntn>
#     <trtCntn>폐업자 (과세유형: 부가가치세 일반과세자, 폐업일자:2017-12-31) 입니다.&#xa;* 과세유형 전환된 날짜는 2017년 10월 01일 입니다.</trtCntn>
#     </map>
# """

xmlStr = """
<map id='' >
    <map id='resultMsg' >
        <detailMsg></detailMsg>
        <msg></msg>
        <code></code>
        <result>S</result>
    </map>
    <trtEndCd>Y</trtEndCd>
    <smpcBmanEnglTrtCntn>The business registration number is not registered</smpcBmanEnglTrtCntn>
    <nrgtTxprYn>Y</nrgtTxprYn>
    <smpcBmanTrtCntn>등록되어 있지 않은 사업자등록번호 입니다. </smpcBmanTrtCntn>
    <trtCntn>사업을 하지 않고 있습니다.</trtCntn>
</map>
"""

tree = elemTree.fromstring(xmlStr)

#datas = tree.find('./nrgtTxprYn')
#print(datas.text)

datas = tree.find('./trtEndCd')
print(datas.text)

datas = tree.find('./smpcBmanTrtCntn')

print(datas.text)

datas = tree.find('./trtCntn')

print(datas.text)