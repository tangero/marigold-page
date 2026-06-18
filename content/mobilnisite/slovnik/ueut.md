---
slug: "ueut"
url: "/mobilnisite/slovnik/ueut/"
type: "slovnik"
title: "UEUT – User Equipment Under Test"
date: 2025-01-01
abbr: "UEUT"
fullName: "User Equipment Under Test"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/ueut/"
summary: "User Equipment Under Test (UEUT, testované uživatelské zařízení) označuje UE zařízení, které je předmětem testů shody, výkonu nebo interoperability podle specifikací 3GPP. Jde o klíčový koncept v cert"
---

UEUT je uživatelské zařízení (User Equipment), které je předmětem testů shody, výkonu nebo interoperability podle specifikací 3GPP.

## Popis

User Equipment Under Test (UEUT, testované uživatelské zařízení) je formální označení v rámci testovacího rámce 3GPP pro zařízení UE procházející standardizovanými ověřovacími postupy. Je ústřední pro specifikace jako TS 36.521/523 (LTE), TS 38.521/523 (NR) a TS 34.121, které definují protokoly pro testování shody. UEUT je zařízení, jehož chování, signály a protokoly jsou pečlivě měřeny a vyhodnocovány vůči normativním požadavkům stanoveným v technických specifikacích 3GPP.

Architektura testování UEUT zahrnuje řízené laboratorní prostředí. Klíčové komponenty zahrnují samotné UEUT, testovací systém, který emuluje kompletní síť (zahrnující [RF](/mobilnisite/slovnik/rf/) konformní testovací systém simulující funkce základnové stanice), a různá měřicí zařízení. Testovací systém generuje standardizované testovací signály a scénáře (např. specifické referenční měřicí kanály, podmínky mobility, signalizační procedury) a odezva UEUT je zachycena a analyzována. To pokrývá tři hlavní domény: výkon v rádiovém kmitočtovém pásmu (RF), správu rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) a shodu protokolů.

Jak testování funguje, je vysoce procedurální. Pro RF testování se měří charakteristiky vysílače UEUT (např. výstupní výkon, kmitočtová chyba, kvalita modulace) a charakteristiky přijímače (např. citlivost, blokování) za různých podmínek. Pro RRM testování se vyhodnocuje výkon UEUT v procedurách, jako je výběr buňky, předávání hovoru a měření. Testování protokolů ověřuje, že UEUT správně implementuje signalizační protokoly vrstvy 2 a 3 (např. [RRC](/mobilnisite/slovnik/rrc/), [NAS](/mobilnisite/slovnik/nas/)), prováděním testovacích případů se specifickými sekvencemi zpráv a kontrolou správnosti a časování odpovědí UEUT.

Jeho úlohou je sloužit jako definitivní důkaz shody. Zařízení, které úspěšně projde sérií testů jako UEUT, je považováno za shodné se standardy 3GPP, což je předpokladem pro komerční nasazení a interoperabilitu sítě. Tento proces zajišťuje, že UE od různých výrobců budou spolehlivě fungovat na jakékoli kompatibilní síti, čímž se zachovává celková kvalita, výkon a bezpečnost globálního mobilního ekosystému. Je to základní kámen certifikace zařízení organizacemi jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)).

## K čemu slouží

Koncept UEUT byl vytvořen k řešení kritického problému interoperability sítí a konzistence výkonu na trhu s více dodavateli. V počátcích buněčné technologie, bez důsledného standardizovaného testování, se mohla zařízení od různých výrobců na síti chovat nepředvídatelně, což způsobovalo přerušená volání, interference a celkové zhoršení služeb. To brzdilo růst a spolehlivost mobilní komunikace.

Řeší potřebu jednotného srovnávacího kritéria kvality. Specifikace 3GPP definují, *co* musí UE dělat, ale specifikace testů shody (definující postupy pro UEUT) definují, *jak ověřit*, že to dělá správně. Toto oddělení zajišťuje, že požadavky jsou testovatelné a jednoznačné. Rámec UEUT poskytuje společnou, opakovatelnou a objektivní metodologii pro výrobce k ověření jejich návrhů a pro certifikační orgány k udělení schválení, čímž zajišťuje rovné podmínky a chrání operátory sítí před vadnými zařízeními.

Historicky se jeho formalizace vyvíjela s každou generací. Výrazně zaveden v Release 15 pro testování 5G NR, navázal na desetiletí vývoje testovací metodologie od GSM a LTE. Motivací pro jeho pokračující vývoj je rostoucí složitost nových technologií: massive [MIMO](/mobilnisite/slovnik/mimo/), agregace nosných, duální konektivita a ultra-spolehlivá nízkolatentní komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) všechny zavádějí nová chování, která musí být důsledně testována. Koncept UEUT zajišťuje, že jak se rozhraní pro přenos po rádiu a protokoly stávají sofistikovanějšími, mechanismy pro ověření shody zařízení drží krok, čímž chrání investice do sítí a zkušenost uživatelů.

## Klíčové vlastnosti

- Předmět standardizovaných testovacích případů shody pro výkon RF, RRM a protokolů
- Testováno v řízeném prostředí s vybavením pro emulaci sítě
- Ověřování vůči normativním požadavkům v sériích specifikací 3GPP TS 36/38 a série 34
- Klíčové pro certifikaci zařízení organizacemi jako GCF a PTCRB
- Zajišťuje interoperabilitu mezi UE od více dodavatelů a síťovou infrastrukturou
- Rozsah testování zahrnuje povinné i volitelné funkce UE deklarované výrobcem

## Definující specifikace

- **TS 34.121** (Rel-9) — UE Conformance Spec for FDD Radio
- **TS 34.123** (Rel-18) — UE Conformance Specification
- **TS 34.229** (Rel-19) — IMS SIP/SDP UE Conformance Testing for 5GS
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.523** (Rel-19) — UE Conformance Test Spec for Idle Mode
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.508** (Rel-19) — 5G NR UE Radio Transmission & Reception
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [UEUT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ueut/)
