---
slug: "spr"
url: "/mobilnisite/slovnik/spr/"
type: "slovnik"
title: "SPR – Successful PSCell Addition/Change Report"
date: 2026-01-01
abbr: "SPR"
fullName: "Successful PSCell Addition/Change Report"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/spr/"
summary: "Hlášení generované uživatelským zařízením (UE) po úspěšném dokončení procedury přidání nebo změny PSCell ve scénářích dual connectivity (DC) nebo carrier aggregation (CA). Poskytuje síti potvrzení a p"
---

SPR je hlášení generované uživatelským zařízením (UE) po úspěšném přidání nebo změně PSCell, které potvrzuje konfiguraci SCG síti za účelem efektivního řízení mobility a správy prostředků v dual connectivity nebo carrier aggregation.

## Popis

Hlášení o úspěšném přidání/změně PSCell (SPR) je klíčová signalizační zpráva v sítích 3GPP, konkrétně v kontextu operací dual connectivity ([DC](/mobilnisite/slovnik/dc/)) a carrier aggregation ([CA](/mobilnisite/slovnik/ca/)). Přenáší ji uživatelské zařízení (UE) do sítě, konkrétně k hlavnímu uzlu ([MN](/mobilnisite/slovnik/mn/)) prostřednictvím sekundárního uzlu ([SN](/mobilnisite/slovnik/sn/)) v architekturách [EN-DC](/mobilnisite/slovnik/en-dc/) nebo [NGEN-DC](/mobilnisite/slovnik/ngen-dc/), po úspěšném provedení procedury přidání nebo změny PSCell (Primary Secondary Cell). PSCell je hlavní buňkou sekundární skupiny buněk ([SCG](/mobilnisite/slovnik/scg/)), kterou spravuje sekundární uzel (např. gNB v NR nebo en-gNB v EN-DC). SPR slouží jako explicitní potvrzení, že UE úspěšně aplikovalo novou konfiguraci rádiových prostředků pro SCG, včetně nového PSCell, nařízenou sítí prostřednictvím zprávy [RRC](/mobilnisite/slovnik/rrc/) Reconfiguration.

Generování a přenos SPR je spuštěno specifickými podmínkami definovanými v protokolu RRC. Když UE přijme zprávu RRCReconfiguration obsahující konfiguraci `secondaryCellGroup` (pro přidání nebo změnu SCG), aplikuje novou konfiguraci. Po úspěšném dokončení náhodného přístupu k novému PSCell a aplikaci konfigurace SCG sestaví UE zprávu RRCReconfigurationComplete. Pokud rekonfigurace zahrnovala `sCellToReleaseList` nebo `sCellToAddModList` pro SCG, nebo zahrnovala změnu samotného PSCell, UE zahrne SPR do této zprávy RRCReconfigurationComplete. SPR obsahuje kritické informační prvky, jako je `measResultSCG`, který zahrnuje výsledky měření pro nový PSCell (jako RSRP a RSRQ) a případně další měření buněk SCG, čímž poskytuje síti okamžitou zpětnou vazbu o rádiových podmínkách nově nakonfigurovaných buněk.

Z architektonického hlediska proudí SPR od UE k SN (který ji přijímá jako součást RRC zprávy přes rozhraní vzduchu) a SN následně přeposílá relevantní obsah k MN přes rozhraní Xn nebo X2-C (např. ve zprávě SN Reconfiguration Complete). To umožňuje, aby byl MN, který spravuje celkové spojení a řízení mobility, informován o úspěšné rekonfiguraci SCG. Informace v SPR jsou zásadní pro algoritmy správy rádiových prostředků (RRM) sítě. Potvrzují úspěch procedury podobné handoveru v rámci SCG, umožňují síti ověřit, že UE je správně připojeno k zamýšlenému PSCell, a poskytují čerstvá měřicí data, která lze použít pro následná rozhodnutí o mobilitě, vyvažování zátěže a přizpůsobení spojení.

