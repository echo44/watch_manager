
import pyinotify
import funks
import set_up


path = funks.get_path()

# создаем watch manager
watch_manager = pyinotify.WatchManager()
watch_manager.add_watch(path, pyinotify.ALL_EVENTS, rec=True)

# создаем обработчик событий
event_handler = set_up.MyEventHandler()

# запускаем отслеживание событий
notifier = pyinotify.Notifier(watch_manager, event_handler)
notifier.loop()
