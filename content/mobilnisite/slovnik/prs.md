---
slug: "prs"
url: "/mobilnisite/slovnik/prs/"
type: "slovnik"
title: "PRS – Positioning Reference Signal"
date: 2025-01-01
abbr: "PRS"
fullName: "Positioning Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prs/"
summary: "Referenční signál v downlinku speciálně navržený pro pozicovací měření v LTE a NR. Je vysílán základnovými stanicemi se známým vzorem, což umožňuje UE měřit rozdíly časů příjmu (RSTD) pro techniky jak"
---

PRS je referenční signál v downlinku určený pro pozicování v LTE a NR, vysílaný základnovými stanicemi se známým vzorem, aby umožnil měření na UE, jako je RSTD pro OTDOA.

## Popis

Positioning Reference Signal (PRS) je fyzický signál definovaný v 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a následně pro NR, explicitně navržený k usnadnění přesného určení polohy uživatelského zařízení (UE). Jedná se o pseudonáhodnou sekvenci vysílanou eNodeB (v LTE) nebo gNB (v NR) na specifických zdrojových prvcích v časově-frekvenční mřížce downlink rádiového rámce. Na rozdíl od buněčně specifických referenčních signálů ([CRS](/mobilnisite/slovnik/crs/)) používaných pro odhad kanálu a demodulaci je PRS optimalizován pro měření času příchodu a vyznačuje se vlastnostmi jako nízká interference, konfigurovatelné muting vzory a vysoká periodicita. UE používá přijatý PRS z více sousedních buněk k výpočtu Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)), což je základní měření pro metodu pozicování Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)). Síť poskytuje UE pomocná data konfigurace PRS – včetně šířky pásma PRS, periody, subframe offsetu a muting sekvence – prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) nebo protokolů [LPP](/mobilnisite/slovnik/lpp/), což umožňuje UE efektivně detekovat a měřit tyto signály i ze slabých buněk.

Architektonicky jsou generování a vysílání PRS zpracovávány fyzickou vrstvou základnové stanice. Signál je konstruován pomocí Goldovy sekvence inicializované parametry odvozenými od Physical Cell ID ([PCI](/mobilnisite/slovnik/pci/)) buňky, indexu konfigurace PRS a čísla systémového rámce, což zajišťuje jeho jedinečnost a předvídatelnost pro každou buňku. Ve frekvenční oblasti může být PRS konfigurován na různých šířkách pásma (např. 6 až 100 resource blocks v LTE) a může být vysílán na více anténních portech (používajících stejnou sekvenci) pro podporu transmit diversity. Klíčovou vlastností je PRS muting, kdy jsou určité PRS příležitosti z buňky nevysílány podle definovaného vzoru; to snižuje interferenci ze silných buněk a umožňuje UE slyšet PRS slabších sousedních buněk, což je zásadní pro přesná RSTD měření v heterogenních sítích. Časová struktura zahrnuje pozicovací subframy, které se vyskytují periodicky (např. každých 160, 320, 640 nebo 1280 ms), což představuje kompromis mezi latencí měření a síťovou režií.

Jak PRS funguje v praxi, zahrnuje koordinaci napříč sítí. Lokalizační server (např. [LMF](/mobilnisite/slovnik/lmf/)) určí optimální konfiguraci PRS pro geografickou oblast a sdělí ji zapojeným eNodeB/gNB prostřednictvím backhaul rozhraní. Tyto základnové stanice pak synchronně vysílají svůj PRS podle dohodnuté konfigurace. UE po přijetí pomocných dat naladí svůj přijímač během konfigurovaných pozicovacích subframů, provede korelaci přijatého signálu s očekávanou sekvencí PRS pro každou měřenou buňku a odhadne čas příchodu. Porovnáním časů příchodu ze alespoň tří geograficky rozptýlených buněk může UE nebo síť vypočítat polohu UE pomocí multilaterace. V NR byl PRS (často označovaný jako NR-PRS nebo jednoduše PRS) vylepšen podporou širších šířek pásma (až do plné šířky nosné), beamformingem a provozem v pásmech FR2 (mmWave), využívajíc směrový přenos ke zlepšení přesnosti. Návrhové principy zajišťují, že PRS je odolný vůči mnohocestnému úniku a má vysoký poměr signálu k šumu a interferenci (SINR), což přímo přispívá k jemnější časové rozlišovací schopnosti a následně k lepší přesnosti lokalizace.

