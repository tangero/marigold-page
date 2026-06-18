---
slug: "udre"
url: "/mobilnisite/slovnik/udre/"
type: "slovnik"
title: "UDRE – User Differential Range Error"
date: 2025-01-01
abbr: "UDRE"
fullName: "User Differential Range Error"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/udre/"
summary: "Klíčový výkonnostní ukazatel pro lokalizaci metodou OTDOA v LTE a 5G NR. Kvantifikuje chybu v odhadovaném rozdílu vzdáleností mezi uživatelským zařízením a dvěma základnovými stanicemi, což přímo ovli"
---

UDRE je klíčová metrika pro OTDOA lokalizaci, která kvantifikuje chybu v odhadovaném rozdílu vzdáleností mezi uživatelským zařízením a dvěma základnovými stanicemi, přičemž nižší hodnoty indikují přesnější lokalizaci.

## Popis

User Differential Range Error (UDRE) je statistická míra nejistoty spojené s měřeními pro lokalizaci metodou [OTDOA](/mobilnisite/slovnik/otdoa/) v sítích 3GPP, konkrétně definovaná pro LTE a 5G NR. OTDOA je downlinková lokalizační metoda, při které uživatelské zařízení (UE) měří rozdíl času příchodu signálů z více sousedních základnových stanic (eNodeB v LTE, gNB v NR) vzhledem k referenční buňce. UDRE charakterizuje chybu v odhadovaném geometrickém rozdílu vzdáleností mezi UE a každou dvojicí základnových stanic zapojených do měření. Typicky je vyjádřena jako směrodatná odchylka (např. v metrech) a je kritickou součástí rozpočtu lokalizační chyby.

Výpočet a aplikace UDRE zahrnuje několik síťových prvků. Lokalizační server (např. Evolved Serving Mobile Location Centre, [E-SMLC](/mobilnisite/slovnik/e-smlc/), nebo Location Management Function, [LMF](/mobilnisite/slovnik/lmf/)) často asistuje v procesu OTDOA. Server může poskytnout uživatelskému zařízení asistenční data, která mohou zahrnovat očekávaná měření [RSTD](/mobilnisite/slovnik/rstd/) a přidružené ukazatele kvality. UDRE může být odvozena nebo odhadnuta na základě faktorů, jako je poměr signálu k šumu, vícecestné šíření, geometrie buněk (zředění přesnosti) a synchronizační chyby mezi základnovými stanicemi. UE používá naměřené hodnoty RSTD a jejich přidružené nejistoty (jako je UDRE) v multilateračním algoritmu (např. odhad metodou nejmenších čtverců) pro výpočet své polohy. Hodnoty UDRE váží jednotlivá měření v tomto algoritmu; měření s nižší UDRE (vyšší spolehlivostí) mají větší váhu, což vede k přesnějšímu určení polohy.

V praxi není UDRE vždy explicitně signalizována, ale je konceptuálně nedílnou součástí lokalizačních protokolů. Standardy jako 3GPP TS 36.355 (LTE Positioning Protocol, [LPP](/mobilnisite/slovnik/lpp/)) a TS 37.355 (NR Positioning Protocol, NRPPa) definují kontejnery pro přenos výsledků měření a metrik kvality. Celková přesnost lokalizace hlášená aplikaci (např. pro nouzové služby nebo komerční služby založené na poloze) je přímo ovlivněna agregovanou UDRE napříč všemi měřenými buňkami. Síťoví operátoři a výrobci zařízení optimalizují faktory ovlivňující UDRE, jako je nasazení synchronizovaných sítí (např. pomocí [GPS](/mobilnisite/slovnik/gps/) nebo [IEEE](/mobilnisite/slovnik/ieee/) 1588), optimalizace vzorů referenčních signálů (Positioning Reference Signals, [PRS](/mobilnisite/slovnik/prs/)) a použití pokročilého zpracování signálu v UE pro potlačení vícecestného šíření, vše za účelem minimalizace této chyby.

## K čemu slouží

Účelem UDRE je poskytnout kvantifikovatelnou a standardizovanou míru kvality jednotlivých měření rozdílu vzdáleností metodou OTDOA. Přesná lokalizace je regulatorním požadavkem (např. pro lokalizaci nouzových hovorů, E911/E112) a klíčovým prvkem pro řadu komerčních služeb (navigace, sledování majetku, geofencing). Rané metody buněčné lokalizace často poskytovaly pouze jednoduchou polohu bez podrobné metriky spolehlivosti, což ztěžovalo aplikacím posoudit její věrohodnost.

Zavedení UDRE a souvisejících metrik ve standardech 3GPP řešilo potřebu sofistikovanější kvality služby lokalizace. Umožňuje lokalizačnímu algoritmu (v UE nebo síťovém serveru) optimálně kombinovat více potenciálně zašuměných měření. Vážením měření podle jejich UDRE může algoritmus vytvořit přesnější a statisticky robustnější odhad polohy než prostý průměr. To je zvláště důležité v náročných rádiových prostředích, jako jsou městské kaňony nebo vnitřní prostory, kde mohou být některá měření kvůli silnému vícecestnému šíření nebo slabému signálu velmi nespolehlivá. UDRE tedy umožňuje síti splnit přísné požadavky na přesnost pro nouzové služby a podporuje vývoj vysoce přesných aplikací založených na poloze.

## Klíčové vlastnosti

- Kvantifikuje nejistotu v měřeních rozdílu vzdáleností založených na OTDOA
- Vyjádřena jako směrodatná odchylka, typicky v metrech
- Používá se k vážení měření v multilateračních lokalizačních algoritmech
- Je ovlivněna kvalitou signálu, synchronizačními chybami a vícecestným šířením
- Nedílná součást lokalizačních protokolů jako LPP a NRPPa
- Přímo ovlivňuje hlášenou přesnost určení polohy UE

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [UDRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/udre/)
