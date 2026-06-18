---
slug: "udl"
url: "/mobilnisite/slovnik/udl/"
type: "slovnik"
title: "UDL – User Data Length"
date: 2002-01-01
abbr: "UDL"
fullName: "User Data Length"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/udl/"
summary: "Parametr udávající délku uživatelských dat v rámci konkrétní protokolové datové jednotky nebo zprávy. Jde o základní pole v různých protokolech 3GPP, které vymezuje velikost přenášených dat pro správn"
---

UDL je parametr udávající délku uživatelských dat v rámci konkrétní protokolové datové jednotky nebo zprávy, který vymezuje velikost přenášených dat pro jejich správné parsování a zpracování.

## Popis

User Data Length (UDL) je základní parametr nebo informační prvek nacházející se v různých specifikacích protokolů 3GPP. Nejde o samostatnou síťovou funkci nebo službu, ale o kritické datové pole používané k označení délky (obvykle v oktetech nebo bajtech) uživatelských dat nebo přenášených dat, která následují v rámci konkrétní protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), zprávy nebo kontejneru. Primárním účelem pole UDL je umožnit přijímající entitě – ať už jde o mobilní stanici, základnovou stanici nebo uzel jádra sítě – správně parsovat příchozí zprávu. Díky znalosti přesné délky části s uživatelskými daty může přijímač odlišit přenášená data od následujících řídicích polí, výplně nebo dalších zpráv, čímž zajišťuje přesnou interpretaci a zpracování.

V praxi je pole UDL součástí struktury mnoha zpráv vrstvy 3 ([L3](/mobilnisite/slovnik/l3/)) a aplikační vrstvy. Například ve specifikacích služby krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)) UDL udává délku samotné krátké zprávy. V jiných kontextech může definovat délku uživatelských dat v rámci protokolové datové jednotky [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol) nebo konkrétního kontejneru zprávy [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum). Velikost samotného tohoto pole (např. 1 oktet) omezuje maximální délku uživatelských dat, kterou může popsat. Síťový prvek nebo uživatelské zařízení (UE) generující zprávu vypočítá délku svého uživatelského datového payloadu, zakóduje tuto hodnotu do pole UDL a umístí ji na definovanou pozici v hlavičce zprávy. Příjemce tuto hodnotu nejprve extrahuje a poté přečte přesný počet oktetů určený jako uživatelská data.

Role UDL je zásadní pro spolehlivou digitální komunikaci. Poskytuje samoopisný mechanismus pro data proměnné délky, což je zásadní pro efektivitu. Bez něj by protokoly vyžadovaly pevnou délku přenášených dat (plýtvání šířkou pásma) nebo složité sekvence oddělovačů (zvýšení režie zpracování a rizika chyb). Explicitním uvedením délky zůstávají protokoly robustní a efektivní. Zpracování UDL je základní funkcí implementovanou v softwaru protokolového zásobníku všech zařízení kompatibilních se standardy 3GPP. Ačkoli je koncept jednoduchý, jeho správná implementace je klíčová pro interoperabilitu; nesoulad v interpretaci délky může vést ke zkreslení zprávy, protokolovým chybám a výpadkům služeb.

Specifikace TS 23.048, kde je UDL významně odkazováno, se zabývá bezpečnostními mechanismy. V takovém kontextu může být UDL použito k určení délky uživatelských dat, která je třeba chránit konkrétním bezpečnostním algoritmem, čímž se zajistí, že funkce integrity a důvěrnosti jsou aplikovány na správné množství dat. To zdůrazňuje, jak je UDL stavebním parametrem využívaným napříč různými funkčními oblastmi – od přenosu dat v uživatelské rovině po signalizaci v řídicí rovině a bezpečnost – v rámci systémové architektury 3GPP.

## K čemu slouží

Parametr User Data Length existuje, aby řešil základní problém přenosu informací proměnné délky přes digitální protokol. Komunikační protokoly potřebují spolehlivý způsob, jak může přijímač určit, kde jeden kus uživatelských dat končí a kde začíná další řídicí pole nebo zpráva. Zprávy pevné délky jsou pro různé služby neefektivní, protože buď data oříznou, nebo je doplní prázdnými bity.

UDL poskytuje jednoduché, efektivní a robustní řešení. Zahrnutím indikátoru délky na známou pozici v hlavičce zprávy se protokol stává samorámcujícím. Tento přístup minimalizuje režii ve srovnání s použitím jedinečných bitových sekvencí jako oddělovačů, které by se mohly náhodně objevit v samotných uživatelských datech (což by vyžadovalo escape mechanismy). Také zjednodušuje logiku parsování v softwarových a hardwarových implementacích, což vede k spolehlivějším a výkonnějším síťovým prvkům a uživatelským zařízením.

Historicky je použití indikátorů délky dobře zavedeným principem v telekomunikacích a počítačových sítích (např. v IP hlavičkách). 3GPP tento koncept přijalo napříč svými sadami protokolů, aby zajistilo strukturovanou a jednoznačnou výměnu dat. Jeho zařazení do bezpečnostní specifikace, jako je TS 23.048, podtrhuje jeho důležitost při definování rozsahu kryptografických operací, čímž se zajišťuje, že ochrana integrity nebo šifrování je aplikováno přesně na zamýšlený blok uživatelských dat, což je klíčové pro robustnost zabezpečení.

## Klíčové vlastnosti

- Udává délku v oktetech pro přidružená uživatelská data (payload)
- Umožňuje parsování protokolových datových jednotek (PDU) proměnné délky
- Základní pole v různých zprávách vrstvy L3 a aplikační vrstvy
- Podporuje efektivní využití šířky pásma tím, že umožňuje proměnnou velikost přenášených dat
- Zásadní pro správnou činnost bezpečnostních algoritmů na definovaných blocích dat
- Základní stavební prvek pro interoperabilitu protokolů

## Související pojmy

- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [UDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/udl/)
