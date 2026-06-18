---
slug: "gap"
url: "/mobilnisite/slovnik/gap/"
type: "slovnik"
title: "GAP – Generic Address Parameter"
date: 2025-01-01
abbr: "GAP"
fullName: "Generic Address Parameter"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gap/"
summary: "Parametr používaný ve signalizačních protokolech k přenosu adresních informací v obecném, flexibilním formátu. Umožňuje přenos různých typů adres, jako jsou IP adresy nebo čísla E.164, v rámci řídicíc"
---

GAP je obecný signalizační parametr používaný k flexibilnímu přenosu různých typů adresních informací, jako jsou IP adresy nebo čísla E.164, v rámci řídicích zpráv za účelem zajištění interoperability sítě.

## Popis

Parametr Generic Address [Parameter](/mobilnisite/slovnik/parameter/) (GAP) je základní datová struktura definovaná v rámci signalizačních protokolů 3GPP, primárně specifikovaná v TS 23.066. Slouží jako kontejner pro předávání adresních informací standardizovaným, technologicky neutrálním způsobem. Parametr je navržen s strukturou Type-Length-Value ([TLV](/mobilnisite/slovnik/tlv/)), kde pole 'Type' identifikuje formát přenášené adresy (např. IPv4, IPv6, E.164, [SIP](/mobilnisite/slovnik/sip/) [URI](/mobilnisite/slovnik/uri/)), pole 'Length' udává velikost adresních dat a pole 'Value' obsahuje skutečné oktety adresy. Tento strukturovaný přístup umožňuje síťovým uzlům správně parsovat a interpretovat adresy bez předchozí znalosti konkrétní aplikace nebo služby generující zprávu.

GAP se používá na více rozhraních a v protokolech uvnitř jádra sítě, zejména v kontextu [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile network Enhanced Logic) a dalších mechanismů řízení služeb. Když služební uzel, jako je Service Control Point ([SCP](/mobilnisite/slovnik/scp/)), potřebuje poskytnout pokyny pro směrování nebo účtování, může do GAP zahrnout adresní informace – například cíl přesměrovaného hovoru nebo identifikátor pro účtování. Příjemní síťový prvek, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC, dekóduje GAP na základě jeho typu a použije adresu k provedení požadované operace, jako je připojení hovoru na konkrétní číslo nebo aplikace specifického pravidla účtování.

Obecná povaha parametru je jeho hlavní předností a poskytuje dlouhodobě použitelný mechanismus pro přenos adresních informací s nástupem nových adresních formátů. Jeho návrh zajišťuje zpětnou kompatibilitu; síťové prvky podporující GAP mohou ignorovat typy adres, kterým nerozumí, nebo je zpracovat na základě standardizovaných postupů. Tato flexibilita je klíčová pro vývoj mobilních sítí, neboť podporuje přechod od tradičních adres okruhově přepínané telefonie k paketovým identifikátorům, jako jsou IP adresy a URI, a tím usnadňuje konvergenci hlasových a datových služeb.

## K čemu slouží

Parametr Generic Address [Parameter](/mobilnisite/slovnik/parameter/) byl zaveden, aby vyřešil problém rigidních, pevně zakódovaných adresních polí v raných telekomunikačních signalizačních protokolech. Před jeho standardizací protokoly často obsahovaly vyhrazená pole pro konkrétní typy adres, například pole pro číslo E.164 a samostatné pole pro IP adresu. Tato nepružnost ztěžovala zavádění nových adresních formátů nebo služeb bez úprav specifikace protokolu a upgradu všech síťových prvků, což vedlo k problémům s interoperabilitou a pomalému nasazování služeb.

GAP byl vytvořen, aby poskytl jednotný, rozšiřitelný kontejner pro adresní informace, a oddělil tak signalizační protokol od konkrétní sémantiky adres. To umožňuje síťovým operátorům a poskytovatelům služeb zavádět nové typy adres a související služby pouhým definováním nového kódu typu v rámci frameworku GAP, aniž by vyžadovali změny základních struktur zpráv protokolu. Podporuje dynamickou povahu moderní telekomunikace, kde jedna relace může zahrnovat více typů adres napříč různými doménami.

Motivace vychází z potřeby větší flexibility v řízení služeb a směrování, zejména s nástupem konceptů inteligentní sítě (IN), jako je CAMEL. GAP umožňuje pokročilé služby – jako je překlad čísel, přesměrování hovorů na IP koncové body nebo služebně specifické účtování – tím, že umožňuje servisní logice komunikovat komplexní adresní informace směrovací infrastruktuře standardizovaným způsobem. Řeší omezení předchozích přístupů tím, že poskytuje jediný, dobře definovaný parametr, který se může vyvíjet spolu se sítí, čímž zajišťuje dlouhodobou životaschopnost a snižuje náklady a složitost síťových upgradů.

## Klíčové vlastnosti

- Kódování Type-Length-Value (TLV) pro flexibilitu a rozšiřitelnost
- Podpora více typů adres (E.164, IP adresy, SIP URI atd.)
- Odděluje signalizační protokol od sémantiky adres
- Umožňuje pokročilé řízení služeb v architekturách CAMEL a dalších IN
- Usnadňuje interoperabilitu mezi síťovými prvky od různých dodavatelů
- Poskytuje dlouhodobě použitelný mechanismus pro zavádění nových adresních formátů

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [TLV – Type, Length, Value](/mobilnisite/slovnik/tlv/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [GAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gap/)
