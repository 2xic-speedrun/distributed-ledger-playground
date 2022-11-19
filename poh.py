import hashlib

"""
Idea is that since no hash function is predictable. It has to 
be computed in sequence.

Some data is created and is to be timestamped. 
Then you combine that data with the previous hash.

We know that the data was not created after the hash, because it would have
broken the hash chain.

"""

"""
The cool thing is that verification can happen in parallel.

You just have to split up the sequence of hashes.

"""

"""
To prevent malicious attacks all previous hashes need to refer to the last hash
"""

# The basic idea in code

hash_function = hashlib.sha256

def hash(str):
	return hash_function(str.encode()).hexdigest()

ROOT_HASH = hash("1234")

sequence_i = [
	(ROOT_HASH, 0)
]
for i in range(1, 10):
	sequence_i.append((hash(sequence_i[-1][0] + str(i)), i))

# can run in parallel
def validators_chunk(start_hash, start_counter, items):
	prev_hash = start_hash
	for index, i in enumerate(items[1:]):
		prev_hash = hash(prev_hash + str(i[1]))
		assert i[0] == prev_hash

"""
This can then run in parallel
"""
validators_chunk(
	ROOT_HASH, 0, sequence_i[:5]
)

validators_chunk(
	*sequence_i[5], sequence_i[5:]
)
