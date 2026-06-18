---
slug: "hw"
url: "/mobilnisite/slovnik/hw/"
type: "slovnik"
title: "HW – Hardware"
date: 2025-01-01
abbr: "HW"
fullName: "Hardware"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hw/"
summary: "V kontextu 3GPP je HW běžná zkratka pro Hardware (hardwarové vybavení), odkazující na fyzické komponenty síťových zařízení a uživatelských zařízení (UE). Specifikace jako TS 25.467 pojednávají o hardw"
---

HW je běžná 3GPP zkratka pro Hardware (hardwarové vybavení), což označuje fyzické komponenty síťových zařízení a uživatelských zařízení (UE), jak jsou specifikovány pro požadavky a testování.

## Popis

Ve specifikacích 3GPP je 'HW' standardní zkratkou pro Hardware (hardwarové vybavení). Označuje fyzické, hmatatelné komponenty tvořící síťovou infrastrukturu a uživatelská zařízení, na rozdíl od softwaru (SW) nebo firmware. Technická specifikace TS 25.467 se například zabývá architekturou [UTRAN](/mobilnisite/slovnik/utran/) pro 3G/UMTS a zahrnuje odkazy na hardwarové aspekty základnových stanic (NodeBs), radiových síťových řadičů (RNCs) a dalších síťových prvků. Hardware zahrnuje širokou škálu komponent, včetně vysokofrekvenčních ([RF](/mobilnisite/slovnik/rf/)) transceiverů, antén, jednotek pro zpracování základního pásma, výkonových zesilovačů, filtrů, skříní, kabeláže a chladicích systémů.

Role hardwaru v 3GPP síti je zásadní. Poskytuje fyzickou platformu, na které běží všechny síťové protokoly a softwarové funkce. Například hardware NodeB musí splňovat přísné požadavky na RF výkon týkající se výstupního výkonu, frekvenční stability, parazitních emisí a citlivosti přijímače, jak jsou definovány ve specifikacích 3GPP. Tyto požadavky zajišťují, že hardware nezpůsobuje škodlivé rušení jiným systémům a může spolehlivě fungovat v různých environmentálních podmínkách. Hardwarová architektura přímo ovlivňuje klíčové síťové parametry výkonu, jako je pokrytí, kapacita, datová propustnost a energetická účinnost.

Z perspektivy implementace a standardizace specifikace 3GPP definují logické funkce a rozhraní sítě. Zároveň však stanovují výkonnostní a shodové požadavky, které hardware musí splňovat. To je klíčové pro interoperabilitu. Zatímco 3GPP nenařizuje konkrétní čipovou sadu nebo mechanický design, definuje 'black box' chování, které musí každý kompatibilní hardware vykazovat. Specifikace pokrývají aspekty jako podporovaná frekvenční pásma, šířky kanálů, modulační schémata (která diktují požadavky na linearitu RF) a konfigurace [MIMO](/mobilnisite/slovnik/mimo/) antén. Dále jsou standardizovány postupy testování hardwaru, aby se ověřilo, že komerční zařízení splňuje tyto požadavky před nasazením v síti operátora. Termín 'HW' v kontextu dokumentu 3GPP tedy často poukazuje na fyzickou vrstvovou realizaci standardizovaných logických funkcí.

## K čemu slouží

Explicitní odkaz na Hardware (HW) ve specifikacích 3GPP slouží k oddělení požadavků na fyzickou implementaci od definic logických protokolů a softwaru. Primárním účelem je zajistit, aby fyzická zařízení vyráběná různými výrobci byla vzájemně spolupracující, spolehlivě fungovala a vyhovovala regulatorním požadavkům (např. využití spektra, elektromagnetická kompatibilita). Bez standardizovaných hardwarových požadavků by mohly mít základnové stanice jednoho dodavatele nekompatibilní [RF](/mobilnisite/slovnik/rf/) charakteristiky s UE jiného dodavatele, nebo by mohly způsobovat nadměrné rušení, čímž by narušily síť.

Historicky, jak se mobilní technologie vyvíjela od analogové (1G) k digitální (2G GSM), stala se potřeba komplexní hardwarové standardizace zřejmou pro dosažení globálního roamingu a sítí s více dodavateli. 3GPP tuto filozofii převzala a rozšířila. Problémy řešené HW specifikacemi zahrnují zajištění konzistentního radiového výkonu v různých geografických trzích (s různými frekvenčními pásmy), definování odolnosti zařízení vůči prostředí (např. rozsahy provozních teplot) a stanovení testovacích metodologií, které dávají operátorům jistotu v zařízeních, která nakupují.

Motivace pro detailní rozpracování HW aspektů je hluboce praktická. Poskytuje jasnou hranici mezi standardizovaným rozhraním/výkonem ('co') a proprietární implementací ('jak'). To umožňuje inovace v hardwarovém designu (např. účinnější výkonové zesilovače, kompaktní formáty) a zároveň zaručuje, že všechny takové inovace budou bezproblémově fungovat v rámci většího standardizovaného systému. Specifikace jako TS 25.467 pomáhají vytvořit konkurenční trh se síťovým hardwarem, kde se dodavatelé mohou odlišovat cenou, velikostí, spotřebou energie a funkcemi, ale všichni musí splňovat stejná základní výkonnostní kritéria, aby byli 3GPP-kompatibilní.

## Klíčové vlastnosti

- Zahrnuje fyzické komponenty jako RF jednotky, antény, procesory základního pásma a napájecí systémy.
- Podléhá přísným výkonnostním požadavkům definovaným 3GPP pro rádiový přenos a příjem.
- Musí vyhovovat regulatorním požadavkům na využití spektra a elektromagnetické emise.
- Poskytuje fyzický základ pro všechny síťové softwarové a protokolové operace.
- Dodavateli rozlišován na základě účinnosti, kapacity, formátu a nákladů při splnění standardizovaných rozhraní.
- Ověřován prostřednictvím standardizovaných postupů testování shody k zajištění interoperability.

## Související pojmy

- [RF – Repeater type 2-O](/mobilnisite/slovnik/rf/)

## Definující specifikace

- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B

---

📖 **Anglický originál a plná specifikace:** [HW na 3GPP Explorer](https://3gpp-explorer.com/glossary/hw/)
