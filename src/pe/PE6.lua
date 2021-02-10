--
-- Created by IntelliJ IDEA.
-- User: decha
-- Date: 2/10/2021
-- Time: 1:06 AM
-- To change this template use File | Settings | File Templates.
--

function sumofsquares(a)
    sum = 0
    for t = 1, a do
        sum = sum + t^2
    end
    return sum
end

function squareofsums(a)
    sum = 0
    for t = 1, a do
        sum = sum + t
    end
    return sum^2
end

sqofs = squareofsums(100)
sofsq = sumofsquares(100)
print ("Difference between sum of squares " .. sofsq .. " and square of sums " .. sqofs .. " is " .. sqofs - sofsq)


