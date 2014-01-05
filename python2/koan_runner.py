import os
import sys
import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  

import unittest

class koanHandler(PatternMatchingEventHandler):
  """A simple pattern event for .py files"""
  patterns = ["*.py"]

  def process(self,event):
    print event.src_path
    os.system("python contemplate_koans.py")
  def on_modified(self,event):
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