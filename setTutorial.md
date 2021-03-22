<center>
<h1> Sets </h1>
</center>

Your stomach starts growling after that last tutorial. You look at the clock but its already way past breakfast so you really shouldn't eat waffles at this time. You flick on the TV and see a Dominoes commercial and now you are craving a pizza. 

You get on the your phone, open the Dominoes app and start creating your pizza. You decide to go with build your own 4 topping pizza. After you finish and submit your order, you get a call from Dominoes and they say, "Hey we just got your order for that 4 topping pizza, does it matter what toppings go first?" You say, "Uhhh no just as long as it is on the pizza." He replies, "So you are saying order doesn't matter?" "Yes that is what I am saying." 

![pizza](pizza.png)

Hmmm that sounds like a <strong>set data structure</strong> to me!

That long intro was to introduce our new data structure tutorial <strong>sets</strong>! There are a few key elements that sets unique to other data structures, let's go over them:

* Order is not important
* No duplicates allowed
* Store info in a set to make it efficient
* Iterable
* Mutable

Lets see how it looks in code:
```python
# Hey look its 3/4 toppings of our pizza
pizzaSet = set(["Pepperoni", "Bacon", "Mushrooms"])
print(pizzaSet)

#adding our final topping
pizzaSet.add("Olives")
print(pizzaSet)
```
<strong>Output:</strong>
```python
{'Mushrooms', 'Bacon', 'Pepperoni'}
{'Olives', 'Mushrooms', 'Bacon', 'Pepperoni'}
```
Notice when we hit the play button again:
```python
{'Mushrooms', 'Bacon', 'Pepperoni'}
{'Mushrooms', 'Olives', 'Bacon', 'Pepperoni'}
```
Woah, 'Mushrooms' and 'Olives' changed places. And why is that? That's right, because order doesn't matter!

## Hashing

Wait like hashbrowns? No, I don't have to make everything about food in my tutorials, okay? Hashing is basically just the way we use the set, we are able to add, remove, and test for membership in O(1) time, we'll come back to performance in a second.


