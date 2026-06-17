---
slug: "nagnp"
url: "/mobilnisite/slovnik/nagnp/"
type: "slovnik"
title: "NAGNP – North American GSM Number Portability"
date: 2025-01-01
abbr: "NAGNP"
fullName: "North American GSM Number Portability"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nagnp/"
summary: "North American GSM Number Portability (NAGNP) je standard definovaný 3GPP, který umožňuje mobilním účastníkům v Severní Americe zachovat svá telefonní čísla při přechodu k jinému poskytovateli služeb"
---

NAGNP je standard 3GPP pro Severní Ameriku, který umožňuje mobilním účastníkům zachovat svá telefonní čísla při změně poskytovatele služeb definováním potřebné síťové architektury, signalizace a databázových dotazů pro směrování hovorů.

## Popis

North American GSM Number Portability (NAGNP) je specifická implementace přenositelnosti čísel přizpůsobená pro sítě založené na GSM v regionu Severní Ameriky (především USA a Kanada). Funguje na základním principu oddělení telefonního čísla účastníka (Directory Number) od jeho síťové lokace a poskytovatele služeb. Když je číslo portováno, hovory na toto číslo musí být směrovány do nové sítě namísto té původní.

Technická implementace zahrnuje centralizovanou databázi přenositelnosti čísel (Number Portability Database, [NPDB](/mobilnisite/slovnik/npdb/)), kterou často spravuje neutrální třetí strana. Když ústředna mobilního spojení (Mobile Switching Center, [MSC](/mobilnisite/slovnik/msc/)) nebo bránová MSC (Gateway MSC, [GMSC](/mobilnisite/slovnik/gmsc/)) obdrží požadavek na sestavení hovoru na mobilní číslo, musí zjistit, zda bylo číslo portováno. To se provádí pomocí databázového dotazu. V modelu NAGNP je dotaz typicky spuštěn na přepojovacím uzlu (switch) v síti volajícího. Tento uzel analyzuje volané číslo (konkrétně číselný plán oblasti, NPA-NXX), aby na základě lokální tabulky přenosných číselných rozsahů rozhodl, zda je dotaz nutný.

Pokud je dotaz vyžadován, MSC/GMSC sestaví signalizační zprávu, například ANSI-41 Location Request (LOCREQ) nebo dotaz založený na SIP, a odešle ji do NPDB přes Signal Transfer Point (STP) nebo přímo přes IP síť. NPDB obsahuje záznamy mapující portovaná čísla na identifikátory jejich současné obslužné sítě, jako je Location Routing Number ([LRN](/mobilnisite/slovnik/lrn/)). LRN je unikátní desetimístné číslo, které jednoznačně identifikuje ústřednu (switch) aktuálně obsluhující portovaného účastníka. Databáze tento LRN vrátí dotazujícímu se uzlu.

Ústředna volajícího pak použije tento LRN namísto volaného telefonního čísla (Directory Number) k směrování hovoru přes veřejnou telefonní síť (PSTN) nebo mobilní síť. Hovor je doručen na správnou MSC v síti nového příjemce. Tento proces je pro koncové uživatele z velké části transparentní. Architektura také zahrnuje mechanismy pro podporu SMS a dalších služeb pro portovaná čísla, které vyžadují podobné databázové dotazy ze strany SMSC nebo jiných síťových prvků.

## K čemu slouží

NAGNP byl vytvořen za účelem splnění regulatorních požadavků v Severní Americe, které vyžadovaly bezdrátovou místní přenositelnost čísel (Wireless Local Number Portability, WLNP). Před jeho implementací bylo mobilní číslo účastníka trvale svázáno s jeho původním poskytovatelem služeb. Přechod k jinému poskytovateli znamenal změnu telefonního čísla, což byla významná nepříjemnost působící jako bariéra konkurence tím, že zákazníky uzamykala (jev známý jako 'zákaznická setrvačnost').

Problém, který NAGNP řeší, je technická výzva oddělení telefonního čísla – základní směrovací adresy v PSTN a mobilních sítích – od konkrétního fyzického přepojovacího uzlu (switch) nebo síťového poskytovatele. Starší schémata směrování předpokládala, že prefix čísla (NPA-NXX) přímo určuje obslužného operátora a ústřednu. Přenositelnost tento předpoklad narušuje a vyžaduje dodatečný krok dotazu pro nalezení aktuální síťové lokace.

3GPP standardizoval NAGNP, aby zajistil interoperabilitu mezi zařízeními různých výrobců a sítěmi různých operátorů v rámci regionu Severní Ameriky, který používá signalizaci jádra sítě ANSI-41 (později vyvinutou do standardů 3GPP2) spolu s GSM radiovým přístupem. Specifikace poskytla společný rámec pro dotazy, odpovědi (s využitím konceptu Location Routing Number) a procedury, čímž zabránila fragmentaci a zajistila konzistentní uživatelský zážitek z přenositelnosti napříč všemi operátory GSM/UMTS na trhu. Řešila omezení proprietárních nebo nestandardních řešení, která by bránila bezproblémovému provozu.

## Klíčové vlastnosti

- Definuje použití centralizované databáze přenositelnosti čísel (Number Portability Database, NPDB) pro ukládání záznamů o portování
- Specifikuje Location Routing Number (LRN) jako klíčový směrovací identifikátor pro ústřednu (switch) portovaného účastníka
- Podporuje mechanismy dotazů při vzniku hovoru (metoda All Call Query - ACQ) pro efektivní směrování
- Integruje se s signalizačními protokoly jádra sítě ANSI-41 (IS-41) a vyvíjejícími se protokoly 3GPP2
- Umožňuje přenositelnost pro hlasové hovory, SMS a další doplňkové služby
- Poskytuje procedury pro aktualizaci NPDB, když účastník portuje své číslo

## Definující specifikace

- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [NAGNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nagnp/)
