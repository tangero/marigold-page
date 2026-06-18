---
slug: "5gsm"
url: "/mobilnisite/slovnik/5gsm/"
type: "slovnik"
title: "5GSM – 5G Session Management"
date: 2025-01-01
abbr: "5GSM"
fullName: "5G Session Management"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5gsm/"
summary: "5GSM je protokol pro správu PDU sezení v sítích 5G. Zajišťuje zřizování, změnu a uvolňování sezení mezi UE a SMF. Je klíčový pro umožnění různorodých služeb 5G se specifickými požadavky na QoS."
---

5GSM je protokol pro správu zřizování, změny a uvolňování PDU sezení mezi UE a SMF v sítích 5G, který umožňuje služby se specifickými požadavky na QoS.

## Popis

5G Session Management (5GSM) je protokol řídicí roviny definovaný v architektuře 5G System (5GS). Působí mezi uživatelským zařízením (UE) a funkcí správy sezení ([SMF](/mobilnisite/slovnik/smf/)) za účelem správy paketových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) sezení, což je základní konektivní služba poskytující konektivitu uživatelské roviny mezi UE a konkrétní datovou sítí ([DN](/mobilnisite/slovnik/dn/)). Protokol 5GSM je přenášen v signalizačních zprávách Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) mezi UE a funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), přičemž AMF transparentně přeposílá zprávy 5GSM do SMF a zpět. Toto oddělení signalizace správy sezení od signalizace správy přístupu a mobility (kterou zajišťuje protokol [5GMM](/mobilnisite/slovnik/5gmm/)) je klíčovým architektonickým principem 5G, umožňujícím nezávislé škálování a vývoj funkcí správy sezení a mobility.

Hlavní funkcí 5GSM je zřizovat, měnit a uvolňovat PDU sezení. Proces zřizování PDU sezení zahrnuje odeslání žádosti o zřízení PDU sezení ze strany UE do sítě, což vyvolá akci SMF vybrat funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), vytvořit potřebnou N4 relaci s UPF a vyjednat požadované parametry QoS. Protokol 5GSM přenáší klíčové informace, jako je identifikátor PDU sezení (PDU Session ID), vybraný název datové sítě ([DNN](/mobilnisite/slovnik/dnn/)), požadovaná informace pro výběr řezu sítě (S-NSSAI) a typ PDU sezení (např. IPv4, IPv6, IPv4v6, Ethernet nebo nestrukturovaný). Také spravuje aktivaci, změnu a deaktivaci QoS toků v rámci PDU sezení, mapuje toky služebních dat na konkrétní QoS toky s definovanými hodnotami 5G identifikátoru QoS (5QI), garantovanou přenosovou rychlostí toku (GFBR) a maximální přenosovou rychlostí toku (MFBR).

Kromě základní správy životního cyklu sezení podporuje 5GSM pokročilé funkce nezbytné pro služební architekturu 5G. Umožňuje vyjednávání a správu volby konfigurace protokolu (PCO), což SMF poskytuje parametry, jako jsou adresy DNS serverů. Také podporuje procedury změny PDU sezení iniciované UE, což umožňuje UE požadovat změny charakteristik sezení, například přidání nebo odebrání QoS toku. Dále jsou procedury 5GSM těsně integrovány s řezy sítě; S-NSSAI obsažené v signalizaci 5GSM zajišťuje, že je PDU sezení zřízeno v rámci správné instance řezu sítě, což poskytuje zamýšlené charakteristiky služby a izolaci. Protokol také zajišťuje uvolňování PDU sezení, ať už iniciované UE nebo sítí, a tím zajišťuje řádné uvolnění prostředků v SMF, UPF a UE.

## K čemu slouží

5GSM byl vytvořen jako součást nové architektury 5G Core (5GC) k řešení omezení protokolu správy sezení Evolved Packet System (EPS) používaného v 4G/LTE. V EPS byly správa sezení a mobility těsněji propojeny v rámci jediného protokolu (respektive ESM a EMM). Koncepční princip služební architektury 5G a dekompozice síťových funkcí si vyžádaly čisté oddělení funkce správy přístupu a mobility (AMF) od funkce správy sezení (SMF). 5GSM existuje jako specializovaný a efektivní protokol pro správu sezení, který může fungovat nezávisle na podkladové přístupové technologii (3GPP přístup jako NR nebo ne-3GPP přístup jako Wi-Fi) a lze jej škálovat pro podporu obrovské různorodosti případů užití v 5G.

Protokol řeší problém správy komplexních, na službu orientovaných konektivních sezení s dynamickými požadavky na QoS. Předchozí systémy měly rigidnější modely QoS. 5GSM je navržen tak, aby podporoval široké spektrum typů PDU sezení (nejen IP), včetně ethernetových a nestrukturovaných typů, což je klíčové pro aplikace vertikálních odvětví a konvergenci pevných a mobilních sítí. Také poskytuje signalizační základ pro řezy sítě, což umožňuje, aby jedno UE mělo více souběžných PDU sezení, z nichž každé může být v jiném řezu sítě s naprosto odlišnými charakteristikami výkonu a zabezpečení. To byl významný vývoj oproti modelu přenašečů v EPS, který umožňuje skutečně služebně orientovanou konektivitu.

Dále bylo vytvoření 5GSM motivováno potřebou zvýšené efektivity a flexibility. Oddělením signalizace správy sezení může síť optimalizovat umístění a škálování SMF nezávisle na AMF. Protokol podporuje změnu sezení iniciovanou UE, což dává aplikacím přímější kontrolu nad jejich síťovými prostředky. Také zjednodušuje integraci ne-3GPP přístupu, protože stejný protokol 5GSM je používán bez ohledu na to, jak se UE připojuje k 5GC, což poskytuje jednotnou zkušenost se správou sezení. V podstatě je 5GSM klíčovým protokolem, který překládá požadavky služeb na vysoké úrovni do konkrétních, proveditelných pravidel konektivity uživatelské roviny v rámci sítě 5G.

## Klíčové vlastnosti

- Spravuje životní cyklus (zřízení, změna, uvolnění) PDU sezení
- Podporuje více typů PDU sezení: IPv4, IPv6, IPv4v6, Ethernet, nestrukturovaný
- Vyjednává a spravuje QoS toky s podrobnými parametry 5QI, GFBR a MFBR
- Integruje se s řezy sítě prostřednictvím S-NSSAI pro izolaci sezení a služebně specifické zacházení
- Umožňuje změnu sezení iniciovanou UE pro dynamické požadavky služeb
- Funguje nezávisle na přístupové technologii (3GPP i ne-3GPP) prostřednictvím přenosu v NAS

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [5GMM – 5G Mobility Management](/mobilnisite/slovnik/5gmm/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 38.508** (Rel-19) — 5G NR UE Radio Transmission & Reception

---

📖 **Anglický originál a plná specifikace:** [5GSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gsm/)
