import requests
import re
import PySimpleGUI as sg


# 主程序， 爬取有道翻译
def chengxu(qew):
  url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
  key = qew
  formdata = {
  "i": key,
  "from": "AUTO",
  "to": "AUTO",
  "smartresult": "dict",
  "client": "fanyideskweb",
  "salt": "16112233040580",
  "sign": "40739706fc6c6aa920b3b480edbcad03",
  "lts": "1611223304058",
  "bv": "7ed82d8c4f6f875a004e4a5e63dcf728",
  "doctype": "json",
  "version": "2.1",
  "keyfrom": "fanyi.web",
  "action": "FY_BY_REALTlME"
}

  header = {
    "UserAgent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
}


  response = requests.post(url, headers = header, data=formdata).text
  resp = r'"tgt":"(.*?)"}]]}'
  end = re.findall(resp, response)
  return end[0]
  # return end
  # tuxing(end)
#   该函数用作创建图形界面与用户交互




#
#chengxu("你好")

def tuxing():
    data = sg.theme_list()
    list1 = ["2018四级", "2019四级", "2020四级", "2021四级"]
    list2 = ["2018六级", "2019六级", "2020六级", "2021六级"]
    layout = [
            # [sg.Listbox(data, size=(10,30))],
            [sg.T("请输入要翻译的内容:", size=(20, 1), text_color="blue", font=("宋体", 21)), sg.T("各年英语考试宝典", font=('黑体', 22),
                                                                                        text_color="#FF0080")],
            [sg.InputText(key='use', size=(40, 1)), sg.Listbox(list1, key='i', size=(30, 4), bind_return_key=False, no_scrollbar=True,)],
            [sg.InputText(key='vis', visible=False, default_text=" ")],

            [sg.Button("确认", size=(40, 1), font=("宋体", 10), bind_return_key=True), sg.Button("切换到六级"), sg.B("切换到四级")]
        ]
    window = sg.Window("翻译器", layout)
    sg.theme('DarkRed2')

    while True:
        event, values = window.read()
        # lol = chengxu(qew=str(values['use']))

        if event == None:
                break
        if event == '确认':
            if str(values['use']) == "":
                sg.popup("请重新输入")
            else:
                lol = chengxu(qew=str(values['use']))
            # sg.popup(lol)
                window['vis'].update(visible=True, value=lol)
                continue
        if event == "切换到六级":
            window['i'].update(values=list2)
            # window["切换到六级"].update(text="切换到四级")
        if event =="切换到四级":
            window['i'].update(values=list1)
        # if event == "切换到四级":
        #     window['i'].update(values=list1)
        #     window["切换到四级"].update(text="切换到六级")
            # window['user'].update(
            #     values=lol
            # )
            # window("liu").update(
            #     text="切换到四级"
            #  )

    window.close()
tuxing()
#     def chengxu(self):
#         url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
#         key = self.provice
#         formdata = {
#             "i": key,
#             "from": "AUTO",
#             "to": "AUTO",
#             "smartresult": "dict",
#             "client": "fanyideskweb",
#             "salt": "16112233040580",
#             "sign": "40739706fc6c6aa920b3b480edbcad03",
#             "lts": "1611223304058",
#             "bv": "7ed82d8c4f6f875a004e4a5e63dcf728",
#             "doctype": "json",
#             "version": "2.1",
#             "keyfrom": "fanyi.web",
#             "action": "FY_BY_REALTlME"
#         }
#
#         header = {
#             "UserAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
#         }
#
#         response = requests.post(url, headers=header, data=formdata).text
#         resp = r'"tgt":"(.*?)"}]]}'
#         self.end = re.findall(resp, response)
#
# Dog()