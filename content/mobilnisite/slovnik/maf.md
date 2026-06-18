---
slug: "maf"
url: "/mobilnisite/slovnik/maf/"
type: "slovnik"
title: "MAF – Mobile Additional Function"
date: 2025-01-01
abbr: "MAF"
fullName: "Mobile Additional Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/maf/"
summary: "Standardizovaná doplňková služba v sítích 3GPP, která poskytuje další telefonní funkce nad rámec základního zpracování hovorů. Umožňuje operátorům nabízet rozšířené služby, jako je přesměrování hovorů"
---

MAF je standardizovaná doplňková služba v sítích 3GPP, která poskytuje další telefonní funkce nad rámec základního zpracování hovorů, jako je např. přesměrování hovorů, zákazy a identifikace.

## Popis

Mobile Additional Function (MAF) je rámec definovaný ve specifikacích 3GPP pro implementaci doplňkových služeb v mobilních sítích. Funguje jako nedílná součást funkcí řízení hovorů a správy relací, typicky umístěná ve služební vrstvě jádra sítě. Rámec MAF poskytuje standardizovaný způsob definování a správy funkcí, které upravují nebo rozšiřují základní chování hovoru, a komunikuje s entitami jádra sítě, jako je [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre), nebo v pozdějších architekturách s IMS (IP Multimedia Subsystem) prostřednictvím aplikačních serverů. Jeho provoz je řízen služební logikou, která je spouštěna konkrétními událostmi hovoru nebo akcemi účastníka, jako je vytočení čísla, přijetí příchozího hovoru nebo aktivace servisního kódu. Tato logika pak dá síti pokyn k provedení akcí, jako je přeměrování hovoru, zobrazení informací o volajícím nebo omezení sestavení hovoru na základě předdefinovaných podmínek. Architektura je navržena modulárně, což umožňuje nezávislý vývoj a nasazení různých služeb MAF při sdílení společné infrastruktury pro řízení a správu dat účastníků. Její role je klíčová pro umožnění bohaté sady funkcí očekávaných v moderní telefonii, zajištění interoperability mezi různými dodavateli síťových zařízení a poskytování konzistentního uživatelského zážitku podle standardů 3GPP.

## K čemu slouží

MAF byla vytvořena za účelem standardizace implementace doplňkových telefonních služeb v globálních mobilních sítích, což představuje posun od proprietárních řešení specifických pro jednotlivé dodavatele. Před takovou standardizací čelili operátoři výzvám při nabízení konzistentních funkcí, zejména při integraci zařízení od více dodavatelů, což bránilo interoperabilitě a zvyšovalo složitost. Standardizace MAF v rámci 3GPP si kladla za cíl tyto problémy vyřešit poskytnutím společného rámce a souboru specifikací pro služby, jako je přesměrování hovorů, čekání na hovor a identifikace volajícího. To umožnilo síťovým operátorům spolehlivě nasazovat rozšířené služby a zajistit, že funkce budou pro účastníky bezproblémově fungovat bez ohledu na použité síťové vybavení. Historický kontext spočívá ve vývoji od základní hlasové telefonie k službám mobilní komunikace s bohatými funkcemi, kde rostla poptávka účastníků po kontrole a personalizaci jejich komunikačního zážitku. Definováním MAF umožnila 3GPP konkurenční trh s přidanými službami při zachování spolehlivosti sítě a zjednodušení poskytování a správy služeb pro operátory.

## Klíčové vlastnosti

- Standardizovaná implementace doplňkových telefonních služeb
- Modulární architektura pro nezávislé nasazení služeb
- Integrace s funkcemi řízení hovorů v jádru sítě
- Podpora služební logiky a dat specifických pro účastníka
- Spouštění služeb na základě událostí v závislosti na stavech hovoru
- Zajišťuje interoperabilitu v síťových prostředích s více dodavateli

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSS – Mobile Satellite Services](/mobilnisite/slovnik/mss/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [MAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/maf/)
