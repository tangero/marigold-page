---
slug: "lstf"
url: "/mobilnisite/slovnik/lstf/"
type: "slovnik"
title: "LSTF – Location Subscriber Translation Function"
date: 2025-01-01
abbr: "LSTF"
fullName: "Location Subscriber Translation Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lstf/"
summary: "LSTF je síťová funkce v architektuře služeb polohování (LCS), která překládá identifikátory účastníků (jako MSISDN) na síťové směrovací adresy (jako IP adresy nebo adresy signalizace SS7). Umožňuje po"
---

LSTF (Location Subscriber Translation Function) je síťová funkce v architektuře služeb polohování (Location Services), která překládá identifikátory účastníků na síťové směrovací adresy, aby umožnila správné směrování požadavků na polohové služby.

## Popis

Location Subscriber Translation Function (LSTF) je kritická komponenta definovaná ve specifikaci 3GPP TS 23.271 pro architekturu služeb polohování ([LCS](/mobilnisite/slovnik/lcs/)). Jejím hlavním úkolem je provádět překlad identifikátorů, konkrétně mapování veřejné identity účastníka, jako je [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Subscriber International [ISDN](/mobilnisite/slovnik/isdn/) Number) nebo [IMSI](/mobilnisite/slovnik/imsi/) (International Mobile Subscriber Identity), na aktuální síťové směrovací informace potřebné k dosažení zařízení uživatele nebo obsluhujícího síťového uzlu. Tyto směrovací informace typicky zahrnují IP adresu ústředny [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Center) nebo uzlu SGSN (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node) v okruhově přepínané a paketově přepínané doméně, nebo v novějších vydáních entity [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) či [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function). LSTF funguje jako adresářová nebo rezoluční služba v rámci systému LCS.

Z architektonického hlediska je LSTF často implementována jako součást nebo v úzké součinnosti s Gateway Mobile Location Center (GMLC), což je hlavní vstupní bod pro externí klienty LCS žádající o polohové informace. Když klient LCS (např. síť tísňových služeb, orgán pro zákonný odposlech nebo komerční poskytovatel služeb) odešle požadavek na polohu s MSISDN účastníka, GMLC se dotazuje LSTF, aby získal adresu aktuálně obsluhujícího uzlu. LSTF může tento překlad provést dotazem na HLR (Home Location Register) nebo HSS (Home Subscriber Server), aby získala profil účastníka a informace o aktuálně obsluhujícím uzlu. V některých nasazeních může být funkce LSTF integrována přímo do GMLC nebo HLR/HSS, ale logicky se jedná o samostatnou funkci, která abstrahuje proces překladu.

Jak to funguje, zahrnuje posloupnost kroků: Po přijetí požadavku na překlad od GMLC použije LSTF poskytnutý identifikátor účastníka k dotazování HLR/HSS přes standardní rozhraní jako MAP (Mobile Application Part) nebo Diameter. HLR/HSS odpoví adresou MSC, SGSN, MME nebo AMF, který aktuálně obsluhuje účastníka. LSTF pak tuto směrovací adresu vrátí GMLC, který může následně přeposlat požadavek na polohu správnému obsluhujícímu uzlu (který pak zapojí rádiovou přístupovou síť k určení polohy zařízení). Tento proces je klíčový, protože mobilní zařízení jsou ze své podstaty pohyblivá; jejich připojovací bod k síti se mění a statický identifikátor jako MSISDN neobsahuje směrovací informace. LSTF zajišťuje, že požadavky na polohu jsou dynamicky směrovány do správné části sítě, což umožňuje včasné a přesné získání polohy pro služby jako E911, sledování vozového parku nebo polohově cílená reklama.

## K čemu slouží

LSTF byla vytvořena k řešení základního problému směrování v mobilních polohových službách: externí klienti znají účastníka podle veřejného identifikátoru (jako telefonní číslo), ale síť potřebuje znát aktuální technickou adresu síťového uzlu (jako MSC), který daného účastníka obsluhuje, aby doručila požadavek na polohu. Před standardizovanými funkcemi jako LSTF se polohové služby spoléhaly na ad-hoc metody nebo vyžadovaly, aby klienti měli přímý přístup k databázím jádra sítě, což bylo nejisté, neefektivní a neškálovatelné. LSTF poskytuje standardizovaného, bezpečného zprostředkovatele, který abstrahuje vnitřní topologii sítě a správu mobility od externích entit.

Historicky, jak nabývaly polohové služby na významu pro tísňové služby (E112/E911), zákonné odposlechy a komerční aplikace v 3GPP Release 6, vznikla potřeba robustní architektury, která by zvládla dynamickou povahu mobilních sítí. LSTF řeší omezení spočívající v absenci vyhrazeného překladového mechanismu, který mohl vést k neúspěšným požadavkům na polohu nebo zpožděním, pokud byl kontaktován nesprávný síťový uzel. Centralizací překladové funkce zjednodušuje provoz GMLC, zlepšuje spolehlivost a zvyšuje bezpečnost kontrolou přístupu k informacím o směrování účastníků.

Navíc LSTF podporuje vývoj sítě tím, že poskytuje konzistentní rozhraní bez ohledu na podkladovou generaci sítě (2G, 3G, 4G, 5G). Jak se jádro sítě vyvíjelo od okruhově přepínaných MSC k paketově přepínaným MME a AMF, překladová logika LSTF se přizpůsobila tak, aby dotazovala příslušný HLR nebo HSS a interpretovala nové typy uzlů. Toto zajistilo zpětnou kompatibilitu a plynulý provoz pro klienty LCS, kteří nemusí být vědomi konkrétní síťové technologie obsluhující účastníka, čímž se budoucí investice do polohových služeb staly odolnější vůči změnám.

## Klíčové vlastnosti

- Překládá identifikátory účastníků (MSISDN, IMSI) na adresy aktuálně obsluhujícího síťového uzlu (např. IP adresy MSC, SGSN, MME, AMF)
- Integruje se s HLR/HSS přes protokoly MAP nebo Diameter pro získání aktuálních polohových dat účastníka v reálném čase
- Funguje jako kritická komponenta v architektuře Gateway Mobile Location Center (GMLC)
- Umožňuje správné směrování požadavků na polohu pro mobilní zařízení napříč různými generacemi sítí
- Podporuje klíčové služby jako tísňové volání (E911/E112) a zákonný odposlech
- Poskytuje standardizované rozhraní, které abstrahuje topologii sítě od externích klientů LCS

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lstf/)
