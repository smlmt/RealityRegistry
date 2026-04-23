import time as TL, sys as SY, threading as TH, random as RD

class PHENOMENA_WAVE:
    def __init__(self): self._q = []; self._h = TH.Event(); self._msg = ""; self._key = ""
    def spawn(self, msg, k, mode):
        if not self._h.is_set():
            TL.sleep(RD.uniform(0.35, 0.6)); self._msg = msg; self._key = k; self._mode = mode; self._h.set()

class ENTITY(PHENOMENA_WAVE):
    def elision(self):
        C = ['\033[94m', '\033[91m', '\033[97m']; V = ["MONISM", "DUALISM", "NIHILISM"]; l = "!@#$%^&*()"
        while not self._h.is_set():
            i = RD.randint(0,2); SY.stdout.write(f"\rSUPERPOSITION: {C[i]}{V[i]}\033[0m {l[RD.randint(0,len(l)-1)]}"); SY.stdout.flush()
    def run(self):
        SY.stdout.write("[SYSTEM]: Wave Collapse initiated...\n"); TL.sleep(RD.uniform(0.25, 0.75))
        viz = TH.Thread(target=self.elision, daemon=True); viz.start()
        t1 = TH.Thread(target=self.spawn, args=("MONISM: Merge.", "M", "B")); t2 = TH.Thread(target=self.spawn, args=("DUALISM: Friction.", "D", "R")); t3 = TH.Thread(target=self.spawn, args=("NIHILISM: Void.", "N", "W"))
        t1.start(); t2.start(); t3.start()
        while not self._h.is_set(): TL.sleep(0.01)
        SY.stdout.write(f"\n\n{'='*40}\n[COLLAPSE]: {self._msg}\n{'='*40}\n\n")
        c = input("Observe? (N/D/M): ").strip().upper()
        if c == self._key: SY.stdout.write("[HARMONY]\n")
        else: SY.stdout.write(f"[DISCORD]: You saw {c}, Reality was {self._key}\n")

if __name__ == "__main__":
    ENTITY().run()