Mechanismus SPR zvyšuje spolehlivost a efektivitu operací s více spojeními. Bez takového hlášení by síť musela úspěch odvozovat nepřímo, což by mohlo vést k opožděné detekci selhání nebo suboptimálním stavům prostředků. Poskytnutím potvrzené aktualizace stavu pomáhá SPR udržovat synchronizaci mezi konfigurací UE a pohledem sítě, snižuje čas potřebný k zotavení z neúspěšných pokusů o rekonfiguraci a podporuje pokročilé funkce, jako je rychlé přidání SCG pro směrování provozu a zlepšení přenosových rychlostí. Je základním prvkem pro robustní provoz funkcí jako NR-DC, NE-DC a NR CA, kde rychlá a spolehlivá konfigurace sekundárních uzlů je nezbytná pro využití plného potenciálu agregovaného spektra a nasazení s více RAT.

## K čemu slouží

SPR bylo zavedeno, aby řešilo specifické výzvy řízení a správy vzniklé se zavedením dual connectivity a pokročilé carrier aggregation v sítích 3GPP. Před DC zahrnovaly události mobility typicky změnu jedné buňky (handover) s jasným hlášením úspěchu/selhání. S DC, kde je UE připojeno k hlavnímu a sekundárnímu uzlu současně, se procedury jako přidání, změna nebo uvolnění sekundární skupiny buněk (SCG) staly složitějšími. Síť potřebovala spolehlivý mechanismus k potvrzení, že UE úspěšně provedlo tyto složité rekonfigurační příkazy, zejména kritický krok přístupu k novému PSCell.

Hlavním problémem, který SPR řeší, je absence explicitního hlášení úspěchu pro modifikace SCG. Bez něj by síť mohla předpokládat, že rekonfigurace byla úspěšná na základě odeslání příkazu, zatímco UE ji mohlo selhat aplikovat kvůli rádiovým problémům nebo chybám v konfiguraci. To by mohlo vést k desynchronizovanému stavu, kdy síť plánuje data na prostředcích, které UE nemůže používat, což způsobuje ztrátu dat a neefektivní využití prostředků. SPR poskytuje mechanismus uzavřené smyčky řízení, který zajišťuje, že entita RRM sítě obdrží definitivní potvrzení a čerstvá rádiová měření, což jí umožňuje činit informovaná následná rozhodnutí.

Historicky, jak se 3GPP vyvíjelo od LTE Carrier Aggregation (které zahrnovalo jediný eNB) k Dual Connectivity mezi LTE a později 5G NR, potřeba mezilehlé koordinace se zesílila. SPR, zavedené v kontextu těchto vylepšení, se stalo základním kamenem spolehlivé správy více spojení. Podporuje nadřazené cíle zvýšení přenosových rychlostí, plynulé mobility a vyvažování zátěže napříč více uzly nebo frekvencemi tím, že dává síti ověřený 'zelený signál' před plným využitím nově nakonfigurovaných sekundárních prostředků. Toto explicitní hlášení je zvláště klíčové pro robustnost funkcí jako podmíněné přidání/změna PSCell (CPAC), kde hlášení úspěchu validuje provedení dříve připravené podmíněné konfigurace.

## Klíčové vlastnosti

- Spuštěno po úspěšné aplikaci rekonfigurace SCG zahrnující přidání nebo změnu PSCell.
- Obsahuje pole `measResultSCG` s výsledky měření (např. RSRP/RSRQ) pro nový PSCell.
- Přenášeno uvnitř zprávy `RRCReconfigurationComplete` od UE do sítě.
- Poskytuje explicitní potvrzení síťovému RRM pro spolehlivou synchronizaci stavu.
- Podporuje jak architektury LTE-NR Dual Connectivity (EN-DC), tak NR-NR Dual Connectivity (NR-DC).
- Umožňuje rychlejší zotavení z neúspěšných pokusů o rekonfiguraci tím, že poskytuje jasné vymezení úspěchu/selhání.

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 29.154** (Rel-19) — Nt Reference Point Protocol
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.816** (Rel-10) — PCRF Failure & Restoration Study
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 32.421** (Rel-19) — Subscriber & Equipment Trace Concepts & Requirements
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 32.820** (Rel-8) — Charging Architecture Study for Evolved 3GPP
- **TS 32.843** (Rel-13) — PS Domain Online Charging in Roaming
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [SPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/spr/)
