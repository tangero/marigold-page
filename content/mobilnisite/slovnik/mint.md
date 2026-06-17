---
slug: "mint"
url: "/mobilnisite/slovnik/mint/"
type: "slovnik"
title: "MINT – Minimization of Service Interruption"
date: 2026-01-01
abbr: "MINT"
fullName: "Minimization of Service Interruption"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mint/"
summary: "Soubor funkcí a procedur 3GPP navržených ke zkrácení doby přerušení služby, kterou zažívá uživatelské zařízení (UE) při událostech mobility, jako je předávání spojení mezi buňkami nebo přístupovými te"
---

MINT je soubor funkcí a procedur 3GPP navržených ke zkrácení doby přerušení služby pro uživatelské zařízení (UE) při událostech mobility, jako je předávání spojení (handover).

## Popis

Minimization of Service Interruption (MINT) je soubor mechanismů standardizovaných v 3GPP ke zkrácení doby, po kterou nemůže uživatelské zařízení (UE) odesílat ani přijímat data uživatelské roviny během procedur mobility. K přerušení služby obvykle dochází při provádění předání spojení (handover), kdy UE přepíná své spojení ze zdrojového síťového uzlu (např. gNB, [eNB](/mobilnisite/slovnik/enb/)) na cílový uzel. Techniky MINT fungují na principu optimalizace fází přípravy, provedení a znovu-nastavení předání spojení jak na úrovni rádiové přístupové sítě (RAN), tak na úrovni jádra sítě (CN).

Z architektonického hlediska MINT zahrnuje vylepšení v několika síťových funkcích. V RAN zahrnuje funkce jako časná příprava handoveru, kdy zdrojový uzel iniciuje načtení kontextu a rezervaci prostředků v cílovém uzlu dlouho předtím, než je skutečný příkaz k handoveru odeslán UE. To je specifikováno v protokolech RAN (např. [NGAP](/mobilnisite/slovnik/ngap/), XnAP). Další klíčovou technikou je handover typu "Make-Before-Break", zvláště relevantní ve scénářích s více spojeními, jako je duální konektivita ([DC](/mobilnisite/slovnik/dc/)) nebo agregace nosných ([CA](/mobilnisite/slovnik/ca/)), kde UE naváže spojení s cílovou buňkou při zachování spojení se zdrojovou buňkou, čímž se eliminuje období přerušení. Jádro sítě podporuje MINT prostřednictvím procedur, jako je optimalizace "Handover without TAU/RAU" pro mobilitu v idle režimu a vylepšení rozhraní N26 pro mobilitu mezi různými jádry sítě (CN) mezi 5GC a EPC.

Z provozní perspektivy MINT funguje minimalizací sekvenčních kroků při handoveru. Například v typickém handoveru z LTE na NR přispívají ke zpoždění měření a hlášení UE, příprava cílové buňky, odvození bezpečnostních klíčů a přepnutí cesty v jádře sítě. Procedury MINT tyto úlohy tam, kde je to možné, paralelizují. Mezi klíčové zapojené komponenty patří funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) pro koordinaci aspektů jádra sítě, zdrojové a cílové gNB pro koordinaci na úrovni RAN a samotné UE, které musí podporovat vylepšené procedury [RRC](/mobilnisite/slovnik/rrc/). Jeho role je v 5G sítích klíčová pro splnění přísných požadavků komunikací s ultra-spolehlivým nízkým zpožděním (URLLC) a pro zajištění plynulého zážitku u služeb v reálném čase, jako je hlas (VoNR) nebo průmyslová automatizace, při změně buňky.

## K čemu slouží

MINT byl vytvořen, aby řešil inherentní přerušení služby, k němuž dochází při předávání spojení v celulárních sítích, což je obzvláště problematické pro případy užití 5G vyžadující vysokou spolehlivost a nízké zpoždění, jako jsou autonomní vozidla, vzdálená chirurgie a rozšířená realita. Tradiční procedury handoveru, ač spolehlivé, zahrnovaly sérii sekvenčních signalizačních kroků, které mohly vést k přerušením v řádu stovek milisekund, což je pro tyto nové služby nepřijatelné. Omezení předchozích přístupů spočívala v jejich reaktivní povaze a nedostatku koordinace mezi RAN a CN během kritické fáze provedení handoveru.

Motivace pro standardizaci MINT ve vydání Release 17 a novějších vychází z principu návrhu 5G podporovat různé požadavky služeb. Před MINT pomohla vylepšení jako přesměrování dat (Data Forwarding) během handoveru v LTE, ale plně neeliminovala dobu přerušení, zejména při handoveru mezi různými gNB nebo mezi různými systémy. MINT poskytuje systematický rámec pro analýzu a snížení každé složky zpoždění handoveru. Řeší problémy jako prodloužené přerušení při handoveru mezi různými rádiovými přístupovými technologiemi ([IRAT](/mobilnisite/slovnik/irat/)) mezi 4G a 5G a při handoverech ve vysokofrekvenčních pásmech (mmWave), kde jsou buňky menší a handovery častější. Minimalizací přerušení zajišťuje kontinuitu služby, což je klíčový ukazatel výkonnosti pro síťové operátory a základní požadavek pro komerční úspěch kritických aplikací využívajících 5G.

## Klíčové vlastnosti

- Časná příprava handoveru a podmíněný handover ke snížení latence rozhodování a provedení
- Provedení handoveru typu "Make-Before-Break" ve scénářích s více spojeními k eliminaci mezery ve službě
- Optimalizovaná signalizace jádra sítě pro mobilitu mezi různými AMF a mezi různými systémy ke snížení zpoždění přepnutí cesty
- Vylepšené mechanismy přenosu kontextu UE mezi zdrojovým a cílovým uzlem pro urychlení nastavení přístupové vrstvy (access stratum)
- Podpora handoveru bez aktualizace sledované oblasti (TAU) nebo registrační oblasti (RAU) pro mobilitu v idle/neaktivním režimu
- Integrace s dělením sítě (network slicing) k zajištění aplikace politik MINT na úrovni každého řezu sítě podle jeho požadavků na službu

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [MINT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mint/)
