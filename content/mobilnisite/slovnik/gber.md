---
slug: "gber"
url: "/mobilnisite/slovnik/gber/"
type: "slovnik"
title: "GBER – Average Gross Bit Error Rate"
date: 2025-01-01
abbr: "GBER"
fullName: "Average Gross Bit Error Rate"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gber/"
summary: "Klíčový ukazatel výkonu (KPI), který měří průměrný poměr chybně přijatých bitů k celkovému počtu vyslaných bitů před dekódováním kanálu. Jde o hrubé měření kvality rádiového spoje používané k hodnocen"
---

GBER je průměrný poměr chybně přijatých bitů k celkovému počtu vyslaných bitů před dekódováním kanálu, sloužící jako hrubý ukazatel kvality rádiového spoje (KPI) pro hodnocení výkonu modulace a plánování pokrytí sítě.

## Popis

Průměrná hrubá chybovost bitů (Average Gross Bit Error Rate – GBER) je základním měřením na fyzické vrstvě, které kvantifikuje hrubou chybovost digitálního komunikačního spoje před aplikací jakéhokoli dopředného opravování chyb ([FEC](/mobilnisite/slovnik/fec/)) nebo dekódování kanálu. Je definována jako průměrný počet chybných bitů dělený celkovým počtem bitů vyslaných za stanovené měřicí období. Na rozdíl od chybovosti bitů ([BER](/mobilnisite/slovnik/ber/)) měřené po dekódování (čistá BER) odráží GBER inherentní kvalitu rádiového kanálu, včetně vlivu šumu, interference, útlumu a výkonu samotného modulačního schématu.

GBER měří přijímač, typicky na výstupu demodulátoru. Přijímač porovnává přijatou bitovou sekvenci (která může být poškozena) s referenční sekvencí nebo v praktických systémech využívá pilotní symboly či dekódovanou verzi dat (když je možné spolehlivé dekódování) k odhadu chyb. Toto měření se provádí kontinuálně nebo periodicky na vyhrazených fyzických kanálech nebo na kanálech pro přenos hovorů/dat během aktivních relací. Výsledek je často časově průměrován (např. přes stovky milisekund nebo sekund), aby se vyhladily účinky rychlého útlumu a poskytla stabilní metrika pro algoritmy vyšších vrstev.

Tato metrika hraje několik klíčových rolí v řízení rádiových zdrojů (RRM). Za prvé je přímým vstupem pro algoritmy adaptace spoje ([LA](/mobilnisite/slovnik/la/)). Síť (např. základnová stanice nebo NodeB/eNodeB/gNB) využívá nahlášené nebo odhadované hodnoty GBER, často spolu s dalšími metrikami jako indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), k výběru nejvhodnějšího modulačního a kódovacího schématu ([MCS](/mobilnisite/slovnik/mcs/)). Vysoká GBER signalizuje špatný kanál a vede k použití robustnější (nižší) modulace a silnějšího kanálového kódování. Naopak nízká GBER umožňuje použít vyšší modulaci a vyšší kódové rychlosti pro maximalizaci propustnosti. Za druhé se GBER používá při rozhodování o předávání spojení a optimalizaci pokrytí. Trvale vysoká GBER na obsluhující buňce může spustit měření sousedních buněk a vést k předání spojení. Nástroje pro plánování sítě také používají cílové hodnoty GBER k modelování oblastí pokrytí buněk a určení optimálního umístění základnových stanic a nastavení výkonu.

## K čemu slouží

GBER existuje jako klíčová metrika výkonnosti nízké úrovně pro objektivní hodnocení hrubé kvality přenosu rádiového rozhraní. Před rozšířením sofistikovaných adaptivních technik sítě pracovaly s pevnou modulací a kódováním. Zavedení technologií jako [EDGE](/mobilnisite/slovnik/edge/) a [HSPA](/mobilnisite/slovnik/hspa/) a později LTE a NR, které zásadně spoléhají na dynamickou adaptaci spoje, vytvořilo potřebu po přesném měření stavu kanálu v reálném čase pro informování o volbě [MCS](/mobilnisite/slovnik/mcs/). Jednoduché ukazatele síly přijímaného signálu (RSSI nebo RSCP) jsou nedostatečné, protože nezohledňují interferenci nebo specifickou náchylnost modulace k chybám.

Hlavní problém, který GBER řeší, je poskytnutí síti přímého měření počtu bitů poškozených kanálem před opravou chyb (FEC). To je zásadní, protože účinnost kanálového kódování se liší; znalost hrubé chybovosti umožňuje systému předpovědět, zda dané MCS po dekódování uspěje. Umožňuje jemné doladění kompromisu mezi datovou rychlostí (spektrální účinností) a spolehlivostí. Bez přesného odhadu GBER by adaptace spoje byla méně efektivní, což by vedlo buď k nadměrným retransmisím (pokud je MCS příliš agresivní), nebo k plýtvání kapacitou (pokud je MCS příliš konzervativní).

Historicky jeho specifikace v řadě technických zpráv (TS 26.975, 26.976 atd.) podtrhuje jeho význam pro testování výkonnosti a benchmarkování kodeků a rádiových nosičů. Poskytuje standardizovanou, jednoznačnou metriku pro výrobce zařízení a operátory k ověření, že rádiový spoj splňuje minimální požadavky na kvalitu pro podporu hlasových, video nebo datových služeb, čímž zajišťuje interoperabilitu a konzistentní uživatelský zážitek. Odstraňuje omezení používání pouze metrik po dekódování, které směšují kvalitu kanálu s výkonem dekodéru.

## Klíčové vlastnosti

- Měří hrubou chybovost bitů před dekódováním kanálu (pre-FEC)
- Slouží jako přímý ukazatel kvality rádiového kanálu (SNR, interference)
- Klíčový vstup pro algoritmy dynamické adaptace spoje a výběru MCS
- Používá se v algoritmech pro rozhodování o předání spojení a řízení rádiových zdrojů
- Standardizovaná metrika pro testování shody a benchmarkování výkonu sítě
- Časově průměrována pro zmírnění dopadu rychlého útlumu

## Související pojmy

- [BER – Basic Encoding Rules](/mobilnisite/slovnik/ber/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [GBER na 3GPP Explorer](https://3gpp-explorer.com/glossary/gber/)
