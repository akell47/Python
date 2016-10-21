# While loop
# similar to if - execute code inside of loop if some condition is true
# while continue to execute as long as the condition is true
# not if its true, while it is true

count = 0

if count <= 5:
    print "the if statement says:", count

while count <=5:
    print "the while statement says", count
    # need =+ so that it is not an infinite loop
    count += 1

loop_condition = True

while loop_condition:
    print "I'm Loopy, the loop"
    loop_condition = False

# square numbers 1 to 10
num = 1

while num <= 10:
    print num ** 2
    num += 1
