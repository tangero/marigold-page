---
slug: "tar"
url: "/mobilnisite/slovnik/tar/"
type: "slovnik"
title: "TAR – Toolkit Application Reference"
date: 2025-01-01
abbr: "TAR"
fullName: "Toolkit Application Reference"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tar/"
summary: "Jedinečný identifikátor aplikace SIM/USIM v rámci SIM Application Toolkit (SAT) nebo USIM Application Toolkit (USAT) podle 3GPP. Rozlišuje různé aplikace toolkitu na UICC, umožňuje síťové příkazy a sl"
---

TAR je jedinečný identifikátor aplikace SIM/USIM, který rozlišuje různé aplikace toolkitu na UICC, umožňuje síťové příkazy a služby s přidanou hodnotou.

## Popis

Toolkit Application Reference (TAR) je číselný kód, typicky o délce 3 bajtů, který jednoznačně identifikuje konkrétní aplikaci v prostředí [SIM](/mobilnisite/slovnik/sim/) Application Toolkit ([SAT](/mobilnisite/slovnik/sat/)) nebo [USIM](/mobilnisite/slovnik/usim/) Application Toolkit ([USAT](/mobilnisite/slovnik/usat/)) na Universal Integrated Circuit Card (UICC), což zahrnuje karty SIM a USIM. Slouží jako klíčový parametr pro směrování příkazů mezi sítí a správnou aplikací na kartě. V architektuře operací toolkitu se TAR používá v proaktivních příkazech odesílaných z UICC do mobilního zařízení ([ME](/mobilnisite/slovnik/me/)) a v obálkových příkazech odesílaných z ME do UICC, čímž zajišťuje, že každý příkaz zpracuje zamýšlená aplikace. To umožňuje koexistenci více nezávislých aplikací na stejné UICC bez vzájemného ovlivňování.

Jak to funguje: TAR je přiřazen během vývoje a zřizování aplikace toolkitu. Když síť (např. prostřednictvím [OTA](/mobilnisite/slovnik/ota/) platforem) potřebuje komunikovat s konkrétní aplikací – například za účelem aktualizace služby, spuštění menu nebo odeslání dat – zahrne TAR do paketu příkazu. ME příkaz přijme a přepošle jej na UICC, která použije TAR k jeho nasměrování na příslušnou aplikační logiku. Podobně, když aplikace na UICC iniciuje proaktivní příkaz (jako zobrazení textu nebo navázání hovoru), zahrne svůj TAR, aby ME mohlo správně asociovat odpověď. TAR je často spárován s dalšími identifikátory, jako je Application Identifier ([AID](/mobilnisite/slovnik/aid/)), ale je specificky optimalizován pro efektivitu protokolu toolkitu. Je uložen v nevolatilní paměti na UICC a je referencován v adresářové struktuře aplikace.

Mezi klíčové komponenty patří samotná hodnota TAR, která musí být na dané UICC jedinečná pro každou aplikaci, aby se předešlo konfliktům; vrstvy protokolu toolkitu, které přenášejí příkazy označené TAR; a entity správy aplikací na UICC, které TAR interpretují. TAR hraje zásadní roli v zabezpečení, protože může být používán spolu s kryptografickými klíči pro zabezpečenou komunikaci, což zajišťuje, že pouze autorizované sítě mohou přistupovat k určitým aplikacím nebo je modifikovat. Jeho návrh podporuje široké spektrum služeb, od základních aktualizací menu po komplexní finanční transakce v mobilním bankovnictví, a to poskytnutím spolehlivého adresovacího mechanismu v omezeném prostředí čipové karty.

## K čemu slouží

TAR byl vytvořen k řešení potřeby správy více aplikací na jedné kartě [SIM](/mobilnisite/slovnik/sim/)/USIM v rámci frameworku SIM Application Toolkit, který vznikl koncem 90. let 20. století k umožnění služeb s přidanou hodnotou nad rámec základní telefonie. Před zavedením TAR byly SIM karty z velké části statické, s omezenou schopností hostovat dynamické aplikace nebo přijímat síťové příkazy. Když operátoři chtěli zavádět služby jako mobilní bankovnictví, informační aktualizace a vlastní menu, byl vyžadován způsob, jak jedinečně identifikovat a adresovat jednotlivé aplikace na kartě bez narušení ostatních. TAR tuto schopnost poskytl a vyřešil tak problém multiplexování aplikací na sdílené hardwarové platformě.

Historicky byl TAR představen ve 3GPP Release 5 jako součást vylepšení USIM Application Toolkit, navazující na dřívější koncepty GSM SAT od ETSI. Motivací byla rostoucí složitost služeb založených na UICC a potřeba zabezpečené a efektivní komunikace mezi sítí a aplikacemi na kartě. Předchozí přístupy postrádaly standardizovaný referenční systém, což vedlo k proprietárním řešením bránícím interoperabilitě. TAR umožnil operátorům a poskytovatelům služeb spolehlivě nasazovat a spravovat aplikace přes vzdušné rozhraní (OTA), čímž podpořil obchodní modely pro personalizované mobilní služby.

Dále TAR usnadňuje zabezpečení a důvěru tím, že umožňuje asociovat kryptografické klíče s konkrétními aplikacemi prostřednictvím hodnoty TAR, což zajišťuje ochranu citlivých operací (např. platebních transakcí). Řeší omezení dřívějších verzí toolkitu tím, že poskytuje škálovatelný, budoucím vývojem neovlivnitelný identifikátor fungující napříč technologiemi GSM, UMTS a pozdějšími. Vytvoření TAR bylo klíčové pro vývoj UICC z jednoduchého autentizačního modulu na multi-aplikační platformu, což umožnilo inovace jako služby NFC, správu identit a zřizování IoT zařízení, které spoléhají na přesné adresování aplikací.

## Klíčové vlastnosti

- Jedinečný 3bajtový identifikátor pro aplikace SIM/USIM toolkitu
- Umožňuje směrování příkazů mezi sítí a konkrétními aplikacemi na UICC
- Podporuje proaktivní a obálkové příkazy v protokolech SAT/USAT
- Usnadňuje zabezpečenou komunikaci asociací klíčů s hodnotami TAR
- Umožňuje koexistenci více aplikací na jedné UICC bez konfliktů
- Nezbytný pro správu aplikací a aktualizace přes vzdušné rozhraní (OTA)

## Související pojmy

- [USAT – Universal Subscriber Identity Module Application Toolkit](/mobilnisite/slovnik/usat/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.112** (Rel-8) — USAT Interpreter System Architecture
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API

---

📖 **Anglický originál a plná specifikace:** [TAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tar/)
