-- hsh - The Haskell Shell Terminal
-- Made by Paulo Elienay II

-- imports
import System.Environment

-- testing imports
main = putStrLn "USER: " >> (print =<< getEnv "USER")
