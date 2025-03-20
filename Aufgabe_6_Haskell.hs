module Aufgabe_6_Haskell (zaehlGeradeZahlen) where

-- Funktion nimmt eine Liste von Integern entgegen und gibt die Anzahl der geraden Zahlen in der Liste zurück
zaehlGeradeZahlen :: [Int] -> Int
-- filtert die geraden Zahlen aus der Liste und gibt die Länge der Liste zurück
zaehlGeradeZahlen xs = length (filter even xs)

main :: IO ()
main = do
    print (zaehlGeradeZahlen [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
