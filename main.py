import random

# Daftar hewan-hewan
HEWAN_LIST = [
    # Hewan berkaki empat
    "ayam", "ular", "rusa", "gajah", "harimau", "unta", "badak", "kucing", "anjing", "sapi",
    "kerbau", "kuda", "domba", "kambing", "babi", "onta", "zebu", "llama", "alpaka", "moose",
    "rusa", "elk", "bison", "yak", "gnu", "antelop", "gazelle", "impala", "kudu", "oryx",
    "lemur", "tarsier", "loris", "maki", "beruk", "monyet", "simpanse", "gorila", "orangutan", "gibbon",
    "beruang", "panda", "berang", "lutra", "weasel", "musang", "rakun", "badger", "porcupine", "landak",
    "tikus", "tuan", "tuan", "kelinci", "kelinci", "arnab", "tupaia", "bunglon", "iguana", "basilisk",
    "tokek", "kadal", "cicak", "bunglon", "ular", "ular", "cobra", "python", "boa", "viper",
    
    # Hewan terbang
    "burung", "ayam", "bebek", "angsa", "itik", "trulek", "merpati", "dara", "burung", "elang",
    "alap", "rajawali", "elang", "burung", "burung", "nuri", "kakak", "lovebird", "kakatua", "macaw",
    "budgerigar", "finch", "sparrow", "robin", "wren", "nightingale", "lark", "swallow", "swift", "hoopoe",
    "woodpecker", "cuckoo", "owl", "eagle", "kestrel", "peregrine", "hawk", "vulture", "stork", "crane",
    "heron", "egret", "ibis", "flamingo", "pelican", "cormorant", "gannet", "penguin", "albatross", "petrel",
    "kingfisher", "bee-eater", "roller", "hoopoe", "hornbill", "toucan", "parrot", "parakeet", "budgie", "lory",
    "lorikeet", "kea", "kaka", "cockatoo", "macaw", "amazon", "grey", "african", "eclectus", "vasa",
    "bat", "kelelawar", "codot", "emeu", "emu", "ostrich", "rhea", "cassowary", "kiwi", "tinamou",
    
    # Hewan air
    "ikan", "ikan", "nila", "bawal", "mujair", "lele", "gurame", "mas", "karper", "belut",
    "patin", "gabus", "tawes", "barbel", "ikan", "bandeng", "milkfish", "anchovies", "sardine", "herring",
    "salmon", "trout", "tuna", "bonito", "mackerel", "perch", "pike", "carp", "catfish", "dory",
    "flounder", "cod", "haddock", "halibut", "sole", "turbot", "grouper", "snapper", "barramundi", "mullet",
    "bass", "bream", "carp", "eel", "catfish", "pufferfish", "seahorse", "pipefish", "lionfish", "scorpionfish",
    "stonefish", "rayfish", "manta", "eagle", "ray", "stingray", "guitar", "sawfish", "shark", "whale",
    "dolphin", "porpoise", "manatee", "dugong", "sea", "lion", "seal", "walrus", "otter", "beaver",
    "platypus", "echidna", "turtle", "tortoise", "crocodile", "alligator", "caiman", "gharial", "frog", "toad",
    "salamander", "newt", "axolotl", "caecilian", "octopus", "squid", "cuttlefish", "nautilus", "crab", "lobster",
    "shrimp", "prawn", "crawfish", "crayfish", "barnacle", "scallop", "clam", "mussel", "oyster", "snail",
    "slug", "worm", "earthworm", "leech", "sea", "star", "starfish", "sea", "urchin", "brittle", "star",
    
    # Hewan darat lainnya
    "singa", "harimau", "leopard", "macan", "panther", "jaguar", "cougar", "puma", "lynx", "bobcat",
    "serval", "caracal", "cheetah", "ocelot", "margay", "jaguarundi", "pronghorn", "chamois", "ibex", "markhor",
    "argali", "bighorn", "mouflon", "bharal", "takin", "muskox", "saola", "megamuntjac", "deer", "musk",
    "cheetal", "hog", "sambar", "fallow", "roe", "white", "black", "sika", "axis", "pampas",
    "pudu", "brocket", "muntjac", "chevrotain", "musk", "deer", "pronghorn", "giraffidae", "okapi", "camelid",
    "camel", "dromedary", "bactrian", "llama", "guanaco", "vicuna", "alpaca", "equine", "horse", "donkey",
    "zebra", "quagga", "onager", "kiang", "kulan", "hemione", "wild", "ass", "bovine", "ox",
    "aurochs", "gayal", "zebu", "yak", "banteng", "anoa", "buffalo", "african", "carabao", "water",
    "bison", "american", "european", "caribou", "pronghorn", "gazelle", "dorcas", "springbok", "gemsbok", "oryx",
    "addax", "dibatag", "dik", "dik", "duiker", "chevrotain", "pronghorn", "chamois", "goral", "serow",
    "gorilla", "chimpanzee", "bonobo", "orangutan", "gibbon", "siamang", "monkey", "macaque", "baboon", "mandrill",
    "gelada", "colobus", "langur", "leaf", "monkey", "proboscis", "nasalis", "douc", "snub", "nosed",
    "howler", "spider", "woolly", "capuchin", "squirrel", "titi", "night", "monkey", "owl", "monkey",
    "tarsier", "lemur", "ring", "tailed", "ruffed", "sifaka", "indri", "aye", "aye", "loris",
    "sloth", "anteater", "armadillo", "pangolin", "echidna", "platypus", "mole", "shrew", "hedgehog", "tenrec",
    "golden", "mole", "elephant", "shrew", "hyrax", "aardvark", "rabbit", "hare", "pika", "rodent",
    "squirrel", "chipmunk", "prairie", "dog", "marmot", "groundhog", "dasyurid", "marsupial", "mole", "shrew",
    "quokka", "wombat", "koala", "possum", "glider", "sugar", "glider", "brushtail", "possum", "cuscus",
    "tree", "kangaroo", "wallaby", "quokka", "potoroo", "burrowing", "bettong", "rat", "kangaroo", "musky",
    "rat", "kangaroo", "boongary", "rainforest", "boomer", "gray", "kangaroo", "red", "kangaroo", "eastern",
    "grey", "kangaroo", "western", "grey", "kangaroo", "antilopine", "kangaroo", "musky", "rat", "kangaroo",
    
    # Hewan mitologi/legenda
    "naga", "phoenix", "griffin", "dragon", "unicorn", "pegasus", "sphinx", "hydra", "basilisk", "wyvern"
]

