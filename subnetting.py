import ipaddress


def subnetting(network, amount_of_subnets):

    bits_to_reserve = (amount_of_subnets - 1).bit_length()

    new_prefix = network.prefixlen + bits_to_reserve

    if new_prefix > 32:
        raise ValueError(
            "Nätverket är för litet för att skapa så många subnät."
        )

    return list(network.subnets(new_prefix=new_prefix))


print("                         TESTA SUBNETTING                          ")
print("-------------------------------------------------------------------")
print("I det här programmet kan du dela upp ett IPv4-nätverk i subnät.")
print("-------------------------------------------------------------------")

try:
    amount_of_subnets = int(input("Hur många subnät behöver du? > "))

    if amount_of_subnets <= 0:
        raise ValueError("Antalet subnät måste vara större än 0.")

    network_input = input(
        "Ange nätverket med mask, till exempel 192.168.1.0/24 > "
    )

    network = ipaddress.ip_network(network_input, strict=False)

    subnets = subnetting(network, amount_of_subnets)

    print("")
    print("----------------------------")
    print(f"Ursprungligt nätverk: {network}")
    print(f"Ny nätmask: /{subnets[0].prefixlen}")
    print(f"Antal skapade subnät: {len(subnets)}")
    print("----------------------------")
    print("")

    for counter, subnet in enumerate(subnets, start=1):
        print(f"{counter} Subnät: {subnet}")
        print(f"   Första adress: {subnet.network_address}")
        print(f"   Sista adress:  {subnet.broadcast_address}")
        print("")

    input("Tryck ENTER för att stänga")

except ValueError as error:
    print("----------------------------")
    print(f"Fel: {error}")
    print("----------------------------")
    input("Tryck ENTER för att stänga")
