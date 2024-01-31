# Introduction to Programming

## Assignment: Task 1

### The Problem

Pizza takeaways are popular. There is a wide variety from which to choose, ranging from international franchises to small local businesses.

For reasons that are not clear, the pricing of takeaway pizzas is very rarely straightforward. Prices vary depending on many factors. These might include the number ordered, the time of day the order is placed, the day of the week itself, whether the order will be collected, or even whether an app was used to place the order.

A computer program is often the only practical way to work out the price of a takeaway pizza order.

### The Task

In this task you will develop a program that will assist one Pizza Provider to calculate how much to charge a customer for a given order. The rules to be applied are set out below.

Beckett Pizza Plaza (henceforth *BPP*) offers a range of pizzas for collection or delivery. In common with all others in the marketplace, the pricing of individual pizzas is simple, but things become more complex with a complete order. In an attempt to simpify this needlessly complex state of affairs, BPP has decided to offer only one discount.

*The customer must order FOUR pizzas. The pizzas are priced differently, but the cheapest will not be charged for.*

This would commonly be called a "Four-for-Three" offer.

Your task is to create a program that accepts four pizza prices, and carries out the required calculation to determine what the customer should be charged. The program should also display the discount the customer has achieved (which is at most 25%).

### Examples

The following illustrate what should happen when the program executes in a variety of situations. 

Here, four pizzas have the same price, so the total is three times the price, and the discount is 25%.

```text
Beckett Pizza Plaza 4-for-3 Offer
=================================

Enter Price of Pizza #1: 12
Enter Price of Pizza #2: 12
Enter Price of Pizza #3: 12
Enter Price of Pizza #4: 12

Order Total is £36.00, a fabulous discount of 25%!
```

Now, one of the pizzas is cheaper, so this is the "free" one. The discount is slightly less.

```text
Beckett Pizza Plaza 4-for-3 Offer
=================================

Enter Price of Pizza #1: 12
Enter Price of Pizza #2: 12
Enter Price of Pizza #3: 12
Enter Price of Pizza #4: 11

Order Total is £36.00, a fabulous discount of 24%!
```

Finally, four differently priced pizzas result in a more complex calculation. (The first three are, obviously, the ones paid for.)

```text
Beckett Pizza Plaza 4-for-3 Offer
=================================

Enter Price of Pizza #1: 14.99
Enter Price of Pizza #2: 16.99
Enter Price of Pizza #3: 15.99
Enter Price of Pizza #4: 11.00

Order Total is £47.97, a fabulous discount of 19%!
```

A good solution should also handle incorrect input. It is not necessary to provide an exact error message, but
here are some sample error cases to consider. There are probably more.

```text
Beckett Pizza Plaza 4-for-3 Offer
=================================

Enter Price of Pizza #1: 0
Please enter a valid price!
Enter Price of Pizza #1: pepperoni
Please enter a valid price!
Enter Price of Pizza #1: 15.99
Enter Price of Pizza #2: -1.99
Please enter a valid price!
```
