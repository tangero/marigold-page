---
slug: "mtrf"
url: "/mobilnisite/slovnik/mtrf/"
type: "slovnik"
title: "MTRF – Mobile Terminating Roaming Forwarding"
date: 2025-01-01
abbr: "MTRF"
fullName: "Mobile Terminating Roaming Forwarding"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mtrf/"
summary: "MTRF je servisní funkce, která umožňuje roamujícímu účastníkovi přijímat příchozí hovory, i když navštívená síť nedokáže hovor dokončit. Hovor přesměruje na předem definované číslo (např. hlasovou sch"
---

MTRF je servisní funkce, která přesměruje příchozí hovor pro roamujícího účastníka na předem definované číslo nebo do sítě, pokud navštívená síť hovor nedokáže dokončit, čímž zajišťuje jeho dokončení.

## Popis

Mobile Terminating Roaming Forwarding (MTRF) je standardizovaná služba 3GPP navržená ke zvýšení úspěšnosti dokončení hovorů pro roamující účastníky. Funguje v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně a je řízena domovskou veřejnou pozemní mobilní sítí ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka. Když je mobilně ukončovaný hovor (příchozí hovor) směrován k účastníkovi, který roamuje v navštívené [PLMN](/mobilnisite/slovnik/plmn/) ([VPLMN](/mobilnisite/slovnik/vplmn/)), a VPLMN hovor nedokáže úspěšně doručit (např. kvůli nedostupnosti účastníka, přetížení sítě nebo servisním omezením), je spuštěn mechanismus MTRF. HPLMN po obdržení indikace selhání od VPLMN může hovor přesměrovat na alternativní cíl určený účastníkem nebo operátorem sítě, jako je systém hlasové schránky, jiné telefonní číslo nebo aplikační server.

Architektura zahrnuje několik uzlů jádra sítě. Klíčovou entitou je domovský lokální registr ([HLR](/mobilnisite/slovnik/hlr/)) v HPLMN, který ukládá profil služby MTRF účastníka a číslo pro přesměrování. Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) v HPLMN je zodpovědné za dotazování HLR (prostřednictvím [MAP](/mobilnisite/slovnik/map/) Send Routing Information) za účelem získání směrovacích instrukcí pro příchozí hovor. Když je hovor směrován na Visited MSC (VMSC) VPLMN a VMSC zjistí, že jej nemůže ukončit u účastníka, odešle do HPLMN indikaci selhání MAP Provide Roaming Number nebo podobnou. To spustí v GMSC nebo specializovaném řídicím uzlu aplikaci logiky MTRF, která přeběží hovor na základě profilu účastníka.

Fungování MTRF zahrnuje specifický signalizační tok. Nejprve GMSC přijme příchozí hovor a dotazuje se HLR. HLR poskytne Mobile Station Roaming Number (MSRN) pro směrování hovoru k VMSC. VMSC se pokusí o stránkování účastníka. Pokud stránkování selže (např. bez odpovědi, účastník v nepokryté oblasti nebo je zaneprázdněn jinou službou v okruhově spínané doméně), VMSC odešle hlášení o selhání GMSC. GMSC, nyní vědomé selhání ukončení, zahájí druhý dotaz na HLR konkrétně pro instrukce MTRF. HLR pak vrátí číslo, na které se má hovor přesměrovat (např. přístupové číslo hlasové schránky). GMSC následně přeběží hovor na toto číslo, čímž dokončí proceduru přesměrování hovoru transparentně pro volajícího.

Úlohou MTRF je zvýšit spolehlivost služeb a uživatelský komfort pro roamující účastníky, zajistit kontinuitu služeb a spokojenost zákazníků. Jedná se o síťovou službu, což znamená, že nevyžaduje podporu na uživatelském zařízení (UE). Funkce je zvláště cenná ve scénářích s nedostatečnými mezinárodními roamingovými dohodami nebo technickými omezeními v některých navštívených sítích. Doplňuje další služby dokončení hovoru, jako je Call Forwarding on Not Reachable (CFNRc), ale je specificky přizpůsobena pro roamingový kontext, kde HPLMN udržuje kontrolu nad rozhodnutím o přesměrování.

## K čemu slouží

MTRF bylo zavedeno, aby vyřešilo problém nedoručených hovorů roamujícím účastníkům, což byla významná bolest jak pro uživatele, tak pro operátory. Před zavedením MTRF, pokud navštívená síť nedokázala hovor ukončit (z důvodů jako dočasný výpadek sítě, nedostatek odpovědi na stránkování nebo nekompatibility), hovor prostě selhal, což vedlo ke špatné zákaznické zkušenosti a potenciální ztrátě příjmů operátorů. Existující služby přesměrování hovorů (jako CFNRc) byly typicky ukotveny v navštívené síti, která je nemusela vždy podporovat nebo je konzistentně aplikovat pro roamující účastníky.

Primární motivací bylo dát operátorovi domovské sítě větší kontrolu nad procesem dokončení hovoru pro své účastníky, když jsou v zahraničí. To řeší omezení, kdy schopnosti nebo politiky navštívené sítě mohou zabránit úspěšnému ukončení hovoru. Centralizací logiky přesměrování v HPLMN zajišťuje MTRF konzistentní servisní zkušenost bez ohledu na vlastnosti navštívené sítě. Také umožňuje domovským operátorům implementovat obchodní pravidla, jako je přesměrování na systém hlasové schránky domovské sítě, což může být výhodné z důvodů nákladů nebo kvality služeb.

Historicky bylo MTRF standardizováno v 3GPP Release 10 jako součást pokračujících vylepšení roamingových služeb. Jeho vytvoření bylo hnací silou požadavků operátorů na robustnější a inteligentnější roamingové mechanismy, zejména s růstem mezinárodního cestování. Vyplnilo mezeru v existující sadě nástrojů tím, že poskytlo standardizovaný, interoperabilní způsob řešení selhání doručení hovoru v roamingovém scénáři, čímž zvýšilo celkovou efektivitu sítě a spokojenost účastníků.

## Klíčové vlastnosti

- Síťově řízené přesměrování hovoru pro roamující účastníky při selhání ukončení
- Spouštěno indikacemi selhání od navštívené sítě (např. účastník nedostupný)
- Cíl přesměrování (číslo) uložen a spravován domovskou sítí (HLR/HSS)
- Funguje transparentně pro volajícího a uživatelské zařízení (UE)
- Zvyšuje míru dokončení hovorů a spolehlivost roamingových služeb
- Standardizované MAP signalizační procedury mezi HPLMN a VPLMN

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [VMSC – Visited Mobile Switching Center](/mobilnisite/slovnik/vmsc/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging

---

📖 **Anglický originál a plná specifikace:** [MTRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtrf/)
