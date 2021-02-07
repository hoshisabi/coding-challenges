function fib (a)
  if a == 1 then
    return 1
  elseif a == 2 then
    return 2
  else
    return fib(a-1) + fib(a-2)
  end
end

i = 1
sum = 0
repeat
  fibret = fib(i)
  i = i + 1
  if (fibret % 2 == 0) then
    sum = sum + fibret
  end
until fibret > 4000000
print ("Stopped at " .. i .. " and sum was " .. sum)