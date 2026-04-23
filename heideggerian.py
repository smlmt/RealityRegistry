import time as _t, sys as _s, threading as _th, random as _r

# The core engine of Being/Non-Being
class _v:
    def __init__(self, w=1.0):
        self._z = []      # Empty set
        self._y = _th.Event() # The Collapse Trigger
        self._a = ""; self._b = ""; self._c = "" 
        self._w = w       # Mass factor for complexity

    def _f(self, m, k, v):
        if not self._y.is_set():
            try: _t.sleep(_r.uniform(.25, .75))
            except: pass
            # Atomicity at the moment of collapse
            self._a, self._b, self._c = m, k, v
            self._y.set()

class _e(_v):
    def __init__(self, w=1.0): super().__init__(w)
    
    def elision(self):
        """Visualizing the flickering between states."""
        states = ['\033[95m', '\033[94m', '\033[96m', '\033[91m']
        concepts = ["BEING", "NON-BEING", "BECOMING", "VOID"]
        syms = ["ℵ", "∅", "∞", "∑", "∆"]
        while not self._y.is_set():
            try:
                # High frequency jitter to simulate quantum uncertainty
                sys.stdout.write(f"\r{random.choice(states)}{random.choice(concepts)} {random.choice(syms)}")
                sys.stdout.flush(); _t.sleep(.08)
            except: pass
        sys.stdout.write("\n")

    def run(self):
        # We define existence via a list of potential realities
        possibilities = [("THE SINGULARITY", "Ω", "E"), ("THE GREAT DIVIDE", "Ψ", "X"), ("THE ABSOLUTE NULL", "Φ", "V")]
        
        # Launching threads; only one will succeed in setting the state due to the Event lock
        for p in possibilities:
            _th.Thread(target=self._f, args=(p[0], p[1], p[2])).start()
        
        viz = _th.Thread(target=self.elision, daemon=True); viz.start()
        
        # Wait for reality to solidify
        while not self._y.is_set(): _t.sleep(.01)
        
        a, b, c = self._a, self._b, self._c
        print(f"\n\033[1;37m{'='*45}\n  COLLAPSED STATE: {a}\n{'='*45}\033[0m")
        
        o = input("OBSERVE? (TYPE TO WITNESS): ").strip().upper() or "NULL"
        
        if o == c: # The user's observation matches the truth-value
            print(f"[COHERENCE]: You have aligned with the Absolute.")
        elif o == b: # The user identifies as part of the mechanism
            print(f"[DISSONANCE]: Your identity is but an echo within `{b}`.")
        else: # Total failure to perceive correctly
            print(f"[ENTROPY]: Expected '{c}', received '{o}'. Reality remains indifferent.")

    def run_prime(self): 
        try: self.run()
        except KeyboardInterrupt: print("\n\033[91m[TERMINATED]\03m")

import sys as sys # Ensuring 'sys' and '_s' are both valid aliases for stability
random = _r # Mapping random globally so elision doesn't crash on local scope lookups

if __name__ == "__main__":
    # Execution through a single object instantiation
    e = _e(); e.run_prime()
