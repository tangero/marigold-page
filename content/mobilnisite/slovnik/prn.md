---
slug: "prn"
url: "/mobilnisite/slovnik/prn/"
type: "slovnik"
title: "PRN – Provide Roaming Number"
date: 2025-01-01
abbr: "PRN"
fullName: "Provide Roaming Number"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/prn/"
summary: "Dočasné MSISDN přidělené VLR pro umožnění směrování hovorů k roamujícímu účastníkovi. Jedná se o klíčový mechanismus v sítích GSM/UMTS pro navazování příchozích hovorů, když je účastník mimo svou domo"
---

PRN je dočasné MSISDN přidělené VLR, které umožňuje směrování hovorů k roamujícímu účastníkovi a zajišťuje plynulé příchozí spojení mimo jeho domovskou síť.

## Popis

Procedura Provide Roaming Number (PRN) je procedura jádra sítě a související parametr definovaný ve specifikacích 3GPP pro sítě GSM a UMTS. Funguje jako součást protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)), konkrétně v rámci operace MAP Send Routing Information ([SRI](/mobilnisite/slovnik/sri/)). Když je hovor určen mobilnímu účastníkovi, který roamuje v navštívené síti, Gateway Mobile Switching Center ([GMSC](/mobilnisite/slovnik/gmsc/)) v domovské síti požádá Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) o informace pro směrování. HLR následně odešle žádost PRN k Visited Mobile Switching Center ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo k asociovanému Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), kde je účastník aktuálně registrován. Primárním účelem této žádosti je získat dočasné, síťově specifické číslo, které lze použít k směrování hovoru do navštíveného [MSC](/mobilnisite/slovnik/msc/).

Po přijetí žádosti PRN VLR/VMSC přidělí Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)) z fondu čísel vyhrazeného pro tento účel. Toto MSRN je dočasné E.164 číslo, které vypadá jako běžné telefonní číslo, ale používá se pouze pro interní síťové směrování. VLR/VMSC toto MSRN vrátí HLR v odpovědi PRN. HLR pak toto MSRN přepošle žadateli, GMSC. GMSC použije toto MSRN k směrování hovoru přes Public Switched Telephone Network (PSTN) nebo IP-based core network ke správnému VMSC. Jakmile je hovor navázán nebo selže, VMSC uvolní MSRN zpět do fondu pro budoucí použití, což z něj činí dynamický a efektivní zdroj.

Mechanismus PRN je architektonicky klíčový, protože odděluje trvalou identitu účastníka (MSISDN) od fyzické směrovací cesty potřebné k jeho dosažení. Umožňuje ochranu polohy a efektivní využití číselných zdrojů. Procedura zahrnuje několik klíčových síťových prvků: HLR jako centrální databázi účastníků, VLR jako dočasnou databázi návštěvníků, VMSC jako přepojovací bod v navštívené síti a GMSC jako vstupní bod pro příchozí hovory. Signalizace je přenášena přes sítě SS7 nebo IP-based SIGTRAN s použitím protokolu MAP. Operace PRN zahrnuje parametry jako IMSI účastníka, číslo MSC a podporované síťové schopnosti, což zajišťuje přesnost směrovacích informací a možnost doručení hovoru s příslušnými službami.

## K čemu slouží

Procedura PRN byla vytvořena za účelem řešení základního problému směrování telefonních hovorů k mobilnímu účastníkovi, který je mimo geografické pokrytí svého domovského síťového operátora. V raných celulárních systémech by bez takového mechanismu bylo nemožné, aby ústředna domovské sítě věděla, jak nasměrovat hovor k účastníkovi, jehož poloha se dynamicky mění a je spravována jinou sítí. PRN poskytuje standardizovanou, bezpečnou metodu pro sítě, jak si vyměňovat dočasná směrovací čísla, aniž by odhalovaly přesnou polohu účastníka nebo vyžadovaly trvalý přenos čísel mezi operátory.

Historicky, před standardizací GSM a protokolu MAP, se používala proprietární řešení nebo jednodušší pevné směrování, což omezovalo plynulé mezinárodní roamování. Mechanismus PRN, zavedený v 3GPP Release 4 jako součást architektury jádra sítě GSM, umožnil automatizované získávání směrovacích informací v reálném čase. Řešil omezení, jako jsou statické směrovací tabulky, které byly pro mobilní uživatele neproveditelné, a potřebu manuálního zásahu síťových operátorů k nastavení cest hovorů. Poskytnutím dynamického, na požadavek přidělovaného směrovacího čísla umožnil efektivní využití mezinárodního telefonního číslovacího plánu (E.164) a vytvořil základ pro komerční roamingové dohody mezi operátory, které definují moderní globální mobilní komunikaci.

Procedura také podporuje nezbytné doplňkové služby, jako je přesměrování hovorů a optimální směrování. Řeší problém, jak spojit hovor, aniž by volající strana musela znát dočasnou polohu účastníka nebo vytočit jiné číslo. Z pohledu sítě umožňuje distribuci zátěže a škálovatelnost, protože MSRN jsou sdružována a znovu používána. Vytvoření procedury PRN bylo motivováno potřebou škálovatelné, interoperabilní a efektivní globální roamingové infrastruktury, což byla klíčová prodejní výhoda technologie GSM oproti dřívějším celulárním systémům.

## Klíčové vlastnosti

- Dynamické přidělování dočasných čísel Mobile Station Roaming Number (MSRN) z vyhrazeného fondu
- Integrální součást procedury MAP Send Routing Information (SRI) pro doručení hovoru
- Umožňuje směrování příchozích hovorů k roamujícím účastníkům bez odhalení jejich přesné polohy
- Používá standardní formát čísel E.164 pro plynulé propojení PSTN/PLMN
- Podporuje nezbytné doplňkové služby a scénáře optimálního směrování
- Mechanismus uvolňování čísel zajišťuje efektivní opakované využití omezených číselných zdrojů

## Související pojmy

- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.453** (Rel-19) — PCAP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/prn/)
