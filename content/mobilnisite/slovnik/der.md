---
slug: "der"
url: "/mobilnisite/slovnik/der/"
type: "slovnik"
title: "DER – Distinguished Encoding Rules"
date: 2025-01-01
abbr: "DER"
fullName: "Distinguished Encoding Rules"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/der/"
summary: "DER je sada kódovacích pravidel pro ASN.1 (Abstract Syntax Notation One) používaná k serializaci strukturovaných dat do deterministického, jednoznačného binárního formátu. Zajišťuje integritu dat a in"
---

DER je sada kódovacích pravidel pro ASN.1, která serializuje strukturovaná data do deterministického binárního formátu, čímž zajišťuje integritu dat a interoperabilitu pro protokoly 3GPP prostřednictvím kanonického kódování.

## Popis

Distinguished Encoding Rules (DER) jsou podmnožinou Basic Encoding Rules ([BER](/mobilnisite/slovnik/ber/)) pro ASN.1 navrženou tak, aby pro jakoukoli danou hodnotu ASN.1 vytvořila jednoznačné, kanonické binární kódování. ASN.1 je standardní jazyk pro popis rozhraní používaný v telekomunikacích k definici datových struktur nezávislých na konkrétních strojových kódovacích technikách. DER ukládá na BER dodatečná omezení, která zajišťují, že existuje právě jeden způsob, jak zakódovat datovou strukturu ASN.1. Této deterministické vlastnosti je dosaženo vynucením pravidel, jako je používání forem s určitou délkou, vynechávání volitelných výchozích hodnot a řazení prvků množin (set) kanonickým způsobem. Ve specifikacích 3GPP je DER rozsáhle používáno pro kódování bezpečnostně citlivých informací, certifikátů a datových jednotek protokolů ([PDU](/mobilnisite/slovnik/pdu/)), kde je vyžadován jednoznačný reprezentační formát.

Architektura kódování DER je nedílnou součástí vrstev protokolového zásobníku definovaných v 3GPP. Funguje na prezentační vrstvě, transformuje abstraktní datové typy definované v modulech ASN.1 – například v 3GPP TS 24.109 pro Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo TS 31.113 pro aplikace UICC – do kompaktního, jednoznačného proudu bajtů. Tento proud může být přenášen přes síťová rozhraní nebo bezpečně uložen. Mezi klíčové komponenty patří definice typů ASN.1, samotná kódovací pravidla a dekodéry, které data z binárního formátu rekonstruují. Proces kódování zahrnuje označování datových typů, specifikaci délek a kódování hodnot, a to vše při dodržování kanonických omezení DER, aby se zabránilo možnosti více platných kódování pro stejná data.

Úloha DER v ekosystému 3GPP je klíčová pro zajištění interoperability a bezpečnosti mezi síťovými elementy od Release 6 dále. Používá se v protokolech, jako jsou ty pro autentizaci a dohodu klíčů ([AKA](/mobilnisite/slovnik/aka/)), kde musí být certifikáty a podepsaná data vyměňována mezi uživatelským zařízením (UE), obslužnými uzly a autentizačními centry. Poskytnutím deterministického kódování DER umožňuje spolehlivé ověřování digitálních podpisů, protože jakákoli změna v kódování by podpis zneplatnila. To je zásadní v manažerských a bezpečnostních specifikacích, jako je TS 32.401 pro správu výkonu a TS 32.809 pro účtování, kde jsou integrita dat a neodmítnutelnost prvořadé. Použití DER tak podporuje důvěryhodnost mechanismů v sítích 3GPP a umožňuje bezpečnou komunikaci a konzistentní zpracování dat napříč různými implementacemi.

## K čemu slouží

DER vzniklo za účelem řešení omezení Basic Encoding Rules ([BER](/mobilnisite/slovnik/ber/)), která připouštějí více platných kódování pro stejnou datovou strukturu ASN.1. Tato nejednoznačnost představovala významné problémy pro bezpečnostní aplikace, zejména pro digitální podpisy a správu certifikátů, kde je pro ověření integrity a autenticity vyžadováno přesné binární porovnání. V telekomunikacích, zejména v rámci standardů 3GPP počínaje Release 6, se potřeba spolehlivé, jednoznačné kódovací metody stala naléhavou s tím, jak se sítě vyvíjely, aby podporovaly složitější bezpečnostní protokoly a interoperabilní systémy napříč různými dodavateli a platformami.

Historický kontext vychází z přijetí ASN.1 v raných telekomunikačních protokolech, kde bylo BER dostatečné pro základní výměnu dat, ale nedostatečné pro operace kritické z hlediska bezpečnosti. DER tento problém řeší vynucením kanonických kódovacích pravidel, čímž zajišťuje, že jakákoli daná hodnota ASN.1 má jedinou, deterministickou binární reprezentaci. Tím se odstraňují problémy, jako jsou neshody v kódování při ověřování podpisů, které by mohly vést k bezpečnostním slabinám nebo provozním selháním. V 3GPP je toto zásadní pro specifikace týkající se správy (např. TS 32.452 pro integraci alarmů), účtování (např. TS 32.453 pro zpracování záznamů o účtovaných datech) a bezpečnosti (např. TS 33.113 pro autentizaci), kde musí být data konzistentně zpracovávána napříč síťovými elementy.

Poskytnutím standardizovaného, jednoznačného kódování DER usnadňuje interoperabilitu ve více-dodavatelských nasazeních 3GPP a umožňuje bezproblémovou komunikaci mezi komponentami jádra sítě, uzly rádiového přístupu a uživatelskými zařízeními. Podporuje vývoj síťových služeb tím, že zajišťuje, že se bezpečnostní rámce – jako jsou ty pro síťové řezy (network slicing) nebo IoT aplikace – mohou spolehnout na důvěryhodné kódování dat, čímž řeší omezení předchozích přístupů, kterým chyběla determinovanost a které by mohly ohrozit integritu systému.

## Klíčové vlastnosti

- Kanonické kódování zajišťující jednoznačnou binární reprezentaci pro každou hodnotu ASN.1
- Deterministický výstup vhodný pro digitální podpisy a bezpečnostní ověřování
- Podmnožina Basic Encoding Rules (BER) s dodatečnými omezeními pro jednoznačnou serializaci
- Podpora kódování s určitou délkou (definite-length) za účelem eliminace redundance při přenosu dat
- Kompatibilita s definicemi typů ASN.1 používanými napříč specifikacemi protokolů 3GPP
- Vynucování pravidel pro řazení prvků množin (set) a vynechávání volitelných výchozích hodnot

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.409** (Rel-19) — IMS Performance Management Measurements
- **TS 32.452** (Rel-19) — PM Measurements for Home Node B Subsystem
- **TS 32.453** (Rel-19) — PM for Home eNodeB Subsystem (HeNS)
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.863** (Rel-13) — PM Measurement Metadata Definition

---

📖 **Anglický originál a plná specifikace:** [DER na 3GPP Explorer](https://3gpp-explorer.com/glossary/der/)
