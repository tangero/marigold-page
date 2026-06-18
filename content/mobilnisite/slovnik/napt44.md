---
slug: "napt44"
url: "/mobilnisite/slovnik/napt44/"
type: "slovnik"
title: "NAPT44 – Network Address and Port Translation IPv4 to IPv4"
date: 2025-01-01
abbr: "NAPT44"
fullName: "Network Address and Port Translation IPv4 to IPv4"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/napt44/"
summary: "NAPT44 je specifický typ překladu síťových adres a portů (Network Address and Port Translation), kde jsou jak interní (privátní), tak externí (veřejná) rodina adres IPv4. Jedná se o standardní funkci"
---

NAPT44 je standardní funkce Carrier-Grade NAT, která mapuje mnoho privátních IPv4 adres na sdílený fond veřejných IPv4 adres pomocí překladu síťových adres a portů (Network Address and Port Translation), přičemž obě rodiny adres jsou IPv4.

## Popis

NAPT44 explicitně označuje funkci překladu síťových adres a portů (Network Address and Port Translation), kde k překladu dochází výhradně v doméně IPv4 adres. Přijímá pakety pocházející od UE s privátními IPv4 adresami (např. z rozsahů 10.0.0.0/8, 172.16.0.0/12 nebo 192.168.0.0/16) a překládá jejich zdrojovou IP adresu a číslo zdrojového portu na veřejnou IPv4 adresu a jedinečný port z operátorova fondu. Přípona '44' označuje IPv4-IPv4, čímž se odlišuje od překladových mechanismů zahrnujících IPv6 (např. [NAPT64](/mobilnisite/slovnik/napt64/)). Jedná se o klíčovou technologii stojící za většinou nasazení Carrier-Grade [NAT](/mobilnisite/slovnik/nat/) (CGN) v mobilních sítích.

Provozně funkce NAPT44, typicky integrovaná v [PGW](/mobilnisite/slovnik/pgw/) nebo [UPF](/mobilnisite/slovnik/upf/), udržuje dynamickou mapovací tabulku. Každá položka koreluje 5-tici z interní sítě (zdrojová IP, zdrojový port, cílová IP, cílový port, transportní protokol) s přeloženou 5-ticí používanou v externí síti. Pro odchozí TCP nebo [UDP](/mobilnisite/slovnik/udp/) relace přiděluje jedinečný externí port pro každý interní socket, což umožňuje multiplexování tisíců současných spojení od různých UE na jednu veřejnou IP adresu. Překlad je obousměrný a stavový; pro příchozí pakety se veřejná cílová IP adresa a port používají jako klíč pro vyhledání odpovídající privátní IP adresy a portu, čímž je zajištěno správné doručení.

Technická implementace musí zvládat různé okrajové případy: fragmentaci paketů, překlad chybových zpráv [ICMP](/mobilnisite/slovnik/icmp/) a keep-alive mechanismy pro dlouhodobé relace. Pro podporu aplikací citlivých na chování NAT implementace NAPT44 často obsahují ALG (Application Layer Gateways) pro specifické protokoly jako [SIP](/mobilnisite/slovnik/sip/), [FTP](/mobilnisite/slovnik/ftp/) nebo RTSP, které upravují datovou část aplikace tak, aby odrážela přeložené adresy. Dále specifikace 3GPP definují rozhraní pro správu NAPT44, což operátorům umožňuje monitorovat velikost překladových tabulek, vazby a konfigurovat parametry jako rozsahy přidělování portů a časové limity relací pro optimalizaci využití zdrojů a zajištění kontinuity služeb.

## K čemu slouží

NAPT44 existuje jako standardizované, škálovatelné řešení základního ekonomického a technického omezení způsobeného vyčerpáním IPv4 adres pro operátory mobilních sítí. Jeho primárním účelem je umožnit poskytovateli služeb připojit extrémně velký počet koncových zařízení k veřejnému IPv4 internetu pomocí relativně velmi malého fondu globálně unikátních IPv4 adres. Tím přímo řeší problém omezeného adresního prostoru IPv4 (přibližně 4,3 miliardy adres), který je nedostatečný pro desítky miliard připojených zařízení.

Před všudypřítomným nasazením NAPT44 v přepravních sítích čelili operátoři neudržitelné volbě mezi získáváním stále dražších veřejných IPv4 adres a omezením růstu. NAPT44 poskytlo praktickou a okamžitou strategii zmírnění. Umožnilo použití privátního IPv4 adresování pro celou základnu účastníků v rámci mobilní páteřní sítě, přičemž veřejné adresy jsou vyžadovány pouze na hraničních překladových bodech. Tato architektonická změna proměnila vzácný zdroj (veřejné IPv4 adresy) ve sdílený, multiplexovaný zdroj, což dramaticky zvýšilo efektivitu využití adres.

Kromě šetření adres slouží NAPT44 i provozním účelům. Zjednodušuje správu sítě vytvořením jasné demarkační linie mezi privátní služební sítí a veřejným internetem. Může sloužit jako přirozený bod vynucování politiky pro filtrování provozu, zákonné odposlechy a účtování založené na využití. Ačkoli se nejedná o bezpečnostní funkci jako takovou, zakrývá interní strukturu sítě a poskytuje základní úroveň utajení. Jeho standardizace v 3GPP zajistila, že všichni výrobci implementovali kompatibilní, interoperabilní a vysoce výkonná řešení CGN, což bylo klíčové pro udržení kvality služeb a kompatibility aplikací v sítích více výrobců.

## Klíčové vlastnosti

- Provádí stavový překlad IPv4-IPv4 adres a portů pro TCP, UDP a ICMP
- Klíčová technologie umožňující Carrier-Grade NAT (CGN) v mobilních sítích
- Dynamicky přiděluje porty ze sdíleného fondu pro multiplexování mnoha privátních IP adres na méně veřejných IP adres
- Obsahuje podporu Application Layer Gateways (ALG) pro asistenci protokolům citlivým na NAT
- Integrováno s řízením politik pro povolení/zákaz překladu na APN nebo účastníka
- Poskytuje záznamy a informace o vazbách pro řešení problémů a regulatorní shodu

## Související pojmy

- [NAT44 – Network Address Translation IPv4 to IPv4](/mobilnisite/slovnik/nat44/)

## Definující specifikace

- **TR 23.975** (Rel-19) — IPv6 Transition Scenarios for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [NAPT44 na 3GPP Explorer](https://3gpp-explorer.com/glossary/napt44/)
