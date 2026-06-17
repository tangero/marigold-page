---
slug: "cmos"
url: "/mobilnisite/slovnik/cmos/"
type: "slovnik"
title: "CMOS – Complementary Metal Oxide Semiconductor"
date: 2025-01-01
abbr: "CMOS"
fullName: "Complementary Metal Oxide Semiconductor"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cmos/"
summary: "CMOS je základní polovodičová technologie používaná k výrobě integrovaných obvodů, včetně těch v mobilních zařízeních a síťových prvcích. Umožňuje výrobu procesorů, pamětí a RF komponent s nízkou spot"
---

CMOS je základní polovodičová technologie používaná k výrobě integrovaných obvodů s nízkou spotřebou, vysokou hustotou a nízkými náklady, které jsou klíčové pro mobilní zařízení a síťové prvky v systémech 3GPP.

## Popis

Complementary Metal Oxide Semiconductor (CMOS) je technologie pro konstrukci integrovaných obvodů ([IC](/mobilnisite/slovnik/ic/)). Je založena na použití komplementárních a symetrických párů tranzistorů MOSFET typu p a typu n pro logické funkce. Klíčovým architektonickým principem je, že pouze jeden typ tranzistoru (buď pMOS, nebo nMOS) je zapnutý ve stabilním logickém stavu, což minimalizuje statickou spotřebu energie. Toho je dosaženo prostřednictvím obvodových návrhů, kde oba typy tranzistorů pracují v tandemu; například v základním CMOS invertoru tranzistor pMOS přitáhne výstup na vysokou úroveň, když je vstup nízký, a tranzistor nMOS přitáhne výstup na nízkou úroveň, když je vstup vysoký.

V kontextu systémů 3GPP je CMOS technologie základním výrobním procesem pro křemíkové čipy, které tvoří uživatelské zařízení (UE), jako jsou chytré telefony a IoT zařízení, stejně jako hardware základnových stanic (např. gNB). Tyto čipy zahrnují centrální aplikační procesor, modemový procesor základnového pásma zpracovávající vrstvy protokolového zásobníku (PHY, [MAC](/mobilnisite/slovnik/mac/), RLC atd.), paměť (SRAM, DRAM) a stále častěji i integrované komponenty RF transceiveru. Výrobní proces zahrnuje vytváření tranzistorů na křemíkovém substrátu definováním oblastí s různým dopingem (p a n), jejich izolaci tenkou oxidovou vrstvou („metal oxide“ historicky odkazuje na materiál hradla) a jejich propojení kovovými propoji.

Role CMOS v síti je všudypřítomná, ale nepřímá. Určuje fyzické schopnosti síťových uzlů. Pokroky ve škálování CMOS procesu (zmenšování tranzistorů) umožňují složitější a rychlejší zpracování základnového pásma, což umožňuje implementaci pokročilých funkcí 3GPP, jako je dekódování massive [MIMO](/mobilnisite/slovnik/mimo/), sofistikované kódování kanálu ([LDPC](/mobilnisite/slovnik/ldpc/), Polar) a zpracování protokolů vyšších vrstev. Pro RF front-endy CMOS umožňuje integraci výkonových zesilovačů, šumově nízkých zesilovačů, míchačů a filtrů na stejný čip jako digitální procesor (SoC – System on Chip), čímž se snižují náklady a velikost. Nízká spotřeba je zásadní pro výdrž baterie UE, zejména u funkcí vyžadujících neustálé výpočty, jako je odhad stavu kanálu a beamforming. Navíc nákladová efektivita a vysoká výtěžnost výroby CMOS jsou důvodem, proč mohou být zařízení kompatibilní s 3GPP vyráběna ve velkém měřítku po celém světě.

## K čemu slouží

CMOS technologie existuje jako dominantní polovodičový výrobní proces díky své vynikající energetické účinnosti ve srovnání s dřívějšími technologiemi, jako je NMOS nebo bipolární tranzistory. Primární problém, který řeší, je vysoká statická spotřeba energie, která sužovala rané integrované obvody, omezovala jejich složitost a vyžadovala významné chlazení. Komplementární návrh zajišťuje, že ve stabilním stavu neexistuje přímá cesta pro stejnosměrný proud ze zdroje napájení do země, což drasticky snižuje odběr energie v klidovém stavu. To byl revoluční pokrok pro digitální elektroniku.

Historický kontext jejího přijetí v telekomunikacích je spojen s miniaturizací a demokratizací bezdrátových zařízení. Před rozšířeným používáním CMOS byla mobilní zařízení objemná, s krátkou výdrží a omezenou výpočetní schopností. Motivace pro použití CMOS v implementacích 3GPP je mnohostranná: umožňuje vytváření složitých, nízkopříkonových procesorů základnového pásma schopných zpracování signálu v reálném čase pro pokročilé technologie radiového přístupu (od UMTS po 5G NR); umožňuje integraci celých systémů na jediný čip, čímž se snižuje fyzická velikost a cena UE; a její neustálé škálování (podle Moorova zákona) poskytuje stále rostoucí počet tranzistorů potřebných pro podporu nových, výpočetně náročných funkcí 3GPP, jako je agregace nosných, modulace vyššího řádu (256QAM) a funkce správy síťového řezání.

## Klíčové vlastnosti

- Extrémně nízká statická spotřeba energie díky komplementárnímu návrhu tranzistorů
- Vysoká odolnost vůči šumu a robustní logické úrovně napětí
- Škálovatelný výrobní proces umožňující nepřetržité zvyšování hustoty tranzistorů
- Schopnost integrovat analogové (RF) a digitální obvody na stejném čipu
- Vysoká výtěžnost výroby a nákladová efektivita pro hromadnou produkci
- Podpora širokého rozsahu napájecích napětí, což napomáhá správě napájení

## Definující specifikace

- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [CMOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmos/)
