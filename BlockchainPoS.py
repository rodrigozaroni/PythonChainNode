import random

class BlockchainPoS(Blockchain):
    def __init__(self, stakers):
        super().__init__()
        self.stakers = stakers

    def select_validator(self):
        total_stake = sum(self.stakers.values())
        pick = random.uniform(0, total_stake)
        current = 0
        for validator, stake in self.stakers.items():
            current += stake
            if current >= pick:
                return validator
        return None

stakers = {'Alice': 50, 'Bob': 30, 'Charlie': 20}
blockchain_pos = BlockchainPoS(stakers)

selected_validator = blockchain_pos.select_validator()
print(f"Validador selecionado: {selected_validator}")
