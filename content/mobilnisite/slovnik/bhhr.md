---
slug: "bhhr"
url: "/mobilnisite/slovnik/bhhr/"
type: "slovnik"
title: "BHHR – Beside Head and Hand Right Side"
date: 2025-01-01
abbr: "BHHR"
fullName: "Beside Head and Hand Right Side"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/bhhr/"
summary: "Standardizovaný fantomový model používaný pro testy shody měrného absorpčního poměru (SAR) bezdrátových zařízení. Představuje lidskou hlavu a ruku umístěnou na pravé straně zařízení, což umožňuje přes"
---

BHHR je standardizovaný fantomový model představující hlavu a ruku na pravé straně, používaný pro testy shody měrného absorpčního poměru (SAR) k měření absorpce energie vysokofrekvenčního záření a zajištění bezpečnosti mobilních zařízení.

## Popis

Beside Head and Hand Right Side (BHHR) je přesně definovaný antropomorfní fantomový model standardizovaný v rámci specifikací 3GPP pro testování elektromagnetické expozice. Skládá se z podrobného geometrického znázornění lidské hlavy (včetně simulátorů ucha, tváře a mozkové tkáně) a pravé ruky, umístěných v konkrétní prostorové konfiguraci vůči testovanému zařízení ([DUT](/mobilnisite/slovnik/dut/)). Fantom je naplněn tkáňově ekvivalentní kapalinou, která napodobuje dielektrické vlastnosti lidských tkání v různých kmitočtových pásmech mobilních sítí (např. pásma do 6 GHz a milimetrové vlny).

Během testování je bezdrátové zařízení umístěno v přímém kontaktu s BHHR fantomem podle standardizovaných testovacích poloh definovaných v 3GPP TS 38.161 a souvisejících specifikacích. Zařízení pracuje na maximálním vysílacím výkonu, zatímco sofistikované sondové systémy měří rozložení elektrického pole uvnitř simulátoru tkáně fantomu. Tato měření jsou zpracována výpočetními algoritmy pro výpočet prostorově průměrovaného špičkového měrného absorpčního poměru (SAR), který představuje rychlost, jakou je vysokofrekvenční energie absorbována tělesnými tkáněmi, měřenou ve wattech na kilogram (W/kg).

Architektura BHHR fantomu zahrnuje specifické anatomické rysy klíčové pro přesné testování: detailní tvar ucha ovlivňující polohu zařízení, geometrii ruky ovlivňující vazbu antény a vrstvy tkáně s přesně řízenými dielektrickými vlastnostmi. Materiály fantomu musí udržovat konzistentní elektrické charakteristiky (permitivitu a vodivost) v celém pracovním kmitočtovém rozsahu, s tolerancemi typicky do ±5 % cílových hodnot. Testovací postupy specifikují více orientací zařízení a scénářů použití, aby bylo zajištěno komplexní posouzení expozice.

Tento fantomový model pracuje ve spojení s automatickými pozicovacími systémy a robotickými sondami, které systematicky skenují měřicí oblast uvnitř simulátoru tkáně. Systém sbírá tisíce měřicích bodů k vytvoření trojrozměrné mapy rozložení SAR. Pokročilé algoritmy následného zpracování pak identifikují nejvyšší 1g nebo 10g kubický objem tkáně (podle požadavků různých regulatorních standardů) a vypočítají průměrnou hodnotu SAR. Celý měřicí systém musí být pravidelně kalibrován pomocí referenčních dipólových antén a validačních fantomů, aby byla zajištěna přijatelná míra nejistoty měření.

