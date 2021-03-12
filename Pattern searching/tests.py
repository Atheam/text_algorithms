from kmp import kmp_string_matching
from finite_automata import finite_automata_search
from naive import naive_pattern
from kmp import prefix_function
from finite_automata import build_automata
import time



def measure_time(algorithm,text,pattern):
	start = time.time()
	algorithm(text,pattern)
	end = time.time()
	return end-start

def measure_build_time(algorithm,pattern):
	start = time.time()
	algorithm(pattern)
	end = time.time()
	return end-start


filename = "test_text.txt"
pattern = "art"



with open(filename) as f:
	text = f.read()


#print only once and check if output is the same for clarity of output
print(naive_pattern(text,pattern))
print(naive_pattern(text,pattern) == finite_automata_search(text,pattern) == kmp_string_matching(text,pattern))

#naive worst case

print("Time comparision based on text file")
print("Naive algorithm time: ",measure_time(naive_pattern, text, pattern))
print("Finite automata time: ", measure_time(finite_automata_search, text, pattern ))
print("KMP algorithm time: ", measure_time(kmp_string_matching, text, pattern ))




naive_worst_text = "A"*1000000 

naive_worst_pattern = "A"*100000 

print("Time comparistion based on worst naive algorithm case")
print("Naive algorithm time: ",measure_time(naive_pattern, naive_worst_text, naive_worst_pattern))
print("Finite automata time: ", measure_time(finite_automata_search, naive_worst_text, naive_worst_pattern ))
print("KMP algorithm time: ", measure_time(kmp_string_matching, naive_worst_text, naive_worst_pattern ))


print()

#automata worst case
automata_worst_pattern = "abcdefghijklmnoprstuwxyz"*30



print("Automata build time: ",measure_build_time(build_automata,pattern = automata_worst_pattern))
print("Prefix function build time: ",measure_build_time(prefix_function,pattern= automata_worst_pattern))







