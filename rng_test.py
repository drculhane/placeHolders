import numpy as np ; import arkouda as ak ; ak.connect()

limit = 10**3 ; Jenny = 8675309

# create the rng, set parameters, do the first call

rng = ak.random.default_rng(Jenny)

c = 10 ; b = 2**32 ; a = -b ; lam = 1

first_call_float_pda = rng.uniform(a,b,c)

np.random.seed(Jenny) # because I get some random #s from np, too

# Do the followimg thing many times.

# Recreate the rng.
# Do a random number of calls to other (or the same) generators.
# Get another uniform.
# Check against the original.

for i in range(limit) :
    rng = ak.random.default_rng(Jenny)
    Ctr = 1 + np.random.randint(50)
    for j in range(Ctr) :
            k = np.random.randint(6)
            match k :
                case 0 :
                    int_pda = rng.integers(a,b,c)
                case 1 :
                    uni_pda = rng.uniform(a,b,c)
                case 2 :
                    poi_pda = rng.poisson(lam,c)
                case 3 :
                    nor_pda = rng.normal(a,b,c)
                case 4 :
                    ran_pda = rng.random(c)
                case 5 :
                    sno_pda = rng.standard_normal(c)
    subsequent_call_float_pda = rng.uniform(a,b,c)
    if (first_call_float_pda == subsequent_call_float_pda).all() :
        print ("Test ",i," failed. Ctr = ",Ctr)
    if i%100 == 0:
        print ("Passing test ",i," of ",limit)

print ("All done.")
ak.disconnect()
