---
slug: "prc"
url: "/mobilnisite/slovnik/prc/"
type: "slovnik"
title: "PRC – Pseudo-Range Correction"
date: 2025-01-01
abbr: "PRC"
fullName: "Pseudo-Range Correction"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prc/"
summary: "PRC je korekční parametr používaný v lokalizaci metodou Observed Time Difference of Arrival (OTDOA) ke zlepšení přesnosti určení polohy. Kompenzuje časové rozdíly mezi základnovými stanicemi a umožňuj"
---

PRC je korekční parametr používaný v OTDOA lokalizaci k vyrovnání časových rozdílů mezi základnovými stanicemi, čímž zvyšuje přesnost určení polohy UE.

## Popis

Korekce pseudodosahu (Pseudo-Range Correction, PRC) je klíčovým parametrem standardizované metody lokalizace Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) podle 3GPP. OTDOA je síťově asistovaná, UE-bazovaná lokalizační technika, při které UE měří rozdíl v čase příchodu referenčních signálů (např. Positioning Reference Signals – [PRS](/mobilnisite/slovnik/prs/) v LTE/NR) z více sousedních základnových stanic (eNodeB/gNodeB) a referenční buňky. Tento nezpracovaný naměřený časový rozdíl se nazývá Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)). Tato měření však nejsou dokonale synchronizovaná kvůli nedokonalostem v časové distribuci sítě.

PRC představuje korekční hodnotu, kterou síť přenáší do UE a která zohledňuje relativní časový posun mezi okamžiky vysílání lokalizačních referenčních signálů z různých základnových stanic. Konceptuálně platí, že pokud UE změří RSTD, skutečný geometrický časový rozdíl příchodu (potřebný pro hyperbolické lokalizační výpočty) je přibližně RSTD + PRC. PRC typicky poskytuje lokalizační server (např. Evolved Serving Mobile Location Centre – [E-SMLC](/mobilnisite/slovnik/e-smlc/) nebo Location Management Function – [LMF](/mobilnisite/slovnik/lmf/)), který zná časové vztahy v síti, často odvozené z měření jednotkami Location Measurement Units ([LMU](/mobilnisite/slovnik/lmu/)) nebo přímo od základnových stanic, pokud jsou synchronizovány pomocí [GNSS](/mobilnisite/slovnik/gnss/) nebo [IEEE](/mobilnisite/slovnik/ieee/) 1588.

Z architektonického hlediska jsou PRC součástí asistenčních dat doručovaných UE v postupu OTDOA. UE přijímá seznam sousedních buněk pro OTDOA měření spolu s jejich PRS konfigurací a přidruženými hodnotami PRC (a případně s příbuzným parametrem RSTD nejistoty). UE provádí měření RSTD, aplikuje přijaté PRC a poté používá korigované pseudodosahy (úměrné korigovaným časovým rozdílům) k řešení soustavy hyperbolických rovnic pro určení svých souřadnic. Výpočet může být proveden v UE (UE-bazovaný) nebo mohou být měření odeslána zpět do sítě k výpočtu (UE-asistovaný).

Přesnost PRC přímo ovlivňuje výslednou přesnost lokalizace. Pokud by byla síť dokonale synchronizovaná (např. všechny gNBy mají společný časový zdroj jako GPS), byly by PRC nulové. V reálných nasazeních, zejména v asynchronních nebo částečně synchronizovaných sítích (běžné v indoor nebo hustě urbanizovaných scénářích), jsou PRC nenulové a zásadní. Generování a distribuce přesných PRC s nízkou latencí jsou proto klíčovými funkcemi lokalizační architektury, které umožňují OTDOA splňovat regulační (např. E-911) a komerční požadavky služeb založených na poloze.

## K čemu slouží

PRC byl zaveden, aby umožnil přesnou OTDOA lokalizaci v praktických, neideálních nasazeních mobilních sítí. Základní princip OTDOA vyžaduje, aby čas vyslání lokalizačních signálů z různých základnových stanic byl znám vůči společnému časovému referenčnímu bodu. V ideální, dokonale synchronizované síti tato podmínka platí a nezpracovaná RSTD měření UE přímo odpovídají geometrickým časovým rozdílům. Dosažení a udržení dokonalé synchronizace napříč všemi buňkami ve velké síti je však nákladné a často nepraktické, zejména pro malé buňky nebo v prostředích, kde nejsou dostupné GNSS signály pro synchronizaci.

PRC tento problém řeší oddělením požadavku na dokonalou synchronizaci v reálném čase od lokalizační funkce. Umožňuje síti fungovat s běžnou úrovní synchronizace (nebo dokonce být asynchronní) a přitom podporovat vysoce přesnou lokalizaci. Lokalizační server vypočítá časové posuny mezi buňkami na základě své znalosti sítě (z měření LMU nebo hlášení základnových stanic) a poskytne tyto posuny UE jako PRC v podobě korekčních dat. Tento přístup je flexibilnější a nákladově efektivnější než vynucování ultrapřesné synchronizace v celé síti.

Historicky, jak nabývaly na významu služby založené na poloze a regulační požadavky na lokalizaci nouzových volajících (např. FCC E-911), potřebovalo 3GPP robustní lokalizační metody pro LTE (zavedené v Release 9). OTDOA byla vyvinuta jako primární metoda a mechanismus PRC byl klíčovou inovací umožňující její fungování v reálných podmínkách. Řešil omezení dřívějších metod lokalizace v buněčných sítích, jako jsou Cell-ID a Enhanced Cell-ID, které nabízely nízkou přesnost, a poskytl standardizovanou, škálovatelnou techniku využívající existující infrastrukturu mobilní sítě bez ukládání neúnosných požadavků na synchronizaci, což připravilo cestu pro následná vylepšení v NR.

## Klíčové vlastnosti

- Korekční parametr aplikovaný na nezpracovaná RSTD měření v OTDOA lokalizaci
- Kompenzuje relativní časové posuny mezi vysílacími body (základnovými stanicemi)
- Doručován do UE jako součást lokalizačních asistenčních dat poskytovaných sítí
- Umožňuje přesnou lokalizaci v sítích bez dokonalé synchronizace
- Zásadní pro splnění přesnostních požadavků nouzových služeb (E-911) a komerčních LBS
- Generován a spravován lokalizačním serverem sítě (E-SMLC/LMF)

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [PRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/prc/)
