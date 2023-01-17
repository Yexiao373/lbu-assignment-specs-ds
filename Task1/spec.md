# Introduction to Programming

## Assignment: Task 1

### The Problem

Many businesses offer their products with a "list price", and then apply various discounts to certain types of
customer. A large pizza chain is rarely able to charge full price for a pizza, for example. And very few customers
are willing to pay the full price.

This means that the web sites of such businesses have to carry out calculations that takes what the customer has
ordered to arrive at a final price.

### The Task

A certain pizza takeaway offers any of its pizzas for a fixed price. All pizzas cost the same, regardless of recipe.
For every pizza ordered, a customer may order another for half price. In addition, if the total order is over £50 (after
the "half price" discount), a whopping 35% discount is applied to the total. 

To be clear, the "half price" offer only applies where a full price pizza has been ordered. So an order of four pizzas
would be charged at two full price, two half price. A order for five pizzas would be *three* full price, and two half
price.

Your task is to write a program that takes the current price of a single pizza, finds how many the customer has
ordered, and applies any relevant discounts.

### Examples

The following illustrate what should happen when the program executes in a variety of situations. 

Here, two pizzas just score the "half price" offer.

```text
Beckett Pizza Plaza
===================

Enter today's pizza price: 10
Enter number of pizzas on the order: 2

Total Cost: £15.00.
```

Here there is an odd number of pizzas, so two are full price, and one is half price.

```text
Beckett Pizza Plaza
===================

Enter today's pizza price: 10
Enter number of pizzas on the order: 3

Total Cost: £25.00.
```

This large order (on a more expensive day) causes the big 35% discount to kick in. The calculation will have been
three pizzas at £15, three half price at £7.50 to give a total of £67.50. This is discounted to £43.875, which is
displayed as shown.

```text
Beckett Pizza Plaza
===================

Enter today's pizza price: 15
Enter number of pizzas on the order: 6

Total Cost: £43.88.
```

A good solution should also handle incorrect input. It is not necessary to provide an exact error message, but
here are some sample error cases to consider. There are probably more.

```text
Beckett Pizza Plaza
===================

Enter today's pizza price: 0
Invalid Input.

Beckett Pizza Plaza
===================

Enter today's pizza price: 5
Enter number of pizzas on the order: 0
Invalid Input.

Beckett Pizza Plaza
===================

Enter today's pizza price: 5
Enter number of pizzas on the order: -1
Invalid Input.
```
