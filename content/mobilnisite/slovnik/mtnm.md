---
slug: "mtnm"
url: "/mobilnisite/slovnik/mtnm/"
type: "slovnik"
title: "MTNM – Multi Technology Network Management"
date: 2025-01-01
abbr: "MTNM"
fullName: "Multi Technology Network Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mtnm/"
summary: "Standardizovaný rámec pro správu více-dodavatelských, více-technologických sítí, vyvinutý TM Forum a přijatý 3GPP. Umožňuje jednotnou správu různorodých síťových prvků, jako jsou 2G, 3G, 4G a transpor"
---

MTNM je standardizovaný rámec vyvinutý TM Forum a přijatý 3GPP pro jednotnou správu více-dodavatelských, více-technologických sítí (jako 2G, 3G, 4G) a transportní infrastruktury.

## Popis

Multi Technology Network Management (MTNM) je komplexní rámec pro správu standardizovaný [TM](/mobilnisite/slovnik/tm/) Forum a odkazovaný ve specifikacích 3GPP pro správu složitých telekomunikačních sítí. Jeho architektura je založena na sdíleném informačním modelu ([SID](/mobilnisite/slovnik/sid/)) a sadě standardizovaných rozhraní, primárně využívajících technologie jako [CORBA](/mobilnisite/slovnik/corba/) a později webové služby, k usnadnění komunikace mezi systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) nebo systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)). Jádrem MTNM je jeho technologicky neutrální objektový model, který abstrahuje specifické detaily podkladových síťových technologií – jako jsou GSM, UMTS, LTE a optický transport – do společné sady spravovaných objektů. To umožňuje jedinému NMS provádět správu poruch, konfiguraci, správu výkonu a zabezpečení napříč heterogenním síťovým prostředím. Mezi klíčové komponenty patří rozhraní-N (Itf-N) pro severozápadní komunikaci z EMS do NMS a detailní modely pro reprezentaci síťových zdrojů, jako je zařízení, připojení a trasy. Jeho rolí je poskytovat jednotný provozní pohled, umožňovat automatizované zřizování, komplexní zajištění služeb a efektivní využití zdrojů bez závislosti na proprietárním systému správy jediného dodavatele. Oddělením vrstvy správy od podkladových síťových technologií MTNM podporuje interoperabilitu a zjednodušuje integraci nových síťových prvků a služeb při vývoji sítí operátorů.

## K čemu slouží

MTNM byl vytvořen k řešení významných provozních výzev vznikajících z rozšíření různorodých síťových technologií a dodavatelů v rámci infrastruktury jednoho operátora. Historicky měla každá síťová technologie (např. 2G, 3G) a zařízení každého dodavatele svůj vlastní proprietární systém správy, což vedlo k izolovaným provozním úlům. Tato fragmentace měla za následek vysoké provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) kvůli potřebě specializovaného personálu a složitým integračním snahám, pomalé nasazování služeb a obtíže při dosahování holistického pohledu na výkon sítě a poruchy. [TM](/mobilnisite/slovnik/tm/) Forum za účasti hlavních operátorů a dodavatelů vyvinul MTNM ke standardizaci rozhraní a informačních modelů pro správu. Jeho přijetí do specifikací 3GPP poskytlo standardizovanou předlohu pro správu síťových prvků definovaných 3GPP spolu s dalšími technologiemi. Primární motivací bylo snížení nákladů na integraci, umožnění více-dodavatelské interoperability a zefektivnění síťových operací poskytnutím společného rámce pro správu. To umožňuje operátorům spravovat celou svou síť – od rádiového přístupu přes jádro po transport – prostřednictvím jednotnějšího systému, což zlepšuje agilitu a snižuje čas uvedení nových služeb na trh.

## Klíčové vlastnosti

- Technologicky neutrální informační model založený na Sdíleném informačním/datovém modelu (SID) TM Forum
- Standardizované severozápadní rozhraní-N (Itf-N) pro integraci EMS s NMS
- Podpora správy síťových prvků od více dodavatelů a pro více technologií
- Komplexní funkce správy zahrnující správu Poruch, Konfiguraci, Výkon a Zabezpečení (FCAPS)
- Modelování síťových zdrojů jako spravovaných objektů, jako je Zařízení, Fyzické a Logické koncové body a entity Připojení/Trasy
- Umožnění komplexního zřizování a zajištění služeb napříč heterogenními doménami

## Související pojmy

- [MTOSI – Multi Technology Operations System Interface](/mobilnisite/slovnik/mtosi/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [SID – Silence Insertion Descriptor](/mobilnisite/slovnik/sid/)

## Definující specifikace

- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 32.818** (Rel-8) — SA5 MTOSI XML Harmonization Study

---

📖 **Anglický originál a plná specifikace:** [MTNM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtnm/)
