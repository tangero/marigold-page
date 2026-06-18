---
slug: "c-r"
url: "/mobilnisite/slovnik/c-r/"
type: "slovnik"
title: "C/R – Command/Response field bit"
date: 2025-01-01
abbr: "C/R"
fullName: "Command/Response field bit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/c-r/"
summary: "Bit C/R je jednobitové pole v hlavičce protokolové datové jednotky (PDU) vrstvy 2, primárně v protokolech jako LAPDm a jeho derivátech. Rozlišuje mezi příkazovým rámcem odeslaným jednou entitou a odpo"
---

C/R je jednobitové pole v hlavičce PDU vrstvy 2, které rozlišuje rámec typu příkaz od rámce typu odpověď a definuje řídicí vztah pro operace datového spoje.

## Popis

Bit pole Příkaz/Odpověď (C/R) je základní součástí protokolové architektury vrstvy datového spoje (vrstva 2) v systémech 3GPP, konkrétně v rámci procedur přístupu ke spojení na D-kanálu ([LAPD](/mobilnisite/slovnik/lapd/)) a jeho mobilní adaptace LAPDm. Jedná se o jeden binární bit umístěný v adresním poli hlavičky protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)). Jeho jediným účelem je označit, zda je přenášený rámec 'Příkaz' nebo 'Odpověď'. Toto označení není absolutní, ale relativní vůči komunikačnímu kontextu mezi dvěma partnerskými entitami, typicky mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a sítí (např. základnovou stanicí [BSS](/mobilnisite/slovnik/bss/)). Entita iniciující proceduru nebo odesílající rámec vyžadující specifické potvrzení nastaví bit C/R na hodnotu označující Příkaz. Přijímající entita při odpovědi s odpovídajícím potvrzením nebo odpovědním rámcem nastaví bit C/R na hodnotu označující Odpověď. Tento jednoduchý mechanismus vytváří pro dobu trvání operace logického spoje jasný vztah typu pán-služebník nebo příkaz-odpověď.

Z technické perspektivy bit C/R funguje ve spojení s dalšími poli hlavičky vrstvy 2, jako je identifikátor přístupového bodu služby ([SAPI](/mobilnisite/slovnik/sapi/)) a identifikátor koncového bodu terminálu ([TEI](/mobilnisite/slovnik/tei/)). Interpretace hodnoty bitu C/R (0 nebo 1) je definována rolí komunikujících entit. Například v signalizaci rozhraní Um (mezi MS a BSS) jsou rámce odesílané ze sítě do mobilní stanice s SAPI=0 (řízení hovoru) definovány jako příkazy, když C/R=1, a jako odpovědi, když C/R=0. Naopak rámce odesílané z mobilní stanice do sítě s SAPI=0 jsou příkazy, když C/R=0, a odpovědi, když C/R=1. Tato interpretace závislá na roli je klíčová pro zabránění nejednoznačnosti. Bit umožňuje protokolům jako LAPDm implementovat vyvážené a nevyvážené asynchronní procedury, spravovat více logických spojení přes jeden fyzický kanál a koordinovat přenos rámců, jejich opakovaný přenos a řízení chyb.

Při provozu bit C/R řídí procedury jako potvrzování rámců pomocí dozorovacích rámců Receiver Ready ([RR](/mobilnisite/slovnik/rr/)), Receiver Not Ready ([RNR](/mobilnisite/slovnik/rnr/)) a Reject (REJ). Příkazový I-rámec (informační rámec) bude mít svůj bit C/R nastaven podle role odesílatele. Odpovídající potvrzení RR vrácené zpět bude mít bit C/R nastaven na opačnou hodnotu, což jej jasně identifikuje jako odpověď. To je nezbytné pro správnou funkci stavových automatů protokolu, které zajišťují, že jsou zpracovávány pouze očekávané odpovědní rámce. Dále při více-rámcové operaci používané pro přenos dat závisí řazení I-rámců (pomocí pořadových čísel N(S) a N(R)) na jednoznačném dialogu příkaz-odpověď zavedeném bitem C/R, aby byla zachována integrita a pořadí dat. Jeho role je čistě řídicí v rámci vrstvy datového spoje; nepřenáší uživatelská data, ale je nepostradatelný pro spolehlivé navázání, udržování a ukončení signalizačních spojů, která přenášejí zprávy vyšších vrstev pro správu mobility, řízení hovorů a správu relací.

