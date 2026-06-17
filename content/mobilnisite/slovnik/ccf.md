---
slug: "ccf"
url: "/mobilnisite/slovnik/ccf/"
type: "slovnik"
title: "CCF – Charging Collection Function"
date: 2026-01-01
abbr: "CCF"
fullName: "Charging Collection Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ccf/"
summary: "Funkce pro shromažďování účtovacích údajů (CCF) je prvek jádra sítě zodpovědný za shromažďování, korelaci a předávání záznamů o účtování dat (CDR) z uzlů sítě do fakturační domény. Je nezbytná pro pře"
---

CCF je funkce jádra sítě, která shromažďuje, koreluje a předává záznamy o účtování dat (CDR) z uzlů sítě do fakturační domény pro účtování účastníkům.

## Popis

Funkce pro shromažďování účtovacích údajů (CCF) je kritická součást architektury účtování 3GPP, konkrétně část systému offline účtování ([OFCS](/mobilnisite/slovnik/ofcs/)). Jejím hlavním úkolem je sloužit jako centrální sběrný bod pro záznamy o účtování dat ([CDR](/mobilnisite/slovnik/cdr/)) generované různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) zapojenými do relace účastníka. Mezi tyto NF patří Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN), Gateway GPRS Support Node (GGSN), Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) a později vyvinuté uzly jako Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway (S-GW) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)). CCF přijímá tyto CDR prostřednictvím standardizovaných rozhraní, primárně s využitím referenčního bodu Rf založeného na protokolu Diameter.

Architektonicky se CCF nachází mezi síťovými prvky generujícími účtovací informace a fakturační doménou ([BD](/mobilnisite/slovnik/bd/)). Po přijetí CDR provádí CCF několik klíčových kroků zpracování. Nejprve provádí korelaci, která spočívá v propojení více dílčích CDR generovaných různými síťovými uzly pro jedinou relaci účastníka (např. hlasový hovor nebo datovou relaci) do jediného souvislého záznamu. To je zásadní, protože relace může procházet více síťovými doménami (např. přístupovou, jádrovou). CCF pro přesné provedení tohoto úkolu využívá korelační identifikátory obsažené v CDR.

Po korelaci CCF záznamy formátuje a konsoliduje. Může provádět validační kontroly, aby zajistila integritu a úplnost dat. Zpracované a agregované CDR jsou následně předány fakturační doméně pro tarifikaci, fakturaci a vyúčtování. Provoz CCF může být založen na relacích, kdy shromažďuje záznamy po dobu trvání služby, nebo na událostech, pro jednorázové transakce. Její návrh zajišťuje spolehlivost a často zahrnuje mechanismy pro zpracování ukládání CDR, detekci duplicit a zaručené doručení, aby se zabránilo ztrátám příjmů.

Ve vyvinuté architektuře 5G, ačkoli se termín CCF v původní podobě používá méně často, jsou její funkční odpovědnosti distribuovány a vyvinuty v rámci účtovací funkce (CHF) jako součásti účtovacího rámce 5G. Nicméně základní principy shromažďování, korelace a předávání účtovacích informací zůstávají fundamentální. Implementace CCF je klíčová pro podporu složitých účtovacích scénářů, včetně těch pro roaming, vyúčtování mezi operátory a podrobného účtování vyžadovaného pro architektury založené na službách a síťové slicing.

## K čemu slouží

CCF byla vytvořena, aby řešila rostoucí složitost účtování v mobilních sítích, zejména se zavedením paketově přepínaných datových služeb ve verzi 3GPP Release 99 (UMTS). Předchozí systémy s přepojováním okruhů měly relativně přímočaré účtovací modely založené na délce hovoru. Nástup služeb GPRS a později IP Multimedia Subsystem (IMS) zavedl scénáře s více relacemi, více službami a více operátory, kde účtovací data generovaly četné, geograficky rozptýlené síťové uzly. Bez centralizované funkce pro sběr a korelaci by bylo téměř nemožné přesně rekonstruovat úplný fakturační záznam pro aktivitu jednotlivého uživatele, což by vedlo k fakturačním chybám, únikům příjmů a neschopnosti podporovat pokročilé tarifní modely.

CCF vyřešila problém fragmentovaných účtovacích informací. Poskytla standardizovaný, spolehlivý mechanismus pro shromažďování CDR ze všech zapojených síťových funkcí, jejich korelaci do jednotného záznamu relace a jejich bezpečné doručení do fakturačního systému. To umožnilo operátorům implementovat podrobné a přesné účtování pro nové datové služby, jako je prohlížení internetu, streamování videa a hlasové služby založené na IMS (VoIP). Stala se také základem pro účtování mezi operátory v roamingových scénářích, kde je nutné si účtovací data vyměňovat mezi domovskou a navštívenou sítí.

Dále zavedení CCF formalizovalo architekturu offline účtování v rámci 3GPP a oddělilo řízení účtování v reálném čase (řešené systémem online účtování) od sběru fakturačních dat po události. Toto oddělení umožnilo škálovatelné, vysoce výkonné fakturační systémy schopné zvládnout obrovský objem CDR generovaný v moderních mobilních sítích. Její vývoj je poháněn potřebou podporovat stále složitější služby, kvalitativně diferencované účtování (QoS) a nakonec architekturu založenou na službách v 5G, kde jsou její funkce integrovány do flexibilnější účtovací funkce.

## Klíčové vlastnosti

- Centralizované shromažďování záznamů o účtování dat (CDR) z více síťových funkcí
- Korelace dílčích CDR z různých uzlů do jednotných záznamů relace
- Spolehlivé předávání formátovaných CDR do fakturační domény
- Podpora standardizovaného rozhraní Rf založeného na Diameteru pro doručování CDR
- Validace a kontrola integrity účtovacích informací
- Zpracování jak dat účtování založených na relacích, tak na událostech

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.804** (Rel-7) — SMS/MMS over IP Access Support
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [CCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccf/)
