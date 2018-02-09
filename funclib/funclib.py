import sys
import re
import os
import time
import copy
import json
import platform


if sys.version[0] != '2':
    from functools import reduce
    raw_input = input


class T(object):

    __version = 'V1.1.4'

    @staticmethod
    def info():
        keys = map(lambda x: re.sub(r'\n|\s|=', '', x[:8]), T.__info.split('T.')[1:])
        docs_vars = vars(T)
        docs_keys = map(lambda x: '_T__' + x, keys)
        docs = {}
        for key in keys:
            docs[key] = docs_vars[docs_keys[keys.index(key)]]
        return {'keys': keys, 'docs': docs}
    __info = """
===================================================================================
                                    Func-Lib
                    A data processing methods lib for Python(2/3)
-----------------------------------------------------------------------------------
                             Author: @CN-Tower
                          Create At: 2018-2-2
                          Update At: 2018-2-10
                            Version: """ + __version + """
                             GitHub: http://github.com/CN-Tower/FuncLib
-----------------------------------------------------------------------------------
                      0: T.info                 1: T.index
                      2: T.find                 3: T.filter
                      4: T.reject               5: T.reduce
                      6: T.contains             7: T.flatten
                      8: T.each                 9: T.uniq
                     10: T.drop                11: T.pluck                
                     12: T.every               13: T.some                
                     14: T.list                15: T.dump
                     16: T.size                17: T.replace
                     18: T.iscan               19: T.log
                     20: T.timer               21: T.now
                     22: T.help                23: T.xyz
===================================================================================
    """

    @staticmethod
    def index(expected, _list):
        if bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            if expected in _list:
                return _list.index(expected)
            elif isinstance(expected, dict):
                for i in range(0, len(_list)):
                    tmp_bool = True
                    for key in expected:
                        if key not in _list[i] or expected[key] != _list[i][key]:
                            tmp_bool = False
                            break
                    if tmp_bool:
                        return i
                return -1
            elif bool(expected) and 'function' in str(type(expected)):
                for i in range(0, len(_list)):
                    if expected(_list[i]):
                        return i
            return -1
        return -1
    __index = """ 
    ### T.index
        Looks through the list and returns the item index. If no match is found,
        or if list is empty, -1 will be returned.
        eg:
            from Tools import T
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]

            Jerry_idx = T.index({"name": 'Jerry'}, persons)
            Mary_idx  = T.index(lambda x: x['name'] == 'Mary', persons)

            print(Jerry_idx)  # => 1
            print(Mary_idx)   # => 2
    """

    @staticmethod
    def find(expected, _list):
        idx = T.index(expected, _list)
        if idx != -1:
            return _list[idx]
        return None
    __find = """
    ### T.find
        Looks through each value in the list, returning the first one that passes
        a truth test (predicate), or None.If no value passes the test the function
        returns as soon as it finds an acceptable element, and doesn't traverse
        the entire list.
        eg:
            from Tools import T
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]

            Jerry = T.find({"name": 'Jerry'}, persons)
            Mary  = T.find(lambda x: x['name'] == 'Mary', persons)

            print(Jerry)  # => {'age': 20, 'name': 'Jerry'}
            print(Mary)   # => {'age': 35, 'name': 'Mary'}
    """

    @staticmethod
    def filter(x):
        pass
    __filter = """"""

    @staticmethod
    def reject(expected, _list):
        index = T.index(expected, _list)
        if index != -1:
            tmp_list = copy.deepcopy(_list)
            del tmp_list[index]
            return T.reject(expected, tmp_list)
        return _list
    __reject = """
    ### T.reject
        Returns the values in list without the elements that the truth test (predicate) passes.
        The opposite of filter.
        eg:
            from Tools import T
            persons = [{"name": "Tom", "age": 12},
                       {"name": "Jerry", "age": 20},
                       {"name": "Mary", "age": 35}]

            not_Mary = T.reject({"name": "Mary"}, persons)
            adults = T.reject(lambda x: x['age'] < 18, persons)

            print(not_Mary)  # => [{"age": 12, "name": "Tom"}, {"age": 20, "name": "Jerry"}]
            print(adults)    # => [{"age": 20, "name": "Jerry"}, {"age": 35, "name": "Mary"}]
    """

    @staticmethod
    def reduce(*args):
        return reduce(*args)
    __reduce = """"""

    @staticmethod
    def contains(expected, _list):
        idx = T.index(expected, _list)
        return idx != -1
    __contains = """
    ### T.contains
        Returns true if the value is present in the list.
        eg:
            from Tools import T
            persons = [{"name": "Tom", "age": 12},
                       {"name": "Jerry", "age": 20},
                       {"name": "Mary", "age": 35}]

            is_contains_Jerry = T.contains({"name": "Jerry", "age": 12}, persons)
            is_contains_Mary = T.contains(lambda x: x['name'] == 'Mary', persons)

            print(is_contains_Jerry)  # => False
            print(is_contains_Mary)   # => True
    """

    @staticmethod
    def flatten(x):
        pass
    __flatten = """"""

    @staticmethod
    def each(x):
        pass
    __each = """"""

    @staticmethod
    def uniq(expected, _list=None):
        is_no_expected = False
        if _list is None:
            _list = expected
            is_no_expected = True
        if isinstance(_list, tuple):
            _list = list(_list)
        if bool(_list) and isinstance(_list, list):
            tmp_list = copy.deepcopy(_list)
            if is_no_expected:
                for i in range(0, len(tmp_list)):
                    if len(tmp_list) <= i + 1:
                        break
                    tmp_list = tmp_list[:i + 1] + T.reject(tmp_list[i], tmp_list[i + 1:])
            else:
                index = T.index(expected, tmp_list)
                if index != -1 and index + 1 < len(tmp_list):
                    tmp_list = tmp_list[:index + 1] + T.reject(expected, tmp_list[index + 1:])
            return tmp_list
        return _list
    __uniq = """
        ### T.uniq
            Produces a duplicate-free version of the array.
            In particular only the first occurence of each value is kept.
            eg:
                from Tools import T
                persons00 = ("Tom", "Tom", "Jerry")
                persons01 = ["Tom", "Tom", "Jerry"]
                persons02 = [{"name": "Tom", "age": 12, "sex": "m"},
                             {"name": "Tom", "age": 20, "sex": "m"},
                             {"name": "Mary", "age": 35, "sex": "f"}]
                demo_list = [False, [], False, True, [], {}, False, '']

                unique_persons00 = T.uniq(persons00)
                unique_persons01 = T.uniq(persons01)
                unique_demo_list = T.uniq(demo_list)
                one_Tom = T.uniq({"name": "Tom"}, persons02)
                one_mail = T.uniq(lambda x: x['sex'] == "m", persons02)

                print(unique_persons00)  # => ["Jerry", "Tom"]
                print(unique_persons01)  # => ["Jerry", "Tom"]
                print(unique_demo_list)  # => [False, [], True, {}, '']
                print(one_Tom)  # => [{'age': 12, 'name': 'Tom', 'sex': 'm'}, {'age': 35, 'name': 'Mary', 'sex': 'f'}]
                print(one_mail)  # => [{'age': 12, 'name': 'Tom', 'sex': 'm'}, {'age': 35, 'name': 'Mary', 'sex': 'f'}]
        """

    @staticmethod
    def drop(_list, is_drop_0=False):
        if bool(_list) and isinstance(_list, list):
            tmp_list = copy.deepcopy(_list)
            list_len = len(tmp_list)
            for i in range(0, list_len):
                for j in range(0, list_len):
                    if j == list_len:
                        break
                    if is_drop_0:
                        drop_condition = not bool(tmp_list[j])
                    else:
                        drop_condition = not bool(tmp_list[j]) and tmp_list[j] != 0
                    if drop_condition:
                        tmp_list.remove(tmp_list[j])
                        list_len -= 1
            return tmp_list
        return _list
    __drop = """
    ### T.drop
        Delete false values expect 0.
        eg:
            from Tools import T
            tmp_list = [0, '', 3, None, [], {}, ['Yes'], 'Test']
            drop_val = T.drop(tmp_list)
            drop_val_and_0 = T.drop(tmp_list, True)

            print(drop_val)        # => [0, 3, ['Yes'], 'Test']
            print(drop_val_and_0)  # => [3, ['Yes'], 'Test']
    """

    @staticmethod
    def pluck(body, *key, **opt):
        if isinstance(body, dict):
            tmp_body = [body]
        else:
            tmp_body = body
        if isinstance(tmp_body, list) or isinstance(tmp_body, tuple):
            for k in key:
                field_k = map(lambda x: x[k], tmp_body)
                if len(field_k) > 0:
                    tmp_body = reduce(T.list, map(lambda x: x[k], tmp_body))
                tmp_body = T.list(tmp_body)
            if bool(opt) and "uniq" in opt and opt['uniq']:
                tmp_body = T.uniq(tmp_body)
        return tmp_body
    __pluck = """
    ### T.pluck
        Pluck the list element of collections.
        eg:
            from Tools import T
            persons = [{"name": "Tom", "hobbies": ["sing", "running"]},
                {"name": "Jerry", "hobbies": []},
                {"name": "Mary", "hobbies": ['hiking', 'sing']}]

            hobbies = T.pluck(persons, 'hobbies')
            hobbies_uniq = T.pluck(persons, 'hobbies', uniq=True)

            print(hobbies)      # => ["sing", "running", 'hiking', 'sing']
            print(hobbies_uniq) # => ["sing", "running", 'hiking']
    """

    @staticmethod
    def every(expected, _list):
        if bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if 'function' in str(type(expected)):
                    if not bool(expected(item)):
                        return False
                elif expected != bool(item):
                    return False
            return True
        return False
    __every = """
    ### T.every
        Returns true if all of the values in the list pass the predicate truth test.
        Short-circuits and stops traversing the list if a false element is found.
        eg:
            from Tools import T
            tmp_list = [0, '', 3, None]
            persons = [{"name": "Tom", "age": 12, "sex": "m"},
                       {"name": "Jerry", "age": 20, "sex": "m"},
                       {"name": "Mary", "age": 35, "sex": "f"}]

            every_true = T.every(True, tmp_list)
            is_all_male = T.every(lambda x: x['sex'] == "m", persons)
            print(every_true)   # => False
            print(is_all_male)  # => False
    """

    @staticmethod
    def some(expected, _list):
        if bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if 'function' in str(type(expected)):
                    if bool(expected(item)):
                        return True
                elif expected == bool(item):
                    return True
            return False
        return False
    __some = """
    ### T.some
        Returns true if any of the values in the list pass the predicate truth test.
        Short-circuits and stops traversing the list if a true element is found.
        eg:
            from Tools import T
            tmp_list = [0, '', 3, None]
            persons = [{"name": "Tom", "age": 12, "sex": "m"},
                       {"name": "Jerry", "age": 20, "sex": "m"},
                       {"name": "Mary", "age": 35, "sex": "f"}]

            some_true = T.some(True, tmp_list)
            is_some_female = T.some(lambda x: x['sex'] == "f", persons)

            print(some_true)       # => True
            print(is_some_female)  # => True
    """

    @staticmethod
    def list(*values):
        def list_handler(val):
            if isinstance(val, list):
                return val
            return [val]
        if len(values) == 0:
            return []
        elif len(values) == 1:
            return list_handler(values[0])
        else:
            return reduce(lambda a, b: list_handler(a) + list_handler(b), values)
    __list = """
    ### T.list
        Return now system time.
        eg:
            from Tools import T
            print(T.list())       # => []
            print(T.list([]))     # => []
            print(T.list({}))     # => [{}]
            print(T.list(None))   # => [None]
            print(T.list('test')) # => ['test']
    """

    @staticmethod
    def dump(_json):
        if isinstance(_json, list) or isinstance(_json, dict) or isinstance(_json, tuple):
            return json.dumps(_json, sort_keys=True, indent=2)
        return _json
    __dump = """
    ### T.dump
        Return a formatted json string.
        eg:
            from Tools import T
            persons = [{"name": "Tom", "hobbies": ["sing", "running"]},
                {"name": "Jerry", "hobbies": []}]
            print(T.dump(persons)) #=>
            [
              {
                "hobbies": [
                  "sing", 
                  "running"
                ], 
                "name": "Tom"
              }, 
              {
                "hobbies": [], 
                "name": "Jerry"
              }
            ]
    """

    @staticmethod
    def size(x):
        pass
    __size = """"""

    @staticmethod
    def replace(x):
        pass
    __replace = """"""

    @staticmethod
    def iscan(exp):
        if isinstance(exp, str):
            try:
                exec(exp)
                return True
            except:
                return False
        return False
    __iscan = """
    ### T.iscan
        Test is the stringlized expression valid.
        eg:

    """

    @staticmethod
    def log(msg='Have no Message!', title='Msg From T-log (V1.0.2)', line_len=85):
        title = isinstance(title, str) and title or str(title) or 'Msg From T-log (V1.0.2)'
        title = len(title) <= 35 and title or title[:35]
        line_b = '=' * line_len
        line_m = '-' * line_len
        title = ' ' * int((line_len - len(title))/2) + title
        print('%s\n%s\n%s' % (line_b, title, line_m))
        print(T.dump(msg))
        print(line_b)
    __log = """
    ### T.log
        Show log clear in console.
        eg:
            from Tools import T
            T.log([{"name": "Tom", "hobbies": ["sing", "running"]}, {"name": "Jerry", "hobbies": []}])

            # =>
===========================================================================
                     (funclib[""" + __version + """]) Doc of T.index 
---------------------------------------------------------------------------
[
  {
    "hobbies": [
      "sing", 
      "running"
    ], 
    "name": "Tom"
  }, 
  {
    "hobbies": [], 
    "name": "Jerry"
  }
]
===========================================================================
    """

    @staticmethod
    def timer(fn, times=60, interval=1):
        if 'function' not in str(type(fn)) or not isinstance(times, int) or not isinstance(interval, int) \
                or times < 1 or interval < 0:
            return
        is_time_out = False
        count = 0
        while True:
            count += 1
            if count == times:
                fn()
                is_time_out = True
                break
            elif fn():
                break
            time.sleep(interval)
        return is_time_out
    __timer = """
    ### T.timer
                Set a interval and times limit.
        eg: 
            from Tools import T
            count = 0
            def fn():
                global count
                if count == 4:
                    return True
                count += 1
                print(count)
            T.timer(fn, 10, 2)
            # =>
                >>> 1  #at 0s
                >>> 2  #at 2s
                >>> 3  #at 4s
                >>> 4  #at 4s
    """

    @staticmethod
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    __now = """
    ### T.now
        Return now system time.
        eg:
            from Tools import T
            print(T.now()) # => '2018-2-1 19:32:10'
    """

    @staticmethod
    def help(*args, **kwargs):
        docs_info = T.info()
        keys = docs_info['keys']
        docs = docs_info['docs']
        if len(args) > 0:
            if args[0] in keys:
                T.__clear()
                T.log(docs[args[0]])
            if 'keep' in kwargs and kwargs['keep']:
                T.help(**kwargs)
        else:
            if not ('keep' in kwargs and kwargs['keep']):
                T.__clear()
                print (docs['info'])
            elif not ('info' in kwargs and kwargs['info']):
                print ('')
                hints = map(lambda x: str(keys.index(x)) + ': T.' + x, keys)
                end = 0
                while True:
                    sta = end
                    end = end + 8
                    if end > len(hints):
                        end = len(hints)
                    print '[' + reduce(lambda a, b: a + ' ' + b, hints[sta:end]) + ']'
                    if end == len(hints):
                        break
                print ('')
            idx = raw_input('Input a index (Nothing input will return): ')
            if idx:
                if T.iscan('int(%s)' % idx) and int(idx) in range(0, len(keys)):
                    T.__clear()
                    key = keys[int(idx)]
                    if idx == '0':
                        print (docs[key])
                        return T.help(keep=True, info=True)
                    else:
                        T.log(docs[key], '(funclib[' + T.__version + ']) Doc of T.' + key)
                T.help(keep=True)
    __help = """
    ### T.help
        Return the FuncLib or it's method doc
        eg:
            T.help('index')
            # => 
===========================================================================
                     (funclib[""" + __version + """]) Doc of T.index 
---------------------------------------------------------------------------
""" + __index + """
===========================================================================
        """
    __xyz = """"""

    @staticmethod
    def __clear():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

