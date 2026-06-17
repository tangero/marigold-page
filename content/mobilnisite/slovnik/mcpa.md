---
slug: "mcpa"
url: "/mobilnisite/slovnik/mcpa/"
type: "slovnik"
title: "MCPA – Multi-Carrier Power Amplifier"
date: 2025-01-01
abbr: "MCPA"
fullName: "Multi-Carrier Power Amplifier"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcpa/"
summary: "Výkonový zesilovač schopný současně zesilovat více rádiových kmitočtových nosných v jediné jednotce. Je klíčový pro efektivitu základnové stanice, protože umožňuje podporu širších přenosových pásem a"
---

MCPA je výkonový zesilovač, který současně zesiluje více rádiových kmitočtových nosných v jediné jednotce, čímž zvyšuje efektivitu základnové stanice díky podpoře širších přenosových pásem a více kmitočtových pásem při současném snížení prostorových nároků a spotřeby energie.

## Popis

Multi-Carrier Power Amplifier (MCPA, vícekanálový výkonový zesilovač) je klíčovou součástí vysokofrekvenční (RF) části základnové stanice (eNodeB v LTE, gNB v NR). Na rozdíl od tradičních jedno-kanálových výkonových zesilovačů je MCPA navržen pro současné zesílení více RF nosných. Toho je dosaženo pomocí pokročilých linearizačních technik a širokopásmového zesilovacího obvodu, který zachovává integritu signálu v celém agregovaném přenosovém pásmu. Zesilovač musí zpracovávat složený signál všech nosných, což vyžaduje vysokou linearitu, aby se zabránilo intermodulačnímu zkreslení a spektrálnímu rozrůstání, které by mohlo rušit sousední kanály nebo porušit emisní masky definované specifikacemi 3GPP.

Architektonicky MCPA integruje digitální předzkreslení ([DPD](/mobilnisite/slovnik/dpd/)), redukci crest faktoru ([CFR](/mobilnisite/slovnik/cfr/)) a sofistikované filtrování. Vstupní základnové signály pro více nosných jsou digitálně zkombinovány, zpracovány pro linearizaci a následně převedeny na analogový RF signál. Samotné zesílení je typicky prováděno pomocí vysoce účinných polovodičových technologií, jako je LDMOS nebo GaN (nitrid galia), které nabízejí potřebnou výkonovou hustotu a tepelné vlastnosti. Výstup je následně filtrován pro potlačení mimopásmových emisí před vysláním přes anténu. MCPA je těsně integrován s rádiovou jednotkou základnové stanice a často podporuje dálkovou konfiguraci a monitorování parametrů, jako je zesílení, výstupní výkon a korekce linearity.

Jeho role v síti je zásadní pro agregaci více nosných a provoz v více pásmech. Konsolidací zesílení snižuje počet potřebných zesilovacích jednotek, čímž šetří místo, hmotnost a energii na lokalitách buňky. To je obzvláště důležité pro antény Massive [MIMO](/mobilnisite/slovnik/mimo/) a aktivní anténní systémy ([AAS](/mobilnisite/slovnik/aas/)), kde každý anténní prvek může vyžadovat zesílení pro více nosných. MCPA umožňuje operátorům nasadit více nosných a širší kanálová pásma (např. pro 5G NR) bez úměrného zvětšení fyzické velikosti nebo příkonu lokality, čímž efektivně podporuje zhušťování sítě a rozšiřování kapacity.

## K čemu slouží

MCPA byl zaveden jako odpověď na rostoucí poptávku po vyšší kapacitě sítě a spektrální účinnosti v mobilních sítích. Před jeho přijetím základnové stanice typicky používaly jedno-kanálové výkonové zesilovače (SCPA), kde každá RF nosná vyžadovala vlastní zesilovací jednotku. Tento přístup se stal nepraktickým, když operátoři začali nasazovat více kmitočtových pásem a používat agregaci nosných ke zvýšení uživatelských přenosových rychlostí. Architektura SCPA vedla k rozměrným, energeticky náročným a nákladným skříním základnových stanic, což komplikovalo získávání lokalit a zvyšovalo provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) kvůli vyšší spotřebě energie a nárokům na chlazení.

Historicky byl vývoj technologie MCPA urychlen s příchodem LTE-Advanced (od verze Rel-10), které zavedlo agregaci nosných jako klíčovou funkci. Potřeba efektivně zesilovat více agregovaných komponentních nosných motivovala vývoj širokopásmových lineárních zesilovačů. Dále přechod na 5G NR s podporou širokých přenosových pásem (až 100 MHz na nosnou a více) a provozem ve vyšších kmitočtových pásmech (jako mmWave) vyžadoval zesilovače s vynikající účinností a tepelným managementem. MCPA tyto problémy řeší tím, že umožňuje jednomu optimalizovanému zesilovači zpracovávat složený signál více nosných, čímž zjednodušuje návrh RF hardwaru, snižuje počet komponent a zlepšuje celkovou energetickou účinnost, což je klíčové pro dosažení cílů udržitelnosti a snížení celkových nákladů vlastnictví.

## Klíčové vlastnosti

- Současné zesílení více RF nosných v jediné hardwarové jednotce
- Podpora širokopásmového provozu a scénářů agregace nosných
- Integrace pokročilých linearizačních technik, jako je digitální předzkreslení (DPD)
- Vysoká účinnost využívající polovodičovou technologii LDMOS nebo GaN
- Snížené prostorové nároky a hmotnost na lokalitách buňky
- Možnosti dálkového monitorování a konfigurace výstupního výkonu a linearity

## Definující specifikace

- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [MCPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcpa/)