Role BHHR v síťovém ekosystému je zásadně o shodě s bezpečnostními předpisy, nikoli o síťové funkčnosti. Každé mobilní zařízení musí před komerčním nasazením projít testováním SAR pomocí standardizovaných fantomů, jako je BHHR. Síťoví operátoři a výrobci zařízení se spoléhají na tyto standardizované testovací metodiky, aby zajistili, že všechna nasazená zařízení splňují mezinárodní bezpečnostní směrnice (jako jsou např. od ICNIRP a [FCC](/mobilnisite/slovnik/fcc/)), a zároveň si udržují optimální rádiový výkon. Standardizace fantomu napříč specifikacemi 3GPP zajišťuje jednotné testovací metodiky po celém světě, což usnadňuje certifikaci zařízení a přístup na mezinárodní trhy.

## K čemu slouží

BHHR fantom byl vytvořen, aby řešil kritickou potřebu standardizovaného, reprodukovatelného testování vysokofrekvenční expozice z bezdrátových zařízení. Před takovou standardizací používali různí výrobci a testovací laboratoře odlišné návrhy fantomů a testovací metodiky, což vedlo k nekonzistentním výsledkům SAR a obtížím při porovnávání bezpečnostního výkonu zařízení. Tento nedostatek standardizace vytvářel výzvy pro procesy regulatorního schvalování a ztěžoval zajištění jednotné shody s bezpečnostními předpisy v celém odvětví.

Historicky, jak se mobilní zařízení stávala výkonnějšími a pracovala v širším kmitočtovém rozsahu, rostly obavy z možných zdravotních účinků vysokofrekvenční expozice. Regulační orgány po celém světě stanovily limity SAR, ale bez standardizovaných testovacích metod čelili výrobci nejistotě ohledně požadavků na shodu. BHHR fantom spolu se svým protějškem pro levou stranu ([BHHL](/mobilnisite/slovnik/bhhl/)) poskytuje konzistentní anatomický model, který představuje realistické scénáře použití, kdy uživatelé přidržují zařízení u hlavy během hovorů. Tím se řeší omezení jednodušších testovacích sestav, které nezohledňovaly vliv ruky na výkon antény a vzorce vysokofrekvenční expozice.

Vytvoření BHHR bylo motivováno vývojem faktorů formy zařízení a vzorců používání. Moderní smartphony mají složité anténní systémy, které interagují s lidskou tkání různě v závislosti na umístění ruky a orientaci zařízení. BHHR fantom konkrétně řeší scénáře použití pravou rukou, které podle statistických studií představují většinu uživatelů. Zahrnutím hlavy i ruky do testovacího modelu poskytuje přesnější měření SAR než fantomy pouze s hlavou, zejména u zařízení, kde umístění ruky významně ovlivňuje výkon antény a rozložení proudu.

Tato standardizace řeší problém nekonzistentního bezpečnostního testování v různých regionech a laboratořích. Umožňuje výrobcům zařízení navrhovat produkty s jistotou, že jejich testování SAR bude akceptováno více regulačními orgány po celém světě. Dále podporuje vývoj sofistikovanějších anténních návrhů a přenosových technologií tím, že poskytuje spolehlivý rámec pro hodnocení jejich bezpečnostních dopadů. Jelikož 5G zavádí nová kmitočtová pásma a technologie beamformingu, standardizované fantomy jako BHHR se stávají ještě kritičtějšími pro zajištění toho, že inovativní technologie mohou být nasazeny bez kompromisů v uživatelské bezpečnosti.

## Klíčové vlastnosti

- Standardizovaný geometrický model lidské hlavy a pravé ruky pro konzistentní testování
- Tkáňově ekvivalentní kapalina s řízenými dielektrickými vlastnostmi napříč kmitočtovými pásmy mobilních sítí
- Přesně definovaný prostorový vztah mezi zařízením a fantomem pro reprodukovatelné pozicování
- Kompatibilita s automatizovanými robotickými sondovými systémy pro efektivní měření SAR
- Validační postupy zajišťující nejistotu měření v přijatelných mezích
- Podpora více kmitočtových rozsahů včetně pásem do 6 GHz a milimetrových vln

## Definující specifikace

- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [BHHR na 3GPP Explorer](https://3gpp-explorer.com/glossary/bhhr/)