Architektura bitu C/R je konzistentní napříč jeho použitím v různých technických specifikacích 3GPP. Jedná se o nízkourovňovou, trvalou vlastnost signalizačních protokolů vrstvy 2, které se vyvinuly od GSM (používajícího LAPDm) přes UMTS až do LTE a 5G NR pro určité řídicí rovinné protokoly (s adaptacemi ve vrstvách RLC/MAC pro uživatelskou rovinu). I když se konkrétní protokoly využívající přímé pole bitu C/R staly v čistě paketově orientovaných rozhraních pozdějších verzí méně prominentními, základní koncept rozlišování příkazových a odpovědních PDU zůstává zakotven v návrhu stavových automatů následných protokolů vrstvy 2 a 3. Jeho jednoduchost a účinnost v definování komunikačních rolí z něj učinily základní prvek pro spolehlivost signalizace raných digitálních buněčných sítí.

## K čemu slouží

Bit C/R byl vytvořen, aby vyřešil základní problém v komunikaci vrstvy datového spoje přes sdílené nebo point-to-point kanály: jednoznačnou identifikaci rolí. V telekomunikačním systému, kde si dvě partnerské entity vyměňují rámce, je kritické rozlišit mezi rámcem, který iniciuje akci (příkaz), a rámcem, který reaguje na předchozí akci (odpověď). Bez tohoto rozlišení by stavové automaty protokolu mohly špatně interpretovat příchozí rámce, což by vedlo k uváznutí, nesprávnému zacházení s pořadovými čísly nebo neúspěšným procedurám. Bit C/R poskytuje toto rozlišení s minimální režií – pouhým jedním bitem.

Historicky byl tento koncept převzat z protokolu D-kanálu ISDN, LAPD (Q.921), který byl pro mobilní prostředí adaptován jako LAPDm v GSM. Před takovými strukturovanými protokoly vrstvy 2 mohly jednodušší nebo proprietární spoje používat implicitní časování nebo vyhrazené kanály pro příkazy a odpovědi, což bylo méně flexibilní a efektivní. Bit C/R umožnil, aby jeden logický kanál přenášel obousměrné dialogy příkaz/odpověď pro více služeb vyšších vrstev (identifikovaných SAPI), a tím optimalizoval využití vzácných rádiových zdrojů. Vyřešil omezení spočívající v nepřítomnosti trvale přiřazené role 'pána' tím, že učinil označení příkaz/odpověď vlastností každého rámce, určenou rolí odesílatele v daném logickém spoji.

Motivací bylo vytvořit robustní, spolehlivou a standardizovanou signalizační vazbu pro kritické funkce řídicí roviny, jako je zřizování hovoru, předávání hovoru a aktualizace polohy. Tím, že jasně označoval rámce jako příkazy nebo odpovědi, mohl protokol implementovat spolehlivé mechanismy obnovy po chybě (jako opakované přenosy založené na REJ rámcích) a řízení toku. To bylo nezbytné pro udržení kontinuity a kvality služby v prostředí náchylném k chybám. Bit C/R byl tedy klíčovým prvkem umožňujícím automatizovanou, spolehlivou signalizaci, která odlišuje digitální buněčné sítě od jejich analogových předchůdců.

## Klíčové vlastnosti

- Jednobitové pole v adresním poli PDU vrstvy 2
- Definuje rámec buď jako Příkaz, nebo jako Odpověď
- Interpretace závisí na roli (síť vs. mobilní stanice)
- Nezbytný pro fungování LAPDm a podobných protokolů datového spoje
- Umožňuje jasný dialog typu pán-služebník pro stavové automaty protokolu
- Základní pro výměnu dozorovacích rámců (RR, RNR, REJ) a obnovu po chybě

## Související pojmy

- [SAPI – Service Access Point Identifier](/mobilnisite/slovnik/sapi/)
- [TEI – Terminal End-point Identifier](/mobilnisite/slovnik/tei/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [C/R na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-r/)
