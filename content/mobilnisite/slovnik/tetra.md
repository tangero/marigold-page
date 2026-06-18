---
slug: "tetra"
url: "/mobilnisite/slovnik/tetra/"
type: "slovnik"
title: "TETRA – Trans European Trunked RAdio"
date: 2026-01-01
abbr: "TETRA"
fullName: "Trans European Trunked RAdio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tetra/"
summary: "Standard profesionální mobilní radiokomunikace (PMR) pro kritickou komunikaci, přijatý 3GPP za účelem umožnění integrace s celulárními sítěmi. Poskytuje zabezpečené a spolehlivé hlasové a datové služb"
---

TETRA je standard profesionální mobilní radiokomunikace pro kritickou komunikaci, který poskytuje zabezpečené a spolehlivé hlasové a datové služby organizacím, jako jsou složky integrovaného záchranného systému a doprava, a nabízí funkce skupinového volání a přímého režimu provozu.

## Popis

Trans European Trunked RAdio (TETRA) je digitální trunkovaný radiový standard původně vyvinutý [ETSI](/mobilnisite/slovnik/etsi/) pro profesionální a vládní použití, který byl začleněn do specifikací 3GPP pro usnadnění interoperability a konvergence s veřejnými celulárními sítěmi, jako jsou LTE a 5G. V rámci 3GPP je TETRA řešeno v několika technických specifikacích, včetně TS 22.179 (Mission Critical Push to Talk), TS 23.283 (Mission Critical Services Architecture) a TS 36.868 (LTE-based TETRA enhancements). Systém pracuje ve vyhrazených kmitočtových pásmech (obvykle pod 1 GHz) a využívá vícečetný přístup s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) se čtyřmi časovými sloty na nosnou, což nabízí efektivní využití spektra a podporuje hlasové, datové a služby krátkých zpráv.

Z architektonického hlediska se samostatná síť TETRA skládá ze základnových stanic ([TBS](/mobilnisite/slovnik/tbs/)), přepínací a řídicí infrastruktury (TETRA Infrastructure) a mobilních stanic ([MS](/mobilnisite/slovnik/ms/)). Mezi klíčové komponenty patří TETRA Terminal Equipment ([TE](/mobilnisite/slovnik/te/)) pro uživatelské rozhraní a TETRA Mobile Equipment ([ME](/mobilnisite/slovnik/me/)) pro rádiové funkce. Práce 3GPP se zaměřuje na integraci služeb TETRA s jádry LTE/5G, což umožňuje funkce jako Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) přes širokopásmové připojení. To zahrnuje definici funkcí pro vzájemné propojení a bran, které mapují signalizaci TETRA a provoz v uživatelské rovině na protokoly 3GPP, což umožňuje dvou režimovým zařízením bezproblémový přístup k sítím TETRA i celulárním. Například skupinová volání zahájená v síti TETRA mohou být rozšířena na uživatele LTE prostřednictvím aplikačního serveru MCPTT s využitím IMS pro řízení relace.

Provoz TETRA klade důraz na spolehlivost a zabezpečení, s vestavěným šifrováním (na rádiovém rozhraní a end-to-end), rychlým navázáním hovoru (pod 300 ms) a přímým režimem provozu (DMO) pro komunikaci mezi zařízeními bez infrastruktury. V kontextech 3GPP jsou tyto schopnosti vylepšeny integrací s EPS a 5GS. Specifikace jako TS 23.782 a TS 23.783 podrobně popisují scénáře, kdy se sítě TETRA propojují se systémy 3GPP pro kontinuitu služeb, například využití LTE pro vysokorychlostní data při současné závislosti na TETRA pro kritický hlas. Tento hybridní přístup zajišťuje, že organizace pro veřejnou bezpečnost těží z širokopásmových schopností při zachování robustního a prověřeného výkonu TETRA pro životně důležitou komunikaci.

## K čemu slouží

TETRA bylo vytvořeno za účelem splnění přísných požadavků uživatelů profesionální mobilní radiokomunikace, jako jsou policie, hasiči, záchranná služba a dopravní operátoři, kteří potřebují zabezpečenou, okamžitou a skupinově orientovanou komunikaci nad rámec toho, co nabízely komerční celulární sítě. Před TETRA trpěly analogové PMR systémy omezenou kapacitou, špatnou kvalitou hlasu a nedostatkem šifrování, což je činilo nevhodnými pro kritické mise. TETRA tyto nedostatky řešilo digitálním trunkovaným návrhem, který poskytoval efektivní využití spektra, pokročilé funkce jako skupinové volání a přednostní přerušení a silné zabezpečení – čímž reagovalo na potřebu spolehlivé koordinace v nouzových situacích.

Přijetí specifikací souvisejících s TETRA organizací 3GPP, počínaje Release 12, bylo motivováno rostoucí poptávkou po kritické komunikaci s podporou širokopásmového připojení a konvergencí vyhrazených PMR sítí s veřejnou celulární infrastrukturou. Jak se vyvíjely LTE a 5G, nabízely vysokorychlostní data, ale zpočátku postrádaly funkce kritického hlasu vlastní TETRA. Standardizací integrace TETRA umožnilo 3GPP migrační cestu, kde organizace mohly využít LTE/5G pro aplikace jako video streamování nebo datová analýza při zachování prověřených hlasových schopností TETRA, čímž se vyřešil problém technologického přechodu bez obětování operační účinnosti.

Tato integrace dále podporuje regulační a vládní iniciativy pro modernizované sítě pro veřejnou bezpečnost (např. FirstNet v USA, [ESN](/mobilnisite/slovnik/esn/) ve Velké Británii). Řeší omezení izolovaných systémů tím, že umožňuje interoperabilitu mezi sítěmi TETRA a 3GPP, usnadňuje spolupráci mezi agenturami a sdílení zdrojů. Vývoj prostřednictvím releasů 3GPP zajišťuje, že silné stránky TETRA – jako je pokrytí v odlehlých oblastech prostřednictvím DMO a odolnost při zahlcení sítě – jsou doplněny celulárním širokopásmovým připojením, což zajišťuje budoucí připravenost kritické komunikace pro éru IoT, chytrých měst a pokročilých záchranných služeb.

## Klíčové vlastnosti

- Digitální trunkovaná radiokomunikace s TDMA (4 sloty na nosnou) pro efektivní využití spektra
- Zabezpečená komunikace s vestavěným šifrováním a autentizací
- Skupinové volání (push-to-talk) a přímý režim provozu (zařízení-zařízení)
- Rychlé navázání hovoru a přednostní přerušení pro kritické uživatele
- Integrace se sítěmi 3GPP LTE/5G pro širokopásmová data a služby MCPTT
- Robustní pokrytí a spolehlivost pro aplikace kritické z hlediska mise

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)

## Definující specifikace

- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TS 22.468** (Rel-19) — Group Communication System Enabler Requirements
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.779** (Rel-13) — MCPTT over LTE Stage 2 Study
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems
- **TR 26.989** (Rel-19) — MCPTT Enhancement Analysis
- **TS 36.868** (Rel-12) — Study on Group Communication for E-UTRA

---

📖 **Anglický originál a plná specifikace:** [TETRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tetra/)
