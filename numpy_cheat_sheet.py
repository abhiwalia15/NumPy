Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np

>>> np.array([1,2,3])
array([1, 2, 3])
>>> np.array([[1,2,3],[1,2,4],[5,3,1]])
array([[1, 2, 3],
       [1, 2, 4],
       [5, 3, 1]])
>>> np.array([(1,2,3),(1,2,4),(5,3,2)])
array([[1, 2, 3],
       [1, 2, 4],
       [5, 3, 2]])
>>> np.zeros(3)
array([0., 0., 0.])
>>> np.ones(3,3)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    np.ones(3,3)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\numeric.py", line 203, in ones
    a = empty(shape, dtype, order)
TypeError: data type not understood
>>> np.ones((3,3))
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
>>> np.eye(5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
>>> np.array(0,5,1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    np.array(0,5,1)
ValueError: only 2 non-keyword arguments accepted
>>> np.linesepace(0,10,3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    np.linesepace(0,10,3)
AttributeError: module 'numpy' has no attribute 'linesepace'
>>> np.linspace(0,10,2)
array([ 0., 10.])
>>> np.linspace(0,100,6)
array([  0.,  20.,  40.,  60.,  80., 100.])
>>> np.arange(0,10,3)
array([0, 3, 6, 9])
>>> np.arange(0,15).reshape(4,4)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    np.arange(0,15).reshape(4,4)
ValueError: cannot reshape array of size 15 into shape (4,4)
>>> np.arange(1,17).reshape(4,4)
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
>>> arr = np.random.randint(9).reshape(3,3)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    arr = np.random.randint(9).reshape(3,3)
AttributeError: 'int' object has no attribute 'reshape'
>>> arr = np.random.randint(9)
>>> arr
2
>>> arr = arr.array
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    arr = arr.array
AttributeError: 'int' object has no attribute 'array'
>>> arr = np.array(arr)
>>> arr
array(2)
>>> arr = np.random.rand(3,3)
>>> arr
array([[0.14570746, 0.45351408, 0.89635588],
       [0.11789639, 0.84586224, 0.06496138],
       [0.38512206, 0.57569381, 0.68457895]])
>>> arr*10
array([[1.45707464, 4.53514081, 8.96355877],
       [1.17896393, 8.45862244, 0.64961377],
       [3.85122063, 5.75693809, 6.84578954]])
>>> arr.size
9
>>> arr.shape
(3, 3)
>>> arr.dtype
dtype('float64')
>>> arr.astype(int)
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])
>>> arr
array([[0.14570746, 0.45351408, 0.89635588],
       [0.11789639, 0.84586224, 0.06496138],
       [0.38512206, 0.57569381, 0.68457895]])
>>> arr *=10
>>> arr
array([[1.45707464, 4.53514081, 8.96355877],
       [1.17896393, 8.45862244, 0.64961377],
       [3.85122063, 5.75693809, 6.84578954]])
>>> arr
array([[1.45707464, 4.53514081, 8.96355877],
       [1.17896393, 8.45862244, 0.64961377],
       [3.85122063, 5.75693809, 6.84578954]])
>>> arr.astype(int)
array([[1, 4, 8],
       [1, 8, 0],
       [3, 5, 6]])
>>> arr.tolist()
[[1.4570746431881343, 4.535140813072186, 8.96355877025114], [1.1789639281631847, 8.458622436673203, 0.6496137683387448], [3.851220630251071, 5.756938094066037, 6.845789541488902]]
>>> np.info(np.eye)
 eye(N, M=None, k=0, dtype=<class 'float'>, order='C')

Return a 2-D array with ones on the diagonal and zeros elsewhere.

Parameters
----------
N : int
  Number of rows in the output.
M : int, optional
  Number of columns in the output. If None, defaults to `N`.
k : int, optional
  Index of the diagonal: 0 (the default) refers to the main diagonal,
  a positive value refers to an upper diagonal, and a negative value
  to a lower diagonal.
dtype : data-type, optional
  Data-type of the returned array.
order : {'C', 'F'}, optional
    Whether the output should be stored in row-major (C-style) or
    column-major (Fortran-style) order in memory.

    .. versionadded:: 1.14.0

Returns
-------
I : ndarray of shape (N,M)
  An array where all elements are equal to zero, except for the `k`-th
  diagonal, whose values are equal to one.

See Also
--------
identity : (almost) equivalent function
diag : diagonal 2-D array from a 1-D array specified by the user.

Examples
--------
>>> np.eye(2, dtype=int)
array([[1, 0],
       [0, 1]])
>>> np.eye(3, k=1)
array([[ 0.,  1.,  0.],
       [ 0.,  0.,  1.],
       [ 0.,  0.,  0.]])
>>> np.full((3,3),2)
array([[2, 2, 2],
       [2, 2, 2],
       [2, 2, 2]])
>>> arr.view(double)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    arr.view(double)
NameError: name 'double' is not defined
>>> arr.view(int)
array([[-2142949704,  1073172525,  -200566404,  1074930683, -1824784040,
         1075965271],
       [ 1202323007,  1072880905, -1889701300,  1075899088,  -801015114,
         1071958434],
       [-1023090959,  1074712396,  -946048808,  1075250970, -1487931004,
         1075536406]])
>>> arr.view(float)
array([[1.45707464, 4.53514081, 8.96355877],
       [1.17896393, 8.45862244, 0.64961377],
       [3.85122063, 5.75693809, 6.84578954]])
>>> arr.sort()
>>> arr
array([[1.45707464, 4.53514081, 8.96355877],
       [0.64961377, 1.17896393, 8.45862244],
       [3.85122063, 5.75693809, 6.84578954]])
>>> arr.sort()
>>> print(arr,sort())
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(arr,sort())
NameError: name 'sort' is not defined
>>> print(arr.sort())
None
>>> arr
array([[1.45707464, 4.53514081, 8.96355877],
       [0.64961377, 1.17896393, 8.45862244],
       [3.85122063, 5.75693809, 6.84578954]])
>>> arr.sort(axis=0)
>>> arr
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> arr.sort(axis=1)
>>> arr
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> arr.flatten()
array([0.64961377, 1.17896393, 6.84578954, 1.45707464, 4.53514081,
       8.45862244, 3.85122063, 5.75693809, 8.96355877])
>>> arr
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> arr.t
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    arr.t
AttributeError: 'numpy.ndarray' object has no attribute 't'
>>> arr.T
array([[0.64961377, 1.45707464, 3.85122063],
       [1.17896393, 4.53514081, 5.75693809],
       [6.84578954, 8.45862244, 8.96355877]])
>>> arr.resize((3,3))
>>> arr
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> values = [1,2,3]
>>> new_arr = np.append(arr,values)
>>> new_arr
array([0.64961377, 1.17896393, 6.84578954, 1.45707464, 4.53514081,
       8.45862244, 3.85122063, 5.75693809, 8.96355877, 1.        ,
       2.        , 3.        ])
>>> arr
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> np.full(4,2)
array([2, 2, 2, 2])
>>> arr
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> arr2 = np.arange(1,10).reshape(3,3)
>>> arr2
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.concatenate((arr,arr2),axis=0)
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877],
       [1.        , 2.        , 3.        ],
       [4.        , 5.        , 6.        ],
       [7.        , 8.        , 9.        ]])
