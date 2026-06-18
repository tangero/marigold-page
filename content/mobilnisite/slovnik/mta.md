---
slug: "mta"
url: "/mobilnisite/slovnik/mta/"
type: "slovnik"
title: "MTA – Multilateration Timing Advance"
date: 2025-01-01
abbr: "MTA"
fullName: "Multilateration Timing Advance"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mta/"
summary: "Metoda určování polohy v sítích GSM, GERAN a LTE-M, která stanovuje umístění mobilního zařízení měřením časového rozdílu příchodu (TDOA) jeho rádiových signálů na více geograficky rozptýlených základn"
---

MTA je metoda určování polohy, která stanovuje umístění mobilního zařízení měřením časového rozdílu příchodu jeho signálů na více základnových stanic a řešením hyperbolických rovnic.

## Popis

Multilateration Timing Advance (MTA) je síťová metoda určování polohy standardizovaná 3GPP, původně pro GSM/[GERAN](/mobilnisite/slovnik/geran/) a později adaptovaná pro LTE-M (Cat-M) a NB-IoT. Jedná se o formu techniky Time Difference of Arrival (TDOA). Na rozdíl od základního Timing Advance ([TA](/mobilnisite/slovnik/ta/)) používaného pro synchronizaci uplinku, které poskytuje odhad vzdálenosti mezi mobilem a jedinou základnovou stanicí, MTA využívá měření z více základnových stanic (obvykle tří a více) k výpočtu přesné geografické polohy uživatelského zařízení (UE).

Architektura zahrnuje UE, více základnových stanic ([BTS](/mobilnisite/slovnik/bts/) v GSM nebo eNodeB v LTE) a centrální pozicovací uzel. V klasické implementaci GSM je tímto uzlem Serving Mobile Location Center ([SMLC](/mobilnisite/slovnik/smlc/)). Pro LTE-M zahrnuje pozicovací architektura Enhanced Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) a Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v jádru sítě. UE vysílá normální signál v uplinku, například během hovoru nebo odesíláním přístupových burstů. Více okolních základnových stanic, nejen obsluhující, změří čas příchodu tohoto signálu. Každé měření je převedeno na odhad vzdálenosti, ale klíčové je, že tyto odhady obsahují společnou neznámou časovou odchylku z časování vysílání UE.

Základní princip multilaterace spočívá v tom, že *rozdíl* v časech příchodu na párech základnových stanic eliminuje tuto společnou časovou odchylku UE. Tyto časové rozdíly definují hyperbolické křivky, na kterých musí UE ležet. S měřeními z alespoň tří základnových stanic (vytvářejících dva nezávislé časové rozdíly) poskytne průnik těchto hyperbolických křivek 2D určení polohy. Síť (SMLC/E-SMLC/LMF) shromažďuje měření Timing Advance nebo surová měření času příchodu od zapojených základnových stanic prostřednictvím rozhraní Abis (v GSM) nebo protokolu LTE positioning protocol (LPPa). Následně provede výpočet multilaterace, řeší hyperbolické rovnice a stanoví souřadnice UE. Přesnost závisí na geometrii základnových stanic (zředění přesnosti), rádiovém prostředí (vícecestné šíření) a přesnosti časových měření.

V GSM byla MTA často vylepšována dalšími měřeními, jako je Enhanced Observed Time Difference ([E-OTD](/mobilnisite/slovnik/e-otd/)), které vyžadovalo asistenci ze strany UE. Pro LTE-M a NB-IoT je MTA součástí rodiny pozicování [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival), ale přizpůsobená možnostem zařízení IoT s nízkým výkonem a širokou oblastí pokrytí. Od UE může být požadováno provedení specifických pozicovacích procedur, ale náročný výpočet probíhá v síti. MTA poskytuje síťově centrické řešení, které nevyžaduje schopnost GNSS v UE, což ji činí vhodnou pro cenově citlivá a energeticky omezená zařízení IoT pro aplikace jako sledování majetku, logistika a nouzové služby, kde postačuje přibližná poloha.

## K čemu slouží

MTA byla vyvinuta za účelem poskytování služby určování polohy pro mobilní účastníky bez nutnosti spoléhat se na globální družicové navigační systémy (GNSS), jako je GPS, které nebyly v raných mobilech všeobecně dostupné a spotřebovávají značnou bateriovou energii. Primární problém, který řešila, byl regulační, například splnění požadavků amerického E-911 Fáze II na lokalizaci nouzových volajících, a také umožnění komerčních služeb založených na poloze (LBS) v sítích GSM. Základní cell-ID a jediné Timing Advance poskytovaly velmi hrubou polohu (na úrovni sektoru nebo vzdálenostního prstence), což pro mnoho aplikací bylo nedostatečné.

Historický kontext začíná GSM Release 2, kde byly zvažovány základní pozicovací schopnosti. MTA jako síťová metoda TDOA nabízela rovnováhu mezi přesností, náklady a dopadem na síť. Využívala existující buněčnou infrastrukturu – základnové stanice – jako referenční body pro určování polohy. Řešila omezení jednodušších metod využitím inherentních časových měření, která síť již prováděla pro synchronizaci, a jejich vylepšením koordinací napříč více lokalitami. To poskytovalo přesnější určení polohy než samotné cell-ID, aniž by vyžadovalo nový hardware v každém mobilním zařízení.

S příchodem LTE a konkrétně technologií zaměřených na IoT, jako jsou LTE-M a NB-IoT, byl účel MTA obnoven. Mnoho zařízení IoT je nasazeno uvnitř budov, ve sklepech nebo na pohyblivých aktivech, kde jsou signály GNSS slabé nebo nedostupné. Navíc přidání přijímače GNSS zvyšuje cenu zařízení a spotřebu energie, což je v rozporu s cíli IoT dosáhnout desetileté životnosti baterie. MTA poskytuje pro tato zařízení síťovou alternativu. Řeší problém lokalizace zařízení IoT s nízkou složitostí a nízkou spotřebou pro aplikace jako chytré měřiče, zemědělské senzory a sledované kontejnery, kde je často přijatelná přibližná poloha (s přesností na desítky až stovky metrů). Umožňuje operátorům nabízet určování polohy jako službu bez GNSS na straně zařízení, což odpovídá potřebě škálovatelných, nákladově efektivních masivních nasazení IoT.

## Klíčové vlastnosti

- Síťová metoda určování polohy nevyžadující schopnost GNSS v UE
- Využívá měření časového rozdílu příchodu (TDOA) z více základnových stanic
- Vypočítává polohu řešením hyperbolických rovnic, čímž eliminuje časovou odchylku UE
- Využívá existující rádiové signály v uplinku (např. přístupové bursty, normální provoz)
- Centralizovaný výpočet v síťovém uzlu (SMLC, E-SMLC nebo LMF)
- Poskytuje službu určování polohy pro nouzové hovory (E-911) a komerční LBS, zejména pro zařízení IoT

## Definující specifikace

- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mta/)
