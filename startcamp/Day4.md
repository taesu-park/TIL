# Day 4

## Python Dictionary

```python
my_dict = {'apple' : '사과' , 'banana' : '바나나'}

for key, value in my_dict_items():
    print(key,value)
for value in my_dict_items():
    print(value)
```

```python
my_dict = {'apple' : 사과 , 'banana' : 바나나}
my_dict = ['apple']

# => 사과

my_dict['cat']
# => 오류 발생(Key)

my_dict.get('apple')
# => 사과

my_dict.get('cat')
# => None
my_dict.get('cat')
# => Not found


```

