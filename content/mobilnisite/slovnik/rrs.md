---
slug: "rrs"
url: "/mobilnisite/slovnik/rrs/"
type: "slovnik"
title: "RRS – Root Sum of the Squares"
date: 2025-01-01
abbr: "RRS"
fullName: "Root Sum of the Squares"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rrs/"
summary: "Statistická metoda definovaná v 3GPP pro výpočet kombinovaného výkonu více rádiových signálů, používaná zejména při testování Over-the-Air (OTA). Je klíčová pro přesné hodnocení celkového vyzařovaného"
---

RRS (druhá odmocnina ze součtu čtverců) je statistická metoda definovaná v 3GPP pro výpočet kombinovaného výkonu více rádiových signálů, používaná při testování Over-the-Air (OTA) pro hodnocení celkového vyzařovaného výkonu.

## Popis

Root Sum of the Squares (RRS, druhá odmocnina ze součtu čtverců) je matematická a statistická technika specifikovaná v rámci testovacího rámce fyzické vrstvy 3GPP, primárně dokumentovaná v TS 36.143 pro LTE. Je klíčovou součástí metodik testování Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)), konkrétně pro hodnocení celkového vyzařovaného výkonu ([TRP](/mobilnisite/slovnik/trp/)) uživatelského zařízení (UE). Metoda slouží ke kombinaci měření výkonu provedených z více prostorových bodů kolem testovaného zařízení v anechoické komoře. Základní princip spočívá v měření výkonu vyzařovaného anténou/anténami UE na sférické mřížce bodů, čímž se zachytí trojrozměrný vyzařovací diagram. Tato jednotlivá bodová měření, typicky vyjádřená v lineárních jednotkách výkonu (např. miliwattech), se nejprve umocní na druhou a poté sečtou napříč všemi měřicími body. Konečná hodnota TRP se získá odmocněním tohoto součtu, čímž se efektivně získá střední kvadratická hodnota ([RMS](/mobilnisite/slovnik/rms/)) vyzařovaného výkonu přes celou sféru. Tento proces zohledňuje vektorovou povahu elektromagnetických polí a poskytuje jediný komplexní metrický údaj pro celkový výstupní výkon zařízení, nezávislý na jeho směrovosti.

Aplikace RRS je klíčová pro dodržení regulatorních limitů maximálního vysílacího výkonu a pro validaci výkonu základního pásma a [RF](/mobilnisite/slovnik/rf/). Při testování je UE umístěno na pozicionovacím systému, který jej otáčí v azimutálních a elevančních úhlech, zatímco měřicí anténa připojená k přijímači (jako je spektrální analyzátor nebo vektorový signálový analyzátor) zaznamenává přijímaný výkon v každém bodě. Výpočet RRS integruje tato diskrétní měření, aby aproximoval spojitý integrál výkonu přes celý prostorový úhel 4π steradiánů. Tato metoda je přesnější než pouhé převzetí špičkové nebo průměrné hodnoty z několika měření, protože správně váží každý měřicí bod podle prostorového úhlu, který v sférickém souřadnicovém systému reprezentuje. Výsledná hodnota TRP je klíčovým ukazatelem výkonnosti používaným k ověření, že výkonový zesilovač a anténní systém UE fungují správně a efektivně, což ovlivňuje jak rádiový dosah zařízení, tak jeho spotřebu baterie.

Mimo základní TRP princip RRS podkládá i další OTA hodnotící parametry, jako je celková izotropní citlivost (TIS). Jeho standardizace v 3GPP zajišťuje konzistenci a reprodukovatelnost výsledků testů napříč různými laboratořemi a výrobci zařízení. Metodika je navržena tak, aby byla robustní vůči měřicímu šumu a chybám diskretizace, které jsou vlastní vzorkování spojitého vyzařovacího diagramu. Poskytnutím standardizovaného výpočtu RRS umožňuje spravedlivé a přesné srovnání různých modelů UE a zajišťuje, že zařízení splňují přísné výkonnostní požadavky stanovené síťovými operátory a regulačními orgány po celém světě, čímž tvoří základní prvek procesů certifikace zařízení a schvalování typu.

