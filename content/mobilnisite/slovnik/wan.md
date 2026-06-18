---
slug: "wan"
url: "/mobilnisite/slovnik/wan/"
type: "slovnik"
title: "WAN – Wide Area Network"
date: 2025-01-01
abbr: "WAN"
fullName: "Wide Area Network"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wan/"
summary: "V kontextu 3GPP se termín Wide Area Network (WAN) vztahuje k tradičnímu, geograficky rozsáhlému pokrytí mobilní sítě poskytovanému operátorem, typicky s využitím makro buněk. Často je stavěn do kontra"
---

WAN (WAN, širokopásmová síť) je tradiční, geograficky rozsáhlé pokrytí mobilní sítě poskytované operátorem pomocí makro buněk.

## Popis

V rámci standardizace 3GPP se termín Wide Area Network (WAN) používá k popisu konvenčního, rozsáhlého nasazení mobilní sítě, které poskytuje všudypřítomné pokrytí nad městy, regiony nebo státy. Technicky je 3GPP WAN charakterizován použitím makro buněk se základnovými stanicemi (NodeB, eNodeB, gNB) umístěnými na stožárech nebo střechách budov, které nabízejí poloměr pokrytí typicky v rozmezí od několika set metrů až po desítky kilometrů. WAN tvoří primární infrastrukturu pro veřejné mobilní širokopásmové a hlasové služby, fungující v licencovaných kmitočtových pásmech. Jeho architektura následuje hierarchickou systémovou architekturu 3GPP, skládající se z rádiové přístupové sítě (RAN) a jádrové sítě (CN), propojených přenosovými spoji (backhaul).

WAN funguje tak, že geografickou oblast rozděluje na buňky, z nichž každou obsluhuje jedna základnová stanice. Prostřednictvím pokročilých technik, jako je předávání hovoru (handover), řízení výkonu a koordinace rušení, poskytuje uživatelům nepřetržitou podporu mobility při pohybu mezi buňkami. Jádrová síť spravuje autentizaci účastníků, správu relací, ukotvení mobility a připojení k externím sítím, jako je internet. Ve studiích 3GPP, zejména od Release 8 s LTE a později s 5G, se 'WAN' často používá jako výchozí nebo referenční scénář. Například při hodnocení nových rádiových technologií nebo síťových architektur se výkon a požadavky často porovnávají s charakteristikami 'WAN', aby bylo zajištěno, že splňují očekávání pro služby v široké oblasti.

Dále 3GPP používá tento termín k rozlišení servisních scénářů. 'Scénář WAN' implikuje očekávání vysoké mobility, nepřetržitého pokrytí a podpory širokého mixu služeb. To je v kontrastu se scénáři 'hotspot' nebo 'lokální sítě', které cílí na velmi vysokou kapacitu v hustých, malých oblastech. V kontextu integrovaného přístupu a přenosu ([IAB](/mobilnisite/slovnik/iab/)) nebo nesatelitních sítí ([NTN](/mobilnisite/slovnik/ntn/)) se 'WAN' typicky vztahuje k pozemní síti s makro buňkami, která může být těmito dalšími technologiemi doplněna nebo rozšířena. V terminologii 3GPP tedy WAN není jen obecný [IT](/mobilnisite/slovnik/it/) termín, ale specifický operační kontext, který určuje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) pro pokrytí, mobilitu a kapacitu v normalizační práci.

## K čemu slouží

Explicitní použití a definice termínu 'Wide Area Network' v rámci specifikací 3GPP slouží k vytvoření jasného, společného technického kontextu pro požadavky a studie proveditelnosti. Když 3GPP začalo studovat pokročilé technologie jako LTE-Advanced, 5G a síťové segmenty (network slicing), bylo nutné definovat odlišné scénáře nasazení pro přizpůsobení výkonnostních cílů. Scénář WAN představuje základní případ užití mobilních sítí: poskytování bezproblémové služby v široké geografické oblasti, což je primární činnost většiny operátorů.

Tato formalizace řeší problém nejednoznačnosti při diskusích o síťových schopnostech. Definováním charakteristik WAN může 3GPP stanovit specifické požadavky na aspekty jako podpora mobility (např. až 500 km/h pro vysokorychlostní vlaky), spolehlivost pokrytí (např. 95% pokrytí oblasti) a latenci pro služby nasazené v takové oblasti. Vytváří srovnávací měřítko, vůči kterému lze hodnotit vylepšení (jako malé buňky nebo nasazení v milimetrových vlnách). Motivace vychází z potřeby zajistit, aby nové rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)) nebo síťové funkce neohrozily základní službu v široké oblasti, zatímco usilují o zisky ve špičkové přenosové rychlosti nebo kapacitě.

Jeho zařazení do studií od Release 8 výše odráží vyvíjející se prostředí, kde mobilní sítě již nebyly pouze WAN, ale integrovaly se s jinými typy sítí a byly s nimi srovnávány (např. [WLAN](/mobilnisite/slovnik/wlan/) pro lokální přístup). Definice scénáře WAN pomáhá při návrhu systémů, které jsou primárně optimalizovány pro široké pokrytí a mobilitu, přičemž další vlastnosti, jako extrémní kapacita, jsou přidávány pro specifické scénáře. Zajišťuje, že standard nadále slouží základnímu požadavku poskytovat spolehlivou mobilní komunikaci kdekoli v rámci národního nebo regionálního pokrytí.

## Klíčové vlastnosti

- Definuje výchozí scénář nasazení pro všudypřítomné pokrytí mobilní sítí
- Charakterizován makro buňkami s velkými plochami pokrytí
- Podporuje vysokou mobilitu uživatelů a plynulá předání hovoru (handover)
- Funguje v licencovaném spektru pod 6 GHz pro dobrou šířitelnost signálu
- Tvoří primární infrastrukturu pro poskytování veřejných mobilních služeb
- Slouží jako referenční model pro definici klíčových ukazatelů výkonu (KPI) ve studiích 3GPP

## Související pojmy

- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 41.033** (Rel-14) — GSM Lawful Interception Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [WAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/wan/)
