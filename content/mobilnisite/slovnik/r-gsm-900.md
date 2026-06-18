---
slug: "r-gsm-900"
url: "/mobilnisite/slovnik/r-gsm-900/"
type: "slovnik"
title: "R-GSM 900 – Railway GSM 900"
date: 2025-01-01
abbr: "R-GSM 900"
fullName: "Railway GSM 900"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/r-gsm-900/"
summary: "Vyhrazené pásmo GSM-R (GSM pro železnice) v rozsahu 900 MHz, specificky alokované pro železniční komunikační a signalizační systémy. Poskytuje robustní, bezinterferenční hlasové a datové služby pro pr"
---

R-GSM 900 je vyhrazené pásmo GSM-R v rozsahu 900 MHz, alokované pro železniční komunikaci, signalizaci a bezpečnostní systémy, jako je ERTMS.

## Popis

R-GSM 900 je specializovaná frekvenční alokace definovaná 3GPP pro systémy [GSM-R](/mobilnisite/slovnik/gsm-r/) (GSM pro železnice). Funguje ve spárovaných pásmech 876-880 MHz pro uplink (od mobilu k základně) a 921-925 MHz pro downlink (od základny k mobilu), což poskytuje celkovou šířku pásma 4 MHz. Technická definice, Fl(n)=890+0.2*n pro dolní pásmo a [FI](/mobilnisite/slovnik/fi/)(n)=890+0.2*(n-1024) pro horní pásmo, specifikuje přesné kmitočty nosných, kde 'n' je absolutní číslo rádiového frekvenčního kanálu ([ARFCN](/mobilnisite/slovnik/arfcn/)). Tato přesná matematická definice zajišťuje globální harmonizaci a zabraňuje interferencím s veřejnými GSM sítěmi.

Z architektonického hlediska se R-GSM 900 integruje do standardního rámce GSM sítě, ale je nasazována jako vyhrazená, privátní síť podél železničních koridorů. Mezi klíčové síťové komponenty patří základnová stanice ([BTS](/mobilnisite/slovnik/bts/)) instalovaná podél tratí, řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)), které jsou často specializované pro provozní požadavky železnice. Systém podporuje základní funkce GSM-R, jako je služba hlasového hromadného volání ([VGCS](/mobilnisite/slovnik/vgcs/)), služba hlasového vysílání ([VBS](/mobilnisite/slovnik/vbs/)) a rozšířený víceúrovňový přednostní systém s přerušováním (eMLPP) pro upřednostnění kritických bezpečnostních komunikací.

Jeho úlohou v síti je poskytovat vysoce spolehlivou, bezpečnou a dostupnou komunikační vrstvu pro klíčové železniční aplikace. To zahrnuje přímou hlasovou komunikaci mezi strojvedoucím a výpravčím, posunovací operace a především datové spoje pro evropský vlakový zabezpečovací systém (ETCS). Datový spoj GSM-R je přenosovou vrstvou pro telegramy ETCS, přenášející povolení k jízdě a údaje od traťových zařízení k vozidlové jednotce, což tvoří jádro moderního zabezpečovacího zařízení. Vyhrazené pásmo zajišťuje garantovanou kvalitu služby (QoS) a odolnost, protože je izolováno od přetížení a komerčního provozu veřejných mobilních sítí.

## K čemu slouží

R-GSM 900 bylo vytvořeno za účelem standardizace a zabezpečení vyhrazeného rádiového spektra pro železniční komunikaci napříč Evropou a dalšími přijímajícími regiony. Před GSM-R železnice používaly různorodé analogové rádiové systémy, které byly mezinárodně nekompatibilní, měly omezenou kapacitu a postrádaly pokročilé datové služby potřebné pro moderní řízení vlaků. Tato roztříštěnost bránila vytvoření bezproblémové panevropské železniční sítě.

Hlavním problémem, který řeší, je poskytnutí jednotné, digitální a interoperabilní komunikační platformy pro všechny provozní potřeby železnice. Alokací specifického, chráněného pásma eliminuje rušení od provozovatelů veřejných mobilních sítí, čímž zajišťuje, že bezpečnostně kritické komunikace nejsou nikdy blokovány nebo degradovány. To byl základní požadavek pro nasazení ERTMS/ETCS, které závisí na nepřetržité, vysoce integritní výměně dat mezi vlakem a tratí pro automatickou vlakovou ochranu.

Historicky byl vývoj hnán směrnicí Evropské unie zaměřenou na zvýšení bezpečnosti a interoperability železnic. Jako základní technologie byl zvolen standard GSM kvůli své vyspělosti, široké podpoře dodavatelů a schopnosti podporovat jak hlas, tak přepojování okruhů pro data. Vytvoření R-GSM 900 v rámci 3GPP zajistilo, že specifikace jsou udržovány a vyvíjeny spolu s hlavními mobilními standardy, což železničnímu průmyslu poskytlo dlouhodobou stabilitu a podporu ekosystému dodavatelů.

## Klíčové vlastnosti

- Vyhrazené, před rušením chráněné frekvenční pásmo (876-880 MHz UL / 921-925 MHz DL)
- Podpora služeb specifických pro GSM-R: VGCS, VBS a eMLPP
- Poskytuje datovou spojovou vrstvu pro signalizaci ETCS úrovně 2 a 3
- Definováno přesnými vzorci ARFCN pro globální zarovnání kanálů
- Umožňuje přímý režim provozu (DMO) pro komunikaci mimo síť
- Návrh s vysokou dostupností a redundancí pro klíčové operace

## Související pojmy

- [GSM-R – Global System for Mobile Communications – Rail(way)](/mobilnisite/slovnik/gsm-r/)

## Definující specifikace

- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [R-GSM 900 na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-gsm-900/)
