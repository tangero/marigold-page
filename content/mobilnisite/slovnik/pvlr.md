---
slug: "pvlr"
url: "/mobilnisite/slovnik/pvlr/"
type: "slovnik"
title: "PVLR – Previous Visitor Location Register"
date: 2025-01-01
abbr: "PVLR"
fullName: "Previous Visitor Location Register"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pvlr/"
summary: "Parametr Previous VLR (PVLR) se používá při procedurách mobility, například při aktualizaci polohy nebo meziřízení mezi MSC, k identifikaci předchozího obslužného VLR účastníka. Je klíčový pro správné"
---

PVLR je zkratka pro Previous Visitor Location Register, což je parametr sítě identifikující předchozí obslužný VLR účastníka. Slouží k zajištění správného signalizačního provozu a načítání dat během procedur mobility, jako je aktualizace polohy.

## Popis

Previous Visitor Location Register (PVLR) je klíčový datový prvek v architektuře jádra sítí GSM/UMTS/EPS, konkrétně v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně. Nejde o samostatný síťový uzel, ale o parametr – typicky adresu nebo identifikátor – uložený v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a používaný během procedur správy mobility. Když se mobilní účastník přesune z oblasti obsluhy jednoho [MSC](/mobilnisite/slovnik/msc/)/[VLR](/mobilnisite/slovnik/vlr/) do jiné, nový VLR odešle HLR žádost o aktualizaci polohy. Tato žádost obsahuje identitu nového VLR. HLR pak uloží adresu tohoto nového VLR a zároveň po určitou dobu uchovává adresu předchozího VLR (PVLR). Tento historický záznam je pro provoz sítě nezbytný.

Hlavní funkční role PVLR se projevuje při následných signalizačních procedurách. Klíčovým případem užití je obnova dat účastníka. Pokud je aktualizace polohy v HLR úspěšná, ale následné vložení dat účastníka do nového VLR selže, může HLR nařídit novému VLR, aby data obnovil ze starého VLR, který je identifikován parametrem PVLR. Tento mechanismus zvyšuje odolnost. Dále může být informace o PVLR použita při meziřízení mezi MSC nebo při doručování hovorů k roamujícímu účastníkovi k napomáhání správnému směrování signalizačních zpráv, a to zejména ve složitých roamingových scénářích zahrnujících více síťových operátorů.

Z architektonického hlediska je PVLR pole v záznamu dat účastníka v HLR. Jeho hodnotou je globální titul [SS7](/mobilnisite/slovnik/ss7/) nebo adresa síťového uzlu VLR, který účastníka předtím obsluhoval. Správa tohoto parametru je řízena protokoly jako [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part). HLR aktualizuje pole PVLR vždy, když zpracuje úspěšnou aktualizaci polohy z nového VLR: aktuální adresu VLR přesune do pole PVLR a novou adresu uloží jako aktuálně obslužný VLR. Tento dvoukrokový historický záznam je jednoduchým, ale efektivním nástrojem pro spolehlivost sítě a efektivní signalizaci, neboť předchází problémům, jako jsou opuštěné kontexty účastníků ve VLR, a zajišťuje správné doručování hovorů i při přechodných výpadcích sítě nebo rychlém pohybu účastníka.

## K čemu slouží

Koncept PVLR byl zaveden pro řešení specifických problémů souvisejících s mobilitou účastníků a konzistencí dat v raných sítích GSM a byl zachován i v následných vydáních 3GPP. Jeho zavedení motivovala potřeba odolnosti proti chybám během procedury aktualizace polohy. Při čistě sekvenčním procesu, kdy je profil účastníka smazán ze starého [VLR](/mobilnisite/slovnik/vlr/) a následně vložen do nového VLR, by selhání ve fázi vkládání mohlo zanechat účastníka bez provozuschopných dat v jakémkoli VLR, což by vedlo k výpadku služby. PVLR poskytuje záložní mechanismus.

Uchováním adresy předchozího VLR umožňuje [HLR](/mobilnisite/slovnik/hlr/) provést proceduru návratu nebo obnovy. Pokud nový VLR nahlásí selhání při naplnění dat účastníka, může mu HLR nařídit, aby si data stáhl přímo z předchozího VLR (identifikovaného pomocí PVLR), a tím službu obnovil bez nutnosti znovu vše načítat z HLR samotného. Tím se zlepšuje spolehlivost služby a sníží se signalizační zatížení HLR. Dále ve složitých scénářích směrování hovorů, zejména pro roamující účastníky, znalost předchozího obslužného síťového uzlu pomáhá optimalizovat a správně směrovat signalizační zprávy, čímž se zajišťuje efektivní navazování hovorů a dokončování meziřízení. Tím řeší omezení přístupu ke správě mobility bez stavu přidáním minimální vrstvy historického kontextu ke sledování polohy účastníka.

## Klíčové vlastnosti

- Poskytuje záložní adresu pro obnovu dat účastníka při selhaných aktualizacích polohy
- Umožňuje efektivní směrování signalizace při meziřízení mezi MSC a doručování hovorů
- Uložen jako parametr v záznamu účastníka v HLR
- Je využíván protokolem MAP pro správu mobility
- Zvyšuje robustnost sítě a odolnost proti poruchám
- Udržuje jednokrokovou historii obslužného síťového uzlu účastníka

## Související pojmy

- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [PVLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pvlr/)
