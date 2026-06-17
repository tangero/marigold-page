---
slug: "dacs"
url: "/mobilnisite/slovnik/dacs/"
type: "slovnik"
title: "DACS – Distant Active Codec Set"
date: 2025-01-01
abbr: "DACS"
fullName: "Distant Active Codec Set"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dacs/"
summary: "DACS je koncept správy podle 3GPP pro vzdálenou konfiguraci kodeků v telekomunikačních sítích. Umožňuje operátorům spravovat a řídit sady řečových kodeků dostupné na vzdálených síťových prvcích, čímž"
---

DACS je koncept správy podle 3GPP, který umožňuje operátorům sítí vzdáleně konfigurovat a řídit sady řečových kodeků dostupné na vzdálených síťových prvcích, a tím zajistit konzistentní kvalitu hovoru a interoperabilitu.

## Popis

Distant Active Codec Set (DACS) je mechanismus správy definovaný ve specifikacích 3GPP, který umožňuje operátorům sítí vzdáleně konfigurovat a spravovat schopnosti řečových kodeků síťových prvků. V telekomunikačních sítích jsou řečové kodeky klíčové komponenty, které komprimují a dekomprimují hlasové signály pro přenos; různé kodeky nabízejí různý kompromis mezi kvalitou hovoru, efektivitou šířky pásma a složitostí zpracování. DACS poskytuje standardizovaný přístup pro řízení toho, které kodeky jsou aktivní a dostupné pro použití na konkrétních síťových místech, zejména na vzdálených síťových prvcích, k nimž může být obtížný fyzický přístup.

Z architektonického hlediska DACS funguje v rámci frameworku Operations, Administration, and Maintenance (OAM) sítí 3GPP. Zahrnuje systémy správy, které mohou posílat konfigurační příkazy síťovým prvkům, aby aktivovaly nebo deaktivovaly konkrétní sady řečových kodeků. Síťové prvky udržují sadu podporovaných kodeků a DACS umožňuje operátorům vybrat, která podmnožina z nich má být aktivně dostupná pro navázání hlasového hovoru. To je obzvláště důležité v prostředích s více dodavateli, kde různá zařízení mohou podporovat různé kombinace kodeků a operátoři potřebují zajistit konzistentní kvalitu služeb a interoperabilitu napříč svými sítěmi.

DACS funguje prostřednictvím rozhraní pro správu, která umožňují konfiguraci sad kodeků na síťových prvcích. Když síťový prvek přijme DACS konfigurační příkaz, aktualizuje své interní tabulky dostupnosti kodeků, čímž určí, které kodeky mohou být nabídnuty během procedur navazování hovoru. To ovlivňuje proces vyjednávání kodeků mezi koncovými body, čímž se zajistí, že pro přenos hovoru jsou použity pouze schválené kodeky. Tento mechanismus je zvláště cenný pro správu přechodů mezi kodeky, jako například při zavádění nových, efektivnějších kodeků při zachování zpětné kompatibility se staršími zařízeními.

Mezi klíčové komponenty DACS patří systém správy, který iniciuje konfigurační změny, síťové prvky, které implementují sady kodeků, a standardizovaná rozhraní mezi nimi. Síťové prvky musí udržovat jak sadu podporovaných kodeků (všechny kodeky, které hardware/software technicky zvládne), tak aktivní sadu kodeků (podmnožinu, která je aktuálně povolena pro použití). DACS poskytuje mechanismus pro vzdálenou úpravu této aktivní sady bez nutnosti fyzického přístupu k zařízení nebo manuální konfigurace na každém místě.

V širším síťovém kontextu hraje DACS klíčovou roli v řízení kvality služeb a optimalizaci sítě. Řízením toho, které kodeky jsou aktivní, mohou operátoři zajistit konzistentní kvalitu hovoru v celé své síti, řídit spotřebu přenosové kapacity a usnadnit hladké přechody mezi různými generacemi technologií. Také pomáhá při odstraňování problémů s kvalitou hovoru tím, že umožňuje operátorům standardizovat využívání kodeků napříč síťovými segmenty a rychle měnit konfigurace v reakci na síťové podmínky nebo požadavky na služby.

## K čemu slouží

DACS byl vytvořen pro řešení rostoucí složitosti správy kodeků v moderních telekomunikačních sítích. Jak se sítě vyvíjely, aby podporovaly více generací technologií (2G, 3G, 4G a nakonec 5G) a zařízení více dodavatelů, čelili operátoři značným výzvám při udržování konzistentní kvality hovoru a interoperability. Různé síťové prvky od různých dodavatelů mohly podporovat různé sady řečových kodeků, což vedlo k potenciálním problémům s kompatibilitou a nekonzistentním uživatelským zážitkům. DACS poskytuje standardizovaný mechanismus pro vzdálenou správu těchto sad kodeků a zajišťuje, že všechny síťové prvky používají kompatibilní konfigurace kodeků.

Historický kontext vývoje DACS zahrnuje přechod od okruhově přepínaných k paketově přepínaným hlasovým službám a zavedení nových, efektivnějších kodeků. Dřívější přístupy k síťové správě často vyžadovaly manuální konfiguraci nastavení kodeků na každém síťovém prvku, což bylo časově náročné, náchylné k chybám a obtížně škálovatelné ve velkých sítích. Jak sítě rostly ve velikosti a složitosti, potřebovali operátoři způsob, jak centrálně spravovat konfigurace kodeků napříč stovkami nebo tisíci síťových prvků, zejména těch na vzdálených nebo obtížně dostupných místech.

DACS řeší několik konkrétních problémů: umožňuje operátorům zajistit zpětnou kompatibilitu při zavádění nových kodeků, umožňuje centralizované řízení kvality služeb standardizací používání kodeků v celé síti a usnadňuje optimalizaci sítě tím, že umožňuje vzdálené změny konfigurace v reakci na měnící se síťové podmínky nebo vzorce provozu. Bez DACS by se operátoři museli spoléhat na manuální konfigurační procesy, které jsou pomalé, nekonzistentní a obtížně auditovatelné, což by mohlo vést k problémům s kvalitou služeb a zvýšeným provozním nákladům.

## Klíčové vlastnosti

- Vzdálená konfigurace sad řečových kodeků na síťových prvcích
- Standardizované rozhraní správy pro řízení kodeků
- Podpora více typů kodeků a jejich generací
- Centrální správa interoperability kodeků
- Dynamická aktivace/deaktivace kodeků bez přerušení služeb
- Integrace s širšími systémy OAM pro jednotnou správu sítě

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [DACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dacs/)
