"""
    ===================================================================================
                                        Func-Lib
                        A data processing methods lib of python
    -----------------------------------------------------------------------------------
                                 Author: CN-Tower
                                   Date: 2018-2-2
                                Version: V1.1.4
                                 GitHub: http://github.com/CN-Tower/FuncLib
    -----------------------------------------------------------------------------------
                          0: T.help                 1: T.index
                          2: T.find                 3: T.contains
                          4: T.reject               5: T.uniq
                          6: T.drop                 7: T.pluck
                          8: T.every                9: T.some
                         10: T.list                11: T.dump
                         12: T.log                 13: T.timer
                         14: T.now                 15: ALL
    ===================================================================================
"""
from help import Help
import time
import copy
import json
import sys


def check_is_python_v2():
    return sys.version[0] == '2'


if check_is_python_v2():
    from functools import reduce


class T(object):

    help_list = [
        'info', 'help', 'find', 'index', 'where', 'isin', 'reject',
        'every', 'some', 'uniq', 'pluck', 'list', 'dump', 'log', 'timer', 'now'
    ]

    def __init__(self):
        pass

    """ 
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

    """
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
    def find(expected, _list):
        idx = T.index(expected, _list)
        if idx != -1:
            return _list[idx]
        return None

    """
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
    def contains(expected, _list):
        idx = T.index(expected, _list)
        return idx != -1

    """
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
    def reject(expected, _list):
        index = T.index(expected, _list)
        if index != -1:
            tmp_list = copy.deepcopy(_list)
            del tmp_list[index]
            return T.reject(expected, tmp_list)
        return _list

    """
    ### T.uniq
        Produces a duplicate-free version of the array.
        In particular only the first occurence of each value is kept.
        eg:
            from Tools import T
            persons00 = ("Tom", "Tom", "Jerry")
            persons01 = ["Tom", "Tom", "Jerry"]
            unique_persons00 = T.uniq(persons00)
            unique_persons01 = T.uniq(persons01)
            print(unique_persons00)  # => ["Jerry", "Tom"]
            print(unique_persons01)  # => ["Jerry", "Tom"]
            
            persons02 = [{"name": "Tom", "age": 12, "sex": "m"},
                         {"name": "Tom", "age": 20, "sex": "m"},
                         {"name": "Mary", "age": 35, "sex": "f"}]
            
            one_Tom = T.uniq({"name": "Tom"}, persons02)
            one_mail = T.uniq(lambda x: x['sex'] == "m", persons02)
            
            print(one_Tom)   # => [{'age': 12, 'name': 'Tom', 'sex': 'm'}, {'age': 35, 'name': 'Mary', 'sex': 'f'}]
            print(one_mail)  # => [{'age': 12, 'name': 'Tom', 'sex': 'm'}, {'age': 35, 'name': 'Mary', 'sex': 'f'}]
    """
    @staticmethod
    def uniq(expected, _list=None):
        if _list is None:
            _list = expected
            expected = None
        if isinstance(_list, tuple):
            _list = list(_list)
        if bool(_list) and isinstance(_list, list):
            tmp_list = copy.deepcopy(_list)
            if bool(expected) and (isinstance(expected, dict) or 'function' in str(type(expected))):
                index = T.index(expected, tmp_list)
                if index != -1 and index + 1 < len(tmp_list):
                    return tmp_list[:index + 1] + T.reject(expected, tmp_list[index + 1:])
            for i in range(0, len(tmp_list) - 1):
                if len(tmp_list) <= i + 1:
                    break
                tmp_list = tmp_list[:i + 1] + T.reject(tmp_list[i], tmp_list[i + 1:])
            return tmp_list
        return _list

    """
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

    """
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
    def pluck(body, *key, **opt):
        if isinstance(body, dict):
            tmp_body = [body]
        else:
            tmp_body = body
        if isinstance(tmp_body, list):
            for k in key:
                field_k = map(lambda x: x[k], tmp_body)
                if len(field_k) > 0:
                    tmp_body = reduce(T.list, map(lambda x: x[k], tmp_body))
                tmp_body = T.list(tmp_body)
            if bool(opt) and "uniq" in opt and opt['uniq']:
                tmp_body = T.uniq(tmp_body)
        return tmp_body

    """
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
    def every(fn, _list):
        if bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if 'function' in str(type(fn)):
                    if not bool(fn(item)):
                        return False
                elif fn != bool(item):
                    return False
            return True
        return False

    """
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
    def some(fn, _list):
        if bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if 'function' in str(type(fn)):
                    if bool(fn(item)):
                        return True
                elif fn == bool(item):
                    return True
            return False
        return False

    """
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

    """
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
    def dump(_json):
        if isinstance(_json, list) or isinstance(_json, dict) or isinstance(_json, tuple):
            return json.dumps(_json, sort_keys=True, indent=2)
        return _json

    """
    ### T.log
        Show log clear in console.
        eg:
            from Tools import T
            T.log()
            T.log('Hello T-log!')
            T.log('This is Test message!', 'Msg From Test:')
            T.log([{"name": "Tom", "hobbies": ["sing", "running"]}, {"name": "Jerry", "hobbies": []}], 'persons')

            # =>
            ===========================================================================
                                        Msg From T-log (V1.0.2)
            ---------------------------------------------------------------------------
            Have no Message!
            ===========================================================================

            # =>
            ===========================================================================
                                        Msg From T-log (V1.0.2)
            ---------------------------------------------------------------------------
            Hello T-log!
            ===========================================================================

            # =>
            ===========================================================================
                                           Msg From Test:
            ---------------------------------------------------------------------------
            This is Test message!
            ===========================================================================

            # =>
            ===========================================================================
                                             persons
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
    def log(msg='Have no Message!', title='Msg From T-log (V1.0.2)', line_len=85):
        title = isinstance(title, str) and title or str(title) or 'Msg From T-log (V1.0.2)'
        title = len(title) <= 35 and title or title[:35]
        line_b = '=' * line_len
        line_m = '-' * line_len
        title = ' ' * int((line_len - len(title))/2) + title
        print('%s\n%s\n%s' % (line_b, title, line_m))
        print(T.dump(msg))
        print(line_b)

    """
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

    """
    ### T.now
        Return now system time.
        eg:
            from Tools import T
            print(T.now()) # => '2018-2-1 19:32:10'
    """
    @staticmethod
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    """
    ### T.help
        Return the FuncLib or it's method doc
        eg:
            T.help('find')
            # => 
            =====================================================================================
                               Msg From T-log (V1.1.3)
            -------------------------------------------------------------------------------------
            
                ### T.find
                ```
                    Looks through each value in the list, returning the first one that passes
                    a truth test (predicate), or None.If no value passes the test the function
                    returns as soon as it finds an acceptable element, and doesn't traverse
                    the entire list.
            
                    eg:
                        persons = [{"name": "Tom", "age": 12},
                            {"name": "Jerry", "age": 20},
                            {"name": "Mary", "age": 35}]
            
                        Tom = T.find(lambda x: x['name'] == 'Tom', persons)
            
                        print(Tom)  # => {"age": 12, "name": "Tom"}
            
                ```
            
            =====================================================================================
    """
    @staticmethod
    def help(*args):
        help_info = vars(Help).items()
        help_keys = []
        for key, value in help_info:
            if key in T.help_list:
                help_keys.append({key: value})
        help_keys.sort(lambda a, b: T.index(a.keys()[0], T.help_list) - T.index(b.keys()[0], T.help_list))
        help_msg = ''
        if len(args) > 0:
            if args[0] in T.help_list and args[0] != 'info':
                for item in help_keys:
                    if args[0] in item:
                        help_msg = item[args[0]]
                T.log(help_msg)
            elif args[0] in ['a', 'all']:
                for item in help_keys:
                    help_msg += item.values()[0]
                print (help_msg)
            else:
                T.help()
        else:
            help_msg += help_keys[0].values()[0]
            print (help_msg)
            selected_method = raw_input('Input a method\'s index to show it\'s doc: ')

            def check_is_int(x):
                try:
                    int(x)
                    return True
                except:
                    return False
            if check_is_int(selected_method) and int(selected_method) in range(0, len(T.help_list) - 1):
                T.help(T.help_list[int(selected_method) + 1])
            else:
                T.help(selected_method)
