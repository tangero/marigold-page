---
slug: "fpac"
url: "/mobilnisite/slovnik/fpac/"
type: "slovnik"
title: "FPAC – Fixed Part Authorisation Code"
date: 2025-01-01
abbr: "FPAC"
fullName: "Fixed Part Authorisation Code"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fpac/"
summary: "Bezpečnostní kód odvozený z CTS-PIN, používaný k autorizaci částí pevné sítě v celulárních systémech. Zajišťuje zabezpečený přístup a autentizaci pro komponenty pevné infrastruktury a brání neoprávněn"
---

FPAC je Fixed Part Authorisation Code, což je bezpečnostní kód používaný k autorizaci částí pevné sítě v celulárních systémech za účelem zabránění neoprávněnému přístupu.

## Popis

Fixed Part Authorisation Code (FPAC) je bezpečnostní přihlašovací údaj definovaný ve specifikacích 3GPP, konkrétně v TS 43.020. Je algoritmicky odvozen z Cordless Telephony System Personal Identification Number ([CTS-PIN](/mobilnisite/slovnik/cts-pin/)), která slouží jako kořenové tajemství. FPAC funguje jako autorizační token pro zařízení pevné sítě, často označovaná jako Fixed Parts ([FP](/mobilnisite/slovnik/fp/)) v kontextech jako je propojení [DECT](/mobilnisite/slovnik/dect/)/GSM nebo systémy bezšňůrové telefonie. Jeho primární role spočívá v autentizaci pevné infrastruktury vůči jádru sítě nebo vůči jiným síťovým prvkům, čímž zajišťuje, že se do síťových operací mohou zapojit pouze legitimní, provozovatelsky zřízená hardwarová zařízení.

Z architektonického hlediska je FPAC generován a spravován síťovými operátory, typicky v rámci autentizačních serverů nebo modulů [SIM](/mobilnisite/slovnik/sim/). Proces odvození zahrnuje kryptografické algoritmy, které transformují CTS-PIN na FPAC, což zajišťuje, že původní [PIN](/mobilnisite/slovnik/pin/) není přenášen ani uložen v otevřené podobě. Tento kód je následně zřízen do hardwaru Fixed Part během výroby nebo nasazení. Když se Fixed Part pokouší zaregistrovat v síti, předloží FPAC spolu s dalšími identifikátory. Síť tento kód ověří vůči svým záznamům a podle toho přístup povolí nebo zamítne.

Klíčovými komponentami v ekosystému FPAC jsou Authentication Centre (AuC) nebo podobný bezpečnostní modul, který ukládá CTS-PIN a počítá FPAC, hardware Fixed Part, který FPAC bezpečně ukládá, a síťové přístupové protokoly, které umožňují jeho výměnu. FPAC hraje klíčovou roli v prevenci útoků pomocí falešných základnových stanic a neoprávněného rozšiřování sítě, čímž udržuje integritu rádiové přístupové sítě. Je obzvláště relevantní v privátních nebo hybridních sítích, kde může být pevná infrastruktura nasazena podniky nebo v rezidenčních prostředích.

Přestože FPAC má kořeny ve starších standardech GSM a bezšňůrové telefonie, jeho principy autentizace pevných částí nadále ovlivňují bezpečnostní architektury v pozdějších generacích celulárních sítí. Představuje základní přístup k autentizaci zařízení, který zdůrazňuje potřebu ověřovat nejen uživatelská zařízení (UE), ale také síťovou infrastrukturu. Specifikace zajišťuje interoperabilitu mezi výrobci standardizací metody odvození a postupů použití.

## K čemu slouží

FPAC byl vytvořen k řešení bezpečnostních zranitelností v komponentech pevné sítě, zejména v bezšňůrové telefonii a raných celulárních rozšířeních. Před jeho zavedením bylo možné části pevné sítě, jako základnové stanice nebo přístupové body, snadno zfalšovat nebo naklonovat, což vedlo k neoprávněnému přístupu do sítě, krádeži služeb a potenciálním útokům typu denial-of-service. [CTS-PIN](/mobilnisite/slovnik/cts-pin/), ze kterého je FPAC odvozen, byl již zaveden jako metoda uživatelské autentizace v systémech [DECT](/mobilnisite/slovnik/dect/); jeho rozšíření pro autorizaci infrastruktury poskytlo konzistentní bezpečnostní rámec.

Historicky, jak se celulární sítě vyvíjely, aby podporovaly pevný bezdrátový přístup a propojení s bezšňůrovou telefonií (jako DECT/GSM), rostla potřeba autentizovat nejen mobilní terminály, ale také pevnou infrastrukturu, která je propojuje. To bylo zvláště kritické pro rezidenční nebo podnikové základnové stanice, k nimž byl možný fyzický přístup. FPAC tento problém vyřešil tím, že poskytoval kryptograficky odvozený, neopakovatelný kód, který jedinečně identifikoval a autorizoval každý Fixed Part. Zmírnil tak rizika spojená s padělaným zařízením a zajistil, že k síťovým zdrojům mohou přistupovat pouze hardwarová zařízení schválená operátorem.

Vytvoření FPAC bylo motivováno snahou o vytvoření jednotného bezpečnostního modelu napříč různými přístupovými technologiemi. Využitím stávající infrastruktury CTS-PIN minimalizoval dodatečnou složitost a zároveň zvýšil ochranu. Řešil omezení jednoduchých sériových čísel hardwaru nebo statických hesel, která byla náchylná ke krádeži nebo útokům hrubou silou. Proces odvození FPAC přidal vrstvu kryptografické bezpečnosti, což z něj učinilo robustní řešení své doby a položilo základy pro pozdější autentizační mechanismy v sítích 3GPP.

## Klíčové vlastnosti

- Odvozen z CTS-PIN pomocí standardizovaných kryptografických algoritmů
- Používán pro autentizaci Fixed Parts (FP) při síťovém přístupu
- Zabraňuje neoprávněnému nasazení infrastruktury
- Zvyšuje bezpečnost proti útokům pomocí falešných základnových stanic
- Podporuje interoperabilitu mezi zařízeními různých výrobců
- Integruje se s existujícími autentizačními centry (AuC)

## Související pojmy

- [CTS-PIN – CTS-Personal Identification Number](/mobilnisite/slovnik/cts-pin/)
- [DECT – Digital Enhanced Cordless Telecommunications](/mobilnisite/slovnik/dect/)

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [FPAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fpac/)
