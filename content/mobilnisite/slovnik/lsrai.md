---
slug: "lsrai"
url: "/mobilnisite/slovnik/lsrai/"
type: "slovnik"
title: "LSRAI – LSA Spectrum Resource Availability Information"
date: 2025-01-01
abbr: "LSRAI"
fullName: "LSA Spectrum Resource Availability Information"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lsrai/"
summary: "LSRAI je model řídicích informací používaný pro hlášení dostupnosti spektrálních zdrojů v rámci rámce Licencovaného sdíleného přístupu (LSA). Umožňuje dynamické sdílení spektra tím, že informuje systé"
---

LSRAI je model řídicích informací používaný v rámci rámce Licencovaného sdíleného přístupu (Licensed Shared Access) pro hlášení dostupnosti spektrálních zdrojů, který informuje systémy o tom, které kmitočty jsou použitelné v daném čase a místě.

## Popis

LSRAI, neboli [LSA](/mobilnisite/slovnik/lsa/) Spectrum Resource Availability Information, je standardizovaný informační prvek definovaný v rámci specifikací správy 3GPP, především TS 28.301 a TS 28.302. Funguje v širším kontextu regulačního rámce Licencovaného sdíleného přístupu (LSA), který umožňuje sekundárním uživatelům (jako jsou operátoři mobilních sítí) přístup ke kmitočtovým pásmům licencovaným primárním uživatelům (jako jsou vládní nebo satelitní služby) za kontrolovaných podmínek. Datový model LSRAI poskytuje strukturovaný formát pro sdělení aktuální a předpokládané dostupnosti konkrétních bloků spektra, včetně parametrů jako kmitočtový rozsah, geografická oblast (např. definovaná polygony nebo buňkami), časová platnost (počáteční/koncový čas) a maximální povolený vysílací výkon. Tyto informace jsou typicky generovány LSA Repository nebo LSA Controller, který přijímá vstupy od primárních uživatelů nebo regulační databáze, a jsou následně využívány systémy pro správu sítě, jako je Network Manager ([NM](/mobilnisite/slovnik/nm/)) nebo Domain Manager ([DM](/mobilnisite/slovnik/dm/)).

Z architektonického hlediska je LSRAI součástí specifikací rozhraní Itf-N, které definují informační službu mezi systémy pro správu. Umožňuje NM/DM vyžádat a přijímat aktualizace dostupnosti spektra, což umožňuje automatickou nebo poloautomatickou konfiguraci rádiových přístupových síťových (RAN) zařízení. Například když LSRAI indikuje, že určité pásmo 2,3 GHz je dostupné v konkrétním sektoru města, může systém správy nařídit eNodeB nebo gNB v této oblasti aktivovat odpovídající nosné, nakonfigurovat parametry buňky a případně předat uživatele na nově dostupné spektrum. Model podporuje jak hlášení dostupnosti v reálném čase, tak naplánovaná okna dostupnosti, což je klíčové pro koordinaci s primárními uživateli, kteří mohou mít periodické nebo předvídatelné vzorce využití.

V provozu tok zahrnuje LSA Controller (logickou entitu, kterou může provozovat regulátor nebo třetí strana), který agreguje práva a omezení využití původních uživatelů, převádí je na standardizované zprávy LSRAI a zasílá je nebo zpřístupňuje autorizovaným operátorům mobilních sítí. Systém správy operátora pak tyto informace zpracovává, často prostřednictvím mechanismů založených na politikách, aby rozhodl o aktivaci spektra. Klíčové komponenty, které interagují s LSRAI, zahrnují LSA Repository (databázi informací o původních uživatelích), LSA Controller, Network Manager a samotné RAN elementy. Jeho role je klíčová pro umožnění dynamického přístupu ke spektru bez způsobení škodlivého rušení primárním uživatelům, čímž se statické, exkluzivní licence mění na plynulejší, sdílené zdroje, které mohou zvýšit kapacitu a efektivitu sítě, zejména v pásmech jako 2,3–2,4 GHz, která jsou v některých regionech cílena pro LSA.

## K čemu slouží

LSRAI bylo vytvořeno, aby řešilo rostoucí potřebu efektivnějšího využití spektra v kontextu zvyšující se poptávky po mobilních datech a nedostatku spektra. Tradiční modely licencování spektra často vedly k jeho nevyužívání, kdy výluční držitelé licencí plně nevyužívali svá přidělená pásma ve všech geografických oblastech nebo po celou dobu. Koncept Licencovaného sdíleného přístupu ([LSA](/mobilnisite/slovnik/lsa/)) se objevil jako regulační řešení umožňující sekundární přístup při ochraně práv primárních uživatelů. LSRAI poskytuje technický prostředek v rámci systémů správy 3GPP k implementaci tohoto konceptu a řeší problém, jak dynamicky a spolehlivě komunikovat dostupnost spektra od centrální autority (jako je LSA Controller) k více operátorům mobilních sítí.

Historicky bylo sdílení spektra manuální, pomalé a náchylné k chybám, často vyžadující zdlouhavou koordinaci mezi původními a novými uživateli. LSRAI automatizuje tuto výměnu informací a umožňuje úpravy téměř v reálném čase. To bylo motivováno zejména snahou o zpřístupnění kmitočtových pásem, jako je pásmo 2,3 GHz v Evropě, která byla přidělena pro vládní nebo jiné služby, ale měla prostorové a časové mezery. Poskytnutím standardizovaného, strojově čitelného formátu pro informace o dostupnosti umožňuje LSRAI operátorům rychle využít tyto 'bílá místa' k odlehčení provozu, zlepšení pokrytí nebo poskytnutí nových služeb, čímž zlepšuje celkový výkon sítě bez nutnosti nových exkluzivních přidělení spektra.

Vytvoření LSRAI v Release 13 bylo součástí širší práce 3GPP na správě sítě pro pokročilé funkce RAN a flexibilitě spektra. Řešilo omezení předchozích přístupů, kterým chybělo jednotné rozhraní správy pro dynamické sdílení spektra, a umožnilo tak škálovatelná nasazení s více dodavateli. Integrací s existujícími rámci správy, jako je 3GPP Management Service (MnS), zajišťuje LSRAI, že dostupnost spektra může být bezproblémově začleněna do pracovních postupů automatizace a orchestrace sítě, čímž připravuje cestu pro pokročilejší modely sdílení, jako je Citizens Broadband Radio Service ([CBRS](/mobilnisite/slovnik/cbrs/)) v jiných regionech.

## Klíčové vlastnosti

- Strukturovaný informační model pro dostupnost spektra, včetně parametrů kmitočtu, geografie a času
- Integrace s 3GPP Management Service (MnS) prostřednictvím referenčního bodu Itf-N
- Podpora hlášení dostupnosti jak v reálném čase, tak podle plánu
- Umožňuje automatickou konfiguraci RAN na základě aktualizací dostupnosti spektra
- Usnadňuje vyhýbání se rušení tím, že poskytuje sekundárním uživatelům jasné hranice využití
- Standardizovaný formát zajišťuje interoperabilitu mezi různými LSA Controllery a systémy správy operátorů

## Související pojmy

- [LSA – Localised Service Area Identity](/mobilnisite/slovnik/lsa/)

## Definující specifikace

- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 28.302** (Rel-19) — LSA Controller IRP Management Operations
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access

---

📖 **Anglický originál a plná specifikace:** [LSRAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsrai/)
