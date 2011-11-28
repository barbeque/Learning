f :: (Num a) => a -> (a, a)
f x = (x - 1, 0)

g :: (Num a) => a -> a
g x = y where
		(y, _) = f x

-- This Haskell file shows off that you can decide to "not take"
-- any part of a tuple returned from a function. Other functional
-- languages (like ML/F#) offer the same functionality.
-- The key point (the only point, really) is the usage of the bottom
-- character on line 6.
