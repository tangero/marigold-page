---
slug: "vrc"
url: "/mobilnisite/slovnik/vrc/"
type: "slovnik"
title: "VRC – Variable Reference Measurement Channel"
date: 2025-01-01
abbr: "VRC"
fullName: "Variable Reference Measurement Channel"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/vrc/"
summary: "Definovaná konfigurace testovacího kanálu používaná pro ověřování výkonu a testování typové způsobilosti uživatelského zařízení (UE) LTE a LTE-Advanced. Specifikuje sadu proměnných parametrů pro vytvo"
---

VRC je definovaná konfigurace testovacího kanálu používaná v LTE a LTE-Advanced k vytvoření reprodukovatelných, standardizovaných podmínek pro ověřování výkonu přijímače UE.

## Popis

Variable Reference Measurement Channel (VRC, proměnný referenční měřicí kanál) je standardizovaná testovací konfigurace definovaná ve specifikacích 3GPP pro testování shody výkonu přijímače UE. Nejde o kanál používaný v provozní síti, ale o přesně definovaný referenční konstrukt používaný v laboratorních a testovacích prostředích. VRC definuje kompletní sadu parametrů fyzické vrstvy, které společně simulují konkrétní scénář downlinkového přenosu. Mezi tyto parametry patří šířka pásma, modulační schéma ([QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM), kódová rychlost, velikost transportního bloku, alokace zdrojů, konfigurace antén (např. [SISO](/mobilnisite/slovnik/siso/), [MIMO](/mobilnisite/slovnik/mimo/) režimy jako 2x2 prostorové multiplexování) a použití funkcí jako je agregace nosných. Testovací systém nakonfiguruje generátor signálu tak, aby vysílal downlinkový signál odpovídající konkrétní definici VRC.

Testované UE je pak tomuto signálu vystaveno za řízených rádiových podmínek, které jsou emulovány pomocí simulátoru útlumového kanálu implementujícího standardizované modely kanálu (např. Extended Pedestrian A, Extended Vehicular A). Klíčovým výkonnostním metrikem je propustnost měřená na vyšších vrstvách UE, která musí splňovat nebo překročit minimální požadavek stanovený pro daný VRC a stav kanálu. Tento proces validuje schopnost UE správně demodulovat a dekódovat data v realistických a náročných rádiových prostředích. VRC jsou definovány pro různé kategorie UE a sady schopností, což zajišťuje, že je například UE kategorie 6 testováno s konfiguracemi využívajícími podporované funkce, jako je modulace vyššího řádu nebo více prostorových vrstev.

Definice VRC je klíčová pro zajištění interoperability a konzistentního základního výkonu napříč zařízeními od různých výrobců. Tvoří základ pro testy specifikované v testovacích sadách Radio Resource Management ([RRM](/mobilnisite/slovnik/rrm/)) a Radio Transmission and Reception (RTR). Poskytnutím variabilního 'menu' testovacích kanálů umožňuje rámec VRC komplexní pokrytí testování. Jedna testovací případová studie odkazuje na konkrétní identifikátor VRC a kompletní technické detaily tohoto VRC jsou uvedeny v tabulkách specifikace, což neumožňuje žádnou nejednoznačnost pro dodavatele testovacího zařízení nebo certifikační orgány.

## K čemu slouží

Koncept VRC byl vyvinut k řešení potřeby důkladného, opakovatelného a standardizovaného testování výkonu stále složitějších přijímačů UE pro LTE a LTE-Advanced. Starší mobilní technologie také měly referenční měřicí kanály, ale zavedení [MIMO](/mobilnisite/slovnik/mimo/), agregace nosných a modulace vyššího řádu v 3GPP Release 10 (LTE-Advanced) vedlo k obrovskému rozšíření možných provozních stavů. Bez standardizovaných VRC by bylo nemožné spravedlivě porovnávat výkon různých UE nebo definovat minimální výkonnostní požadavky zajišťující dobrou uživatelskou zkušenost v terénu.

Rámec VRC řeší problém explozivního nárůstu testovacích případů tím, že poskytuje sadu reprezentativních konfigurací kanálů, které zatěžují různé aspekty návrhu přijímače. Umožňuje testovacím specifikacím stanovit výkon za specifických, náročných podmínek (např. nízký poměr signál-šum s vysokou modulací nebo vysoký Dopplerův rozptyl s MIMO). To zajišťuje, že UE se nejen připojí k síti, ale také udrží dobrou datovou propustnost v reálných scénářích s útlumem a rušením. Vývoj VRC napříč releasy 3GPP přímo sleduje zavádění nových funkcí, což zajišťuje, že zařízení deklarující podporu například 256QAM nebo prostorového multiplexování se 4 vrstvami jsou na tyto schopnosti důkladně testována.

## Klíčové vlastnosti

- Standardizovaná laboratorní testovací konfigurace pro testování přijímače UE
- Definuje komplexní sadu parametrů přenosu fyzické vrstvy
- Používá se se standardizovanými modely kanálu k emulaci reálných podmínek
- Základ pro ověření výkonu propustnosti v testování shody
- Škálovatelná pro podporu nových kategorií UE a funkcí (CA, MIMO, modulace vyššího řádu)
- Zajišťuje interoperabilitu a konzistentní minimální výkon napříč dodavateli

## Související pojmy

- [FRC – Fixed Reference Measurement Channel](/mobilnisite/slovnik/frc/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 37.976** (Rel-19) — MIMO OTA Test Methodology Study
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology

---

📖 **Anglický originál a plná specifikace:** [VRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vrc/)
