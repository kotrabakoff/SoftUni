class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    bullets = 0

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."

        if self.bullets <= 0:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

# Example:

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
