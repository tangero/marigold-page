---
slug: "rber"
url: "/mobilnisite/slovnik/rber/"
type: "slovnik"
title: "RBER – Residual Bit Error Ratio"
date: 2025-01-01
abbr: "RBER"
fullName: "Residual Bit Error Ratio"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rber/"
summary: "Residual Bit Error Ratio (Zbytkový poměr chybných bitů) je klíčový metrik výkonu, který kvantifikuje poměr chybných bitů datového spoje po aplikaci dekódování korekce chyb. Měří účinnost schématu Forw"
---

RBER je poměr bitů, které zůstávají chybné po dekódování korekce chyb, a měří účinnost schématu FEC na fyzické vrstvě.

## Popis

Residual Bit Error Ratio je definován jako poměr chybně přijatých bitů k celkovému počtu vyslaných bitů, měřený po dekodéru Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)) v přijímači. Jedná se o metriku po dekódování, na rozdíl od Raw [BER](/mobilnisite/slovnik/ber/) měřeného před dekódováním. RBER poskytuje přímé měření integrity dodaných dat spoje. V systémech 3GPP fyzická vrstva využívá kanálové kódování (např. Turbo kódy, [LDPC](/mobilnisite/slovnik/ldpc/) kódy) a prokládání k ochraně datových bloků (transportních bloků) proti vlivům kanálu, jako je šum, interference a útlum. Přijímač tyto bloky dekóduje a jakékoli bity, které nelze opravit, představují zbytkové chyby.

Výpočet RBER typicky zahrnuje ověření kontrolního součtu [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check). Každému transportnímu bloku je na vysílači přidán CRC. Po dekódování v přijímači se CRC přepočítá a porovná. Pokud kontrola CRC selže, celý blok je považován za chybný a může být vyžádán k opětovnému vyslání prostřednictvím [HARQ](/mobilnisite/slovnik/harq/). Odhad RBER pro bloky, které prošly kontrolou CRC, však může vyžadovat sofistikovanější techniky, neboť tyto bloky mohou stále obsahovat neodhalené chyby. Specifikace systémů často definují cílové hodnoty RBER pro různé služby a podmínky kanálu, což řídí výběr modulačních a kódovacích schémat ([MCS](/mobilnisite/slovnik/mcs/)).

RBER je základním vstupem pro algoritmus adaptace přenosových parametrů (link adaptation), který dynamicky volí optimální MCS pro aktuální rádiové podmínky. Vysoká hodnota RBER indikuje, že aktuální MCS je pro kanál příliš agresivní (např. modulace vysokého řádu s nízkou kódovou rychlostí), což vyvolá přechod na robustnější schéma. Naopak, trvale nízká hodnota RBER může umožnit použití MCS s vyšší přenosovou rychlostí pro zlepšení spektrální účinnosti. Cílové hodnoty RBER se liší podle služby: například signalizace vyžaduje extrémně nízký RBER (např. 10^-6), zatímco některý datový provoz na pozadí může tolerovat vyšší RBER. Sledování RBER v čase také poskytuje cenná data pro optimalizaci sítě a řešení problémů s výkonem.

## K čemu slouží

RBER existuje jako klíčový metrik kvality pro vyhodnocení výkonu a spolehlivosti digitálního komunikačního spoje po korekci chyb. Jeho primárním účelem je kvantifikovat účinnost kódování [FEC](/mobilnisite/slovnik/fec/) na fyzické vrstvě a zajistit, aby dodaná data splňovala požadavky na poměr chyb služby nebo aplikace vyšší vrstvy. Bez měření RBER by síť neměla objektivní způsob, jak posoudit, zda zvolené modulační a kódovací schéma poskytuje zamýšlenou úroveň integrity dat, což by mohlo vést k nepřijatelné ztrátě paketů nebo poškozeným informacím pro citlivé služby.

Koncept byl formálně definován ve 3GPP Release 4 v souvislosti s vylepšením možností paketových dat v UMTS. Řešil klíčové omezení pouhého měření nezpracovaného poměru chyb před dekódováním (Raw [BER](/mobilnisite/slovnik/ber/)), který neodráží zisk výkonu poskytovaný výkonnými kanálovými kódy, jako jsou Turbo kódy zavedené v 3G. RBER poskytuje přesnější obraz o kvalitě spoje vnímané uživatelem. Vyřešil problém optimálního přizpůsobení parametrů přenosu fyzické vrstvy požadavkům služby a okamžitému stavu kanálu, což je nezbytné pro efektivní využití spektra v proměnných bezdrátových prostředích.

Jak se s HSPA, LTE a 5G zvyšovaly přenosové rychlosti a diverzita služeb, role RBER se stala ještě důležitější. Zavedení pokročilého FEC jako LDPC kódů v 5G NR vyžadovalo přesnou charakterizaci RBER pro naladění jejich výkonu. Cíle RBER jsou nedílnou součástí definice tříd kvality služeb (QoS) (např. prostřednictvím hodnot 5QI) a jsou klíčovým parametrem při návrhu algoritmů adaptace přenosových parametrů a vnější smyčky adaptace, které jsou zásadní pro dosažení vysoké spolehlivosti a nízké latence moderních buněčných systémů.

## Klíčové vlastnosti

- Měření chyb po dekódování: Kvantifikuje chyby bitů po dekódování FEC, což odráží čistou účinnost kanálového kódu.
- Vstup pro adaptaci přenosových parametrů (link adaptation): Slouží jako klíčový metrik pro dynamický výběr MCS za účelem vyvážení spektrální účinnosti a spolehlivosti přenosu.
- Cíle specifické pro službu: Definovány pro různé typy provozu (např. hlas, video, signalizace) s různými úrovněmi tolerance chyb.
- Monitorování výkonu: Používá se pro vyhodnocení výkonu sítě, optimalizaci a detekci závad na rádiovém spoji.
- Interakce s HARQ: Informuje procesy Hybrid ARQ; vysoký RBER při počátečním přenosu může spustit odlišnou verzi redundance při opakovaném přenosu.
- Mapování parametrů QoS: Propojeno s parametry kvality služeb (QoS) vyšších vrstev, jako je SDU Error Ratio, což ovlivňuje kvalitu služby end-to-end.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods

---

📖 **Anglický originál a plná specifikace:** [RBER na 3GPP Explorer](https://3gpp-explorer.com/glossary/rber/)
