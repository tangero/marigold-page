---
slug: "cwt"
url: "/mobilnisite/slovnik/cwt/"
type: "slovnik"
title: "CWT – Character Waiting Time"
date: 2025-01-01
abbr: "CWT"
fullName: "Character Waiting Time"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cwt/"
summary: "Character Waiting Time (CWT) je parametr ve specifikacích 3GPP, který definuje maximální dobu, po kterou přijímač čeká na úplný znak při asynchronním přenosu dat. Zajišťuje spolehlivé rámování znaků a"
---

CWT (Character Waiting Time) je maximální doba, po kterou přijímač čeká na úplný znak při asynchronním přenosu dat, aby zajistil spolehlivé rámování znaků a synchronizaci v legacy okruhově přepínaných službách.

## Popis

Character Waiting Time (CWT) je základní časový parametr definovaný ve specifikacích 3GPP, primárně pro asynchronní přenos dat v okruhově přepínaných telekomunikačních službách. Určuje maximální dobu, po kterou přijímací entita, jako je mobilní stanice nebo síťové zařízení, bude čekat na příjem úplného znaku (včetně start bitu, datových bitů, paritního bitu a stop bitu), než vyhlásí stav časového limitu nebo chyby. Tento parametr je klíčový pro udržení synchronizace na úrovni znaků mezi vysílačem a přijímačem, zejména v prostředích s proměnným zpožděním šíření nebo nepřesnostmi hodin. Hodnota CWT se obvykle vyjadřuje v milisekundách a je konfigurovatelná na základě přenosové rychlosti a struktury znaku (např. počtu datových bitů, nastavení parity), aby vyhověla různým požadavkům služeb.

V praxi funguje CWT jako ochranný časovač během příjmu znaku. Po detekci start bitu přijímač spustí časovač CWT a vzorkuje příchozí bitový tok na dohodnuté přenosové rychlosti. Pokud není úplný znak až po stop bit přijat před vypršením CWT, může přijímač neúplný znak zahodit, vyvolat žádost o opakovaný přenos nebo signalizovat chybu přenosu v závislosti na používaném protokolu vyšší vrstvy. Tento mechanismus chrání před problémy, jako jsou bitové skluzy, drift hodin nebo přerušení linky, které by jinak mohly vést k chybám rámování nebo nesprávné interpretaci dat. Parametr je obzvláště důležitý v legacy okruhově přepínaných datových službách GSM a UMTS, včetně faxové a modemové komunikace, kde je asynchronní přenos běžný.

Z architektonického hlediska je CWT implementován v protokolech fyzické vrstvy a vrstvy spojení dat systémů 3GPP. Interaguje s dalšími časovými parametry, jako jsou prahové hodnoty Bit Error Rate ([BER](/mobilnisite/slovnik/ber/)) a časování mezi znaky, aby zajistil robustní přenos dat. V rádiové přístupové síti (RAN) a v jádře sítě jsou nastavení CWT vyjednávána během sestavování hovoru nebo aktivace služby, často odvozena ze standardizovaných profilů ve specifikacích jako je 3GPP TS 24.008 pro řízení hovorů. Zatímco jeho význam poklesl s přechodem na paketově přepínané a plně IP sítě v pozdějších vydáních 3GPP, CWT zůstává kritickou součástí pro zpětnou kompatibilitu a specifické IoT nebo M2M aplikace spoléhající na okruhově přepínané přenosy.

Role CWT přesahuje pouhou detekci chyb; přispívá k celkové Quality of Service (QoS) zajištěním integrity dat na úrovni znaků. V systémech s omezenými možnostmi opravy chyb, jako byly rané mobilní datové služby, pomáhá CWT minimalizovat dopad přechodných zhoršení kanálu. Jeho konfigurace musí vyvažovat citlivost – nastavení příliš krátkého CWT může způsobit zbytečné chyby při normálních variacích zpoždění, zatímco nastavení příliš dlouhého může oddálit obnovu po chybě a snížit propustnost. CWT tedy představuje příklad podrobných časových úvah vyžadovaných v telekomunikacích k udržení spolehlivé komunikace přes nepředvídatelné bezdrátové spoje.

## K čemu slouží

CWT byl zaveden, aby řešil výzvy asynchronního přenosu dat přes bezdrátové sítě, kde proměnlivá zpoždění šíření a nepřesnosti hodin mohou narušit rámování znaků. V raných mobilních systémech, jako je GSM, vyžadovaly okruhově přepínané datové služby pro faxové, modemové a dálnopisné aplikace přesné časování pro správnou interpretaci hranic znaků. Bez definované čekací doby by se přijímače mohly nesprávně synchronizovat s vysílaným bitovým tokem, což by vedlo ke zkresleným datům nebo přetrvávajícím chybám. CWT poskytuje standardizovaný mechanismus pro detekci a obnovu z takových ztrát synchronizace, čímž zvyšuje spolehlivost nehlasových služeb.

Vytvoření CWT bylo motivováno potřebou adaptovat protokoly pro asynchronní komunikaci z pevných sítí, běžné u pevnostních modemů, na bezdrátové prostředí. Bezdrátové kanály přinášejí specifická zhoršení, jako je útlum, interference a přerušení při předávání hovoru, která mohou nepředvídatelně prodloužit nebo zkrátit dobu přenosu. Předchozí přístupy v pevných sítích spoléhaly na stabilní zpoždění a přesné hodiny, ale tyto předpoklady v mobilním kontextu selhávaly. CWT jako součást komplexních strategií rámování a synchronizace 3GPP umožnil mobilním sítím podporovat legacy datové aplikace a zároveň zmírňovat problémy specifické pro bezdrátové prostředí, čímž zajišťoval interoperabilitu a uživatelský zážitek.

Historicky řešil CWT omezení raných digitálních mobilních systémů, kterým chyběly sofistikované mechanismy opravy chyb nebo adaptivního časování. Definováním maximální čekací doby na znak umožnil jednodušší a nákladově efektivnější implementace v koncových zařízeních a síťových prvcích, což bylo klíčové pro masové rozšíření mobilních datových služeb. S vývojem 3GPP se role CWT stala součástí širších rámců QoS a spolehlivosti, ačkoli její přímá viditelnost poklesla s přechodem na paketově přepínané technologie. Přesto zůstává relevantní pro specializované aplikace a zpětnou kompatibilitu, což ilustruje důraz 3GPP na detail při zajišťování robustní komunikace napříč různými typy služeb.

## Klíčové vlastnosti

- Definuje maximální čekací dobu pro příjem úplného znaku při asynchronním přenosu
- Zajišťuje synchronizaci na úrovni znaků mezi vysílačem a přijímačem
- Konfigurovatelný na základě přenosové rychlosti a struktury znaku (např. bitů na znak)
- Pomáhá detekovat a obnovit se z chyb rámování způsobených časovými nesoulady
- Podporuje legacy okruhově přepínané datové služby, jako je faxová a modemová komunikace
- Integruje se s protokoly fyzické vrstvy a vrstvy spojení dat pro správu chyb

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CWT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cwt/)
