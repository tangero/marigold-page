---
slug: "mlc"
url: "/mobilnisite/slovnik/mlc/"
type: "slovnik"
title: "MLC – Mobile Location Center"
date: 2025-01-01
abbr: "MLC"
fullName: "Mobile Location Center"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mlc/"
summary: "Prvek jádrové sítě v mobilních sítích 2G, 3G a 4G zodpovědný za poskytování služeb založených na poloze (LCS). Vypočítává zeměpisnou polohu mobilních zařízení, spravuje požadavky na polohu a vynucuje"
---

MLC je prvek jádrové sítě zodpovědný za výpočet zeměpisné polohy mobilních zařízení, správu požadavků na polohu a vynucování nastavení soukromí za účelem poskytování služeb založených na poloze.

## Popis

Mobile Location Center (MLC) je klíčová funkční entita v architektuře služeb založených na poloze ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP. Jejím hlavním úkolem je určit zeměpisnou polohu mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelského zařízení (UE) a poskytnout tuto informaci o poloze autorizovaným klientům, známým jako klienti služeb založených na poloze (LCS Clients). MLC není jediný fyzický uzel, ale logická funkce, která může být distribuována; typicky je rozdělena na Gateway MLC ([GMLC](/mobilnisite/slovnik/gmlc/)) a Serving MLC ([SMLC](/mobilnisite/slovnik/smlc/)). GMLC funguje jako rozhraní mezi mobilní sítí a externími LCS klienty. Zpracovává autentizaci, autorizaci a účtování požadavků na polohu, směruje požadavky do příslušné sítě (pokud je cílové UE v roamingu) a doručuje konečný odhad polohy klientovi. SMLC naopak sídlí blíže k rádiové přístupové síti a je zodpovědná za samotný výpočet polohy. Vybere metodu určování polohy, shromáždí potřebná měřicí data z UE a/nebo sítě (např. z základnových stanic) a vypočítá odhad polohy.

MLC funguje prostřednictvím řady standardizovaných rozhraní a protokolů. GMLC komunikuje s externími klienty přes rozhraní Le, často za použití protokolů jako [MLP](/mobilnisite/slovnik/mlp/) (Mobile Location Protocol). Uvnitř jádrové sítě GMLC komunikuje s [HLR](/mobilnisite/slovnik/hlr/) nebo [HSS](/mobilnisite/slovnik/hss/) přes rozhraní Lh, aby získal směrovací informace (např. který [MSC](/mobilnisite/slovnik/msc/) nebo MME aktuálně obsluhuje cílové UE). Poté přepošle požadavek na polohu do příslušného MSC, SGSN nebo MME přes rozhraní Lg. Požadavek je předán SMLC (přes rozhraní Lb v GERAN, Iupc v UTRAN nebo SLs v E-UTRAN). SMLC řídí relaci určování polohy. V závislosti na metodě – jako je Cell-ID, OTDOA (Observed Time Difference of Arrival), U-TDOA nebo A-GPS – SMLC instruuje UE a/nebo rádiovou síť (např. BSC, RNC, eNB), aby provedla specifická měření. Tato měření (např. časové posuny, síly signálu, GPS pseudovzdálenosti) jsou nahlášena zpět SMLC, která je zpracuje pomocí polohovacích algoritmů, aby odvodila zeměpisnou šířku, délku a odhady přesnosti.

Klíčové komponenty v rámci funkce MLC zahrnují Location Request Handler (v GMLC), Positioning Function (v SMLC) a Privacy Profile Register, který ukládá souhlas účastníka a pravidla soukromí. Role MLC přesahuje pouhý výpočet; je ústřední pro celý ekosystém LCS. Zajišťuje, aby získávání polohy bylo bezpečné, v souladu s pravidly ochrany soukromí a efektivní. Podporuje různé metody určování polohy, aby vyvážila přesnost, dobu odezvy a dopad na síť. Pro služby tísňového volání (např. E911, E112) pracuje MLC v prioritním režimu, aby poskytla rychlou informaci o poloze veřejné tísňové lince (PSAP). V komerčních aplikacích umožňuje služby jako navigace, vyhledávač přátel, reklama založená na poloze a sledování vozového parku. Architektura MLC se vyvinula tak, aby podporovala bezproblémové služby založené na poloze napříč přístupovými technologiemi 2G (GERAN), 3G (UTRAN) a 4G (E-UTRAN).

## K čemu slouží

MLC byl vytvořen za účelem standardizace a umožnění služeb založených na poloze (LBS) v mobilních sítích, což se stalo regulatorním požadavkem a významnou komerční příležitostí. Původně hlavním hybatelem byly služby tísňového volání; vlády nařídily, že mobilní sítě musí být schopny poskytnout polohu volajícího při tísňovém volání (např. 911, 112). Tento požadavek na veřejnou bezpečnost vyžadoval spolehlivý, přesný a síťově integrovaný polohovací systém, který architektura MLC poskytla. Před standardizovanými LCS by jakákoli služba založená na poloze byla proprietárním, neinteroperabilním řešením, což by omezovalo její škálovatelnost a spolehlivost pro kritické služby.

Komerčně vzestup mobilních dat a chytrých telefonů vytvořil obrovský trh pro aplikace využívající polohu. MLC vyřešil problém, jak zpřístupnit inherentní schopnost sítě lokalizovat zařízení (např. prostřednictvím buněčných věží) třetím stranám – poskytovatelům služeb – kontrolovaným, bezpečným a zúčtovatelným způsobem. Řešil klíčové výzvy: soukromí (zajištění, že poloha účastníka není zveřejněna bez souhlasu), bezpečnost (autentizace klientů), interoperabilita (fungování napříč různými dodavateli sítí a generacemi) a přesnost (podpora více polohovacích technik). MLC oddělil obchodní logiku a klientské rozhraní (GMLC) od rádiově specifické polohovací technologie (SMLC), což umožnilo jejich nezávislý vývoj. Tento modulární design umožnil operátorům zavádět nové, přesnější metody určování polohy (jako A-GPS) v rádiové síti, aniž by narušili poskytování služeb stávajícím LCS klientům.

## Klíčové vlastnosti

- Poskytuje bránovou funkcionalitu (GMLC) pro autentizaci, autorizaci a směrování požadavků externích LCS klientů.
- Hostuje obslužnou funkcionalitu (SMLC) pro výběr metod určování polohy a výpočet odhadů polohy.
- Podporuje více polohovacích technik (Cell-ID, OTDOA, U-TDOA, A-GPS) pro různé potřeby přesnosti.
- Vynucuje zásady ochrany soukromí účastníků a kontroluje souhlas před zveřejněním informace o poloze.
- Spolupracuje s prvky jádrové sítě (HLR/HSS, MSC, SGSN, MME) za účelem lokalizace účastníků v roamingu.
- Umožňuje určování polohy pro služby tísňového volání (např. E911) s vysokou prioritou a spolehlivostí.

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GPS – Assisted Global Positioning System](/mobilnisite/slovnik/a-gps/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.297** (Rel-19) — Charging Data Record File Transfer

---

📖 **Anglický originál a plná specifikace:** [MLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mlc/)
