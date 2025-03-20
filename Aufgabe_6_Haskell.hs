-- CountEvens.hs
module CountEvens (countEvens) where

-- Funktion zur Berechnung der Anzahl gerader Zahlen
countEvens :: [Int] -> Int
countEvens xs = length (filter even xs)

main :: IO ()
main = do
    print (countEvens [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
