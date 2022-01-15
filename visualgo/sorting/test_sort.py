def test(sort_function):
    assert sort_function([]) == []
    assert sort_function([3]) == [3]
    assert sort_function([37,2]) == [2, 37]
    print(sort_function([3,38,5,44,15,36,26,27,2,46,4,19,47,49,48]))
    assert sort_function([3,38,5,44,15,36,26,27,2,46,4,19,47,49,48]) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 49]
    
    
    
    print("All tests passed")