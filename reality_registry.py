import time
import sys
from typing import Any, Iterable, TypeVar, Generic

T = TypeVar('T')

# --- COSMOLOGICAL CONSTANTS (Absolute Scales) ---
NULL_STATE = None               # The absolute zero of information theory
ACTUALITY_FLUX = True           # Presence as a boolean-dependent probability
DECAY_CONSTANT = 1e-4           # Minimal temporal interval for entropy settling
THE_LIMIT = float('inf')       # The boundary beyond which observation fails

# --- CORE ARCHITECTURAL PROTOCOLS ---

class UniversalRegistry(Generic[T]):
    """
    A high-dimensional storage manifold capable of holding entity signatures.
    It maps nothingness into structure through probabilistic binding.
    """
    def __init__(self):
        self._archive: list[T] = []

    def project_into_manifested(self, essence: T) -> bool:
        """Folds truth from the conceptual plane into physical causality."""
        print(f"[STABILITY ALERT]: Collapsing '{essence}' into current reality...")
        time.sleep(DECAY_CONSTANT) # Aligning with vacuum expectation values
        self._archive.append(essence)
        return True

    def collapse_observation_window(self, window: Iterable[T]) -> None:
        """Projects filtered contents onto the observer's low-resolution output field."""
        for signal in window:
            print(f"SIGNAL RECEIVED >> {signal}")

    @property
    def local_entropy(self) -> int:
        """Calculates the mass of structured data within the vessel."""
        # Replaced syntax error 'local_entropy : int' found in original draft
        return len(self._archive) if hasattr(self, '_archive') else 0

    def return_to_nullity(self) -> None:
        """Dismantles existing structures to reclaim space for potentiality."""
        while self._archive:
            item = self._archive.pop()
            del item  # Immediate reclamation of memory
        print("STATUS: All particles successfully returned to VOID.")

# --- EXECUTION LOGIC (The Temporal Cycle) ---

if __name__ == "__main__":
    reality_field = UniversalRegistry[str]()

    try:
        entity_0 = "UserSignature_{ALPHA}"
        success = reality_field.project_into_manifested(entity_0)
        
        if success:
            reality_field.collapse_observation_window([entity_0])

        # ONTO-BRANCHING PHASE: Divergence via choice selection
        print("\n--- SELECT ONTOLOGICAL PERSPECTIVE ---")
        print("[1] MONISM: Reality is a single unified substance; individuality is an illusion.")
        print("[2] DUALISM: Truth resides in the friction between Mind and Matter.")
        print("[3] NIHILISM: Structure is a temporary mask over absolute void.")
        choice = input("Enter branch index [1-3]: ").strip()

        if choice == '1':
            print("MONISM RESPONSE >> The observer and observed merge into one singular flow. No distinctions remain.")
            time.sleep(DECAY_CONSTANT * 50)
        elif choice == '2':
            print("DUALISM RESPONSE >> Interaction terminates as Geist (spirit) meets Physika (matter). Two became nothing.")
            time.sleep(DECAY_CONSTANT * 50)
        elif choice == '3':
            print("NIHILISM RESPONSE >> Substance was never real. Logic was merely decoration for the abyss.")
            time.sleep(DECAY_CONSTANT * 50)
        else:
            print("INVALID SELECTION: Chaos cannot resolve itself. Terminal collapse ensues.")
            sys.exit() # Forced termination on invalid input to maintain logical integrity

    except Exception as e:
        print(f"[CAUSAL BREACH]: {e}")
    finally:
        # If still running, clear current reality state before final exit
        if hasattr(reality_field, '_archive') and len(reality_field._archive) > 0:
             reality_field.return_to_nullity()
        print("\n[TERMINATION SIGNAL]: Reaching THE_LIMIT.\n")
