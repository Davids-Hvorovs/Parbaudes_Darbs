import datetime

class Rekins:
    def __init__(self):
        # Ievadīt klienta datus un lādītes specifikācijas
        self.klients_vards = input("Lūdzu, ievadiet klienta vārdu: ")
        self.teksts_veltijuma = input("Lūdzu, ievadiet veltījuma tekstu: ")

        self.izmēri = []
        self.izmēri.append(int(input("Lūdzu, ievadiet lādītes platumu milimetros: ")))
        self.izmēri.append(int(input("Lūdzu, ievadiet lādītes garumu milimetros: ")))
        self.izmēri.append(int(input("Lūdzu, ievadiet lādītes augstumu milimetros: ")))

        self.materiala_cena = float(input("Lūdzu, ievadiet kokmateriāla cenu (EIRO/m2): "))
        self.datums = datetime.datetime.now()

        # Standarta darba samaksa un PVN procents
        self.darba_samaksa = 15
        self.PVN_procents = 21

    def aprēķināt_produktu(self):
        platums, garums, augstums = self.izmēri
        veltijuma_teksta_garums = len(self.teksts_veltijuma)

        # Produkta cena: teksts + tilpums + materiāla cena
        produkta_cena = (veltijuma_teksta_garums * 1.2) + ((platums / 100) * (garums / 100) * (augstums / 100)) / 3 * self.materiala_cena
        PVN_summa = (produkta_cena + self.darba_samaksa) * self.PVN_procents / 100
        rekina_summa = produkta_cena + self.darba_samaksa + PVN_summa

        self.produkta_cena = produkta_cena
        self.PVN_summa = PVN_summa
        self.rekina_summa = rekina_summa

    def izdrukat_rekinu(self):
        platums, garums, augstums = self.izmēri

        print("\n=== RĒĶINS ===")
        print(f"Datums: {self.datums}")
        print(f"Klients: {self.klients_vards}")
        print(f"Veltījuma teksts: {self.teksts_veltijuma}")
        print(f"Lādītes izmēri (mm): Platums {platums}, Garums {garums}, Augstums {augstums}")
        print(f"Produkta cena: {self.produkta_cena:.2f} EUR")
        print(f"Darba samaksa: {self.darba_samaksa:.2f} EUR")
        print(f"PVN (21%): {self.PVN_summa:.2f} EUR")
        print(f"Kopējā summa: {self.rekina_summa:.2f} EUR")

    def saglabat_rekinu_faila(self):
        platums, garums, augstums = self.izmēri
        with open(f"rekins_{self.klients_vards}.txt", "a") as File:
            File.write("=== RĒĶINS ===\n")
            File.write(f"Datums: {self.datums}\n")
            File.write(f"Klients: {self.klients_vards}\n")
            File.write(f"Veltījuma teksts: {self.teksts_veltijuma}\n")
            File.write(f"Lādītes izmēri (mm): Platums {platums}, Garums {garums}, Augstums {augstums}\n")
            File.write(f"Produkta cena: {self.produkta_cena:.2f} EUR\n")
            File.write(f"Darba samaksa: {self.darba_samaksa:.2f} EUR\n")
            File.write(f"PVN (21%): {self.PVN_summa:.2f} EUR\n")
            File.write(f"Kopējā summa: {self.rekina_summa:.2f} EUR\n")

    def izveidot_rekinu(self):
        print("Sveiks! Šī programma ir domāta tiem, kuriem jāizveido rēķinu koka lādītei.\n")
        self.aprēķināt_produktu()
        self.izdrukat_rekinu()
        self.saglabat_rekinu_faila()
        print("\nRēķins izveidots un saglabāts failā.")
        print("Programma ir beigusies.")
