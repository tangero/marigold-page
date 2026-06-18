---
slug: "urpp-sgsn"
url: "/mobilnisite/slovnik/urpp-sgsn/"
type: "slovnik"
title: "URPP-SGSN – User Reachability Request Parameter for SGSN"
date: 2025-01-01
abbr: "URPP-SGSN"
fullName: "User Reachability Request Parameter for SGSN"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/urpp-sgsn/"
summary: "URPP-SGSN je specifický parametr používaný ve signalizaci GTP-C (GPRS Tunnelling Protocol – řídicí rovina) mezi Serving GPRS Support Node (SGSN) a Gateway GPRS Support Node (GGSN) nebo Packet Data Net"
---

URPP-SGSN je signalizační parametr GTP-C odesílaný ze SGSN, který žádá GGSN nebo PGW o poskytování oznámení o dosažitelnosti UE za účelem optimalizace doručování downlink dat.

## Popis

User Reachability Request [Parameter](/mobilnisite/slovnik/parameter/) for [SGSN](/mobilnisite/slovnik/sgsn/) (URPP-SGSN) je podrobný informační prvek v rámci [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol pro řídicí rovinu ([GTP-C](/mobilnisite/slovnik/gtp-c/)), specifikovaný v 3GPP TS 29.272 (Evolved Packet System; Mobility Management Entity and Serving GPRS Support Node related interfaces). Používá se v komunikaci mezi Serving GPRS Support Node (SGSN) – která spravuje mobilitu a relace pro UE v přístupu 2G ([GERAN](/mobilnisite/slovnik/geran/)) a 3G ([UTRAN](/mobilnisite/slovnik/utran/)) – a Gateway GPRS Support Node (GGSN) v jádrech GPRS/UMTS, nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v Evolved Packet Core (EPC). Jeho hlavní funkcí je sdělit žádost SGSN ohledně toho, jak si přeje být informována o změnách stavu dosažitelnosti User Equipment (UE) z pohledu brány.

Operačně je URPP-SGSN zahrnut v GTP-C zprávách jako Create Session Request, Modify Bearer Request nebo specifických Context Request/Response zprávách. Parametr obsahuje příznaky, které specifikují preference SGSN. Klíčovým příznakem je 'Request for UE Reachability Notification'. Když je tento příznak nastaven, instruuje GGSN/PGW, aby monitorovalo přechod UE ze stavu nedosažitelnosti (např. kvůli vypnutí, mimo dosah pokrytí nebo prodlouženým časovačům nečinnosti) zpět do stavu dosažitelnosti. Pokud takový přechod brána detekuje (často proto, že obdrží downlink data pro UE, kterou označila jako nedosažitelnou), GGSN/PGW poté odešle zprávu Downlink Data Notification ([DDN](/mobilnisite/slovnik/ddn/)) do SGSN, i když by ji jinak možná neodeslalo. To spustí v SGSN procedury pagingu k vyhledání a navázání spojení s UE.

Tento mechanismus je klíčovou součástí efektivity sítě a úspory energie u UE. Bez URPP-SGSN by GGSN/PGW mohlo tiše zahazovat pakety downlink dat pro UE, které považuje za nedosažitelné, nebo by mohlo agresivně odesílat zprávy DDN, což vede k nepotřebnému pagingu a signalizační zátěži. Tím, že umožňuje SGSN explicitně žádat oznámení pouze v případě potřeby, síť optimalizuje kompromis mezi zajištěním včasného doručení dat a šetřením signalizačních prostředků rádiové sítě a jádra sítě. Rozhodnutí SGSN nastavit příznak je založeno na její lokální politice, profilu účastníka a povaze aktivovaného Packet Data Protocol (PDP) kontextu nebo PDN připojení.

## K čemu slouží

Parametr URPP-SGSN byl zaveden, aby řešil neefektivitu v zacházení s downlink daty a pagingu pro mobilní zařízení, zejména když se sítě vyvíjely pro podporu neustále zapojené IP konektivity a různorodých datových služeb. V raných verzích GPRS byly mechanismy pro oznamování SGSN o čekajících downlink datech méně propracované, což mohlo vést buď ke ztraceným datům (pokud brána příliš snadno rezignovala), nebo k nadměrnému, baterii vyčerpávajícímu pagingu (pokud byla brána příliš agresivní). Tento problém byl obzvláště relevantní pro smartphony a M2M zařízení s přerušovanou konektivitou nebo dlouhými spánkovými cykly.

URPP-SGSN to řeší tím, že dává kontrolu do rukou SGSN, která má přímější znalost o rádiovém stavu a vzorcích mobility UE. Umožňuje SGSN přizpůsobit chování brány na základě jednotlivé relace. Například pro službu synchronizace na pozadí nemusí SGSN žádat oznámení o dosažitelnosti a akceptovat zpoždění dat. Naopak pro službu zasílání zpráv v reálném čase by oznámení vyžádala, aby zajistila promptní doručení. Tato detailní kontrola optimalizuje využití síťových zdrojů (snížením nepotřebné signalizace pagingu) a zlepšuje uživatelský zážitek tím, že zajišťuje včasné doručení důležitých datových toků, zatímco méně kritické toky umožňuje zpracovávat způsobem šetrnějším k síti a baterii. Jeho specifikace v TS 29.272, počínaje Release 9, byla součástí širší standardizace EPC, která zdokonalila interakce mezi SGSN (pro legacy přístup) a novou entitou PGW.

## Klíčové vlastnosti

- Informační prvek GTP-C definovaný v TS 29.272 pro signalizaci SGSN–GGSN/PGW
- Obsahuje příznaky pro žádost o oznámení o stavu dosažitelnosti UE od brány
- Umožňuje optimalizované spouštění zpráv Downlink Data Notification (DDN)
- Umožňuje SGSN řídit chování pagingu na základě politik pro jednotlivé relace/služby
- Snižuje nepotřebnou signalizaci v jádru sítě a rádiové síti pro nedosažitelná UE
- Podporuje efektivní doručování downlink dat pro neustále zapojená PDN připojení

## Související pojmy

- [GTP-C – GPRS Tunnelling Protocol for Control Plane](/mobilnisite/slovnik/gtp-c/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN

---

📖 **Anglický originál a plná specifikace:** [URPP-SGSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/urpp-sgsn/)
