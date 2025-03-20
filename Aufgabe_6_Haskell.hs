module Aufgabe_6_Haskell (zaehlGeradeZahlen) where

-- Funktion zaehlGeradeZahlen nimmt eine Liste von Integern entgegen und wird die Anzahl der geraden Zahlen zurückgeben.
zaehlGeradeZahlen :: [Int] -> Int
-- Filtert die geraden Zahlen aus der Liste und gibt die Länge der Liste zurück.
zaehlGeradeZahlen xs = length (filter even xs)

main :: IO ()
main = do
    print (zaehlGeradeZahlen [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

