import datetime

def izveidot_rekinu():
    # 1. Programmu palaižot, uz ekrāna tiek izvadīts īss apraksts par programmas darbību.
    print("Sveiks! Šī programma ir domāta tiem kuriem jāizveido rēķinu koka lādītei\n")

    # 2. Programma prasa lietotājam pēc kārtas ievadīt:
    klients_vards = input("Lūdzu, ievadiet klienta vārdu: ")
    teksts_veltijuma = input("Lūdzu, ievadiet veltījuma tekstu: ")

    # Ievadīt lādītes izmērus (platumu, garumu, augstumu) un kokmateriāla cenu
    izmēri = []
    izmēri.append(int(input("Lūdzu, ievadiet lādītes platumu milimetros: ")))
    izmēri.append(int(input("Lūdzu, ievadiet lādītes garumu milimetros: ")))
    izmēri.append(int(input("Lūdzu, ievadiet lādītes augstumu milimetros: ")))

    materiala_cena = float(input("Lūdzu, ievadiet kokmateriāla cenu (EIRO/m2): "))


    rekins = {
        "datums": datetime.datetime.now(),
        "klienta_vards": klients_vards,
        "veltijuma_teksts": teksts_veltijuma,
        "izmēri_mm": izmēri
    }

    # 4. Apreķini
    darba_samaksa = 15
    PVN_procents = 21

    # Izmanto masīvu aprēķinos
    platums, garums, augstums = izmēri

    # Aprēķinat produkta cenu, reizinot veltījuma teksta garumu un izmērus
    veltijuma_teksta_garums = len(teksts_veltijuma)
    produkta_cena = (veltijuma_teksta_garums * 1.2) + ((platums / 100) * (garums / 100) * (augstums / 100)) / 3 * materiala_cena

    PVN_summa = (produkta_cena + darba_samaksa) * PVN_procents / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa

    rekins["produkta_cena"] = produkta_cena
    rekins["PVN_summa"] = PVN_summa
    rekins["rekina_summa"] = rekina_summa

    # 5. Izdrukā rēķina objektu
    print("\n=== RĒĶINS ===")
    print(f"Datums: {rekins['datums']}")
    print(f"Klients: {rekins['klienta_vards']}")
    print(f"Veltījuma teksts: {rekins['veltijuma_teksts']}")
    print(f"Lādītes izmēri (mm): Platums {platums}, Garums {garums}, Augstums {augstums}")

    print(f"Produkta cena: {rekins['produkta_cena']:.2f} EUR")
    print(f"Darba samaksa: {darba_samaksa:.2f} EUR")
    print(f"PVN (21%): {rekins['PVN_summa']:.2f} EUR")
    print(f"Kopējā summa: {rekins['rekina_summa']:.2f} EUR")

    # 6. Ieraksta rēķina datus .txt failā
    with open(f"rekins_{klients_vards}.txt", "w") as fails:
        fails.write("=== RĒĶINS ===\n")
        fails.write(f"Datums: {rekins['datums']}\n")
        fails.write(f"Klients: {rekins['klienta_vards']}\n")
        fails.write(f"Veltījuma teksts: {rekins['veltijuma_teksts']}\n")
        fails.write(f"Lādītes izmēri (mm): Platums {platums}, Garums {garums}, Augstums {augstums}\n")
        fails.write(f"Produkta cena: {rekins['produkta_cena']:.2f} EUR\n")
        fails.write(f"Darba samaksa: {darba_samaksa:.2f} EUR\n")
        fails.write(f"PVN (21%): {rekins['PVN_summa']:.2f} EUR\n")
        fails.write(f"Kopējā summa: {rekins['rekina_summa']:.2f} EUR\n")
    # 7. Programma beidz darbu
    print("\nRēķins izveidots un saglabāts failā.")
    print("Programma ir beigusies.")

# Palaiž funkciju, lai izveidotu rēķinu
izveidot_rekinu()
