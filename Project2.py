from webbrowser import open as openw
import time

def my_break(break_info = None):
    """
    Function to keep track of breaks
    :param break_info: a dictionary with the following keys:
        t_break <int> default is 3
        url <string> default "https://www.youtube.com/watch?v=2vjPBrBU-TM&index=1&list=RDEMieiteXw81tMLBdKv8qkChg"
        t_sleep <int> in seconds, default = 3
    :return:
    """
    if break_info is None:
        break_info = {}
        break_info["t_breaks"] = 3
        break_info["url"] = "https://www.youtube.com/watch?v=2vjPBrBU-TM&index=1&list=RDEMieiteXw81tMLBdKv8qkChg"
        #break_info["t_sleep"] = 60 * 60 # one hour
        break_info["t_sleep"] = 3  # 3 seconds
        # TODO: test for individual keys
        # if <key> in dict

    #total_breaks = 3
    break_count = 0

    while (break_count < break_info['t_breaks']):
        #url = "https://www.youtube.com/watch?v=2vjPBrBU-TM&index=1&list=RDEMieiteXw81tMLBdKv8qkChg"
        openw(break_info['url'])
        #time.sleep(5)
        time.sleep(break_info['t_sleep'])
        break_count += 1


if __name__ == '__main__':
    info = {}
    #my_break(info)
    my_break()

