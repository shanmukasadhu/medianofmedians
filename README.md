# medianofmedians
Python Implementation of Median of Median

Problem Statement: Find k-th smallest number in a given list of numbers.

Psuedocode:
procedure MoM((a1, . . . , an), k) ▷ Find the k-th smallest
if n ≤ 10 then
  Brute force and return the solution
end if
Divide a into n/5 groups of 5 numbers
Let M be the medians of each group 
Find the median of M using MoM(M, |M|/2), call it b and let its
rank in a be k′
if k′ ≥ k then ▷ b is too large
  Remove everything larger than b in a, and get a′
  Return MoM(a′, k)
else ▷ b is too small
  Remove everything smaller than b in a, and get a′
  Return MoM(a′, k − k′)
end if
end procedure
