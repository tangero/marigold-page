---
slug: "ia"
url: "/mobilnisite/slovnik/ia/"
type: "slovnik"
title: "IA – Incoming Access (Closed User Group Supplementary Service)"
date: 2025-01-01
abbr: "IA"
fullName: "Incoming Access (Closed User Group Supplementary Service)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ia/"
summary: "Funkce doplňkové služby Uzavřené skupiny uživatelů (CUG) v GSM/UMTS, která povoluje nebo omezuje schopnost účastníka přijímat příchozí hovory. Spolupracuje s dalšími funkcemi CUG k definování privátní"
---

IA (Incoming Access) je funkce doplňkové služby Uzavřené skupiny uživatelů (CUG) v GSM/UMTS, která řídí, zda může účastník přijímat příchozí hovory od uživatelů mimo svou určenou skupinu privátní sítě.

## Popis

Incoming Access (IA) je specifický atribut nebo schopnost v rámci doplňkové služby Uzavřené skupiny uživatelů ([CUG](/mobilnisite/slovnik/cug/)) definované ve specifikacích 3GPP. CUG je služba vytvářející privátní síť uvnitř veřejné mobilní sítě, která omezuje komunikaci na definovanou skupinu účastníků. Funkce IA konkrétně řídí oprávnění pro příjem příchozích hovorů. CUG předplatné účastníka obsahuje indikátor 'Incoming Access', který může být ve stavu 'povoleno' nebo 'blokováno'. Je-li IA 'povoleno', účastníkovi je dovoleno přijímat příchozí hovory od účastníků, kteří nejsou členy žádné z vlastních CUG účastníka (tj. zvenčí privátní skupiny). Je-li IA 'blokováno', účastník může přijímat příchozí hovory pouze od členů, kteří s ním sdílejí alespoň jeden společný CUG index.

Servisní logika pro IA je implementována v jádru sítě, typicky v domácím registračním centru ([HLR](/mobilnisite/slovnik/hlr/)) a navštíveném ústředně mobilní komunikace (VMSC) nebo [MSC](/mobilnisite/slovnik/msc/) Serveru. HLR ukládá CUG data účastníka, včetně seznamu CUG indexů, ke kterým patří, a přidruženého oprávnění IA pro každý CUG nebo jako obecný příznak předplatného. Když je mobilně ukončený hovor směrován k obsluhující MSC, tato MSC provede CUG interrogaci. Porovná volající číslo (a jeho členství v CUG, pokud je dostupné ze zdrojové sítě) s CUG daty volaného účastníka přijatými z HLR. Klíčová kontrola pro IA zahrnuje určení, zda volající a volaná strana sdílejí společný CUG. Pokud ano, hovor je povolen. Pokud společný CUG nesdílejí, hovor je povolen pokračovat pouze v případě, že je funkce IA volaného účastníka 'povolena'. Pokud je IA 'blokována' a žádný společný CUG neexistuje, MSC hovor odmítne, často s konkrétním tónem nebo hlášením.

IA je jednou z několika vzájemně souvisejících CUG funkcí. Často se používá spolu s 'Outgoing Access' (OA), která řídí schopnost uskutečňovat hovory mimo CUG. Kombinace nastavení IA a OA umožňuje flexibilní konfigurace privátních sítí, například 'hybridní' CUG, kde členové mohou volat do veřejné sítě (OA povoleno), ale nemohou od ní přijímat hovory (IA blokováno). Služba je vyvolávána pro každý mobilně ukončený hovor. Interakce s dalšími doplňkovými službami, jako je blokování hovorů, je také specifikována, přičemž CUG má typicky přednost. IA je základním nástrojem pro podnikové a skupinové služby, který umožňuje vytváření bezpečných, řízených komunikačních prostředí uvnitř veřejné buněčné sítě.

## K čemu slouží

Funkce Incoming Access byla vytvořena, aby poskytla podrobnou kontrolu v rámci služby Uzavřené skupiny uživatelů ([CUG](/mobilnisite/slovnik/cug/)), která sama byla navržena k emulaci funkčnosti privátní telefonní ústředny (PBX) nebo virtuální privátní sítě (VPN) na veřejných mobilních sítích. Raní podnikoví zákazníci požadovali možnost definovat privátní skupiny, kde by komunikace mohla být omezena, ale s flexibilními politikami ohledně interakce s vnějším světem. Jednoduchá, zcela uzavřená skupina (žádné hovory dovnitř ani ven) byla často příliš omezující. Funkce IA vyřešila konkrétní problém řízení příchozích hovorů od nečlenů.

Toto řešilo klíčovou podnikovou potřebu: definovat skupiny, kde by na členy bylo dosažitelné pouze ostatními členy skupiny (IA blokováno), čímž vzniklo bezpečné prostředí pouze pro členy. Alternativně mohla být skupina nakonfigurována tak, aby členové mohli přijímat důležité hovory zvenčí (např. od klientů nebo centrály), zatímco by jejich odchozí hovory byly stále omezeny (pokud je OA blokováno). Tato flexibilita byla zásadní pro přijetí služeb CUG podniky, vládními agenturami a dalšími organizacemi. Umožnila síťovým operátorům nabízet šité na míru komunikační balíčky, které splňovaly specifické bezpečnostní a provozní politiky, generovaly dodatečné příjmy a zákaznickou loajalitu. Standardizace IA v 3GPP Release 4 a její přetrvávání v pozdějších vydáních podtrhuje její trvalou roli jako základní doplňkové služby pro řízenou skupinovou komunikaci.

## Klíčové vlastnosti

- Definuje oprávnění přijímat příchozí hovory zvenčí Uzavřené skupiny uživatelů (CUG) účastníka.
- Atribut se dvěma stavy: 'Incoming Access povoleno' a 'Incoming Access blokováno'.
- Servisní logika vykonávaná v MSC/VMSC během sestavování mobilně ukončeného hovoru.
- Interroguje data o členství v CUG volající a volané strany z HLR.
- Spolupracuje s funkcí Outgoing Access (OA) pro kompletní řízení hovorů v CUG.
- Umožňuje flexibilní modely privátních sítí (např. restrikci pouze příchozích hovorů z veřejné sítě).

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 32.828** (Rel-10) — Study on 3GPP-TMF NRM/SID Alignment
- **TS 32.829** (Rel-10) — Fault Management Alignment Study
- **TS 32.831** (Rel-10) — 3GPP-TMF PM Alignment Study
- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [IA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ia/)
