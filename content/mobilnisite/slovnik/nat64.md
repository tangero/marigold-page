---
slug: "nat64"
url: "/mobilnisite/slovnik/nat64/"
type: "slovnik"
title: "NAT64 – Network Address Translation IPv6 to IPv4"
date: 2025-01-01
abbr: "NAT64"
fullName: "Network Address Translation IPv6 to IPv4"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nat64/"
summary: "NAT64 je překladová technologie, která umožňuje klientům s podporou pouze IPv6 komunikovat se servery s podporou pouze IPv4 na internetu. Je klíčovým přechodovým mechanismem v sítích 3GPP pro nasazení"
---

NAT64 je překladová technologie v sítích 3GPP, která umožňuje klientům s podporou pouze IPv6 komunikovat se servery s podporou pouze IPv4 a poskytuje zpětnou kompatibilitu během přechodu na IPv6.

## Popis

NAT64 je stavový mechanismus pro překlad síťových adres a protokolů definovaný v [IETF](/mobilnisite/slovnik/ietf/) RFC a přijatý 3GPP. Umožňuje komunikaci mezi sítí IPv6 a sítí IPv4 syntézou IPv4 adres z IPv6 adres a překladem hlaviček paketů mezi těmito dvěma protokoly. Typické nasazení NAT64 zahrnuje funkci překladače NAT64, často umístěnou společně s PGW nebo [UPF](/mobilnisite/slovnik/upf/), a server DNS64. Proces začíná, když klient s podporou pouze IPv6 dotazuje název domény. Server DNS64, pokud v odpovědi obdrží pouze záznamy IPv4 (A záznamy), syntetizuje IPv6 adresu vložením IPv4 adresy do určené předpony IPv6 (obvykle 64:ff9b::/96). Klient pak posílá pakety na tuto syntetizovanou IPv6 adresu. Překladač NAT64, který vidí provoz určený pro svou nakonfigurovanou předponu, extrahuje vloženou IPv4 adresu, přeloží hlavičku IPv6 paketu na hlavičku IPv4 a udržuje stavové mapování pro relaci. Pro návratový provoz ze serveru IPv4 překladač proces obrátí a pro klienta zrekonstruuje IPv6 paket. NAT64 podporuje tři hlavní režimy: bezstavový (stateless), stavový (stateful) a 464XLAT. Stavový NAT64 je v mobilních sítích nejběžnější a zpracovává TCP, UDP a [ICMP](/mobilnisite/slovnik/icmp/). Upravuje hlavičky síťové a transportní vrstvy a pro některé protokoly může vyžadovat aplikační brány (ALG). Jeho architektura je klíčová pro mobilní operátory přijímající přístupové sítě pouze s IPv6, protože jim umožňuje přidělovat zařízením IPv6 adresy a zároveň poskytovat bezproblémový přístup k celému internetu.

## K čemu slouží

NAT64 byl vyvinut pro usnadnění přechodu z IPv4 na IPv6. Zatímco IPv6 nabízí podstatně větší adresní prostor, jádro obsahu a služeb internetu zůstalo převážně na IPv4, což vytvořilo problém kompatibility. Nasazení duálního zásobníku (IPv4 a IPv6 současně) na všech zařízeních a sítích bylo složité a stále spotřebovávalo vzácné IPv4 adresy. NAT64 poskytuje síťovým operátorům cestu k nasazení přístupových sítí pouze s IPv6 pro nové účastníky a zařízení, čímž uvolňuje IPv4 adresy pro starší služby nebo jiné využití. Řeší kritický problém připojení zařízení pouze s IPv6 k internetu IPv4, což je nezbytné pro postupnou a zvládnutelnou migraci. V 3GPP jeho standardizace zajistila, že mobilní operátoři mohli s důvěrou zavádět IPv6 s vědomím, že uživatelský zážitek nebude degradován nedostatkem konektivity IPv4. Řešil omezení dřívějších přechodových technologií, jako je duální zásobník, který vyžadoval udržování dvou protokolových zásobníků a adres, a dalších překladových metod, které byly méně škálovatelné nebo transparentní.

## Klíčové vlastnosti

- Stavový překlad IPv6 paketů na IPv4 pakety a naopak
- Integrace s DNS64 pro automatickou syntézu IPv6 adres ze záznamů DNS IPv4
- Podpora jednosměrné komunikace od klientů pouze s IPv6 k serverům IPv4
- Udržování tabulek vazeb a stavů relací pro mapování protokolů a adres
- Kompatibilita s klíčovými transportními protokoly (TCP, UDP, ICMP)
- Umožnění strategií nasazení sítí pouze s IPv6

## Definující specifikace

- **TR 23.975** (Rel-19) — IPv6 Transition Scenarios for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [NAT64 na 3GPP Explorer](https://3gpp-explorer.com/glossary/nat64/)
