# FuncLib

A data processing methods lib of python

For Python2.7

## About
    Author: CN-Tower
    Version: V1.1.3
    Date: 2018-2-2
    GitHub: http://github.com/CN-Tower/dataTools

## Quick Start
```
$ pip install funclib
$ python
>>> from funclib import T
>>> T.help()
```
## Methods
 * [T.help](#thelp)
 * [T.find](#tfind)
 * [T.index](#tindex)
 * [T.where](#twhere) 
 * [T.isin](#tisin)
 * [T.reject](#treject)
 * [T.every](#tevery)
 * [T.some](#tsome)
 * [T.uniq](#tuniq)
 * [T.pluck](#tpluck)
 * [T.list](#tlist)
 * [T.dump](#tdump)
 * [T.log](#tlog)
 * [T.timer](#ttimer)
 * [T.now](#tnow)

## Document

### T.help
```
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

```
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
### T.index
``` 
    Looks through the list and returns the item index. If no match is found,
    or if list is empty, -1 will be returned.

    eg:
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]

        Hint_idx = T.index({"name": 'Mary'}, persons)

        print(Hint_idx)  # => 2
        
```
### T.where
``` 
    Looks through the list and returns the first value that matches all of the
    key-value pairs listed in properties. If no match is found, or if list is
    empty, None will be returned.

    eg:
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]

        person = T.where({"age": 35}, persons)

        print(person)  # => {"age": 35, "name": "Mary"}

```
### T.isin
``` 

    Returns true if the value is present in the list.
    eg:
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]

        is_contains_Marry = T.isin({"name": "Mary", "age": 22}, persons)

        print(is_contains_Marry)  # => False

```
### T.reject
``` 

    Returns the values in list without the elements that the truth test (predicate) passes.
    The opposite of filter.
    eg:
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]

        adult = T.reject(lambda x: x['age'] < 18, persons)

        print(adult)  # => [{"age": 20, "name": "Jerry"}, {"age": 35, "name": "Mary"}]

```
### T.every
``` 

    Returns true if all of the values in the list pass the predicate truth test.
    Short-circuits and stops traversing the list if a false element is found.
    eg:
        tmp_list = [0, '', 3, None]

        every_true = T.every(True, tmp_list)

        print(every_true)  # => False

    eg:
        persons = [{"name": "Tom", "age": 12, "sex": "m"},
           {"name": "Jerry", "age": 20, "sex": "m"},
           {"name": "Mary", "age": 35, "sex": "f"}]

        is_all_male = T.every(lambda x: x['sex'] == "m", persons)

        print(is_all_male)  # => False

```
### T.some
``` 

    Returns true if any of the values in the list pass the predicate truth test.
    Short-circuits and stops traversing the list if a true element is found.
    eg:
        tmp_list = [0, '', 3, None]

        some_true = T.some(True, tmp_list)

        print(some_true)  # => True

    eg:
        persons = [{"name": "Tom", "age": 12, "sex": "m"},
            {"name": "Jerry", "age": 20, "sex": "m"},
            {"name": "Mary", "age": 35, "sex": "f"}]

        is_some_female = T.some(lambda x: x['sex'] == "f", persons)

        print(is_some_female)  # => True

```
### T.drop
``` 

    Delete false values expect 0.
    eg:
        tmp_list = [0, '', 3, None, [], {}, ['Yes'], 'Test']
        drop_val = T.drop(tmp_list)
        drop_val_and_0 = T.drop(tmp_list, True)

        print(drop_val)        # => [0, 3, ['Yes'], 'Test']
        print(drop_val_and_0)  # => [3, ['Yes'], 'Test']

```
### T.uniq
``` 

    Produces a duplicate-free version of the array.
    In particular only the first occurence of each value is kept.
    eg:
        persons = ["Tom", "Tom", "Jerry"]

        persons = T.uniq(persons)

        print(persons)  # => ["Jerry", "Tom"]

    eg:
        persons = [{"name": "Tom", "age": 12, "sex": "m"},
            {"name": "Tom", "age": 20, "sex": "m"},
            {"name": "Mary", "age": 35, "sex": "f"}]

        persons = T.uniq(persons, {"name": "Tom"})

        print(persons)  # => [{"age": 12, "name": "Tom", "sex": "m"}, {"age": 35, "name": "Mary", "sex": "f"}]

```
### T.pluck
``` 

    Pluck the list element of collections.
    eg:
        persons = [{"name": "Tom", "hobbies": ["sing", "running"]},
            {"name": "Jerry", "hobbies": []},
            {"name": "Mary", "hobbies": ['hiking', 'sing']}]

        hobbies = T.pluck(persons, 'hobbies')
        hobbies_uniq = T.pluck(persons, 'hobbies', uniq=True)

        print(hobbies)      # => ["sing", "running", 'hiking', 'sing']
        print(hobbies_uniq) # => ["sing", "running", 'hiking']

```
### T.list
``` 

    Return now system time.
    eg:
        print(T.list())       # => []
        print(T.list([]))     # => []
        print(T.list({}))     # => [{}]
        print(T.list(None))   # => [None]
        print(T.list('test')) # => ['test']
``` 
### T.dump
``` 
    Return a formatted json string.
    eg:
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
```

### T.log
``` 

    Show log clear in console.
    eg:
        T.log()
        T.log('Hello T-log!')
        T.log('This is Test message!', 'Msg From Test:')
        T.log([{"name": "Tom", "hobbies": ["sing", "running"]}, {"name": "Jerry", "hobbies": []}], persons)

        # =>
        ===========================================================================
                                    Msg From T-log (V1.1.3)
        ---------------------------------------------------------------------------
        Have no Message!
        ===========================================================================

        # =>
        ===========================================================================
                                    Msg From T-log (V1.1.3)
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

```

### T.timer
```

    Set a interval and times limit.
    eg:
        count = 0
        def fun():
            return count == 3:
            print(count)
            count += 1
        T.timer(fn, 5, 2)
        # =>
            >>> 1  #at 0s
            >>> 2  #at 2s
            >>> 3  #at 4s

```

### T.now
``` 

    Return now system time.
    eg:
        print(T.now()) # => '2018-2-1 19:32:10'

```
