---
slug: "mnrg"
url: "/mobilnisite/slovnik/mnrg/"
type: "slovnik"
title: "MNRG – Mobile station Not Reachable for GPRS flag"
date: 2025-01-01
abbr: "MNRG"
fullName: "Mobile station Not Reachable for GPRS flag"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mnrg/"
summary: "Příznak v SGSN signalizující, že UE není dosažitelná pro paketově přepínané služby v GPRS/UMTS. Optimalizuje efektivitu sítě tím, že zabraňuje pokusům o paging pro datové relace, když je známo, že UE"
---

MNRG je příznak v SGSN, který signalizuje, že mobilní stanice není dosažitelná pro paketově přepínané služby GPRS, čímž optimalizuje efektivitu sítě tím, že zabraňuje zbytečným pokusům o paging.

## Popis

Příznak Mobile station Not Reachable for [GPRS](/mobilnisite/slovnik/gprs/) (MNRG) je základní parametr správy mobility definovaný ve specifikaci 3GPP TS 23.060 pro jádro sítě GPRS. Jedná se o logický příznak (boolean flag) uložený v Serving GPRS Support Node (SGSN) jako součást kontextu správy mobility ([MM](/mobilnisite/slovnik/mm/)) pro každé UE. Příznak signalizuje, že SGSN stanovilo, že UE není dosažitelné pro paketově přepínané služby, což znamená, že na něj nelze úspěšně vyslat paging za účelem navázání datové relace nebo doručení dat ve směru downlink.

Příznak MNRG je nastaven SGSN na základě specifických událostí ve stavu správy mobility GPRS daného UE. Hlavním spouštěčem je vypršení časovače 'mobile reachable timer'. Když se UE nachází ve stavu připravenosti (v UMTS např. PMM-CONNECTED) a přejde do stavu nečinnosti (PMM-IDLE), spustí se časovače. Pokud UE před vypršením časovače dosažitelnosti mobilní stanice neprovede žádnou periodickou aktualizaci směrovací oblasti (RAU) ani jinou signalizační aktivitu, SGSN usoudí, že UE je pravděpodobně mimo pokrytí nebo vypnuto, a nastaví příznak MNRG. Může být také nastaven po neúspěšných pokusech o paging pro data ve směru downlink. Pokud je příznak nastaven, SGSN následně odmítne jakékoli pokusy o síťem iniciovaný servisní požadavek (např. při příchodu dat downlink) bez provedení pagingu a vrátí příslušnou příčinu selhání.

Příznak je zrušen, když se UE opět stane dosažitelným, což je detekováno při úspěšném provedení procedury RAU, Servisního požadavku nebo Připojení (Attach). MNRG hraje klíčovou roli v efektivitě sítě napříč paketovými jádry sítí 2G (GPRS) a 3G (UMTS). Díky zapamatování si stavu nedosažitelnosti se SGSN vyhne plýtvání rádiovými prostředky a prostředky jádra sítě na opakované pagingové sekvence pro UE, která nereagují. Tato správa je oddělena od dosažitelnosti v doméně okruhového přepojování ([CS](/mobilnisite/slovnik/cs/)) (kterou řeší [MSC](/mobilnisite/slovnik/msc/)/VLR) a je specifická pro doménu paketového přepojování (PS), čímž tvoří základní část logiky správy mobility v SGSN.

## K čemu slouží

Příznak MNRG byl zaveden pro efektivní správu dosažitelnosti v doméně PS v sítích [GPRS](/mobilnisite/slovnik/gprs/) od verze Release 4. V raných paketových datových službách, bez takového příznaku, síť nepamatovala na nedosažitelnost UE. Každý pokus o doručení dat downlink do nečinné UE by spustil celý postup pagingu, i když předchozí pokusy selhaly, což vedlo k výrazné a nehospodárné signalizační zátěži na rádiovém přístupu i v jádru sítě.

To bylo obzvláště důležité, protože GPRS zavádělo koncepty 'always-on' konektivity, kdy mohlo být UE připojeno, ale neaktivně komunikovat. Příznak MNRG tento problém vyřešil tím, že poskytl SGSN trvalý indikátor stavu. Umožňuje síti rychle odmítnout požadavky pro nedosažitelná UE, čímž šetří kapacitu pagingového kanálu a snižuje procesní zátěž na SGSN a uzlech RAN. Také umožňuje rychlejší zpětnou vazbu externím datovým sítím nebo aplikačním serverům, že data nelze doručit, což jim umožňuje data vyrovnávat nebo s nimi vhodně nakládat. Příznak řeší základní problém mobilních paketových dat: efektivní rozlišení mezi nečinným, ale dosažitelným UE a takovým, které je skutečně nedostupné, což je nezbytné pro škálovatelný provoz sítě.

## Klíčové vlastnosti

- Logický příznak (boolean flag) uložený pro každé UE v kontextu MM v SGSN
- Specifický pro dosažitelnost v doméně paketového přepojování (PS) v GPRS/UMTS
- Nastavován primárně po vypršení časovače dosažitelnosti mobilní stanice
- Také nastavován po neúspěšných pokusech o paging
- Zabraňuje zahájení pagingu pro síťem iniciované servisní požadavky, když je nastaven
- Zrušen úspěšnými procedurami iniciovanými UE, jako je RAU nebo Attach

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [MNRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnrg/)
