import math
import secrets
import string


def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculate password entropy in bits: E = L * log2(R)."""
    return length * math.log2(pool_size)


def generate_password(length: int = 16, include_symbols: bool = True) -> tuple[str, int]:
    """
    Generates a cryptographically secure random password.

    Uses Python's `secrets` module (hardware-level OS entropy) and standard `string`
    constants. Uses str.join() for O(N) memory allocation efficiency.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")

    character_pool = string.ascii_letters + string.digits
    if include_symbols:
        character_pool += string.punctuation

    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password, len(character_pool)


def main() -> None:
    print("=" * 55)
    print("   Enterprise Random Password Generator (DecodeLabs)   ")
    print("=" * 55)

    try:
        user_input = input("Enter desired password length [Recommended >= 15]: ").strip()
        length = int(user_input) if user_input else 16

        if length < 1:
            print("[Error] Password length must be at least 1 character.")
            return

        if length < 8:
            print("[Warning] NIST guidelines recommend at least 8 characters (15+ for high security).")

    except ValueError:
        print("[Error] Invalid input. Please enter a valid integer length.")
        return

    password, pool_size = generate_password(length)
    entropy = calculate_entropy(length, pool_size)

    print("\n" + "-" * 55)
    print(f"Generated Password : {password}")
    print(f"Password Length    : {length} characters")
    print(f"Character Pool Size: {pool_size}")
    print(f"Calculated Entropy : {entropy:.2f} bits")
    print("-" * 55)


if __name__ == "__main__":
    main()