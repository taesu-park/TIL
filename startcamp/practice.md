# 어려운거



### 1. 반복문

```python
int_price = []

for price in prices:
    int_price.append(int(price))
print(int_price)
```





### 2. List comprehension



```python
int_price2 = [int(price) for price in prices]
print(int_price2)
```





### 3. map



```python
int_price3 = list(map(int,prices))
print(int_price3)


int_price3 = sorted(int_price3,reverse = True)
# int_price3.sort()
# int_prices3.reverse()
print(int_price3)
# list.sort() : return이 None. 원본 리스트 자체를 변경.
# sorted(list) : return이 정렬된 리스트. 원본 자체는 변경하지 않음
```

