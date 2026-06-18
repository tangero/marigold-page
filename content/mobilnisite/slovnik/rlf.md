---
slug: "rlf"
url: "/mobilnisite/slovnik/rlf/"
type: "slovnik"
title: "RLF – Radio Link Failure"
date: 2026-01-01
abbr: "RLF"
fullName: "Radio Link Failure"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rlf/"
summary: "Stav vyhlášený UE nebo síťovým uzlem (gNB), když se kvalita rádiového spoje zhorší za obnovitelné meze, což vede k selhání spojení. Spouští kritické procedury obnovy, jako je RRC re-establishment nebo"
---

RLF je stav vyhlášený UE nebo gNB, když se kvalita rádiového spoje zhorší za obnovitelné meze, což způsobí selhání spojení a spustí procedury obnovy, jako je RRC re-establishment.

## Popis

Radio Link Failure (RLF) je kritická událost v 3GPP celulárních sítích, při které se rádiové spojení mezi uživatelským zařízením (UE) a jeho obsluhující buňkou stane nepoužitelným a je vyhlášeno jako selhané. Nejde o jediný měřený parametr, ale o procedurální výsledek spuštěný specifickými standardizovanými podmínkami sledovanými jak UE, tak sítí (např. gNB v NR). Primární mechanismus detekce RLF na straně UE je založen na sledování kvality rádiového spoje prostřednictvím měření fyzické vrstvy. V LTE a NR je to typicky řízeno časovači T310 a T311 a čítači jako N310 a N311. Proces zahrnuje kontinuální vyhodnocování kvality downlinku fyzickou vrstvou UE (např. na základě Cell-specific Reference Signal ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Synchronization Signal Block (SSB)/Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) v NR). Pokud kvalita klesne pod práh (Q_out), fyzická vrstva indikuje vyšším vrstvám 'out-of-sync'. Po přijetí souvislého počtu (N310) indikací 'out-of-sync' spustí UE časovač T310. Pokud se kvalita rádiového spojení neobnoví (přijetím N311 indikací 'in-sync') před vypršením T310, UE vyhlásí RLF a zahájí procedury obnovení spojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/) connection re-establishment) ve snaze o obnovu.

Z pohledu sítě může gNB také usoudit na RLF na základě problémů s uplinkem nebo nedostatečného přijetí očekávané zpětné vazby (např. absence [HARQ](/mobilnisite/slovnik/harq/) [ACK](/mobilnisite/slovnik/ack/) potvrzení nebo [CQI](/mobilnisite/slovnik/cqi/) reportů) po určité období. Vyhlášení RLF je definitivní stav, který přesouvá spojení mimo normální provoz. Po vyhlášení RLF UE pozastaví všechny rádiové nosiče kromě SRB0, vybere vhodnou buňku (ne nutně nejsilnější) a vůči této buňce zahájí proceduru RRC Re-establishment. Tato procedura má za cíl rychle obnovit signalizační spojení a při úspěchu může také znovu aktivovat datové nosiče s minimálním přerušením služby. Pokud se re-establishment nezdaří, UE přejde do stavu RRC_IDLE a musí provést nové nastavení spojení. Síť využívá RLF reporty, které může UE zaznamenat a po opětovném připojení odeslat, k analýze příčin selhání. Tyto reporty obsahují cenná data, jako je poloha, měření obsluhující a sousedních buněk před selháním a identifikovaná příčina selhání, což umožňuje funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) pro optimalizaci mobility.

RLF je vnitřně propojeno se správou mobility. Špatné nastavení parametrů handoveru (např. prahové hodnoty, čas do spuštění) je hlavní příčinou RLF, což vede k příliš pozdním nebo příliš časným handoverům, nebo handoverům do nevhodných buněk. Detekce a reportování RLF jsou proto ústřední pro funkce SON pro optimalizaci robustnosti mobility ([MRO](/mobilnisite/slovnik/mro/)). Síť analyzuje statistiky RLF a selhání handoveru, aby automaticky upravila parametry mobility, snížila počet spadlých hovorů a zlepšila uživatelský zážitek. V pokročilých nasazeních, jako je duální konektivita, může být RLF vyhlášeno pro specifickou skupinu buněk (Master nebo Secondary), což spustí specifické akce obnovy bez nutnosti zrušit celé spojení.

## K čemu slouží

Radio Link Failure existuje jako formalizovaný, standardizovaný koncept, který poskytuje jasný a konzistentní mechanismus detekce selhání a obnovy pro rádiová spojení v mobilních sítích. Rádiové prostředí je dynamické; síla signálu se může rychle zhoršit v důsledku mobility uživatele, překážek nebo interference. Bez dobře definované RLF procedury by se UE mohlo donekonečna pokoušet komunikovat přes ztracený spoj, plýtvat baterií a rádiovými prostředky, nebo by spojení přerušilo nekontrolovaným způsobem, což by vedlo ke špatnému uživatelskému zážitku a obtížím v diagnostice sítě. RLF rámec to řeší stanovením jednoznačných kritérií (časovače, čítače, prahové hodnoty) pro vyhlášení selhaného spoje, což zajišťuje, že UE i síť mají společné porozumění stavu spojení.

Jeho vytvoření bylo motivováno potřebou robustní mobility a správy spojení, zejména když se sítě vyvíjely k vyšším rychlostem a složitějším scénářům v LTE (od Rel-8 dále) a 5G NR. Dřívější systémy měly méně sofistikované zpracování selhání spoje. Formální RLF procedury, zavedené a vylepšené od Rel-8/Rel-9 dále, umožňují předvídatelné chování obnovy. Řeší problém 'výpadku rádiového spoje' spuštěním rychlého a standardizovaného pokusu o obnovu (RRC re-establishment), který je rychlejší než navazování nového spojení od nuly. Navíc přidružený mechanismus RLF reportování, významně vylepšený v pozdějších releasech, řeší kritický problém optimalizace sítě 'odstraňování závad selhání mobility'. Shromažďováním podrobných záznamů o selháních od UE mohou operátoři automaticky identifikovat a opravit suboptimální konfigurace sítě (jako jsou parametry handoveru), což přímo zlepšuje spolehlivost sítě a snižuje počet spadlých hovorů. RLF tedy není jen ukazatelem selhání, ale základním prvkem umožňujícím automatizované samoléčení a optimalizaci sítě.

## Klíčové vlastnosti

- Spuštěno indikacemi 'out-of-sync' z fyzické vrstvy překračujícími nastavené prahy (N310, T310)
- Zahajuje proceduru obnovení RRC spojení (RRC connection re-establishment) pro obnovu
- Podporuje podrobné zaznamenávání a reportování selhání (RLF reporty) pro optimalizaci sítě
- Nedílná součást optimalizace robustnosti mobility (MRO) v SON
- Může být detekováno jak UE, tak síťovými uzly
- Konfigurovatelné parametry umožňují ladění pro různé scénáře nasazení a podmínky mobility

## Související pojmy

- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TS 25.704** (Rel-12) — Study on Enhanced Broadcast of System Information
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TR 28.837** (Rel-18) — Technical Report on Trace/MDT Management
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.421** (Rel-19) — Subscriber & Equipment Trace Concepts & Requirements
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 32.442** (Rel-19) — Trace Management IRP: Information Service
- **TS 32.446** (Rel-19) — Trace Management IRP Solution Set Definitions
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TR 33.877** (Rel-18) — Technical Report on Security Aspects of AI/ML in RAN
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.839** (Rel-11) — HetNet Mobility Improvements for LTE
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [RLF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlf/)