# Normalisasi daftar hewan (hapus duplikat dan urutkan)
HEWAN_LIST = sorted(list(set(HEWAN_LIST)))

def main():
    print("=" * 50)
    print("🎮 GAME SAMBUNG KATA HEWAN 🎮")
    print("=" * 50)
    print("\nSelamat datang! Permainan ini dimulai dengan kata hewan.")
    print("Anda harus menyambung dengan hewan lain yang dimulai")
    print("dengan huruf terakhir dari hewan sebelumnya.")
    print("\nContoh: AYAM -> MERPATI -> IKAN -> NURI -> IGUANA -> ANGSA")
    print("\nTulis 'keluar' untuk berhenti bermain.\n")
    
    while True:
        pilihan = input("\n1. Bermain\n2. Keluar\nPilihan (1/2): ").strip().lower()
        
        if pilihan == "2" or pilihan == "keluar":
            print("\nTerima kasih telah bermain! Sampai jumpa! 👋")
            break
        elif pilihan == "1":
            mainkan_game()
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

def mainkan_game():
    # Pilih hewan pertama secara random
    hewan_sekarang = random.choice(HEWAN_LIST)
    daftar_hewan = [hewan_sekarang]
    
    print(f"\n📍 Hewan pertama: {hewan_sekarang.upper()}")
    print(f"Hewan selanjutnya harus dimulai dengan huruf: '{hewan_sekarang[-1].upper()}'")
    
    skor = 0
    
    while True:
        hewan_input = input(f"\n➡️  Hewan berikutnya (harus dimulai '{hewan_sekarang[-1].upper()}'): ").strip().lower()
        
        # Pengecekan input kosong atau keluar
        if hewan_input == "keluar" or hewan_input == "":
            print(f"\n⏹️  Game berakhir!")
            print(f"📊 Skor akhir: {skor} kata")
            print(f"🐾 Daftar hewan yang disambung: {' → '.join([h.upper() for h in daftar_hewan])}")
            break
        
        # Cek apakah huruf pertama sesuai
        if hewan_input[0] != hewan_sekarang[-1]:
            print(f"❌ Salah! Harus dimulai dengan '{hewan_sekarang[-1].upper()}'")
            print(f"💔 Game Over!")
            print(f"📊 Skor akhir: {skor} kata")
            print(f"🐾 Daftar hewan yang disambung: {' → '.join([h.upper() for h in daftar_hewan])}")
            break
        
        # Cek apakah hewan sudah digunakan sebelumnya
        if hewan_input in daftar_hewan:
            print(f"❌ '{hewan_input.upper()}' sudah digunakan!")
            print(f"💔 Game Over!")
            print(f"📊 Skor akhir: {skor} kata")
            print(f"🐾 Daftar hewan yang disambung: {' → '.join([h.upper() for h in daftar_hewan])}")
            break
        
        # Cek apakah hewan ada di daftar (opsional, untuk mode lebih sulit)
        if hewan_input not in HEWAN_LIST:
            tanya = input(f"⚠️  '{hewan_input.upper()}' tidak ada di database. Terima? (y/n): ").lower().strip()
            if tanya != "y":
                print(f"❌ Hewan tidak diterima!")
                print(f"💔 Game Over!")
                print(f"📊 Skor akhir: {skor} kata")
                print(f"🐾 Daftar hewan yang disambung: {' → '.join([h.upper() for h in daftar_hewan])}")
                break
        
        # Hewan diterima
        daftar_hewan.append(hewan_input)
        hewan_sekarang = hewan_input
        skor += 1
        
        print(f"✅ Benar! (Skor: {skor})")
        print(f"🐾 Kata selanjutnya harus dimulai dengan: '{hewan_sekarang[-1].upper()}'")

if __name__ == "__main__":
    main()
