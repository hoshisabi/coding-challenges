for a = 1,1000 do
  for b = 1,1000 - a do
    c = 1000 - (a + b)
    if (a + b + c == 1000) and (a^2 + b^2 == c^2) then
      print("a=" .. a .. " b=" .. b .. " c=" .. c .. " prod=" .. a * b * c)
      return
    end
  end
end