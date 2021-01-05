import os


class HandleMsg:
    def __init__(self):
        self.method = None
        self.url = None
        self.edition = None
        self.data_dict = {}
        self.body = None

        self.file_path = ''
        self.send_main = ''
        self.send_url = ''
        self.send_edition = ''
        self.send_body = ''
        self.send_data_str = ''
        self.send_state = [' 200 ok\r\n', ' 404 not_found\r\n']

    def handle(self, msg):
        message, self.body = msg.split(r'\r\n\r\n', 1)
        request_line_list = message.split(r'\r\n')[0].split(' ')
        request_head_list = message.split(r'\r\n')[1:]
        self.method = request_line_list[0]
        self.url = request_line_list[1]
        self.send_main = self.edition = self.send_edition = request_line_list[2]
        for it in request_head_list:
            key, value = it.split(':', 1)
            self.data_dict[key] = value
        if request_line_list[0] == 'POST':
            self.posthandle()
        elif request_line_list[0] == 'GET':
            self.gethandle()
        else:
            pass
        return self.send_main

    def posthandle(self):
        self.file_path = '/index.html'
        with open('./meg.txt', 'a') as f:
            f.write('\n' + self.body)
        with open('.' + self.file_path, 'r') as f:
            self.send_body = f.read()
        self.send_main = self.send_edition + self.send_state[1] + self.send_data_str + '\r\n' + str(self.send_body)

    def gethandle(self):
        if len(self.url) == 1:
            self.file_path = '/index.html'
        elif '?' in self.url:
            self.file_path = self.url.split('?', 1)[0]
        elif '#' in self.url:
            self.file_path = self.url.split('#', 1)[0]
        else:
            self.file_path = self.url
        if not os.path.isfile('.' + self.file_path):
            self.send_data_str += 'Content-Type: text/html; charset=utf-8\r\n'
            self.send_main = self.send_edition + self.send_state[1] + self.send_data_str + '\r\n' + str(self.send_body)
        else:
            back_name = os.path.splitext(self.file_path)[1]
            if back_name == '.html':
                with open('.' + self.file_path, 'r') as f:
                    self.send_body = f.read()
                self.send_data_str += 'Content-Type: text/html; charset=utf-8\r\n'
                self.send_main = self.send_edition + self.send_state[0] + self.send_data_str + '\r\n' + self.send_body
            elif back_name == '.jpg':
                with open('.' + self.file_path, 'rb') as f:
                    self.send_body = f.read()
                self.send_data_str += 'Content-Type: img/jpg\r\n'
                self.send_main = bytes(self.send_edition + self.send_state[0] + self.send_data_str +
                                       '\r\n', encoding='utf-8') + self.send_body