---
slug: "nref"
url: "/mobilnisite/slovnik/nref/"
type: "slovnik"
title: "NREF – NR Absolute Radio Frequency Channel Number"
date: 2025-01-01
abbr: "NREF"
fullName: "NR Absolute Radio Frequency Channel Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nref/"
summary: "Jedinečný číselný identifikátor pro každý rádiový frekvenční kanál v 5G NR. Poskytuje standardizovanou metodu pro globální odkazování na konkrétní kmitočty nosných, která je nezbytná pro konfiguraci s"
---

NREF je jedinečný číselný identifikátor pro každý rádiový frekvenční kanál v 5G NR, který poskytuje standardizovaný globální odkaz pro kmitočty nosných.

## Popis

NR absolutní číslo rádiového frekvenčního kanálu ([NR-ARFCN](/mobilnisite/slovnik/nr-arfcn/)) je základní parametr definovaný ve specifikacích 3GPP, který se mapuje na konkrétní kmitočet [RF](/mobilnisite/slovnik/rf/) nosné v systému 5G New Radio (NR). Jedná se o lineární, bezrozměrné celé číslo, které jednoznačně identifikuje frekvenční kanál ve všech NR frekvenčních pásmech, včetně jak Frekvenčního rozsahu 1 (FR1: pod 7 GHz), tak Frekvenčního rozsahu 2 (FR2: mmWave, 24,25 GHz a výše). Mapování mezi hodnotou NREF a jejím odpovídajícím absolutním kmitočtem v Hertzech je definováno specifickým vzorcem, který se liší mezi FR1 a FR2 a zohledňuje různé velikosti kanálového rastru (např. 5 kHz, 15 kHz, 60 kHz, 100 kHz). Tento vzorec zajišťuje, že každý platný NREF odkazuje na pozici v kanálovém rastru, na kterou lze umístit středový kmitočet nosné, což je v souladu s konfiguracemi bloku synchronizačních signálů (SSB) a šířky pásma kanálu.

Z architektonického hlediska se NREF používá v celém protokolovém zásobníku NR a síťových rozhraních. V rádiovém rozhraní (Uu) je signalizován v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)), jako je [SIB1](/mobilnisite/slovnik/sib1/), pro označení kmitočtů nosných pro downlink a uplink buňky. Je klíčovou součástí hlášení měření, kde UE hlásí detekované buňky pomocí jejich fyzické identifikace buňky ([PCI](/mobilnisite/slovnik/pci/)) a odpovídajícího NREF. Pro správu sítě a testování se NREF používá ve specifikacích definujících RF požadavky (např. 38.101 pro rádiový přenos a příjem UE, 38.104 pro rádiový přenos a příjem základnové stanice) a v testech shody (např. 38.141 pro testování shody základnových stanic, 38.521 pro testování shody UE). Poskytuje společný referenční bod pro definování charakteristik vysílače a přijímače, jako je výstupní výkon, nežádoucí emise a referenční citlivost, na konkrétních kmitočtech.

Jeho role sahá až k nasazení a optimalizaci sítě. Operátoři používají hodnoty NREF v nástrojích pro plánování sítě k definování kmitočtů nosných. Ve scénářích duální konektivity ([EN-DC](/mobilnisite/slovnik/en-dc/), [NR-DC](/mobilnisite/slovnik/nr-dc/)) nebo agregace nosných ([CA](/mobilnisite/slovnik/ca/)) jsou sekundární buňky (SCell) identifikovány svým NREF spolu s jejich PCI. NREF je také nedílnou součástí definic NR frekvenčních pásem; každé provozní pásmo je spojeno se specifickým rozsahem hodnot NREF pro uplink a downlink. Toto systematické číslování nahrazuje potřebu komunikovat absolutní kmitočty v Hertzech v mnoha signalizačních zprávách, čímž zjednodušuje návrh protokolu a zajišťuje globální konzistenci. Koncept se vyvinul z EARFCN používaného v LTE a byl přizpůsoben širšímu frekvenčnímu rozsahu a flexibilnější numerologii NR.

## K čemu slouží

NREF byl vytvořen, aby poskytl standardizovanou, efektivní a jednoznačnou metodu pro identifikaci kmitočtů rádiových nosných v systému 5G NR. Před 5G používalo LTE EARFCN (E-UTRA Absolute Radio Frequency Channel Number). Se zavedením NR, které podporuje výrazně rozšířené spektrum od pod 1 GHz až po milimetrové vlny (až do 100 GHz), bylo nutné nové číslovací schéma. Stávající schéma LTE nebylo navrženo tak, aby pokrylo tyto extrémní kmitočty nebo nové granularity kanálového rastru vyžadované pro různorodé případy užití NR, jako jsou širokopásmové mmWave nosné. NREF řeší problém odkazování na kmitočty v tomto heterogenním prostředí.

Klíčovou motivací bylo zajistit zpětnou kompatibilitu a budoucí flexibilitu v návrhu protokolu. Definováním lineárního mapování založeného na vzorci může systém snadno začlenit nová frekvenční pásma v budoucích vydáních bez přepracování signalizačního rámce. Řeší omezení přímého používání absolutních hodnot kmitočtu v signalizaci, které by bylo neefektivní z hlediska velikosti zpráv a náchylné k chybám zaokrouhlování. NREF poskytuje kompaktní celočíselnou reprezentaci, kterou mohou snadno zpracovávat síťové prvky a uživatelská zařízení.

Dále řeší klíčové výzvy v oblasti interoperability a testování. Pro globální roaming a certifikaci zařízení je univerzální identifikátor kmitočtu nezbytný. Výrobci, operátoři a dodavatelé testovacích zařízení se všichni spoléhají na NREF jako na společný jazyk pro specifikaci RF charakteristik, provádění testů shody a zajištění, že se UE mohou správně naladit a pracovat na jakékoli NR nosné po celém světě. Je základním kamenem pro automatizovanou konfiguraci sítě, funkce samoorganizujících se sítí (SON) a scénáře sdílení spektra.

## Klíčové vlastnosti

- Globálně jedinečný celočíselný identifikátor pro kmitočty NR nosných
- Samostatné mapovací vzorce pro Frekvenční rozsah 1 (FR1) a Frekvenční rozsah 2 (FR2)
- Soulad s NR kanálovým rastrem (např. 5, 15, 60, 100 kHz) pro umístění na platný kmitočet
- Použití v RRC signalizaci pro informace o kmitočtu buňky (např. v SIB1)
- Základní prvek pro definice RF požadavků a testování shody ve specifikacích 3GPP
- Podpora agregace nosných a vícekonektivity identifikací komponentních nosných

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TR 38.847** (Rel-17) — NR 47.2-48.2 GHz Frequency Range
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [NREF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nref/)
