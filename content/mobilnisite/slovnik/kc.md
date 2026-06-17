---
slug: "kc"
url: "/mobilnisite/slovnik/kc/"
type: "slovnik"
title: "KC – Ciphering Key"
date: 2025-01-01
abbr: "KC"
fullName: "Ciphering Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/kc/"
summary: "KC je 64bitový kryptografický klíč používaný specificky se streamovým šifrovacím algoritmem A5 k šifrování a dešifrování uživatelských dat a signalizace přes rozhraní rádiového přenosu v GSM a raných"
---

KC je 64bitový šifrovací klíč odvozený z autentizace účastníka a používaný s algoritmem A5 k šifrování dat a signalizace přes rozhraní rádiového přenosu v GSM a raných systémech 3GPP.

## Popis

Šifrovací klíč (KC) je základní bezpečnostní prvek definovaný ve specifikacích 3GPP, zejména v TS 31.102 (aplikace USIM) a TS 31.113 (bezpečnost UICC). Jedná se o 64bitový symetrický klíč využívaný výhradně rodinou streamových šifrovacích algoritmů A5 (např. [A5/1](/mobilnisite/slovnik/a5-1/), [A5/2](/mobilnisite/slovnik/a5-2/), A5/3) k zajištění šifrování přes rádiové rozhraní pro rádiový spoj mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou přenosovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) v GSM a jeho vývojových cestách. Architektonicky je KC uložen v bezpečnostní architektuře modulu účastnické identity (SIM) nebo univerzálního modulu účastnické identity (USIM) na UICC a v autentizačním centru (AuC) sítě v domovském registru polohy ([HLR](/mobilnisite/slovnik/hlr/)). Nikdy není přenášen vzduchem; místo toho je generován nezávisle jak mobilním zařízením, tak sítí pomocí sdílených tajných informací.

Provozní životní cyklus KC začíná autentizací účastníka. Když se mobilní zařízení připojí k síti, AuC vygeneruje náhodnou výzvu (RAND) a pomocí sdíleného tajného klíče Ki (jedinečného pro [IMSI](/mobilnisite/slovnik/imsi/) účastníka) a autentizačního algoritmu [A3](/mobilnisite/slovnik/a3/) vypočítá jak podepsanou odpověď (SRES) pro ověření, tak šifrovací klíč KC pomocí derivačního algoritmu klíčů [A8](/mobilnisite/slovnik/a8/). RAND je odeslán mobilnímu zařízení. SIM/USIM, který má stejný Ki, provede identické výpočty pro vygenerování vlastní SRES (odeslané zpět pro autentizaci) a identického KC. Po úspěšné autentizaci síť nařídí MS zahájit šifrování pomocí konkrétní varianty algoritmu A5 a obě strany použijí lokálně uložený KC k inicializaci generátoru šifrovacího proudu šifry A5.

Během hovoru nebo datové relace algoritmus A5 použije KC jako semeno pro generování pseudonáhodného šifrovacího proudu. Tento proud je poté spojen operací XOR s otevřenými daty (hlasovými rámci nebo signalizačními zprávami) za vzniku šifrovaného textu pro přenos přes rádiové rozhraní Um. Proces je symetrický: příjemce použije stejný KC a algoritmus k opětovnému vygenerování identického šifrovacího proudu a dešifrování dat. KC je typicky obnovován pro každou novou relaci nebo může být změněn během hovoru prostřednictvím procedury aktualizace šifrovacího režimu pro zvýšení bezpečnosti. Jeho role je omezena na rádiový přístupový spoj; přenos v jádru sítě využívá samostatné bezpečnostní mechanismy, jako je IPsec. Správa a ukládání KC v rámci UICC se řídí přísnými bezpečnostními protokoly, aby se zabránilo jeho extrakci, což tvoří klíčovou část důvěryhodného kotvení systému.

## K čemu slouží

KC byl vytvořen k řešení kritického problému odposlechu analogových rádiových buněčných komunikací, které byly ze své podstaty nezabezpečené. Před digitálním šifrováním v GSM mohl kdokoli s rádiovým skenerem naslouchat hovorům. Zavedení KC a šifer A5 ve standardu GSM bylo milníkem v poskytování povinné základní důvěrnosti pro miliony uživatelů buněčné sítě. Řešilo to rostoucí obavy o soukromí, jak se mobilní telefonie rozšířila a rádiové spektrum se stalo sdíleným veřejným médiem.

Motivace vycházela z potřeby lehkého, efektivního šifrovacího mechanismu, který by mohl fungovat v rámci přísných výpočetních a latencních omezení mobilního hardwaru konce 80. let 20. století. Návrh zvolil délku klíče 64 bitů jako kompromis mezi bezpečnostní silou a realizační proveditelností. Eleganci systému spočívá v jeho odvození z existujícího autentizačního rámce (pomocí Ki a A3/A8), čímž se vyhnul nutnosti přenášet samotný klíč. Tento model "generování na obou stranách" výrazně snížil riziko expozice klíče ve srovnání se systémy, které by mohly distribuovat relakční klíče v otevřené podobě.

Historický kontext však zahrnuje i jeho omezení. Původní algoritmy A5/1 a A5/2 a délka klíče 64 bitů byly později shledány kryptograficky slabými proti sofistikovaným útokům, což odráželo vývozní kontrolní předpisy a výpočetní předpoklady své doby. Vývoj směrem k 3G (UMTS) tato slabá místa řešil zavedením silnějšího 128bitového šifrovacího klíče (CK) a nových algoritmů (např. KASUMI), ale KC zůstal nezbytný pro zpětnou kompatibilitu v GSM a pro roamingové scénáře. Jeho specifikace v dokumentech USIM (TS 31.102) zajišťuje, že moderní UICC mohou stále podporovat zastaralou bezpečnost GSM, když je to potřeba, což zdůrazňuje jeho roli v dlouhodobém vývoji a interoperabilitě bezpečnosti buněčných sítí.

## Klíčové vlastnosti

- 64bitový symetrický klíč pro streamové šifrovací algoritmy A5
- Odvozen z tajného klíče účastníka Ki pomocí algoritmu A8
- Bezpečně uložen v SIM/USIM a síťovém AuC
- Nikdy nepřenášen přes rádiové rozhraní
- Používán pro šifrování/dešifrování uživatelského provozu a signalizace na rádiové cestě
- Může být aktualizován během relace pro zvýšení bezpečnosti

## Související pojmy

- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [KC na 3GPP Explorer](https://3gpp-explorer.com/glossary/kc/)
