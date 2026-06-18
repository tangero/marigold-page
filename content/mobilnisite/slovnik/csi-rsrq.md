---
slug: "csi-rsrq"
url: "/mobilnisite/slovnik/csi-rsrq/"
type: "slovnik"
title: "CSI-RSRQ – CSI Reference Signal Received Quality"
date: 2025-01-01
abbr: "CSI-RSRQ"
fullName: "CSI Reference Signal Received Quality"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csi-rsrq/"
summary: "CSI-RSRQ je metrika kvality kanálu v 5G NR, odvozená z CSI-RS. Představuje poměr přijatého výkonu CSI-RS k celkovému přijatému výkonu, včetně rušení a šumu, v rámci určené měřicí šířky pásma. Je klíčo"
---

CSI-RSRQ je metrika kvality kanálu v 5G NR, která představuje poměr přijatého výkonu CSI-RS k celkovému přijatému výkonu včetně rušení a šumu v rámci měřicí šířky pásma.

## Popis

CSI-RSRQ ([CSI](/mobilnisite/slovnik/csi/) Reference Signal Received Quality) je kritické měření fyzické vrstvy definované ve standardech 5G New Radio (NR). Kvantifikuje kvalitu přijímaného referenčního signálu pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) vyhodnocením poměru výkonu požadovaného CSI-RS k celkovému výkonu rušení a šumu v měřicím pásmu. Na rozdíl od [RSRP](/mobilnisite/slovnik/rsrp/) (Reference Signal Received Power), které měří sílu signálu, poskytuje CSI-RSRQ metriku podobnou poměru signál/rušení+šum ([SINR](/mobilnisite/slovnik/sinr/)) specifickou pro zdroj CSI-RS, což nabízí komplexnější pohled na kvalitu rádiového spojení za přítomnosti soukanálového rušení a šumu.

Z architektonického hlediska měření CSI-RSRQ provádí uživatelské zařízení (UE) v downlinku. gNodeB nakonfiguruje UE konkrétními zdroji CSI-RS pro měření prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/). UE změří přijatý výkon těchto nakonfigurovaných zdrojů CSI-RS, označovaný jako RSRP_CSI-RS. Současně UE měří celkový přijatý výkon (včetně rušení z jiných buněk, šumu a dalších signálů) ve stejné frekvenční šířce pásma jako zdroj CSI-RS. CSI-RSRQ se poté vypočítá jako (N * RSRP_CSI-RS) / ([E-UTRA](/mobilnisite/slovnik/e-utra/) carrier [RSSI](/mobilnisite/slovnik/rssi/)), kde N je počet bloků zdrojů ([RB](/mobilnisite/slovnik/rb/)), přes které se měří RSSI (Received Signal Strength Indicator), a RSSI zahrnuje celkový širokopásmový výkon. Tento výpočet dává lineární poměr, který je často reportován v dB.

Role CSI-RSRQ v síti je mnohostranná. Je to primární vstup pro reportování informací o stavu kanálu (CSI), které UE poskytuje gNodeB. Toto reportování je zásadní pro pokročilé funkce správy rádiových zdrojů. Na základě CSI-RSRQ může gNodeB provádět přesnou adaptaci spojení, vybírat optimální schéma modulace a kódování (MCS) pro maximalizaci propustnosti při dodržení cílů pro chybovost bloků. Je také klíčové pro procedury správy paprsků, pomáhá identifikovat nejlepší páry vysílacích/přijímacích paprsků hodnocením kvality různých paprsků CSI-RS. Dále měření CSI-RSRQ podporuje správu mobility, včetně rozhodování o předání spojení a převýběru buňky, tím, že poskytuje metriku zaměřenou na kvalitu vedle RSRP.

Klíčové komponenty zapojené do fungování CSI-RSRQ zahrnují nakonfigurované zdroje CSI-RS (s konkrétními časovými/frekvenčními pozicemi, periodicitou a scramblingem), měřicí obvody fyzické vrstvy UE a mechanismy filtrování a reportování vyšších vrstev definované ve specifikacích 3GPP. Měření je navrženo jako flexibilní, podporující různé případy užití, jako je mobilita v připojeném stavu, detekce selhání paprsku a monitorování rádiového spojení. Jeho přesnost je klíčová pro výkon 5G NR, zejména v hustých nasazeních a vysokých kmitočtových pásmech, kde je dynamika rušení výraznější.

## K čemu slouží

CSI-RSRQ bylo zavedeno v 5G NR, aby uspokojilo potřebu robustní metriky kvality kanálu, která bere v úvahu rušení a je specificky přizpůsobena pro pokročilé referenční signály, jako je CSI-RS. V LTE plnilo RSRQ podobný účel pro buňkové referenční signály (CRS), ale oddělená architektura 5G, kde se CSI-RS používá pro paprskově formovaný přenos dat a sledování, vyžadovala vyhrazené měření kvality. Primární problém, který řeší, je umožnění přesného odhadu stavu kanálu ve scénářích omezených rušením, což je zásadní pro vysoké cíle spektrální účinnosti 5G.

Historicky se spoléhalo pouze na RSRP (metriku založenou na výkonu) pro adaptaci spojení a mobilitu, což mohlo vést k neoptimálním rozhodnutím při silném mezibuněčném rušení. Vysoká hodnota RSRP nezaručuje dobrou propustnost, pokud je také vysoká úroveň rušení. CSI-RSRQ poskytuje přímé měření kvality signálu vůči rušení a šumu, čímž tuto mezeru zaplňuje. Jeho vytvoření bylo motivováno vývojem směrem ke složitějším více-paprskovým operacím a zhušťování sítí v 5G, kde se správa rušení stává prvořadou.

Tato technologie řeší omezení předchozích přístupů tím, že je těsně provázána s rámcem CSI. Na rozdíl od LTE RSRQ definovaného pro CRS se CSI-RSRQ měří na konfigurovatelných zdrojích CSI-RS, které mohou být specifické pro paprsek a pro uživatele. To umožňuje přesné hodnocení kvality skutečných paprsků používaných pro přenos dat, namísto celobuněčného průměru. Umožňuje gNodeB činit jemněji odlišená rozhodnutí o plánování a správě paprsků, což přímo zlepšuje uživatelský zážitek a kapacitu sítě v náročných rádiových podmínkách.

## Klíčové vlastnosti

- Měří kvalitu jako poměr výkonu CSI-RS k celkovému přijatému výkonu (RSSI)
- Poskytuje metriku zohledňující rušení pro přesný odhad SINR
- Podporuje konfigurovatelné zdroje CSI-RS pro měření specifická pro paprsek
- Zásadní vstup pro algoritmy reportování CSI a adaptace spojení
- Zlepšuje procedury správy paprsků a detekce selhání paprsku
- Používá se při rozhodování o mobilitě a monitorování rádiového spojení

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements

---

📖 **Anglický originál a plná specifikace:** [CSI-RSRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/csi-rsrq/)
