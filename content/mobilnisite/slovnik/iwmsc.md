---
slug: "iwmsc"
url: "/mobilnisite/slovnik/iwmsc/"
type: "slovnik"
title: "IWMSC – InterWorking Mobile Switching Center"
date: 2025-01-01
abbr: "IWMSC"
fullName: "InterWorking Mobile Switching Center"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iwmsc/"
summary: "Specializované mobilní ústředí (MSC), které zprostředkovává interoperabilitu mezi různými síťovými technologiemi, jako jsou GSM a CDMA nebo PSTN. Zajišťuje převod protokolů a signalizační zprostředkov"
---

IWMSC je specializované mobilní ústředí (Mobile Switching Center), které zprostředkovává interoperabilitu mezi různými síťovými technologiemi tím, že zajišťuje převod protokolů a signalizační zprostředkování.

## Popis

InterWorking Mobile Switching Center (IWMSC) je základní síťový prvek definovaný ve specifikacích 3GPP, primárně pro sítě GSM a UMTS. Jeho hlavní funkcí je působit jako brána a zprostředkovatel mezi mobilní sítí a jinými externími sítěmi, jako je veřejná telefonní síť (PSTN), digitální síť s integrovanými službami ([ISDN](/mobilnisite/slovnik/isdn/)) nebo jiné mobilní sítě používající odlišné technologie (např. [CDMA](/mobilnisite/slovnik/cdma/)). Z architektonického hlediska se jedná o specializovaný typ [MSC](/mobilnisite/slovnik/msc/), který obsahuje dodatečné funkce pro interoperabilitu ([IWF](/mobilnisite/slovnik/iwf/)). Nachází se na hranici mobilní sítě a rozhraní k externím sítím využívá standardizované signalizační protokoly, jako je SS7 (Signaling System No. 7).

Provozně IWMSC provádí kritický převod a adaptaci protokolů. Když je hovor iniciován mobilním účastníkem a je určen účastníkovi v externí síti, signalizace hovoru a uživatelský provoz procházejí přes IWMSC. Převádí mobilní signalizaci (např. [MAP](/mobilnisite/slovnik/map/), BICC) na protokoly srozumitelné externí síti (např. [ISUP](/mobilnisite/slovnik/isup/) pro PSTN). To zahrnuje převod zpráv řízení hovoru, adresních informací (jako je převod [MSISDN](/mobilnisite/slovnik/msisdn/) na čísla E.164) a adaptaci charakteristik přenosového kanálu. V případě uživatelského provozu může zajišťovat převod kodeků, pokud jsou v mobilní síti použity hlasové kodeky (např. [AMR](/mobilnisite/slovnik/amr/)), které externí síť nepodporuje.

Jeho role je klíčová pro zajištění plynulé interoperability služeb. IWMSC není jen pasivní brána; aktivně se účastní procedur navázání, správy a ukončení hovoru. Spolupracuje s bránovou MSC (GMSC) při směrování hovorů. Zatímco GMSC je zodpovědná za dotazování HLR za účelem nalezení obsluhující MSC volaného účastníka, IWMSC zajišťuje fyzické a logické propojení s externím světem. V mnoha implementacích mohou být funkce GMSC a IWMSC kombinovány v jediném síťovém uzlu. IWMSC byl klíčovou komponentou pro umožnění základního roamingu telefonních služeb a propojení v raných sítích 2G a 3G před plným nasazením IP-based core networks.

## K čemu slouží

IWMSC byl vytvořen k řešení základního problému propojování sítí v počátcích digitální mobilní telekomunikace. Když byly sítě GSM nasazovány globálně, potřebovaly se propojit s rozsáhlou stávající infrastrukturou pevných PSTN sítí, aby mohli mobilní uživatelé volat na pevné linky a naopak. Navíc, s příchodem mobilních operátorů používajících různé radiové technologie (jako GSM a CDMA), vznikla potřeba, aby tyto sítě mohly vzájemně spolupracovat. Účelem IWMSC je překlenout tyto technologické rozdíly.

Historicky, před standardizovanými funkcemi pro interoperabilitu, se používaly proprietární brány, což vedlo k problémům s kompatibilitou a vyšším nákladům. Standardizace IWMSP organizací 3GPP poskytla jednotnou architekturu a soubor procedur pro propojování. Řešila omezení jako nekompatibilní signalizační systémy, rozdílné číslovací plány a neodpovídající přenosové schopnosti (např. hlasové kódování). Definováním vyhrazeného síťového prvku zajistilo 3GPP, že mobilní sítě mohou být budovány jako samostatné systémy, které jsou zároveň schopné se připojit ke globálnímu telekomunikačnímu ekosystému, což bylo klíčové pro komerční úspěch a všudypřítomnost mobilních služeb.

## Klíčové vlastnosti

- Převod protokolů mezi signalizací mobilní sítě (např. MAP, BICC) a signalizací externí sítě (např. ISUP, TUP)
- Adaptace přenosového kanálu a převod kodeků pro interoperabilitu hlasového provozu
- Překlad adres mezi identifikátory mobilních účastníků (MSISDN) a číslovacími formáty PSTN/ISDN
- Řízení a zprostředkování hovorů pro navázání, správu a uvolnění mezisíťových hovorů
- Rozhraní jak k jádru mobilní sítě (přes rozhraní MSC), tak k externím sítím (přes SS7 linky)
- Podpora interoperability doplňkových služeb, jako je přesměrování hovorů, přes hranice sítí

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [IWMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/iwmsc/)