## K čemu slouží

PRS byl vytvořen za účelem překonání omezení použití standardních buněčně specifických referenčních signálů (CRS) pro pozicování v LTE. Před Rel-9 byly pozicovací metody jako OTDOA závislé na CRS, ale tyto signály nebyly optimalizovány pro měření času příchodu; trpěly vysokou interferencí (jelikož CRS jsou vysílány neustále a překrývají se mezi buňkami) a poskytovaly nízkou přesnost, zejména v hustě zastavěných městských nebo vnitřních prostředích. Požadavky průmyslu na přesnější lokalizační služby – hnací silou byly regulační požadavky na lokalizaci volajících v nouzových případech (např. FCC E911 Phase II) a růst komerčních aplikací založených na poloze – vyžadovaly dedikovaný referenční signál s nízkou interferencí, navržený od základů pro pozicování.

Zavedení PRS ve 3GPP Release 9 specificky řešilo problém 'hearability' (detekovatelnosti). V OTDOA musí UE detekovat signály z alespoň tří základnových stanic. Často je signál obslužné buňky mnohem silnější než signály sousedních buněk a ty tak přehluší. PRS řeší tento problém prostřednictvím konfigurovatelných muting vzorů a optimalizovaného zvýšení výkonu. Díky potlačení PRS přenosů ze silných buněk v určitých časech se signály slabších buněk stanou detekovatelnými. PRS navíc může být vysílán s vyšší energií na zdrojový prvek (EPRE) než datové signály, čímž se zlepší poměr signálu k šumu na přijímači UE. To přímo zvyšuje přesnost měření RSTD a umožňuje odhady polohy v řádu desítek metrů, ve srovnání se stovkami metrů u dřívějších metod.

Kromě služeb v nouzových situacích umožnil PRS novou třídu komerčních a IoT aplikací vyžadujících spolehlivé venkovní i vnitřní pozicování, jako je sledování majetku, navigace v nákupních centrech a služby založené na blízkosti. Jeho standardizovaný návrh zajistil interoperabilitu mezi různými dodavateli a operátory. S vývojem sítí k 5G NR motivovala potřeba ještě vyšší přesnosti (např. submetrové pro průmyslový IoT) a podpora nových frekvenčních pásem další vylepšení PRS, včetně rozšíření šířky pásma, integrace s beam managementem a podpory agregace nosných. PRS tak představuje klíčový prostředek pro síťové pozicování v rámci 4G i 5G a poskytuje fyzickou vrstvu, která umožňuje realizaci přesných a škálovatelných lokalizačních služeb.

## Klíčové vlastnosti

- Dedikovaná pseudonáhodná sekvence pro pozicování, odlišná od buněčně specifických referenčních signálů (CRS)
- Konfigurovatelná šířka pásma (v NR až na plnou šířku nosné) a periodicita (160 ms až 1280 ms) pro vyvážení přesnosti a režie
- Muting vzory pro snížení interference ze silných buněk, což zlepšuje detekovatelnost slabých sousedních buněk
- Podpora více anténních portů a v NR beamforming pro směrový přenos v pásmu FR2
- Schopnost vysokého zvýšení výkonu (PRS-EPRE-MAX) pro zlepšení poměru signálu k šumu na UE
- Definován pro LTE (E-UTRA) i NR se zpětně kompatibilními principy a perspektivními vylepšeními

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.809** (Rel-12) — Study on RF Pattern Matching for LTE Positioning
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [PRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/prs/)