## K čemu slouží

Účelem standardizace metody Root Sum of the Squares (RRS) v rámci 3GPP bylo stanovit jednotný, přesný a opakovatelný postup pro hodnocení celkového vyzařovaného výkonu mobilních zařízení v prostředí [OTA](/mobilnisite/slovnik/ota/). Před takovou standardizací mohly různé zkušebny a výrobci používat odlišné metodologie (např. jednoduché průměrování, detekci špičky nebo různé techniky numerické integrace) pro výpočet [TRP](/mobilnisite/slovnik/trp/) ze sférických měření. Tento nedostatek konzistence vedl k možným nesrovnalostem ve výsledcích testů, což ztěžovalo objektivní srovnání výkonu zařízení nebo zajištění souladu s regulatorními limity emisí. Metoda RRS byla zavedena, aby tento problém vyřešila poskytnutím definitivního matematického vzorce, který musí všechny strany dodržovat, a tím zaručila, že hodnota TRP hlášená pro UE je vypočtena naprosto stejným způsobem bez ohledu na to, kde se test provádí.

Historicky, jak se mobilní zařízení stávala složitějšími s více anténami (např. pro [MIMO](/mobilnisite/slovnik/mimo/) a diverzitní příjem) a pracovala v rozšiřujícím se rozsahu kmitočtových pásem, se tradiční metody vodivého testování (připojení kabelu přímo k anténnímu portu) staly nedostatečnými. Vodivé testování ignoruje výkon samotné antény a účinky fyzického pouzdra zařízení a ruky uživatele („handset effect“). Testování OTA se objevilo jako nezbytné řešení pro hodnocení zařízení jako celého systému v jeho provozním stavu. Výpočet RRS je základním kamenem tohoto měření výkonu OTA. Řeší základní výzvu převodu konečné množiny diskrétních bodových měření na jediný přesný odhad celkového výkonu vyzařovaného všemi směry. Jeho vytvoření bylo motivováno potřebou fyzikálně správné a statisticky podložené integrační techniky, která je zároveň implementovatelná v automatizovaných testovacích systémech a jednoznačná ve své interpretaci.

Zavedením povinnosti používat RRS ve specifikacích jako TS 36.143 zajistilo 3GPP, že se průmysl posunul ke společnému testovacímu jazyku. To nejen zefektivnilo proces certifikace zařízení, ale také dodalo síťovým operátorům důvěru ve hlášené výkonnostní metriky UE, které schvalují pro své sítě. Přesný TRP, odvozený prostřednictvím RRS, přímo koreluje s efektivním pokrytím zařízení a rozpočtem rádiového spoje, což ovlivňuje celkové plánování sítě a kvalitu služeb. Metoda RRS tedy existuje proto, aby odstranila nejednoznačnost měření, podpořila interoperabilitu v testování a v konečném důsledku zajistila, že koncová uživatelská zařízení spolehlivě fungují v reálných bezdrátových prostředích.

## Klíčové vlastnosti

- Standardizovaný matematický vzorec pro výpočet celkového vyzařovaného výkonu (TRP) ze sférických měření
- Integruje diskrétní měření výkonu přes celý prostorový úhel 4π steradiánů
- Poskytuje střední kvadratickou hodnotu (RMS) vyzařovaného výkonu, která zohledňuje prostorové rozložení
- Základ pro testování shody a výkonu metodou Over-the-Air (OTA)
- Zajišťuje konzistenci a reprodukovatelnost měření napříč různými testovacími laboratořemi
- Použitelná pro testování víceanténních systémů a konfigurací MIMO

## Definující specifikace

- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing

---

📖 **Anglický originál a plná specifikace:** [RRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrs/)
