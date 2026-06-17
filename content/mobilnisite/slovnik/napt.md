---
slug: "napt"
url: "/mobilnisite/slovnik/napt/"
type: "slovnik"
title: "NAPT – Network Address and Port Translation"
date: 2025-01-01
abbr: "NAPT"
fullName: "Network Address and Port Translation"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/napt/"
summary: "NAPT je síťová funkce, která překládá jak IP adresy, tak čísla portů, což umožňuje více privátním IPv4 zařízením sdílet jednu veřejnou IPv4 adresu. Je klíčová pro úsporu omezeného množství veřejných I"
---

NAPT je síťová funkce, která překládá jak IP adresy, tak čísla portů, aby umožnila více privátním zařízením sdílet jednu veřejnou IPv4 adresu, čímž šetří veřejné adresy v sítích 3GPP.

## Popis

Network Address and Port Translation (NAPT) je základní síťová funkce definovaná v architektuře 3GPP, která primárně funguje v uživatelské rovině pro řešení vyčerpání IPv4 adres. Funguje tak, že upravuje zdrojovou IP adresu a zdrojové číslo portu odchozích IP paketů z uživatelského zařízení (UE) v privátní síti a mapuje je na jednu veřejnou IP adresu a unikátní číslo portu na rozhraní směřujícím do veřejné sítě. Pro příchozí pakety provádí reverzní překlad na základě cílového čísla portu a směruje provoz zpět na správnou privátní IP adresu a port. Tento proces je stavový, což vyžaduje, aby zařízení s NAPT udržovalo překladovou tabulku sledující aktivní relace, která mapuje n-tice privátní IP, privátní port, veřejná IP a veřejný port spolu s identifikátory protokolu.

V ekosystému 3GPP je NAPT často implementován v klíčových síťových prvcích, jako je Packet Data Network Gateway (PGW) v 4G nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Jeho integrace je specifikována pro zpracování provozu pro UE, kterým jsou přiděleny privátní IPv4 adresy, typicky z rozsahů jako 10.0.0.0/8. Tato funkce je klíčová pro nasazení Carrier-Grade [NAT](/mobilnisite/slovnik/nat/) (CGN), což mobilním operátorům umožňuje obsluhovat miliony účastníků s omezeným fondem veřejných IPv4 adres. Překladové mechanismy musí být v souladu s různými standardy [IETF](/mobilnisite/slovnik/ietf/) (jako RFC 3022) pro správné zpracování TCP/UDP/[ICMP](/mobilnisite/slovnik/icmp/) paketů, což zajišťuje, kde je to možné, transparentnost pro aplikace, i když může představovat výzvy pro protokoly, které vkládají IP adresy do svého datového obsahu.

Architektonická role NAPT přesahuje pouhou úsporu adres. Poskytuje vrstvu soukromí a zabezpečení tím, že skrývá interní topologii sítě před veřejným internetem. Nicméně také zavádí složitosti pro peer-to-peer aplikace a služby, které vyžadují iniciaci příchozího připojení, což si žádá doplňkové mechanismy jako techniky pro průchod NAT (např. [ICE](/mobilnisite/slovnik/ice/), STUN, TURN). Ve specifikacích 3GPP je chování a řízení NAPT definováno tak, aby zajistilo interoperabilitu mezi síťovými funkcemi a podporovalo vynucování politik, jako je povolení nebo zakázání NAPT na Access Point Name ([APN](/mobilnisite/slovnik/apn/)) nebo na účastníka na základě operátorské politiky.

## K čemu slouží

NAPT byl zaveden, aby přímo řešil kritický nedostatek globálně směrovatelných IPv4 adres, problém, který se zintenzivnil s exponenciálním růstem zařízení připojených k internetu, zejména v mobilních sítích. Před jeho rozšířeným přijetím se sítě často pokoušely přidělovat každému zařízení unikátní veřejnou IP adresu, což se rychle ukázalo jako neudržitelné. NAPT umožňuje operátorovi přidělit jednu veřejnou IPv4 adresu, která je dynamicky sdílena mezi stovkami nebo tisíci účastníků, což dramaticky prodlužuje využitelnost stávajícího adresního prostoru IPv4.

Motivací pro standardizaci NAPT v rámci 3GPP bylo zajistit konzistentní, interoperabilní a škálovatelnou implementaci napříč všemi dodavateli zařízení pro mobilní sítě. Bez takové standardizace by proprietární implementace [NAT](/mobilnisite/slovnik/nat/) mohly vést k nekompatibilitám služeb, nefunkčnosti aplikací a problémům se správou. Definováním NAPT ve specifikacích jako TS 23.228 a TS 29.238 poskytlo 3GPP jasný rámec pro jeho nasazení v bránových uzlech a integrovalo jej se stávajícími funkcemi správy mobility, účtování a řízení politik. To operátorům umožnilo odložit plnou migraci na IPv6 a zároveň pokračovat v podpoře rozsáhlého ekosystému aplikací a služeb založených na IPv4.

NAPT navíc slouží jako základní prvek pro síťovou bezpečnost a vynucování politik. Centralizací odchozí konektivity prostřednictvím překladového bodu mohou operátoři efektivněji implementovat politiky filtrování, logování a správy provozu. Také zjednodušuje návrh sítě tím, že umožňuje použití privátních adresních schémat uvnitř mobilního jádra, čímž odděluje interní topologii sítě od externí směrovací infrastruktury.

## Klíčové vlastnosti

- Překládá jak zdrojovou IP adresu, tak zdrojové číslo portu pro odchozí pakety
- Udržuje stavovou tabulku relací pro mapování n-tic z privátní (lokální) na veřejnou (globální) adresu/port
- Umožňuje Carrier-Grade NAT (CGN) pro rozsáhlé sdílení adres mezi účastníky
- Integrován do brán jádrové sítě (např. PGW, UPF) dle specifikací 3GPP
- Podporuje klíčové transportní protokoly včetně TCP, UDP a ICMP
- Konfigurovatelný na APN nebo na účastníka prostřednictvím mechanismů řízení politik

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture

---

📖 **Anglický originál a plná specifikace:** [NAPT na 3GPP Explorer](https://3gpp-explorer.com/glossary/napt/)
