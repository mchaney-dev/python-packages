# handles HTTP methods
import requests
# html/xml parser
from bs4 import BeautifulSoup
# handles OS routines
import os
# support for type hints
import typing
# garbage collection
import gc
# interpreter interaction
import sys
# memory profiler
from memory_profiler import profile
# time-related functions
import time


all_instances = []
gc.enable()


class ErrorHandler:
    def __init__(self):
        self.PROTECTED_VAR = UserWarning()
        


class Scraper(ErrorHandler):
    def __init__(self):
        self.instance = None
        self.index = None
        self.pid = None
        self.status = None
        
        self.attributes = {
            'instance': self.instance,
            'index': self.index,
            'pid': self.pid,
            'status': self.status
        }
        
        def __new_instance__():
            value = len(all_instances) + 1
            return value
            
        def __new_index__():
            value = len(all_instances) - 1
            return value
        
        def __new_object__():
            self.instance = __new_instance__()
            self.attributes.update({'instance': self.instance})
            all_instances.append(self.instance)
            
            self.index = __new_index__()
            self.attributes.update({'index': self.index})
            
            self.queue = queue()
            self.track = track()
            self.attributes.update({'queue': self.queue.list})
                
        __new_object__()
        
    def __protect_vars__(self, *args):
        name = ['instance', 'index', 'status']
        reference = [self.instance, self.index, self.status]
        
        try:
            for item in name:
                if ((args == item)):
                    raise RuntimeError()
                    break
                else:
                    for key, value in self.attributes:
                        for item in reference:
                            if ((args == item) or (args == value)):
                                raise RuntimeError()
                                break
        except Exception():
            return 1
        else:
            return 0
    
    def get_attr(self, name: str):
        value = self.__getattribute__(name)
        return value
    
    def __update_attr__(self, name: str, new_value):
        self.attributes.update({name: new_value})
    
    def set_attr(self, name: str, new_value):
        try:
            self.__protect_vars__(name, new_value)
        except Exception():
            exit(1)
        else:
            new_value = self.__setattr__(name, new_value)
            self.__update_attr__(name, new_value)
            return new_value
    
    def del_attr(self, name: str):
        if ((name != 'instance') and (name != 'index')):
            self.__delattr__(name)
            self.attributes.__delitem__(name)
            print('attribute ' + name + ' deleted')


class track(Scraper):
    def __init__(self):
        self.root = None
        self.current_page = None
        self.allowed_list = []
        
    def new(self, url: str, parse_type: str, raw_content: bool):
        def parse(url: str, parse_type: str, raw_content: bool):
            obj = requests.get(url)
            
            def perms_helper(obj):
                for key in obj.headers.keys():
                    key = key.lower()
                    if (key == 'set-cookie'):
                        cookie_jar = obj.headers.get(key)
                        cookie_jar = cookie_jar.split('; ')
                        break
                        return cookie_jar
                    else:
                        return None
                    
            def parse_robots(jar):
                for item in jar:
                    if (item.find('domain') != -1):
                        item = item.split('=')
                        break
                    if (item[1].find('www') == -1):
                        self.root = 'http://www' + str(item[1])
                        full_url = str(self.root) + '/robots.txt'
                        perms = requests.get(full_url)
                        perms = perms.text.split('\n')
                        perms.remove('User-agent: *')
                        for line in perms:
                            if (line.startswith('Allow:')):
                                query = line.strip('Allow: ')
                                query = query.strip()
                                self.allowed_list.append(query)
                            elif (line.startswith('User-agent')):
                                break
            
            if (perms_helper(obj) is not None):
                jar = perms_helper(obj)
                parse_robots(jar)
            elif (parse_type == 'html'):
                parser = 'html.parser'
            elif (parse_type == 'xml'):
                parser = 'xml.parser'
                
            if (raw_content is True):
                return obj
            else:
                text_content = obj.text
                soup = BeautifulSoup(text_content, parser)
                return soup
        result = parse(url, parse_type, raw_content)
        self.current_page = url
        return result


class queue(Scraper):
    def __init__(self):
        self.list = []
        
    def add(self, url):
        self.list.append(url)
        
    def remove(self, index):
        obj = self.list[index]
        print(str(obj) + ' deleted')
        self.list.remove(obj)
        
    def clear(self):
        print('clearing queue...')
        self.list.clear()
        
    def current_item(self):
        value = self.list[0]
        return value
    
    def next_item(self):
        value = self.list[1]
        return value

print('---DEBUG---')
print('1. instantiating multiple objects:')
test = Scraper()
print('object 1 memory location: ' + str(test))
print('object 1 attributes: ' + str(test.attributes) + '\n')
test2 = Scraper()
print('object 2 memory location: ' + str(test2))
print('object 2 attributes: ' + str(test2.attributes) + '\n')
test3 = Scraper()
print('object 3 memory location: ' + str(test3))
print('object 3 attributes: ' + str(test3.attributes) + '\n')
test4 = Scraper()
print('object 4 memory location: ' + str(test4))
print('object 4 attributes: ' + str(test4.attributes) + '\n')

print('2. retrieving object attributes with a method:')
print('object 2 instance: ' + str(test2.get_attr('instance')))
print('object 4 instance: ' + str(test4.get_attr('instance')) + '\n')

print("3. changing the value of an object's attribute:")
print('changing object 4 instance to 100')
test4.set_attr('instance', 100)
print('object 4 new instance: ' + str(test4.get_attr('instance')))
print('object 4 new attributes list: ' + str(test4.attributes) + '\n')

print('4. deleting attributes and objects:')
print('deleting object 4 instance attribute')
test4.del_attr('instance')
print('object 4 new attributes list: ' + str(test4.attributes))
print('deleting objects 2-4')
del test2
del test3
del test4

print('\n' + '5. adding an item to a queue:')
print('adding item to object 1 queue')
test.queue.add('http://www.google.com')
test.update_attr('queue', test.queue.list)
print('object 1 new attributes list: ' + str(test.attributes))
print('object 1 current queue item: ' + str(test.queue.current_item()))

print('\n' + '6. adding another queue item:')
print('adding second item to object 1 queue')
test.queue.add('http://www.yahoo.com')
test.update_attr('queue', test.queue.list)
print('object 1 new attributes list: ' + str(test.attributes))
print('object 1 next queue item: ' + str(test.queue.next_item()))

print('\n' + '7. removing first queue item:')
print('removing current queue item from object 1')
test.queue.remove(0)
test.update_attr('queue', test.queue.list)
print('object 1 new attribute list: ' + str(test.attributes))
print('object 1 new current queue item: ' + str(test.queue.current_item()))

print('\n' + '8. scraping a web page without a queue:')
page = test.scrape.new('http://www.google.com', 'html', False)
print('text extracted from web page:')
text = page.text.split('\n')
for item in text:
    item = item.strip()
    print(item)
del page
del text
del item

print('\n' + '9. scraping html title element from the current queue item:')
page = test.scrape.new(str(test.queue.current_item()), 'html', True)
print('content extracted from web page:')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('title'))
del page
del soup
