---
slug: "puci"
url: "/mobilnisite/slovnik/puci/"
type: "slovnik"
title: "PUCI – Protection against Unsolicited Communication for IMS"
date: 2025-01-01
abbr: "PUCI"
fullName: "Protection against Unsolicited Communication for IMS"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/puci/"
summary: "PUCI je bezpečnostní rámec 3GPP v rámci IMS pro identifikaci a blokování nežádoucí komunikace, jako jsou spamové hovory a zprávy. Chrání uživatele před podvody a obtěžováním definováním detekčních mec"
---

PUCI je bezpečnostní rámec 3GPP v rámci IMS, který identifikuje a blokuje nežádoucí komunikaci, jako jsou spamové hovory a zprávy, aby ochránil uživatele před podvody a obtěžováním.

## Popis

Protection against Unsolicited Communication for IMS (PUCI) je standardizovaný bezpečnostní mechanismus definovaný 3GPP pro boj se spamem a další nežádoucí komunikací v rámci sítě IP Multimedia Subsystem (IMS). IMS jako plně IP architektura pro poskytování multimediálních služeb je ze své podstaty zranitelná vůči stejným typům nežádoucího provozu, který obtěžuje internet, jako je spam v IP telefonii ([SPIT](/mobilnisite/slovnik/spit/)) a nežádoucí instantní zprávy. PUCI poskytuje rámec pro identifikaci, hlášení a zmírňování této komunikace za účelem ochrany uživatelského zážitku a síťových zdrojů.

Architektura PUCI zahrnuje několik funkčních entit v jádru IMS. Mezi klíčové součásti patří PUCI Application Server ([AS](/mobilnisite/slovnik/as/)), který hostí logiku pro analýzu signalizace a médií za účelem detekce vzorců ukazujících na spam. Tento AS může komunikovat se Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) přes rozhraní [ISC](/mobilnisite/slovnik/isc/), aby kontroloval zprávy [SIP](/mobilnisite/slovnik/sip/). Může také využívat nebo komunikovat s Reputation Database, která ukládá informace o zdrojích (např. SIP [URI](/mobilnisite/slovnik/uri/), IP adresy) známých jako původci nežádoucí komunikace. Rámec definuje postupy, jak může uživatel nebo síťový operátor nahlásit komunikaci jako nežádoucí, což spustí analýzu a případné zařazení na černou listinu.

Operačně PUCI funguje prostřednictvím kombinace síťových a uživatelem asistovaných mechanismů. Síť může použít heuristickou analýzu parametrů signalizace SIP, vzorců hovorů (např. vysoká frekvence hovorů na různá čísla) nebo dokonce analýzu obsahu. Pokud je komunikace považována za nežádoucí, síť může uplatnit politiky, jako je blokování navázání hovoru/session, jeho přesměrování na server s oznámením nebo jeho propuštění s varovným označením pro uživatele. Uživatel si obvykle může aktivovat osobní černou listinu nebo nahlásit spam prostřednictvím svého User Equipment (UE), které odešle hlášení na PUCI AS. Úkolem rámce je standardizovat tyto interakce mezi UE, jádrem IMS a aplikační vrstvou, čímž zajišťuje interoperabilitu mezi zařízeními různých výrobců a sítěmi poskytovatelů služeb.

## K čemu slouží

PUCI byl vytvořen, aby řešil rostoucí hrozbu spamu a podvodů v telekomunikačních službách založených na IP, konkrétně v ekosystému 3GPP IMS. Když hlasové a zprávové služby migrovaly z tradičních circuit-switched sítí na packet-switched sítě IMS, staly se vystavenými známým zneužitím z internetu. Primárním problémem, který PUCI řeší, je zhoršování důvěry uživatelů a kvality služeb kvůli nežádoucí, často podvodné komunikaci, která může vést k finanční ztrátě, narušení soukromí a prostému obtěžování.

Historicky měla circuit-switched telefonie určité inherentní bariéry proti masovému spamu díky své cenové struktuře a těsnější kontrole, ale VoIP a IMS tyto bariéry významně snížily. Před standardizací PUCI mohli operátoři nasazovat proprietární, neinteroperabilní řešení, což vedlo k fragmentované obraně a špatnému zážitku pro uživatele roamující mezi sítěmi. Motivací pro PUCI bylo poskytnout jednotný, standardy založený přístup, který by mohli implementovat všichni síťoví operátoři 3GPP, a vytvořit tak konzistentnější a účinnější bariéru proti spamu v celosvětovém mobilním ekosystému.

Definováním společného rámce PUCI umožňuje sdílení informací o zdrojích spamu mezi sítěmi a umožňuje vývoj konzistentních uživatelských ovládacích prvků. Řeší omezení předchozích ad-hoc přístupů tím, že zajišťuje, aby zmírňování spamu bylo základní, integrovanou síťovou funkcí, nikoliv dodatečně připojenou aplikací, což zlepšuje jeho účinnost i škálovatelnost, když se IMS stává základem pro všechny komunikační služby, včetně VoLTE a VoNR.

## Klíčové vlastnosti

- Standardizovaný rámec pro detekci spamu v rámci IMS
- Integrace s jádrem IMS prostřednictvím PUCI Application Server
- Podpora jak síťově iniciované, tak uživatelem nahlášené analýzy spamu
- Definuje postupy pro blokování komunikace a doručování varování
- Může komunikovat s databázemi reputace pro hodnocení zdrojů
- Aplikovatelné na různé komunikační služby IMS (hlas, video, zprávy)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SPIT – Spam over IP Telephony](/mobilnisite/slovnik/spit/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 33.838** (Rel-11) — Study on Protection against Unsolicited Communication for IMS
- **TR 33.937** (Rel-19) — Protection against Unsolicited Communication in IMS

---

📖 **Anglický originál a plná specifikace:** [PUCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/puci/)
