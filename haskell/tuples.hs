f :: Integer -> (Integer, Integer)
f x = (x - 1, 0)

g :: Integer -> Integer
g x = y where
		(y, _) = f x
