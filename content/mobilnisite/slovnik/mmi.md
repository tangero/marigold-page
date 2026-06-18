---
slug: "mmi"
url: "/mobilnisite/slovnik/mmi/"
type: "slovnik"
title: "MMI – Man Machine Interface"
date: 2026-01-01
abbr: "MMI"
fullName: "Man Machine Interface"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmi/"
summary: "Rozhraní mezi lidským uživatelem a telekomunikačním zařízením nebo systémem správy sítě. Zahrnuje metody a prostředky pro výměnu informací, včetně displejů, klávesnic, hlasových příkazů a grafických u"
---

MMI je rozhraní mezi lidským uživatelem a telekomunikačním zařízením nebo systémem správy sítě, zahrnující metody jako displeje, klávesnice a hlasové příkazy pro výměnu informací.

## Popis

Rozhraní člověk-stroj (Man Machine Interface, MMI) ve standardech 3GPP označuje komplexní soubor principů, protokolů a specifikací upravujících interakci mezi lidskými uživateli (nebo operátory) a telekomunikačním zařízením. To zahrnuje široké spektrum prvků, od fyzického rozhraní na mobilním terminálu – jako je obrazovka, klávesnice, mikrofon a reproduktor – až po logická a grafická rozhraní používaná pro konfiguraci zařízení, aktivaci služeb a systémy správy sítě. V jádru MMI definuje, jak jsou informace prezentovány uživateli (výstup) a jak jsou vstupy uživatele zachyceny a interpretovány strojem (vstup). To zahrnuje prvky uživatelského rozhraní, struktury menu, hlasové výzvy, hmatovou zpětnou vazbu a funkce usnadnění.

V kontextu uživatelského zařízení (UE) specifikace MMI zajišťují konzistentní a předvídatelný uživatelský zážitek napříč zařízeními od různých výrobců. Pokrývají aspekty jako řízení hovorů (zahájení, přijetí, přidržení), správu doplňkových služeb (např. aktivace přesměrování hovoru), navigaci v menu, zadávání textu a zobrazení informací o stavu sítě (síla signálu, název sítě). MMI je úzce integrováno s operačním systémem zařízení a aplikačním rámcem a zprostředkovává komunikaci mezi akcemi uživatele a podkladovým protokolovým zásobníkem 3GPP. Například když uživatel vytočí číslo, vrstva MMI shromáždí číslice, naformátuje je a předá požadavek entitě řízení hovoru ve vrstvě [NAS](/mobilnisite/slovnik/nas/).

Pro správu sítě má MMI podobu rozhraní systémů podpory provozu ([OSS](/mobilnisite/slovnik/oss/)), často využívajících standardizované jazyky jako Man-Machine Language ([MML](/mobilnisite/slovnik/mml/)) nebo moderní grafická uživatelská rozhraní ([GUI](/mobilnisite/slovnik/gui/)). Tato rozhraní umožňují síťovým operátorům monitorovat výkon sítě, konfigurovat síťové elementy, spravovat poruchy a provádět provizování účastníků. Principy MMI se zde zaměřují na srozumitelnost, efektivitu a bezpečnost, aby se předešlo chybné konfiguraci. Architektura MMI je vrstvená a odděluje prezentační logiku od základních aplikačních a síťových funkcí. Tato abstrakce umožňuje přístup ke stejné základní funkcionalitě (např. úprava profilu účastníka) prostřednictvím různých rozhraní (webové GUI pro operátora, [USSD](/mobilnisite/slovnik/ussd/) kód pro účastníka). Její role je zásadní; bez dobře definovaného MMI nemohou uživatelé efektivně využívat služby a operátoři nemohou spravovat síť.

## K čemu slouží

Standardizace MMI byla hnána potřebou použitelnosti, interoperability a bezpečnosti v telekomunikacích. V raných mobilních systémech vedly proprietární rozhraní k roztříštěnému uživatelskému zážitku, kdy základní funkce jako uskutečnění hovoru nebo kontrola hlasové schránky fungovaly na každém telefonu jinak, což uživatele matlo a bránilo masovému rozšíření. Pro síťové operátory znamenala nekonzistentní správní rozhraní pro zařízení od různých dodavatelů zvýšené provozní náklady a riziko chyb.

Specifikace MMI tyto problémy řeší vytvořením společného rámce. Zajišťují, že základní funkce mají předvídatelné chování, což je klíčové pro přijetí uživateli a pro umožnění služeb závislých na interakci s uživatelem, jako jsou systémy interaktivní hlasové odpovědi ([IVR](/mobilnisite/slovnik/ivr/)) nebo konfigurace služeb na zařízení. Dále se standardy MMI zabývají kritickými oblastmi, jako je nouzové volání – definují, jak se nouzová čísla vytáčejí a prezentují – a přístupností, což zajišťuje dostupnost telekomunikačních služeb pro uživatele s postižením. Vývoj od základních textových menu k bohatým grafickým rozhraním a nyní k hlasovému a gestickému ovládání v rámci rámce MMI odráží stálý cíl: učinit komplexní síťovou technologii intuitivní a přístupnou lidem, ať už jsou to koncoví uživatelé nebo síťoví inženýři.

## Klíčové vlastnosti

- Standardizuje interakci uživatele s mobilními zařízeními (klávesnice, obrazovka, hlas)
- Definuje procedury pro řízení hovorů a správu služeb
- Specifikuje rozhraní pro provoz a údržbu sítě (OSS)
- Zajišťuje přístupnost pro uživatele s postižením
- Podporuje jak grafická (GUI), tak příkazová (MML) rozhraní
- Spravuje prezentaci informací o stavu sítě a služeb uživateli

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [MMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmi/)
