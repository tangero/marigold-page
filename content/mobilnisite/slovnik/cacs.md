---
slug: "cacs"
url: "/mobilnisite/slovnik/cacs/"
type: "slovnik"
title: "CACS – Common Active Codec Set"
date: 2025-01-01
abbr: "CACS"
fullName: "Common Active Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cacs/"
summary: "CACS je mechanismus definovaný 3GPP pro správu a vyjednávání sady řečových kodeků dostupných pro použití během hovoru mezi sítěmi. Umožňuje efektivní výběr kodeku tím, že sítím dovoluje vyměňovat si s"
---

CACS je mechanismus 3GPP, který umožňuje sítím vyměnit si a dohodnout společnou podmnožinu dostupných řečových kodeků pro hovor, čímž zajišťuje interoperabilitu a optimální kvalitu hlasu napříč doménami operátorů.

## Popis

Common Active Codec Set (CACS) je standardizovaný postup definovaný v 3GPP TS 28.062 pro správu vyjednávání řečových kodeků v meziodběratelských scénářích. Funguje v rámci architektury Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a je speciálně navržen pro interakce na rovině správy mezi síťovými operátory, nikoli jako signalizační protokol v reálném čase používaný během sestavování hovoru. Hlavní architektonickou komponentou implementující CACS je Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) každého operátora. Tyto systémy komunikují prostřednictvím standardizovaných rozhraní Q3 nebo na bázi [CORBA](/mobilnisite/slovnik/corba/) (podle modelu TMN) za účelem výměny informací o správě kodeků.

CACS funguje tak, že stanovuje dohodnutou sadu řečových kodeků, které mohou být aktivně použity pro hovory procházející propojením mezi sítěmi dvou operátorů. Proces je zahájen prostřednictvím akcí správy, kdy NMS jednoho operátora navrhne seznam kodeků NMS druhého operátora. Tento návrh obsahuje identifikátory kodeků (např. pro [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/)) a může zahrnovat i přidružené parametry, jako jsou přenosové rychlosti. Příjemce (NMS) vyhodnotí návrh vůči svým vlastním schopnostem a politikám, případně vyjednává, aby dospěl k vzájemně přijatelné Common Active Codec Set. Tato dohodnutá sada je poté stažena nebo provizionována do příslušných síťových prvků v doméně každého operátora, jako jsou Media Gateways ([MGW](/mobilnisite/slovnik/mgw/)) nebo Mobile Switching Centers (MSC), které tyto informace používají během procedur Transcoding-Free Operation (TrFO) nebo Tandem-Free Operation (TFO) v reálném čase.

Její role v síti je klíčová pro zajištění bezproblémové a vysoce kvalitní interoperability hlasových služeb. Předvyjednáním aktivní sady kodeků na úrovni správy CACS snižuje složitost a možnost selhání během signalizace sestavování hovoru v reálném čase (např. v SIP nebo BICC). Zabrání situacím, kdy jsou navrženy nekompatibilní kodeky, což by v síti vynutilo plýtvavý a kvalitu zhoršující převod kodeků (transkódování). Dále CACS umožňuje operátorům strategicky spravovat své zdroje pro vzájemné propojení, například tím, že se dohodnou na upřednostnění novějších, efektivnějších širokopásmových kodeků, jako je AMR-WB, pro zlepšení zákaznické zkušenosti, nebo na omezení starších kodeků pro zjednodušení konfigurace a údržby sítě.

Klíčovými technickými komponentami jsou rozhraní správy (Q3/CORBA) mezi systémy NMS operátorů, datový model reprezentující sady kodeků a jejich parametry a provizionovací mechanismy, které nasazují dohodnutá CACS data do prvků pro přepojování hlasu. Postup se řídí stavovým strojem, který definuje stavy návrhu, protinávrhu, přijetí a zamítnutí. Úspěšná dohoda vede k tomu, že obě sítě mají synchronizovaný pohled na povolené kodeky pro jejich vzájemné propojení, čímž vytvářejí základní dohodu, na jejímž základě lze efektivně sestavovat hovory v reálném čase bez převodu kodeků.

## K čemu slouží

CACS byl vytvořen k řešení provozních a technických výzev spojených s interoperabilitou řečových kodeků v telekomunikačních prostředích s více dodavateli a operátory. Před jeho standardizací bylo vyjednávání kodeků často řešeno ad hoc během sestavování hovoru nebo prostřednictvím bilaterálních dohod operátorů, které byly ručně konfigurovány. Tento přístup byl neefektivní, náchylný k chybám a ztěžoval zavádění nových kodeků nebo vyřazování starých napříč síťovými hranicemi. Absence standardizovaného postupu správy mohl vést k suboptimálnímu výběru kodeků, častému návratu k transkódování (které spotřebovává další hardwarové zdroje a může zhoršit kvalitu hlasu) a zvýšené provozní zátěži pro síťové inženýry spravující propojení.

Historický kontext CACS je spojen s vývojem sítí 3G/UMTS a snahou o efektivnější hlasové služby. Se zavedením pokročilých kodeků, jako je rodina Adaptive Multi-Rate (AMR) a později Enhanced Voice Services (EVS), se stalo prioritou zajistit, aby tyto kodeky mohly být použity end-to-end, a tím maximalizovat spektrální efektivitu a uživatelský zážitek. Koncept Transcoding-Free Operation (TrFO) a Tandem-Free Operation (TFO) vznikl za účelem eliminace zbytečných transkódovacích jednotek v cestě hovoru. Aby však TrFO/TFO fungovalo napříč hranicemi operátorů, obě sítě potřebovaly předem vědět, které kodeky jsou vzájemně přijatelné. CACS poskytuje nezbytné vyjednávání na rovině správy (out-of-band), aby bylo možné tuto předpokládanou dohodu stanovit, což umožňuje realizaci TrFO/TFO v reálném čase ve velkém měřítku.

Primární motivací pro CACS tedy bylo poskytnout škálovatelný, automatizovatelný a standardizovaný mechanismus, který by operátorům umožnil spravovat své politiky kodeků pro vzájemné propojení. Řeší omezení ruční konfigurace a selhání vyjednávání v reálném čase tím, že přesouvá proces dohody do řízené, méně časově kritické domény operací. To umožňuje plánované nasazování nových kodeků, koordinovanou údržbu a v konečném důsledku umožňuje konzistentní poskytování vysoce kvalitních hovorů mezi účastníky na různých sítích bez kvalitativní penalizace způsobené transkódováním.

## Klíčové vlastnosti

- Standardizovaný postup na rovině správy pro vyjednávání kodeků mezi operátory
- Umožňuje a optimalizuje Transcoding-Free Operation (TrFO) a Tandem-Free Operation (TFO) napříč síťovými hranicemi
- Používá rozhraní založená na TMN (Q3/CORBA) pro komunikaci mezi Network Management Systems
- Definuje formální stavový stroj pro procesy návrhu, protinávrhu a dohody
- Umožňuje strategickou kontrolu nad sadou aktivních kodeků na propojení (např. upřednostnění širokopásmových kodeků)
- Snižuje provozní náklady a složitost automatizací správy interoperability kodeků

## Související pojmy

- [TFO – Tandem Free Operation](/mobilnisite/slovnik/tfo/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [CACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cacs/)
