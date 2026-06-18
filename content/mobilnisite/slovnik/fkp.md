---
slug: "fkp"
url: "/mobilnisite/slovnik/fkp/"
type: "slovnik"
title: "FKP – Flächenkorrekturparameter (Area Correction Parameters)"
date: 2025-01-01
abbr: "FKP"
fullName: "Flächenkorrekturparameter (Area Correction Parameters)"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fkp/"
summary: "Parametry korekce oblasti (FKP) jsou konfigurační parametry používané v LTE a 5G NR k úpravě výpočtu geografické polohy uživatelského zařízení (UE). Opravují systematické chyby v měřeních polohování p"
---

FKP je konfigurační parametr používaný v LTE a 5G NR k opravě systematických chyb v OTDOA polohovacích měřeních, čímž se zlepšuje přesnost výpočtu geografické polohy uživatelského zařízení (UE).

## Popis

Flächenkorrekturparameter (FKP), neboli parametry korekce oblasti, jsou klíčovou součástí metody polohování pomocí pozorovaného časového rozdílu příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) definované v 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (5G). OTDOA je síťová polohovací technika, při které UE měří časový rozdíl příchodu referenčních signálů z více sousedních buněk (eNodeB/gNB) vůči referenční buňce. Tato naměřená referenční časová zpoždění signálu ([RSTD](/mobilnisite/slovnik/rstd/)) se používají k výpočtu hyperbol, jejichž průsečík odhaduje polohu UE. Nicméně nezpracovaná RSTD měření obsahují chyby způsobené neideálními faktory, jako jsou nepřesnosti časové synchronizace mezi základnovými stanicemi a zpoždění šíření signálu nezapočítaná v základním modelu.

FKP fungují tak, že poskytují korekční hodnoty vysílané polohovacím serverem, typicky Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)), k UE prostřednictvím protokolu LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)). Tyto parametry jsou asociovány se specifickými geografickými oblastmi, známými jako oblasti FKP. UE přijímá hodnoty FKP použitelné pro její aktuální nebo očekávanou oblast. Hlavní technickou funkcí FKP je reprezentovat relativní časový posun vysílání polohovacího referenčního signálu ([PRS](/mobilnisite/slovnik/prs/)) sousední buňky ve srovnání s ideální synchronizovanou časovou základnou předpokládanou pro referenční buňku. Aplikací této korekce na své nezpracované RSTD měření pro danou sousední buňku může UE kompenzovat skutečnou chybu časování vysílání základnové stanice.

Z architektonického hlediska je generování FKP úkolem správy sítě. Operátor sítě nebo specializovaný polohovací server musí tyto parametry vypočítat na základě známých, přesných poloh základnových stanic a případně kalibračních měření. Parametry jsou následně nakonfigurovány do polohovací infrastruktury sítě. Klíčovými zapojenými komponentami jsou UE (která korekci aplikuje), základnové stanice (eNodeB/gNB, jejichž časové chyby jsou korigovány) a polohovací server (E-SMLC/LMF), který poskytuje data FKP. Úlohou FKP je zvýšit přesnost OTDOA polohování bez nutnosti dokonalé a nákladné časové synchronizace napříč všemi základnovými stanicemi v síti, což činí hromadné, regulačními požadavky splňující polohové služby (např. pro tísňová volání) proveditelnějšími a přesnějšími.

## K čemu slouží

Technologie FKP existuje k řešení základního problému přesnosti v [OTDOA](/mobilnisite/slovnik/otdoa/) polohování způsobeného chybami časové synchronizace mezi základnovými stanicemi. Teoretická metoda OTDOA předpokládá, že všechny základnové stanice vysílají své polohovací referenční signály v dokonalé synchronizaci. V praktických nasazeních je dosažení a udržení synchronizace na úrovni nanosekund napříč rozsáhlou sítí extrémně náročné a nákladné, i s použitím technologií jako GPS/GNSS nebo IEEE 1588 Precision Time Protocol. Bez korekce se tyto časové chyby přímo převádějí na velké geografické polohové chyby, čímž se OTDOA stává nepoužitelným pro aplikace jako je lokalizace pro tísňová volání (E911/112) nebo polohové služby.

Vytvoření a standardizace FKP byly motivovány potřebou nákladově efektivního a nasaditelného řešení OTDOA. Řeší omezení spočívající v požadavku na dokonalou síťovou synchronizaci zavedením softwarové korekční vrstvy. Namísto investic do ultra-přesné hardwarové synchronizace pro každé místo buňky mohou operátoři charakterizovat existující časové chyby (které jsou v čase relativně stabilní) a vysílat korekční parametry. Tento přístup odděluje přesnost polohování od absolutní kvality síťové synchronizace, což operátorům umožňuje splnit regulační požadavky na přesnost lokalizace s využitím jejich stávající síťové infrastruktury a s přijatelnými kalibračními náklady. Byl to klíčový faktor umožňující komerční životaschopnost síťového polohování v LTE a jeho pokračování v 5G NR.

## Klíčové vlastnosti

- Koriguje buňkově specifické časové posuny pro OTDOA polohovací měření
- Vysílány protokolem LPP z polohovacího serveru (E-SMLC/LMF) k UE
- Asociovány s definovanými geografickými oblastmi FKP pro efektivní správu parametrů
- Zlepšuje přesnost polohování bez nutnosti dokonalé síťové synchronizace
- Podporuje jak polohovací referenční signály LTE (PRS), tak polohovací referenční signály 5G NR (PRS)
- Umožňuje polohové služby splňující regulační požadavky pro tísňová volání (E911)

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [FKP na 3GPP Explorer](https://3gpp-explorer.com/glossary/fkp/)
