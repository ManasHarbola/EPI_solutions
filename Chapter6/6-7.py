def phone_mnemonic(phone_number):
    table = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
    
    mnemonics, sub_mnemonic = [], [0] * len(phone_number)

    def create_mnemonic(idx):
        if idx == len(phone_number):
            mnemonics.append(''.join(sub_mnemonic))
        else:
            for symbol in table[int(phone_number[idx])]:
                sub_mnemonic[idx] = symbol
                create_mnemonic(idx + 1)
    
    create_mnemonic(0)
    return mnemonics
    
print(phone_mnemonic("27"))
