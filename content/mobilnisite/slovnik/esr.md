---
slug: "esr"
url: "/mobilnisite/slovnik/esr/"
type: "slovnik"
title: "ESR – Erroneous Seconds Ratio"
date: 2025-01-01
abbr: "ESR"
fullName: "Erroneous Seconds Ratio"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esr/"
summary: "Klíčový ukazatel výkonu (KPI) používaný v rámci 3GPP samoorganizujících se sítí (SON) a minimalizace jízdních testů (MDT). Měří poměr sekund s přenosovými chybami k celkovému počtu sekund, čímž poskyt"
---

ESR je klíčový ukazatel výkonu, který měří poměr sekund s přenosovými chybami k celkovému počtu sekund, čímž poskytuje detailní pohled na kvalitu rádiového spoje pro optimalizaci sítě.

## Popis

Erroneous Seconds Ratio (ESR) je standardizované měření definované v 3GPP TS 26.904 pro účely percepčního hodnocení kvality hlasu a videa a obecněji pro monitorování kvality rádiového přenosu. Jde o časově založenou metriku, která kvantifikuje výskyt přenosových chyb ovlivňujících služební tok, typicky hlasového hovoru nebo video streamu. 'Erroneous Second' (chybná sekunda) je definována jako jakékoli jednosekundové období, během kterého dojde k alespoň jedné chybě rámce nebo bloku. ESR se pak vypočítá jako počet chybných sekund dělený celkovou dobou měření v sekundách.

V praktickém provozu 3GPP sítě lze ESR měřit v různých bodech. Pro hlasové služby úzce souvisí s E-modelem a dalšími metrikami kvality [ITU-T](/mobilnisite/slovnik/itu-t/), kde vzory chyb přímo ovlivňují vnímanou kvalitu ([MOS](/mobilnisite/slovnik/mos/) skóre). Pro případy užití [MDT](/mobilnisite/slovnik/mdt/) a SON lze uživatelské zařízení (UE) nakonfigurovat tak, aby zaznamenávalo rádiová měření spolu s metrikami kvality na aplikační vrstvě, jako je ESR. UE monitoruje své downlinkové (a potenciálně i uplinkové) rádiové bloky nebo datové jednotky paketů. Pokud je v dané sekundě detekována chyba (např. neúspěšný proces Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)), neobnovitelná chyba Radio Link Control (RLC) nebo ztráta IP paketu), je tato sekunda označena jako chybná.

Tato měření jsou shromažďována systémem správy sítě, jako je Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo SON server. Detailní data ESR, často označená polohou (z [GPS](/mobilnisite/slovnik/gps/) UE nebo síťové lokalizace) a dalšími kontextovými informacemi, jako je identifikátor buňky (cell ID), představují účinný nástroj pro síťové inženýry. Analýzou map nebo trendů ESR mohou identifikovat geografické oblasti se špatnými rádiovými podmínkami, buňky s problémy s interferencí nebo mobility trasy s častými neúspěchy při předávání hovoru (handover). Na rozdíl od jednodušších metrik, jako je průměrná míra bitových chyb ([BER](/mobilnisite/slovnik/ber/)), sekundová povaha ESR ji činí citlivou na chyby v dávkách a krátkodobé výpadky, které významně degradují uživatelský zážitek u služeb v reálném čase.

ESR je součástí širšího rámce měření kvality uživatelského zážitku (QoE). Spolupracuje s dalšími [KPI](/mobilnisite/slovnik/kpi/), jako je propustnost, zpoždění a rozkmity (jitter), aby poskytla ucelený pohled na výkon služby. Její standardizace v rámci 3GPP zajišťuje, že měření shromážděná UE od různých výrobců jsou srovnatelná, což umožňuje efektivní automatizovanou i manuální optimalizaci sítě v prostředích s více dodavateli.

## K čemu slouží

ESR byla standardizována, aby uspokojila potřebu přesných, na uživatele zaměřených měření kvality v mobilních sítích, což představuje posun od jednoduchých metrik orientovaných na síť, jako je síla signálu (RSRP) nebo kvalita kanálu (CQI). Tradiční jízdní testy pro optimalizaci sítě byly drahé, sporadické a nedokázaly zachytit skutečný uživatelský zážitek za všech podmínek. Funkce Minimalizace jízdních testů (MDT), zavedená přibližně v 3GPP Release 10, si kladla za cíl využít obrovský počet komerčních UE jako stále aktivních měřicích sond.

ESR poskytuje přímou, kvantifikovatelnou vazbu mezi poruchami na fyzické/rádiové vrstvě a vnímanou kvalitou služby, zejména pro služby konverzace citlivé na zpoždění, jako je Voice over LTE (VoLTE). Před existencí takových standardizovaných metrik citlivých na aplikaci měli operátoři potíže přesně určit oblasti, kde i přes dostatečné pokrytí signálem způsobovaly občasné chyby špatnou kvalitu hovoru. ESR tuto mezeru zaplňuje měřením chybových událostí v časové doméně, tak jak je zažívá aplikace.

Její vytvoření bylo motivováno posunem odvětví k daty řízené, automatizované optimalizaci sítě (SON) a potřebou garantovat kvalitu prémiových služeb, jako je vysoce kvalitní hlas a videohovory. Shromažďováním ESR od UE v terénu mohou operátoři vytvářet přesné, dynamické mapy kvality služby, automaticky spouštět optimalizační algoritmy (např. úpravy sklonu antén, nastavení výkonu nebo parametrů předání hovoru) a proaktivně identifikovat degradující síťové prvky dříve, než ovlivní velký počet účastníků, čímž zlepšují celkovou spokojenost zákazníků a snižují provozní náklady.

## Klíčové vlastnosti

- Časově založená metrika měřící hustotu chybových událostí (chybné sekundy na celkový počet sekund)
- Přímo koreluje chyby na rádiové/linkové vrstvě s kvalitou uživatelského zážitku (QoE) na aplikační vrstvě
- Používá se jako klíčový vstup pro funkce MDT (Minimalizace jízdních testů) a SON (samoorganizující se sítě)
- Může být měřena a zaznamenávána uživatelským zařízením (UE), čímž poskytuje detailní výkonnostní data označená polohou
- Standardizovaná definice zajišťuje interoperabilitu mezi více dodavateli pro sběr měření a analýzu
- Zvláště relevantní pro hodnocení kvality služeb v reálném čase, jako jsou VoLTE a ViLTE

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS

---

📖 **Anglický originál a plná specifikace:** [ESR na 3GPP Explorer](https://3gpp-explorer.com/glossary/esr/)
