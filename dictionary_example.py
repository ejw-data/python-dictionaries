import os


votes = ['mo', 'mo', 'jessica', 'erin', 'jessica', 'mo', 'taylor']

# initialize empty dictionary
election_results = {}

# add item to dictionary
election_results["mo"] = 1
print(f'Here is the first vote added to dictiony: "mo" has {election_results["mo"]} votes')

election_results["mo"] = 32
print(f'Here is "mo" updated: "mo" has {election_results["mo"]} votes')

try:  
    print(f'What happens if we search for a name not in the dictionary?  {election_results["jim"]}')
except: 
    print(f'We get an error of a value not found if we search for election_results["jim"]')


print(f"what does this command do?  {election_results.keys()}")


# why does this fail?  when would it work?
# what if we run it now and then rerun it after uncommenting the next line?  What is the difference?
# election_results['mo'] = 1

for vote in votes:
    election_results[vote] = election_results[vote] + 1

# early code draft
# grab one vote at a time
for vote in votes:
    # check if that votes (key) is in the dictionary
    # if true then add one to the existing key
    if vote in election_results.keys():
        election_results[vote] = election_results[vote] + 1
    # if false then add key to dictionary with a value of 1
    else:
        election_results[vote] = 1

print(election_results)

# Intermediate code
# grab one vote at a time
for vote in votes:
    # check if that votes (key) is in the dictionary
    # if true then add one to the existing key
    if vote in election_results.keys():
        election_results[vote] = election_results[vote] + 1
    # if false then add key to dictionary with a value of 1
    else:
        election_results[vote] = 1

print(election_results)



# Final code
# grab one vote at a time
for vote in votes:
    # check if that votes (key) is in the dictionary
    # if true then add one to the existing key
    if vote in election_results.keys():
        election_results[vote] += 1
    # if false then add key to dictionary with a value of 1
    else:
        election_results[vote] = 1

print(election_results)




