import os
import re

class Command:
    def execute_cmd_result(self,commend):
        result_list=[]
        result=os.popen(commend).readlines()
        for i in result:
            if i =='\n':
                continue
            result_list.append(i.strip('\n'))
        return  result_list

    def execute_cmd(self, commend):
        return os.popen(commend)


    def get_device(self):
        results = self.execute_cmd_result('adb devices')
        device_info = []

        if len(results) >= 2:
            for result in results:
                if 'List' in result:
                    continue
                port = str(result).split("\t")
                if port[1] == 'device':
                    device_info.append(port[0])
            return device_info[0]
        else:
            return None
