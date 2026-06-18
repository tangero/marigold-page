---
slug: "oli"
url: "/mobilnisite/slovnik/oli/"
type: "slovnik"
title: "OLI – Originating Line Information"
date: 2025-01-01
abbr: "OLI"
fullName: "Originating Line Information"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/oli/"
summary: "Originating Line Information (OLI, informace o volající lince) je parametr používaný v signalizaci hovorů v rámci IP Multimedia Subsystem (IMS). Identifikuje typ linky nebo služby, ze které hovor poch"
---

OLI je parametr signalizace hovoru v IMS, který identifikuje typ volající linky, jako je například telefonní automat nebo mobilní síť, pro účely účtování, směrování a servisní logiky.

## Popis

Originating Line Information (OLI, informace o volající lince) je standardizovaný parametr přenášený v rámci signalizačních zpráv [SIP](/mobilnisite/slovnik/sip/), konkrétně v hlavičce P-Asserted-Identity nebo v jiných odpovídajících polích dle definice 3GPP. Jedná se o číselný nebo alfanumerický kód udávající charakteristiky linky, ze které hovor nebo relace v síti IMS pochází. Hodnotu OLI typicky vkládá Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) volající sítě nebo Application Server ([AS](/mobilnisite/slovnik/as/)) na základě abonentních dat nebo konfigurace sítě.

V architektuře IMS se parametr OLI šíří od sítě volajícího účastníka přes Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) do sítě příjemce. Tvoří součást záznamů o detailech hovoru ([CDR](/mobilnisite/slovnik/cdr/)) generovaných pro účely účtování. Operátoři sítí a poskytovatelé služeb používají OLI k rozlišení různých typů původu hovoru, což umožňuje diferencované tarify, specifické směrovací politiky (např. priorita nouzových hovorů z telefonních automatů) nebo spouštění přidaných služeb.

Definice a použití parametru jsou specifikovány v 3GPP TS 24.229 (IP multimedia call control protocol) a TS 29.163 (Interworking between the IP Multimedia ([IM](/mobilnisite/slovnik/im/)) Core Network (CN) subsystem and Circuit Switched ([CS](/mobilnisite/slovnik/cs/)) networks). Zatímco jeho základní funkce zůstala neměnná, jeho existence zajišťuje zpětnou kompatibilitu a spolupráci s legacy okruhově komutovanými sítěmi, kde byly podobné informace o lince používány v signalizaci [ISUP](/mobilnisite/slovnik/isup/). OLI je klíčovým prvkem pro zákonné odposlechy, detekci podvodů a zajištění regulatorní shody přesným identifikováním charakteru přístupu volající strany.

## K čemu slouží

OLI byl zaveden za účelem překlenutí sémantické mezery mezi tradiční okruhově komutovanou telefonií a novým IP-based IMS. V legacy sítích PSTN/ISDN parametr Calling Party's Category v signalizaci ISUP přenášel podobné informace o volající lince (např. běžný účastník, telefonní automat, testovací linka). Tato data byla nezbytná pro fakturační systémy a síťové operace.

Při migraci na IMS a čistě IP sítě vznikla potřeba zachovat tento klíčový informační prvek, aby bylo možné udržet stávající obchodní logiku, regulatorní požadavky a schopnosti služeb. OLI řeší problém ztráty kontextu původu při přechodu hovorů z TDM na IP. Zajišťuje, že poskytovatelé služeb mohou i nadále aplikovat rozdílné účtování, implementovat specifické směrování pro určité typy linek (jako jsou volné hovory z telefonních automatů) a plnit zákonné povinnosti týkající se trasování a identifikace hovorů.

Jeho vytvoření bylo motivováno požadavkem na paritu funkcí mezi sítěmi a bezproblémovou spolupráci během přechodového období. Bez OLI by sítě IMS postrádaly standardizovaný mechanismus pro předávání této třídy informací, což by vedlo k nekonzistencím v účtování, poskytování služeb a potenciálním porušením telekomunikačních předpisů.

## Klíčové vlastnosti

- Standardizovaný parametr v rámci signalizace SIP/IMS
- Identifikuje typ volající linky (např. telefonní automat, mobilní síť, ISDN)
- Používá se pro fakturační diferenciaci a účtování
- Umožňuje specifickou servisní logiku a rozhodování o směrování
- Podporuje regulatorní shodu a zákonné odposlechy
- Usnadňuje spolupráci s legacy okruhově komutovanými sítěmi

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [OLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/oli/)
