import sys
import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  

import unittest
from runner.mountain import Mountain

        


class koanHandler(PatternMatchingEventHandler):
  """A simple pattern event for .py files"""
  patterns = ["*.py"]

  def process(self,event):
    Mountain().walk_the_path(sys.argv)

  def on_modified(self,event):
    self.process(event)

  def on_created(self,event):
    self.process(event)

if __name__ == '__main__':

  args = sys.argv[1:]
  observer = Observer()
  observer.schedule(koanHandler(), path=args[0] if args else '.',recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
      observer.stop()

  observer.join()