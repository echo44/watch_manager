import funks
import socket
import pyinotify
import time
import os

loop, ip, port = funks.get_args()
sock = socket.socket()
sock.connect((ip, port))

class MyEventHandler(pyinotify.ProcessEvent):
    """Хранит функции по обработке событий"""
    def process_IN_ACCESS(self, event):
        """Получен доступ к файлу"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_ACCESS event:" + event.pathname + " temp file"
            else:
                report = "IN_ACCESS event: " + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_ACCESS event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_ATTRIB(self, event):
        """Метаданные файла изменены"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_ATTRIB event:" + event.pathname + " temp file"
            else:
                report = "IN_ATTRIB event: " + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_ATTRIB event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_CLOSE_NOWRITE(self, event):
        """Файл открытый без права записи закрыт"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_CLOSE NOWRITE event:" + event.pathname + " temp file"
            else:
                report = "IN_CLOSE NOWRITE event: " + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_CLOSE NOWRITE event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_CLOSE_WRITE(self, event):
        """Файл открытый на запись закрыт"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_CLOSE WRITE event:" + event.pathname + " temp file"
            else:
                report = "IN_CLOSE WRITE event: " + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_CLOSE WRITE event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_CREATE(self, event):
        """Создан файл/папка"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_CREATE event:" + event.pathname + " temp file"
            else:
                report = "IN_CREATE event:" + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_CREATE event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_DELETE(self, event):
        """Файл/папка удалена"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_DELETE event:" + event.pathname + " temp file"
            else:
                report = "IN_DELETE event:" + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_DELETE event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_MODIFY(self, event):
        """Файл изменен"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_MODIFY event:" + event.pathname + " temp file"
            else:
                report = "IN_MODIFY event: " + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_MODIFY event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)

    def process_IN_OPEN(self, event):
        """Файл открыт"""
        try:
            way = str(event.pathname)
            if ".swp" in way:
                report = "IN_OPEN event:" + event.pathname + " temp file"
            else:
                report = "IN_OPEN event: " + event.pathname + " " + str(os.path.getsize(event.pathname))
        except FileNotFoundError:
            report = "IN_OPEN event:" + event.pathname + " temp file"
        finally:
            msg = report.encode("utf-8")
            sock.send(msg)
            time.sleep(loop)
