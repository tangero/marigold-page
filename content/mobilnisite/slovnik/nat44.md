---
slug: "nat44"
url: "/mobilnisite/slovnik/nat44/"
type: "slovnik"
title: "NAT44 – Network Address Translation IPv4 to IPv4"
date: 2025-01-01
abbr: "NAT44"
fullName: "Network Address Translation IPv4 to IPv4"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nat44/"
summary: "NAT44 je funkce jádra sítě, která překládá privátní IPv4 adresy na veřejné IPv4 adresy, což umožňuje více zařízením v privátní síti sdílet jednu veřejnou IP adresu. Šetří tak omezený prostor veřejných"
---

NAT44 je funkce jádra sítě, která překládá privátní IPv4 adresy na veřejné IPv4 adresy, což umožňuje více zařízením sdílet jednu veřejnou IP adresu a šetří tak prostor veřejných IPv4 adres.

## Popis

NAT44 funguje jako stavový překladový mechanismus, typicky implementovaný v síťových branách, jako je Packet Data Network Gateway (PGW) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v architekturách 3GPP. Jeho primární funkcí je mapovat privátní, nesměrovatelné IPv4 adresy (definované v RFC 1918) používané v lokální síti účastníka nebo mobilním zařízení na jednu nebo více veřejných, globálně směrovatelných IPv4 adres přiřazených operátorovi. Proces zahrnuje modifikaci IP hlavičky a u některých protokolů i dat vyšších vrstev (jako [FTP](/mobilnisite/slovnik/ftp/) nebo SIP), aby bylo zajištěno end-to-end spojení. Zařízení NAT44 udržuje překladovou tabulku, která váže interní privátní IP adresu a číslo portu na externí veřejnou IP adresu a port. U odchozích paketů nahradí zdrojovou privátní adresu/port veřejným mapováním; u příchozích paketů provede zpětné vyhledání a překlad na základě cílového portu a adresy. Tato tabulka je dynamicky vytvářena z odchozích toků a záznamy jsou typicky po určité době nečinnosti odstraněny. V sítích 3GPP je NAT44 klíčový pro nasazení Carrier-Grade [NAT](/mobilnisite/slovnik/nat/) (CGN), což mobilním operátorům umožňuje obsloužit obrovský počet účastníků s omezeným fondem veřejných IPv4 adres. Integruje se s řízením politik pro správu relací a může komunikovat s Application Function ([AF](/mobilnisite/slovnik/af/)) pro požadavky specifické pro průchod aplikací. Ačkoli je účinný pro úsporu adres, porušuje end-to-end princip internetu a může komplikovat peer-to-peer aplikace a bezpečnostní protokoly síťové vrstvy.

## K čemu slouží

NAT44 byl vytvořen, aby řešil bezprostřední vyčerpání globálního prostoru IPv4 adres. Jak počet zařízení připojených k internetu explodoval, původní 32bitové schéma adresování IPv4, poskytující přibližně 4,3 miliardy adres, se ukázalo jako nedostatečné. NAT44 umožňuje, aby jednu veřejnou IP adresu sdílely stovky nebo tisíce privátních zařízení, což dramaticky prodlužuje životnost stávající IPv4 infrastruktury. Toto poskytlo kritické dočasné řešení, zatímco se průmysl připravoval na dlouhodobou migraci na IPv6. Přineslo také sekundární benefit základního zastření sítě, protože interní hostitelé nejsou z veřejného internetu přímo adresovatelní, což poskytuje jednoduchý firewallový efekt. V sítích 3GPP bylo jeho přijetí hnáněno masivním rozsahem mobilních broadbandových předplatných, kde se přiřazení unikátní veřejné IPv4 adresy každému smartphonu, tabletu nebo IoT zařízení stalo ekonomicky i technicky neproveditelným. Vyřešil problém připojení rychle rostoucí uživatelské základny k IPv4 internetu bez nutnosti okamžitého, rozsáhlého nasazení IPv6.

## Klíčové vlastnosti

- Stavový překlad privátních IPv4 adres na veřejné IPv4 adresy
- Port Address Translation (PAT) pro multiplexování více privátních relací na jednu veřejnou IP adresu
- Dynamické vytváření a správa záznamů vazeb a relací v překladové tabulce
- Integrace s 3GPP řízením politik a účtování pro NAT s povědomím o relaci
- Podpora funkcí Application Layer Gateway (ALG) pro asistování specifickým protokolům (např. SIP, FTP)
- Carrier-Grade škálovatelnost pro nasazení ve velkých sítích poskytovatelů služeb

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [NAT64 – Network Address Translation IPv6 to IPv4](/mobilnisite/slovnik/nat64/)

## Definující specifikace

- **TR 23.975** (Rel-19) — IPv6 Transition Scenarios for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [NAT44 na 3GPP Explorer](https://3gpp-explorer.com/glossary/nat44/)
