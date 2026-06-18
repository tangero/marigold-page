---
slug: "kek"
url: "/mobilnisite/slovnik/kek/"
type: "slovnik"
title: "KEK – Key Encryption Key (TETRA)"
date: 2026-01-01
abbr: "KEK"
fullName: "Key Encryption Key (TETRA)"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kek/"
summary: "Šifrovací klíč pro klíče používaný v bezpečnostním kontextu TETRA (Terrestrial Trunked Radio) v rámci standardů 3GPP. Jedná se o kryptografický klíč speciálně určený k ochraně jiných klíčů během přeno"
---

KEK je šifrovací klíč pro klíče používaný v systémech TETRA k kryptografické ochraně jiných klíčů během přenosu nebo uložení, což zajišťuje bezpečnou distribuci klíčů.

## Popis

V rámci specifikací 3GPP, které řeší interoperabilitu a zabezpečení pro kritické komunikace, je Key Encryption Key (KEK) koncept převzatý ze standardu [TETRA](/mobilnisite/slovnik/tetra/) (Terrestrial Trunked Radio). TETRA je profesionální systém mobilní a trunkované radiokomunikace používaný složkami integrovaného záchranného systému, dopravy a armádou. KEK hraje klíčovou roli v systému správy kryptografických klíčů TETRA. Jeho primární funkcí je poskytnout vrstvu nepřímé ochrany pro klíče šifrující provoz nebo jiný citlivý klíčový materiál.

Z architektonického hlediska je KEK symetrický klíč, který je předem sdílen nebo navázán pomocí bezpečného protokolu mezi autorizovanými entitami, jako je centrum správy klíčů (KMC) a TETRA terminál nebo síťový uzel. Nepoužívá se přímo k šifrování hlasového nebo datového provozu uživatele. Místo toho slouží k zašifrování jiných klíčů, známých jako klíče pro šifrování provozu ([TEK](/mobilnisite/slovnik/tek/)) nebo sezení, které jsou následně přenášeny potenciálně nezabezpečenými kanály. Tento proces je často označován jako zabalení klíče nebo šifrování klíče. Entita přijímající zašifrovaný TEK použije stejný KEK k jeho dešifrování, načež může být TEK použit pro zabezpečení skutečné komunikace.

Jak to funguje, zahrnuje hierarchii klíčů. Dlouhodobý KEK, který má relativně dlouhý životní cyklus, se používá k ochraně krátkodobých TEK. Když je navázáno nové sezení nebo je třeba TEK aktualizovat, KMC vygeneruje TEK, zašifruje jej pomocí KEK (např. pomocí standardního algoritmu jako [AES](/mobilnisite/slovnik/aes/)) a zašle šifrovaný text cílovému zařízení. Zařízení, které má stejný KEK, provede dešifrování, aby získalo TEK. Tato metoda zajišťuje, že citlivý TEK není během distribuce nikdy vystaven v čitelné podobě. Specifikace 3GPP (např. TS 23.283, TS 24.883) odkazují na tento mechanismus v kontextu interoperability mezi sítěmi 3GPP (jako LTE/5G pro kritické komunikace) a sítěmi TETRA, což zajišťuje, že může být zachována komplexní bezpečnost, když je třeba klíče nebo bezpečnostní kontexty převádět nebo spravovat napříč těmito heterogenními systémy.

## K čemu slouží

KEK existuje, aby řešil základní problém bezpečné distribuce klíčů v řízeném rádiovém systému s uzavřenou skupinou, jako je [TETRA](/mobilnisite/slovnik/tetra/). Distribuce jedinečného provozního klíče každému členu velké skupiny pro každé sezení by byla logisticky náročná, pokud by byla prováděna fyzickými prostředky. KEK poskytuje škálovatelné řešení. Zavedením sdíleného KEK v rámci skupiny (např. policejní jednotky) může síť efektivně a bezpečně vysílat nebo multicastovat nové sezení klíčů všem členům jejich zašifrováním pomocí skupinového KEK.

Historicky byl TETRA navržen pro vysoce zabezpečenou kritickou komunikaci, kde tradiční protokoly pro dohodu klíčů v buněčných sítích nemusí pro všechny provozní modely stačit, zejména pro skupinovou komunikaci a bezdrátovou obnovu klíčů. Model KEK poskytuje přímou kontrolu a efektivitu pro správu skupinových klíčů. Jeho zařazení do standardů 3GPP, zejména od vydání 15, bylo motivováno potřebou, aby služby Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) přes sítě 3GPP bezproblémově spolupracovaly se stávajícími sítěmi TETRA, které jsou široce nasazeny pro veřejnou bezpečnost.

Tento přístup řeší omezení, kdy je třeba s každou distribucí klíčů zacházet jako s jedinečnou, zabezpečenou transakcí typu point-to-point. KEK umožňuje efektivní hromadné nebo skupinové aktualizace klíčů, což je nezbytné během bezpečnostních incidentů nebo rutinní rotace klíčů. Pro 3GPP je zahrnutí porozumění TETRA KEK nezbytné pro funkce bezpečnostní brány nebo funkce interoperability ([IWF](/mobilnisite/slovnik/iwf/)), které potřebují mapovat nebo převádět bezpečnostní kontexty mezi službou [MCPTT](/mobilnisite/slovnik/mcptt/) (Mission Critical Push-To-Talk) 3GPP a starší sítí TETRA, což zajišťuje, že komplexní bezpečnostní řetězec není přerušen.

## Klíčové vlastnosti

- Používá se k šifrování (zabalení) jiných kryptografických klíčů, primárně klíčů pro šifrování provozu (TEK)
- Vytváří dvouvrstvou hierarchii klíčů: dlouhodobý KEK chrání krátkodobé sezení klíčů
- Umožňuje efektivní a bezpečnou bezdrátovou distribuci sezení klíčů skupinám zařízení
- Založeno na symetrické kryptografii, vyžadující předchozí navázání sdíleného klíče mezi entitami
- Odkazováno ve specifikacích 3GPP pro interoperabilitu TETRA-3GPP pro kritické komunikace
- Podporuje modely správy klíčů pro zabezpečenou skupinovou komunikaci

## Související pojmy

- [TETRA – Trans European Trunked RAdio](/mobilnisite/slovnik/tetra/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [KEK na 3GPP Explorer](https://3gpp-explorer.com/glossary/kek/)