>>> np.concatenate((arr,arr2),axis=1)
array([[0.64961377, 1.17896393, 6.84578954, 1.        , 2.        ,
        3.        ],
       [1.45707464, 4.53514081, 8.45862244, 4.        , 5.        ,
        6.        ],
       [3.85122063, 5.75693809, 8.96355877, 7.        , 8.        ,
        9.        ]])
>>> np.split(arr,3)
[array([[0.64961377, 1.17896393, 6.84578954]]), array([[1.45707464, 4.53514081, 8.45862244]]), array([[3.85122063, 5.75693809, 8.96355877]])]
>>> np.split(arr,5)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 778, in split
    len(indices_or_sections)
TypeError: object of type 'int' has no len()

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    np.split(arr,5)
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 784, in split
    'array split does not result in an equal division')
ValueError: array split does not result in an equal division
>>> np.hsplit(arr,5)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 778, in split
    len(indices_or_sections)
TypeError: object of type 'int' has no len()

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    np.hsplit(arr,5)
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 846, in hsplit
    return split(ary, indices_or_sections, 1)
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 784, in split
    'array split does not result in an equal division')
ValueError: array split does not result in an equal division
>>> np.hsplit(arr,2)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 778, in split
    len(indices_or_sections)
TypeError: object of type 'int' has no len()

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    np.hsplit(arr,2)
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 846, in hsplit
    return split(ary, indices_or_sections, 1)
  File "C:\python 3.6.5\lib\site-packages\numpy\lib\shape_base.py", line 784, in split
    'array split does not result in an equal division')
ValueError: array split does not result in an equal division
>>> np.hsplit(arr,1)
[array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])]
>>> arr[:,1]
array([1.17896393, 4.53514081, 5.75693809])
>>> arr[:,1]>4
array([False,  True,  True])
>>> arr2
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> arr2(arr2>5)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    arr2(arr2>5)
TypeError: 'numpy.ndarray' object is not callable
>>> (arr2 >5) & (arr2%2==0)
array([[False, False, False],
       [False, False,  True],
       [False,  True, False]])
