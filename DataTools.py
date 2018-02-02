""" ===================================================================================
                                      The T lib
                        A data processing methods lib of python
    -----------------------------------------------------------------------------------
                                 Author: CN-Tower
                                Version: V1.0.2
                                   Date: 2018-2-2
                                 GitHub: http://github.com/CN-Tower/dataTools
    -----------------------------------------------------------------------------------
                                      * T.find
                                      * T.find_index
                                      * T.find_where
                                      * T.contains
                                      * T.reject
                                      * T.every
                                      * T.some
                                      * T.uniq
                                      * T.pluck
                                      * T.list
                                      * T.log
                                      * T.now
    ===================================================================================
"""
import time
import copy


class T(object):
    def __init__(self):
        pass

    @staticmethod
    def find(fn, _list):
        if bool(fn) and bool(_list) and 'function' in str(type(fn))\
                and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if fn(item):
                    return item
        return None
    """ -----------------------------------------------------------------------------------
    ### T.find
        Looks through each value in the list, returning the first one that passes
        a truth test (predicate), or None.If no value passes the test the function
        returns as soon as it finds an acceptable element, and doesn't traverse
        the entire list.
        eg:
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]
            Tom = T.find(lambda x: x['name'] == 'Tom', persons)
            print(Tom)  # => {"name": "Tom", "age": 18}
        ===================================================================================
    """

    @staticmethod
    def find_index(obj, _list):
        if bool(obj) and bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            if obj in _list:
                return _list.index(obj)
            elif isinstance(obj, dict):
                for i in range(0, len(_list)):
                    tmp_bool = True
                    for key in obj:
                        if key not in _list[i] or obj[key] != _list[i][key]:
                            tmp_bool = False
                            break
                    if tmp_bool:
                        return i
                return -1
            return -1
        return -1
    """ -----------------------------------------------------------------------------------
    ### T.find_index
        Looks through the list and returns the item index. If no match is found,
        or if list is empty, -1 will be returned.
        eg:
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]
            Hint_idx = T.find_index({"name": 'Mary'}, persons)
            print(Hint_idx)  # => 2
        ===================================================================================
    """

    @staticmethod
    def find_where(obj, _list):
        idx = T.find_index(obj, _list)
        if idx != -1:
            return _list[idx]
        return None
    """ -----------------------------------------------------------------------------------
    ### T.find_where
        Looks through the list and returns the first value that matches all of the
        key-value pairs listed in properties. If no match is found, or if list is
        empty, None will be returned.
        eg:
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]
            person = T.find_where({"age": 35}, persons)
            print(person)  # => {"name": "Mary", "age": 35}
        ===================================================================================
    """

    @staticmethod
    def contains(item, _list):
        idx = T.find_index(item, _list)
        return idx != -1
    """ -----------------------------------------------------------------------------------
    ### T.contains
        Returns true if the value is present in the list.
        eg:
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]
            is_contains_Marry = T.contains({"name": "Mary", "age": 22}, persons)
            print(is_contains_Marry)  # => False
        ===================================================================================
    """

    @staticmethod
    def reject(fn, _list):
        if bool(fn) and bool(_list) and isinstance(_list, list) and 'function' in str(type(fn)):
            tmp_list = copy.deepcopy(_list)
            for item in tmp_list:
                if fn(item):
                    tmp_list.remove(item)
            return tmp_list
        return _list
    """ -----------------------------------------------------------------------------------
    ### T.reject
        Returns the values in list without the elements that the truth test (predicate) passes.
        The opposite of filter.
        eg:
            persons = [{"name": "Tom", "age": 12},
                {"name": "Jerry", "age": 20},
                {"name": "Mary", "age": 35}]
            adult = T.reject(lambda x: x['age'] < 18, persons)
            print(adult)  # => [{"name": "Jerry", "age": 20}, {"name": "Mary", "age": 35}]
        ===================================================================================
    """

    @staticmethod
    def every(fn, _list):
        if bool(fn) and bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if 'function' in str(type(fn)):
                    if not bool(fn(item)):
                        return False
                elif fn != bool(item):
                    return False
            return True
        return False
    """ -----------------------------------------------------------------------------------
    ### T.every
        Returns true if all of the values in the list pass the predicate truth test.
        Short-circuits and stops traversing the list if a false element is found.
        eg:
            tmp_list = [0, '', 3, None]
            every_true = T.every(True, tmp_list)
            print(every_true)  # => False

            persons = [{"name": "Tom", "age": 12, "sex": "m"},
               {"name": "Jerry", "age": 20, "sex": "m"},
               {"name": "Mary", "age": 35, "sex": "f"}]
            is_all_male = T.every(lambda x: x['sex'] == "m", persons)
            print(is_all_male)  # => False
        ===================================================================================
    """

    @staticmethod
    def some(fn, _list):
        if bool(fn) and bool(_list) and (isinstance(_list, list) or isinstance(_list, tuple)):
            for item in _list:
                if 'function' in str(type(fn)):
                    if bool(fn(item)):
                        return True
                elif fn == bool(item):
                    return True
            return False
        return False
    """ -----------------------------------------------------------------------------------
    ### T.some
        Returns true if any of the values in the list pass the predicate truth test.
        Short-circuits and stops traversing the list if a true element is found.
        eg:
            tmp_list = [0, '', 3, None]
            some_true = T.some(True, tmp_list)
            print(some_true)  # => True

            persons = [{"name": "Tom", "age": 12, "sex": "m"},
                {"name": "Jerry", "age": 20, "sex": "m"},
                {"name": "Mary", "age": 35, "sex": "f"}]
            is_some_female = T.some(lambda x: x['sex'] == "f", persons)
            print(is_some_female)  # => True
        ===================================================================================
    """

    @staticmethod
    def drop(_list):
        if bool(_list) and isinstance(_list, list):
            tmp_list = copy.deepcopy(_list)
            list_len = len(tmp_list)
            for i in range(0, list_len):
                for j in range(0, list_len):
                    if j == list_len:
                        break
                    if tmp_list[j] != 0 and not bool(tmp_list[j]):
                        tmp_list.remove(tmp_list[j])
                        list_len -= 1
            return tmp_list
        return _list
    """ -----------------------------------------------------------------------------------
    ### T.drop
        Delete false values expect 0.
        eg:
            tmp_list = [0, '', 3, None, [], {}, ['Yes'], 'Test']
            drop_val = T.drop(tmp_list)
            print(some_true)  # => [0, 3, ['Yes'], 'Test']
        ===================================================================================
    """

    @staticmethod
    def uniq(_list, obj=None):
        if bool(_list):
            if bool(obj) and isinstance(obj, dict):
                is_find = False
                tmp_list = copy.deepcopy(_list)
                for item in tmp_list:
                    tmp_bool = True
                    for key in obj:
                        if key not in item or item[key] != obj[key]:
                            tmp_bool = False
                            break
                    if tmp_bool:
                        if is_find:
                            tmp_list.remove(item)
                        is_find = True
                return tmp_list
            return list(set(_list))
        return _list
    """ -----------------------------------------------------------------------------------
    ### T.uniq
        Produces a duplicate-free version of the array.
        In particular only the first occurence of each value is kept.
        eg:
            persons = ["Tom", "Tom", "Jerry"]
            persons = T.uniq(persons)
            print(persons)  # => ["Tom", "Jerry"]
        eg:
            persons = [{"name": "Tom", "age": 12, "sex": "m"},
                {"name": "Tom", "age": 20, "sex": "m"},
                {"name": "Mary", "age": 35, "sex": "f"}]
            persons = T.uniq(persons, {"name": "Tom"})
            print(persons)  # => [{"name": "Tom", "age": 12}, {"name": "Mary", "age": 35}]
        ===================================================================================
    """

    @staticmethod
    def pluck(body, *key, **opt):
        tmp_body = isinstance(body, dict) and [body] or body
        if isinstance(tmp_body, list):
            for k in key:
                tmp_body = reduce(T.list, map(lambda x: x[k], tmp_body))
                tmp_body = T.list(tmp_body)
            if bool(opt) and "uniq" in opt and opt['uniq']:
                tmp_body = T.uniq(tmp_body)
        return tmp_body
    """ -----------------------------------------------------------------------------------
    ### T.pluck
        Pluck the list element of collections.
        eg:
            persons = [{"name": "Tom", "hobbies": ["sing", "running"]},
                {"name": "Jerry", "hobbies": []},
                {"name": "Mary", "hobbies": ['hiking', 'sing']}]

            hobbies = T.pluck(persons, 'hobbies')
            print(hobbies) # => ["sing", "running", 'hiking', 'sing']

            hobbies = T.pluck(persons, 'hobbies', uniq=True)
            print(hobbies) # => ["sing", "running", 'hiking']
        ===================================================================================
    """

    @staticmethod
    def list(*values):
        if len(values) == 0:
            return []
        elif len(values) == 1:
            return isinstance(values[0], list) and values[0] or [values[0]]
        else:
            return reduce(lambda a, b: (isinstance(a, list) and a or [a]) + (isinstance(b, list) and b or [b]), values)
    """ -----------------------------------------------------------------------------------
    ### T.list
        Return now system time.
        eg:
            print(T.now()) # => '2018-2-1 19:32:10'
        ===================================================================================
    """

    @staticmethod
    def log(msg='Have no Message!', title='Msg From T-log (V1.0.2)', line_len=85):
        title = isinstance(title, str) and title or str(title) or 'Msg From T-log (V1.0.2)'
        title = len(title) <= 35 and title or title[:35]
        line_b = '=' * line_len
        line_m = '-' * line_len
        title = ' ' * int((line_len - len(title))/2) + title
        print('%s\n%s\n%s' % (line_b, title, line_m))
        print(msg)
        print(line_b)
    """ -----------------------------------------------------------------------------------
    ### T.log
        Show log clear in console.
        eg:
            T.log(msg='Test message Test message Test message Test message!', title='Msg From Test:')
        ===================================================================================
    """

    @staticmethod
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    """ -----------------------------------------------------------------------------------
    ### T.now
        Return now system time.
        eg:
            print(T.now()) # => '2018-2-1 19:32:10'
        ===================================================================================
    """

