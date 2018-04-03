
# Made by Arta (Alex Kim)
# This code encrypts a word using a key with the same amount of letters
# It uses alphabetical indices to determine what letter to encrypt to

# Using an alphabet list to generate a list of letters to encrypt from
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
FINAL_LIST = []
for x in range(0, len(alphabet_list)):
    alphabet_list.append(alphabet_list[x].upper())
for y in range(0, int(len(alphabet_list)/2)):
    FINAL_LIST.append(alphabet_list[y])
    FINAL_LIST.append(alphabet_list[len(alphabet_list) - y - 1])


class ArtaEncryptor: # Creating the class

    def __init__(self, word="", key=""):
        self.word = word
        self.key = key

    def get_word(self):
        return self.word

    def get_key(self):
        return self.key

    def set_word(self, new_word):
        self.word = new_word

    def set_key(self, new_key):
        self.key = new_key

    def find_index(self, letter):
        for i in range(0, len(FINAL_LIST)):
            if letter == FINAL_LIST[i]:
                return i

    def pad_key(self):  # Padding the key to match the length of word
        if len(self.word) > len(self.key):
            index_limit = len(self.key)
            for i in range(len(self.key), len(self.word)):
                self.key += self.key[i-index_limit]
        else:
            new_key = ""
            for i in range(0, len(self.word)):
                new_key += self.key[i]
            self.set_key(new_key)

    def encrypt(self):  # Encryption is done by adding the letter at i position for both word and key
                        # Uses i as index to find the corresponding letter in FINAL_LIST
        encrypted = ""
        self.pad_key()
        for i in range(0, len(self.get_word())):
            encrypted_letter = FINAL_LIST[(self.find_index(self.get_word()[i]) + self.find_index(self.get_key()[i])) % 52]
            encrypted += encrypted_letter
        return encrypted

    def decrypt(self):  # Decryption is done by the same mechanism, but reversed from encrypt()
        decrypted = ""
        self.pad_key()
        for i in range(0, len(self.get_word())):
            decrypted_letter = FINAL_LIST[self.find_index(self.get_word()[i]) - self.find_index(self.get_key()[i])]
            decrypted += decrypted_letter
        return decrypted


def main():
    arta_key = input("Enter the key : ")
    choice = input("Encrypt or Decrypt ? ( E/D ): ")
    if choice in ["E", "e"]:
        arta_word = input("Enter the word you want to encrypt : ")
        arta_encryption = ArtaEncryptor(arta_word, arta_key)
        print("The encrypted word is " + arta_encryption.encrypt())
    elif choice in ["D", "d"]:
        arta_word = input("Enter the word you want to decrypt : ")
        arta_encryption = ArtaEncryptor(arta_word, arta_key)
        print("The decrypted word is " + arta_encryption.decrypt())
    else:
        print("Invalid input")


if __name__ == '__main__':
    main()
