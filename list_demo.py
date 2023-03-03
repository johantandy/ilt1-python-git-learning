paths = ['ML', 'Cloud']

print(paths)
print(paths[0],paths[1])

paths.append('Android')
print(paths)
print(paths[0],paths[1],paths[2])

paths.remove('Cloud')
print(paths)

paths.insert(1, 'Mobile')
print(paths)

paths.pop(1)
print(paths)
paths[1] = "haha"
print(paths)