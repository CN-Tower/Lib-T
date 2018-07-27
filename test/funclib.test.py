import unittest
from funclib import fn

class TestDict(unittest.TestCase):
    def test_index(self):
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]
        self.assertEqual(fn.index({"name": 'Jerry'}, persons), 1)
        self.assertEqual(fn.index(lambda x: x['name'] == 'Mary', persons), 2)

    def test_find(self):
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]
        Jerry = fn.find({"name": 'Jerry'}, persons)
        Mary  = fn.find(lambda x: x['name'] == 'Mary', persons)
        self.assertDictEqual(
            fn.find({"name": 'Jerry'}, persons),
            {'name': 'Jerry', 'age': 20},
            msg=None
        )
        self.assertDictEqual(
            fn.find(lambda x: x['name'] == 'Mary', persons),
            {'name': 'Mary', 'age': 35},
            msg=None
        )

    def test_filter(self):
        persons = [{"name": "Tom", "age": 20},
            {"name": "Jerry", "age": 20},
            {"name": "Jerry", "age": 35}]
        age20 = fn.filter({"age": 20}, persons)
        Jerrys = fn.filter(lambda x: x['name'] == 'Jerry', persons)
        self.assertTrue(len(age20) == 2 and fn.every({'age': 20}, age20))
        self.assertTrue(len(Jerrys) == 2 and fn.every({'name': 'Jerry'}, Jerrys))

    def test_reject(self):
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]
        not_age20 = fn.reject({"age": 20}, persons)
        not_Jerry = fn.reject(lambda x: x['name'] == 'Jerry', persons)
        self.assertTrue(len(not_age20) == 2 and not fn.every({'age': 20}, not_age20))
        self.assertTrue(len(not_Jerry) == 2 and not fn.every({'name': 'Jerry'}, not_Jerry))

    def test_reduce(self):
        self.assertEqual(fn.reduce(lambda a, b: a + b, [1 , 2, 3, 4]), 10)

    def test_contains(self):
        persons = [{"name": "Tom", "age": 12},
            {"name": "Jerry", "age": 20},
            {"name": "Mary", "age": 35}]
        self.assertFalse(fn.contains({"name": "Jerry", "age": 12}, persons))
        self.assertTrue(fn.contains(lambda x: x['name'] == 'Mary', persons))

    def test_flatten(self):
        self.assertListEqual(
            fn.flatten([1, [2], [3, [[4]]]]),
            [1, 2, 3, [[4]]],
            msg=None
        )
        self.assertListEqual(
            fn.flatten([1, [2], [3, [[4]]]], True),
            [1, 2, 3, 4],
            msg=None
        )

    def test_uniq(self):
        persons = [{"name": "Tom", "age": 12, "pet": {"species": "dog", "name": "Kitty"}},
            {"name": "Tom", "age": 20, "pet": {"species": "cat", "name": "wang"}},
            {"name": "Mary", "age": 35, "pet": {"species": "cat", "name": "mimi"}}]
        self.assertListEqual(
            fn.uniq(["Tom", "Tom", "Jerry"]),
            ["Tom", "Jerry"],
            msg=None
        )
        self.assertListEqual(
            fn.uniq([False, [], False, True, [], {}, False, '']),
            [False, [], True, {}, ''],
            msg=None
        )
        self.assertListEqual(
            fn.uniq(persons, '/name'),
            [{"name": "Tom", "age": 12, "pet": {"species": "dog", "name": "Kitty"}},
             {"name": "Mary", "age": 35, "pet": {"species": "cat", "name": "mimi"}}],
            msg=None
        )
        self.assertListEqual(
            fn.uniq(persons, '/pet/species'),
            [{"name": "Tom", "age": 12, "pet": {"species": "dog", "name": "Kitty"}},
             {"name": "Tom", "age": 20, "pet": {"species": "cat", "name": "wang"}}],
            msg=None
        )

    def test_pluck(self):
        persons = [{"name": "Tom", "hobbies": ["sing", "running"]},
            {"name": "Jerry", "hobbies": []},
            {"name": "Mary", "hobbies": ['hiking', 'sing']}]
        self.assertListEqual(
            fn.pluck(persons, 'hobbies'),
            ["sing", "running", 'hiking', 'sing'],
            msg=None
        )
        self.assertListEqual(
            fn.pluck(persons, 'hobbies', uniq=True),
            ["sing", "running", 'hiking'],
            msg=None
        )

    def test_get(self):
        Tom = {
            "name": "Tom",
            "age": 12,
            "pets": [
                {"species": "dog", "name": "Kitty"},
                {"species": "cat", "name": "mimi"}
            ]
        }
        self.assertEqual(fn.get(Tom, '/age'), 12)
        self.assertEqual(fn.get(Tom, '/pets/0/species'), 'dog')
        self.assertEqual(fn.get(Tom, '/pets/1/name'), 'mimi')
        self.assertTrue(fn.get(Tom, '/pets/1/name', 'str'))
        self.assertFalse(fn.get(Tom, '/pets/1/name', 'int'))

    def test_every(self):
        persons = [{"name": "Tom", "age": 12, "sex": "m"},
            {"name": "Jerry", "age": 20, "sex": "m"},
            {"name": "Mary", "age": 35, "sex": "f"}]
        self.assertFalse(fn.every(5, [1, 1, 2, 3, 5, 8]))
        self.assertFalse(fn.every({"sex": "m"}, persons))
        self.assertFalse(fn.every(lambda x: x['age'] > 18, persons))

    def test_some(self):
        persons = [{"name": "Tom", "age": 12, "sex": "m"},
            {"name": "Jerry", "age": 20, "sex": "m"},
            {"name": "Mary", "age": 35, "sex": "f"}]
        self.assertTrue(fn.some(5, [1, 1, 2, 3, 5, 8]))
        self.assertTrue(fn.some({"sex": "m"}, persons))
        self.assertTrue(fn.some(lambda x: x['age'] > 18, persons))

    def test_tolist(self):
        fn.tolist()       # => []
        fn.tolist([])     # => []
        fn.tolist({})     # => [{}]
        fn.tolist(None)   # => [None]
        fn.tolist('str')  # => ['str']
        self.assertListEqual(fn.tolist(), [], msg=None)
        self.assertListEqual(fn.tolist([]), [], msg=None)
        self.assertListEqual(fn.tolist({}), [{}], msg=None)
        self.assertListEqual(fn.tolist(None), [None], msg=None)
        self.assertListEqual(fn.tolist('str'), ['str'], msg=None)

    def test_drop(self):
        tmp_list = [0, '', 3, None, [], {}, ['Yes'], 'Test']
        self.assertListEqual(fn.drop(tmp_list), [3, ['Yes'], 'Test'], msg=None)
        self.assertListEqual(fn.drop(tmp_list, True), [0, 3, ['Yes'], 'Test'], msg=None)

    def test_test(self):
        self.assertFalse(fn.test(r'ab', 'Hello World!'))
        self.assertTrue(fn.test(r'll', 'Hello World!'))

    def test_replace(self):
        self.assertEqual(fn.replace(r'Tom', 'Jack', 'Hello I\'m Tom!'), 'Hello I\'m Jack!')

    def test_iscan(self):
        self.assertTrue(fn.iscan("int('5')"))
        self.assertFalse(fn.iscan("int('a')"))

    def test_typeof(self):
        self.assertTrue(fn.typeof(None, 'non'))
        self.assertFalse(fn.typeof(True, 'str'))
        self.assertTrue(fn.typeof([], 'map', 'lst', 'tup'))
        self.assertTrue(fn.typeof(lambda x: x, 'fun'))

    def test_typeval(self):
        self.assertEqual(fn.typeval('test', 'str'), 'test')
        self.assertListEqual(fn.typeval([], 'lst'), [], msg=None)
        self.assertFalse(fn.typeval({}, 'lst'))
        
if __name__=='__main__':
    unittest.main()