>>> arr^
SyntaxError: invalid syntax
>>> arr^arr
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    arr^arr
TypeError: ufunc 'bitwise_xor' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> ~arr
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    ~arr
TypeError: ufunc 'invert' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> (~arr)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    (~arr)
TypeError: ufunc 'invert' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> arr[arr<5]
array([0.64961377, 1.17896393, 1.45707464, 4.53514081, 3.85122063])
>>> np.add(arr,1)
array([[1.64961377, 2.17896393, 7.84578954],
       [2.45707464, 5.53514081, 9.45862244],
       [4.85122063, 6.75693809, 9.96355877]])
>>> np.add(arr2,1)
array([[ 2,  3,  4],
       [ 5,  6,  7],
       [ 8,  9, 10]])
>>> np.subtract(arr2,3)
array([[-2, -1,  0],
       [ 1,  2,  3],
       [ 4,  5,  6]])
>>> np.multiply(arr2,2)
array([[ 2,  4,  6],
       [ 8, 10, 12],
       [14, 16, 18]])
>>> np.divide(arr2,0)

Warning (from warnings module):
  File "__main__", line 1
RuntimeWarning: divide by zero encountered in true_divide
array([[inf, inf, inf],
       [inf, inf, inf],
       [inf, inf, inf]])
>>> np.power(arr2,2)
array([[ 1,  4,  9],
       [16, 25, 36],
       [49, 64, 81]], dtype=int32)
>>> np.divide(arr,arr2)
array([[0.64961377, 0.58948196, 2.28192985],
       [0.36426866, 0.90702816, 1.40977041],
       [0.55017438, 0.71961726, 0.99595097]])
>>> arr == arr2
array([[False, False, False],
       [False, False, False],
       [False, False, False]])
>>> np.array_equal(arr,arr2)
False
>>> np.sqrt(arr)
array([[0.80598621, 1.08580105, 2.61644598],
       [1.20709347, 2.12958701, 2.9083711 ],
       [1.96245271, 2.39936202, 2.9939203 ]])
>>> np.sin(arr)
array([[ 0.60487889,  0.92421085,  0.53339084],
       [ 0.99354066, -0.98433263,  0.82270634],
       [-0.6515516 , -0.50229186,  0.44504024]])
>>> np.cos(arr2)
array([[ 0.54030231, -0.41614684, -0.9899925 ],
       [-0.65364362,  0.28366219,  0.96017029],
       [ 0.75390225, -0.14550003, -0.91113026]])
>>> np.sec(arr)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    np.sec(arr)
AttributeError: module 'numpy' has no attribute 'sec'
>>> np.tan(arr)
array([[ 0.75959514,  2.42014405,  0.63058335],
       [ 8.75545783,  5.58260044, -1.44723779],
       [ 0.858882  , -0.58088694, -0.49696815]])
>>> np.cosec(arr2)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    np.cosec(arr2)
AttributeError: module 'numpy' has no attribute 'cosec'
>>> np.cot(arr)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    np.cot(arr)
AttributeError: module 'numpy' has no attribute 'cot'
>>> np.log(arr)
array([[-0.4313773 ,  0.16463603,  1.9236338 ],
       [ 0.37643076,  1.51185613,  2.13518633],
       [ 1.34839014,  1.75040575,  2.19316733]])
>>> np.abs(arr2)
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.abs(arr)
array([[0.64961377, 1.17896393, 6.84578954],
       [1.45707464, 4.53514081, 8.45862244],
       [3.85122063, 5.75693809, 8.96355877]])
>>> np.ceil(arr)
array([[1., 2., 7.],
       [2., 5., 9.],
       [4., 6., 9.]])
>>> np.floor(arr)
array([[0., 1., 6.],
       [1., 4., 8.],
       [3., 5., 8.]])
>>> np.round(arr)
array([[1., 1., 7.],
       [1., 5., 8.],
       [4., 6., 9.]])
>>> arr.sum()
41.696922625492604
>>> arr.sum(axis=0)
array([ 5.95790904, 11.47104284, 24.26797075])
>>> arr2.sum(axis=0)
array([12, 15, 18])
>>> arr2.sum(axis=1)
array([ 6, 15, 24])
>>> np.std()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    np.std()
TypeError: std() missing 1 required positional argument: 'a'
>>> arr.std()
2.944935181624676
>>> np.std(arr,arr2)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    np.std(arr,arr2)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\fromnumeric.py", line 3038, in std
    **kwargs)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 140, in _std
    keepdims=keepdims)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 94, in _var
    rcount = _count_reduce_items(arr, axis)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 55, in _count_reduce_items
    items *= arr.shape[ax]
TypeError: only integer scalar arrays can be converted to a scalar index
>>> np.std(arr2)
2.581988897471611
>>> np.var(arr2)
6.666666666666667
>>> arr.corrcoef()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    arr.corrcoef()
AttributeError: 'numpy.ndarray' object has no attribute 'corrcoef'
>>> 
